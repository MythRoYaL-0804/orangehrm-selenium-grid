import allure
import datetime
import os
import inspect
from common.utils.logs.logger import setup_logger
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional

logger = setup_logger(__name__)

def take_screenshot(driver: WebDriver, test_case_name, status, browser_name):
    """
    Chụp ảnh màn hình và lưu vào thư mục screenshots/{date}/{module}/{file}/
    """
    try:
        # ⛔ Kiểm tra cấu hình cho phép chụp ảnh không
        if os.getenv("ENABLE_SCREENSHOT", "true").lower() != "true":
            logger.info("[ℹ️] Chụp screenshot đang tắt trong .env (ENABLE_SCREENSHOT=false)")
            return
        
        date_str = datetime.datetime.now().strftime("%Y%m%d")

        current_frame = inspect.currentframe()
        
        file_path: Optional[str] = None
        
        while current_frame:
            candidate = inspect.getfile(current_frame)
            if "tests" in candidate:
                file_path = candidate
                break
            current_frame = current_frame.f_back

        if not file_path:
            raise FileNotFoundError("❌ Không thể xác định file test để lưu screenshot")

        test_file = os.path.normpath(file_path)
        parts = test_file.split(os.sep)
        test_module = parts[parts.index("tests") + 1] if "tests" in parts else "unknown"
        test_file_name = os.path.splitext(parts[-1])[0].replace("test_", "") if parts else "unknown"

        folder_path = os.path.join("screenshots", date_str, test_module, test_file_name)
        os.makedirs(folder_path, exist_ok=True)

        file_name = f"{test_case_name}_{status}_{browser_name}_{datetime.datetime.now().strftime('%H%M%S')}.png"
        full_path = os.path.join(folder_path, file_name)

        driver.save_screenshot(full_path)
        allure.attach.file(full_path, name=file_name, attachment_type=allure.attachment_type.PNG)
        logger.info(f"[📸] Đã lưu screenshot tại: {full_path}")   
    except Exception as e:
        logger.error(f"[⚠️] Lỗi khi chụp screenshot: {e}")
   