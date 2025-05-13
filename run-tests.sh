#!/bin/bash

# ================================
# 📅 Tạo thư mục báo cáo theo ngày và giờ
# ================================
DATE_DIR=$(date +"%Y%m%d")
TIMESTAMP=$(date +"%H%M%S")
REPORT_DIR="reports/${DATE_DIR}"
mkdir -p "$REPORT_DIR"

# Link tắt đến báo cáo mới nhất
rm -f reports/latest
ln -s "$REPORT_DIR" reports/latest

# ================================
# 🌐 Trình duyệt cần test
# ================================
BROWSERS=("chrome" "edge")
PIDS=()
OVERALL_EXIT_CODE=0

# ================================
# 🚀 Khởi động Selenium Grid
# ================================
echo "🚀 Starting Selenium Grid infrastructure..."
docker-compose up -d selenium-hub chrome-node edge-node

# 🔁 Đợi selenium-hub sẵn sàng (tốt hơn sleep)
echo "⏳ Waiting for selenium-hub to be ready..."
until curl -s http://localhost:4444/wd/hub/status | grep -q '"ready":true'; do
  echo "⌛ Hub not ready, retrying..."
  sleep 2
done
echo "✅ Selenium Grid is ready!"

# ================================
# 🧪 Chạy test cho từng browser
# ================================
run_tests_for_browser() {
    local browser=$1
    echo "🔸 Running tests on: $browser"
    
    docker-compose run --rm -T test-runner pytest \
        -v \
        -s \
        -n 2 \
        --dist loadscope \
        --browser="$browser" \
        --html="${REPORT_DIR}/report_${browser}_${TIMESTAMP}.html" \
        --self-contained-html \
        --capture=tee-sys \
        --log-cli-level=INFO \
        --log-cli-format="%(asctime)s [%(levelname)s] %(message)s" \
        --log-cli-date-format="%Y-%m-%d %H:%M:%S" \
        tests/
    
    return $?
}

# 🔁 Chạy song song các trình duyệt
for browser in "${BROWSERS[@]}"; do
    run_tests_for_browser "$browser" &
    PIDS+=($!)
done

# 🧵 Đợi tất cả kết thúc
for PID in "${PIDS[@]}"; do
    wait $PID || OVERALL_EXIT_CODE=1
done

# ================================
# 🧹 Dọn selenium grid
# ================================
echo "🧹 Cleaning up containers..."
docker-compose down

# ================================
# 📢 In báo cáo
# ================================
echo "============================================="
for browser in "${BROWSERS[@]}"; do
    echo "📄 Test report for $browser → ${REPORT_DIR}/report_${browser}_${TIMESTAMP}.html"
done
echo "============================================="

# ================================
# ✅ Thông báo kết quả
# ================================
if [ "$OVERALL_EXIT_CODE" == "0" ]; then
    echo "✅ All tests PASSED successfully!"
else
    echo "❌ Some tests FAILED. Please check the reports above."
fi

exit $OVERALL_EXIT_CODE
