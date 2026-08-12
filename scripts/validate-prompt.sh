#!/bin/bash
# validate-prompt.sh — wechat-cover-design prompt 质量校验
# 用法：
#   echo "<prompt>" | bash validate-prompt.sh --all
#   echo "<prompt>" | bash validate-prompt.sh --no-placeholders
#   echo "<prompt>" | bash validate-prompt.sh --has-negative
#   echo "<prompt>" | bash validate-prompt.sh --has-ratio
#   echo "<prompt>" | bash validate-prompt.sh --length
# 任一子校验失败时退出码为 1；--all 全绿退出码为 0。

MODE=$1
INPUT=$(cat)

# 字符数（含多字节，按字节计已足够用于区间判断）
char_count=$(echo "$INPUT" | wc -c)

fail=0

check_no_placeholders() {
  # 残留 {占位符} 是最高频失误：grep 到任意 {xxx} 即失败
  if echo "$INPUT" | grep -qE '\{[^}]*\}'; then
    echo "❌ 存在残留占位符 {xxx}，请全部替换后再交付。"
    return 1
  else
    echo "✅ 无残留占位符。"
    return 0
  fi
}

check_has_negative() {
  if echo "$INPUT" | grep -qi 'negative prompt'; then
    echo "✅ 包含 Negative prompt。"
    return 0
  else
    echo "❌ 缺少 Negative prompt。"
    return 1
  fi
}

check_has_ratio() {
  if echo "$INPUT" | grep -qiE '21:9|2\.35:1|900x383|1260x540'; then
    echo "✅ 包含画幅描述（21:9 / 微信 2.35:1）。"
    return 0
  else
    echo "❌ 未检测到画幅描述（21:9 / 2.35:1 / 900x383 / 1260x540）。"
    return 1
  fi
}

check_length() {
  if [ "$char_count" -ge 300 ] && [ "$char_count" -le 4000 ]; then
    echo "✅ 长度合规（${char_count} 字节，合理区间 300-4000）。"
    return 0
  else
    echo "❌ 长度异常（${char_count} 字节，合理区间 300-4000），疑似缺段落或重复冗余。"
    return 1
  fi
}

case "$MODE" in
  --no-placeholders) check_no_placeholders; exit $? ;;
  --has-negative)    check_has_negative;    exit $? ;;
  --has-ratio)       check_has_ratio;       exit $? ;;
  --length)          check_length;          exit $? ;;
  --all)
    check_no_placeholders || fail=1
    check_has_negative    || fail=1
    check_has_ratio       || fail=1
    check_length          || fail=1
    echo ""
    if [ "$fail" -eq 0 ]; then
      echo "🎉 全部校验通过。"
      exit 0
    else
      echo "⚠️  存在未通过的校验项，请修正后重跑。"
      exit 1
    fi
    ;;
  *)
    echo "用法："
    echo "  echo '<prompt>' | bash validate-prompt.sh --all"
    echo "  echo '<prompt>' | bash validate-prompt.sh --no-placeholders"
    echo "  echo '<prompt>' | bash validate-prompt.sh --has-negative"
    echo "  echo '<prompt>' | bash validate-prompt.sh --has-ratio"
    echo "  echo '<prompt>' | bash validate-prompt.sh --length"
    exit 1
    ;;
esac
