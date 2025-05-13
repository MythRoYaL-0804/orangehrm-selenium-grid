from pages.login_page import LoginPage
from common.utils.waits.wait_loading_disappear import wait_for_dashboard_to_stabilize

def login_success(driver, wait, username, password):
    """
    Đăng nhập và kiểm tra thành công. Dùng ở mọi test case.
    """
    login_page = LoginPage(driver, wait)
    login_page.wait_for_login_ready()
    login_page.login(username, password)
    wait_for_dashboard_to_stabilize(driver)
    dashboard = login_page.verify_login_success()
    assert dashboard.is_displayed(), "⚠️ Login failed: Dashboard header not visible"