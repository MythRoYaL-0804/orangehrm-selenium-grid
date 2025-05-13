import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lấy timeout từ .env, nếu không có thì mặc định 10 giây
DEFAULT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", 10))

def wait_until_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Chờ element xuất hiện và hiển thị (displayed + visible)."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    
def wait_until_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Chờ element có thể click được (visible + enabled)."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    
def wait_until_present(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Chờ element có mặt trong DOM (dù có thể chưa visible)."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    
def wait_until_invisible(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Chờ element biến mất (không còn trong DOM hoặc bị ẩn)."""
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )