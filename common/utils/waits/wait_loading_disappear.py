from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.selectors.login_selectors import XPATH_LOADING_SPINNER
from common.utils.logs.logger import setup_logger

logger = setup_logger(__name__)

def wait_for_dashboard_to_stabilize(driver, timeout=10):
    """Wait until all loading indicators (spinner) are invisible"""
    """Chờ cho đến khi tất cả các chỉ báo tải (spinner) đều vô hình"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.XPATH, XPATH_LOADING_SPINNER))
        )
        logger.info("[✅] Đã chờ loading hoàn tất")
    except Exception as e:
        logger.warning(f"[⚠️] Loading không biến mất sau {timeout}s: {e}")
        raise   