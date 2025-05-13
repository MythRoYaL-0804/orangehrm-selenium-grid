import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.exceptions.custom_exceptions import NavigationException
from common.utils.logs.logger import setup_logger


logger = setup_logger(__name__)

def navigate_to_orangehrm(driver, wait=None, timeout=10):
    """Navigate to the OrangeHRM URL and validate that page is loaded properly"""
    """Điều hướng đến URL OrangeHRM và xác thực rằng trang đã được tải đúng cách"""
    
    url = os.getenv("ORANGEHRM_URL")
    
    if not url:
        raise NavigationException("❌ ORANGEHRM_URL chưa thiết lập trong file .env")
    
    logger.info(f"🌐 Điều hướng đến URL: {url}")
    driver.get(url)
    
    if wait:
        try:
            WebDriverWait(driver, timeout).until(
                EC.any_of(
                    EC.title_contains("OrangeHRM"),
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            )
            logger.info(f"✅ Trang OrangeHRM đã load thành công")
        except Exception as e:
            raise NavigationException(f"❌ Lỗi tải trang OrangeHRM: {e}")