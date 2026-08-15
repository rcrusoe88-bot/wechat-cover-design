#!/usr/bin/env node
/**
 * generate-cover.js — wechat-cover-design 模式B
 * 调用 OpenAI 兼容 Images API 生成公众号封面并保存 PNG（零依赖，仅用内置 fetch）。
 *
 * 用法：
 *   node scripts/generate-cover.js --prompt "<完整英文prompt>" [--theme theme3] [--name 自定义名] [--size 1792x1024] [--crop] [--base-url ...] [--api-key ...] [--quiet]
 *
 * 配置优先级：CLI 参数 > 环境变量(OPENAI_BASE_URL/OPENAI_API_KEY/COVER_IMAGE_MODEL) > config.json
 * 配置文件：本脚本同目录 config.json（已 gitignore，含 api_key 不入库）。
 */
const fs = require('fs');
const path = require('path');

// ---------- 参数解析 ----------
function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      const val = next && !next.startsWith('--') ? next : true;
      if (val !== true) i++;
      args[key] = val;
    }
  }
  return args;
}

const args = parseArgs(process.argv.slice(2));

// ---------- 配置加载（CLI > env > config.json） ----------
let config = {};
const configPath = path.join(__dirname, 'config.json');
if (fs.existsSync(configPath)) {
  try {
    config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch (e) {
    console.error('⚠️  config.json 解析失败，忽略：' + e.message);
  }
}

const baseUrl = args['base-url'] || process.env.OPENAI_BASE_URL || config.base_url || 'https://api.openai.com/v1';
const apiKey  = args['api-key']  || process.env.OPENAI_API_KEY  || config.api_key  || '';
const model   = args['model']    || process.env.COVER_IMAGE_MODEL || config.model || 'dall-e-3';
const size    = args['size']     || config.default_size || '1584x672';
let prompt  = args['prompt']   || '';
const briefPath = args['brief'] || '';
const theme   = args['theme']    || 'custom';
const name    = args['name']     || '';
const outDir  = args['out']      || config.output_dir || path.join(process.cwd(), 'assets', 'covers');
const quiet   = !!args['quiet'];
const crop    = !!args['crop'];

function log(msg) { if (!quiet) console.log(msg); }

if (!briefPath) {
  console.error('A validated final --brief JSON file is required. Prompt-only delivery does not use this adapter.');
  process.exit(1);
}

let brief;
try {
  brief = JSON.parse(fs.readFileSync(briefPath, 'utf8'));
} catch (err) {
  console.error('Could not read --brief JSON: ' + err.message);
  process.exit(1);
}
if (brief.input_quality !== 'final' || !brief.image_prompt || !brief.theme || !brief.title) {
  console.error('The brief is not final or is missing image_prompt, theme, or title data. Run validate_brief.py first.');
  process.exit(1);
}
prompt = brief.image_prompt;

// ---------- 前置校验 ----------
if (!prompt) {
  console.error('❌ 缺少 --prompt。');
  console.error('   用法：node scripts/generate-cover.js --prompt "<英文prompt>" [--theme theme3] [--name 自定义名]');
  process.exit(1);
}
if (!apiKey) {
  console.error('❌ 未配置 API Key。两种配置方式（任选其一）：');
  console.error('   1) 环境变量：OPENAI_API_KEY=sk-xxx（Windows: set OPENAI_API_KEY=sk-xxx）');
  console.error('   2) 配置文件：在 scripts/ 目录创建 config.json：{"api_key": "sk-xxx"}');
  console.error('   国内 provider 同时设置 OPENAI_BASE_URL（智谱 / 阿里百炼 / 硅基流动等，详见 README）');
  process.exit(1);
}

// ---------- 工具 ----------
function timestamp() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`;
}

// ---------- 主流程 ----------
async function main() {
  const url = `${baseUrl.replace(/\/+$/, '')}/images/generations`;
  log(`🖼️   调用 ${url}`);
  log(`    model=${model}  size=${size}`);

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 60000); // 60s 超时

  let res;
  try {
    res = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        prompt,
        n: 1,
        size,
        response_format: 'b64_json',
      }),
      signal: controller.signal,
    });
  } catch (err) {
    clearTimeout(timer);
    if (err.name === 'AbortError') {
      console.error('❌ 请求超时（60s）。若直连 OpenAI 网络受限，请配置国内兼容 provider 的 OPENAI_BASE_URL（见 README）。');
    } else {
      console.error('❌ 网络请求失败：' + err.message);
    }
    process.exit(1);
  }
  clearTimeout(timer);

  if (!res.ok) {
    const body = await res.text().catch(() => '');
    console.error(`❌ HTTP ${res.status}`);
    console.error(`   响应体（透传 provider 信息，便于排查 model/size 是否支持）：${body.slice(0, 1000)}`);
    process.exit(1);
  }

  const json = await res.json().catch(() => null);
  if (!json || !Array.isArray(json.data) || json.data.length === 0) {
    console.error('❌ 响应中无 data 数组。响应摘要：' + JSON.stringify(json).slice(0, 500));
    process.exit(1);
  }

  // 兼容 b64_json 与 url 两种响应
  let buffer = null;
  if (json.data[0].b64_json) {
    buffer = Buffer.from(json.data[0].b64_json, 'base64');
  } else if (json.data[0].url) {
    log('⏬ 响应为 url 形式，二次拉取图片…');
    const imgRes = await fetch(json.data[0].url);
    if (!imgRes.ok) {
      console.error('❌ 拉取图片失败：HTTP ' + imgRes.status);
      process.exit(1);
    }
    buffer = Buffer.from(await imgRes.arrayBuffer());
  } else {
    console.error('❌ 响应中既无 b64_json 也无 url，无法保存。');
    process.exit(1);
  }

  // ---------- 落盘 ----------
  fs.mkdirSync(outDir, { recursive: true });
  const baseName = name || `${theme}-${timestamp()}`;
  const pngPath = path.join(outDir, `cover-${baseName}.png`);
  fs.writeFileSync(pngPath, buffer);

  const memoPath = path.join(outDir, `cover-${baseName}.prompt.txt`);
  fs.writeFileSync(memoPath, `# cover prompt (wechat-cover-design)\nmodel: ${model}\nsize: ${size}\ntheme: ${brief.theme.id || theme}\n\n${prompt}\n\n# title overlay (post-production)\nmain title: ${brief.title.exact_text}\nsubtitle: ${brief.title.subtitle || 'None'}\nzone: ${brief.title.zone}\ntype mood: ${brief.title.type_mood}\ntype palette: ${brief.title.type_palette}\nintegration device: ${brief.title.integration_device}\n`);

  log(`✅ 已保存: ${pngPath}`);
  log(`📝 备忘: ${memoPath}`);

  // ---------- 微信 2.35:1 裁剪/补边指引 ----------
  const match = String(size).match(/^(\d+)x(\d+)$/i);
  if (match) {
    const width = Number(match[1]);
    const height = Number(match[2]);
    const actualRatio = width / height;
    const targetRatio = 2.35;
    const tolerance = 0.02;
    if (Math.abs(actualRatio - targetRatio) <= tolerance) {
      console.log(`\n✅   画幅接近微信封面比例：${width}x${height}（${actualRatio.toFixed(3)}:1）。无需裁剪。`);
    } else if (actualRatio < targetRatio) {
      const targetH = Math.round(width / targetRatio);
      const cropH = Math.max(0, Math.round((height - targetH) / 2));
      console.log(`\n✂️   微信约 2.35:1 裁剪指引（当前 ${width}x${height} = ${actualRatio.toFixed(3)}:1）：`);
      console.log(`  保持宽度 ${width}px，将高度裁到约 ${targetH}px；上下居中各裁约 ${cropH}px。`);
      console.log('  构图时把标题和关键元素放在画面中部 60% 安全区，避免顶部/底部被裁。');
      if (crop) {
        console.log('  ⚠️  --crop 自动居中裁剪仍需可选依赖 sharp；未安装则只输出本指引。');
      }
    } else {
      const targetW = Math.round(height * targetRatio);
      const padW = Math.max(0, Math.round((width - targetW) / 2));
      console.log(`\n↔️   微信约 2.35:1 补边/裁剪指引（当前 ${width}x${height} = ${actualRatio.toFixed(3)}:1）：`);
      console.log(`  可将宽度裁到约 ${targetW}px（左右各裁约 ${padW}px），或在左右补边后再发布。`);
    }
  } else {
    console.log(`\n✂️   自定义尺寸「${size}」无法解析：请按 provider 实际输出宽高确认是否接近 2.35:1。`);
  }
}

main().catch((err) => {
  console.error('❌ 未预期错误：' + err.message);
  process.exit(1);
});
