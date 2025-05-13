from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.selectors.admin.user_management_selectors import *
from selenium.webdriver.common.by import By
from common.utils.waits.wait_loading_disappear import *

def wait_for_user_management_loaded(wait: WebDriverWait):
    """
    Chờ trang User Management (Admin > Users) được load hoàn tất.
    """
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    wait_for_dashboard_to_stabilize(wait)
    wait.until(EC.presence_of_element_located(XPATH_SEARCH_BUTTON))
