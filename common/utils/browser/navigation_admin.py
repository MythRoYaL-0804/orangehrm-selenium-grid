from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.selectors.admin.user_management_selectors import *
from common.utils.waits.wait_admin import *

def navigate_to_user_management(wait: WebDriverWait):
    """
    Điều hướng từ dashboard vào Admin → User Management → Users
    """
    wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_ADMIN_MENU_BUTTON))).click()
    
    wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_USER_MANAGEMENT_SUBMENU))).click()
    
    wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_USER_MANAGEMENT_NAV_LINK))).click()
    
    wait_for_user_management_loaded(wait)