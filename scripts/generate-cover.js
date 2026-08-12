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
const size    = args['size']     || config.default_size || '1792x1024';
const prompt  = args['prompt']   || '';
const theme   = args['theme']    || 'custom';
const name    = args['name']     || '';
const outDir  = args['out']      || config.output_dir || path.join(process.cwd(), 'assets', 'covers');
const quiet   = !!args['quiet'];
const crop    = !!args['crop'];

function log(msg) { if (!quiet) console.log(msg); }

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
  fs.writeFileSync(memoPath, `# cover prompt (wechat-cover-design)\nmodel: ${model}\nsize: ${size}\n\n${prompt}\n`);

  log(`✅ 已保存: ${pngPath}`);
  log(`📝 备忘: ${memoPath}`);

  // ---------- 微信 2.35:1 裁剪指引 ----------
  if (/^1792x1024$/i.test(size)) {
    const targetH = Math.round(1792 / 2.35);     // ≈ 763px
    const cropH = Math.round((1024 - targetH) / 2); // ≈ 131px
    console.log('\n✂️   微信 2.35:1 裁剪指引（当前 1792x1024 = 1.75:1）：');
    console.log(`  目标高度 ≈ ${targetH}px（宽度 1792 不变），上下居中各裁约 ${cropH}px。`);
    console.log('  构图时请把核心标题/元素放在画面中部安全区，避免顶/底被裁。');
    if (crop) {
      console.log('  ⚠️  --crop 自动居中裁剪需可选依赖 sharp；未安装则跳过，仅输出本指引。');
    }
  } else if (!/^\d+x\d+$/i.test(size)) {
    console.log(`\n✂️   自定义尺寸「${size}」：请按 provider 文档确认实际输出比例是否接近 2.35:1。`);
  }
}

main().catch((err) => {
  console.error('❌ 未预期错误：' + err.message);
  process.exit(1);
});
