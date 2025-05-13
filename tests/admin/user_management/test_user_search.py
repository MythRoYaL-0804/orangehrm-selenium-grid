import pytest
from pages.admin.user_management.user_search_page import UserManagementSearch
from common.utils.browser.navigation_admin import navigate_to_user_management
from pages.login_page import LoginPage
from common.base.base_test import BaseTest

@pytest.mark.usefixtures("setup_driver")  # RẤT QUAN TRỌNG
class TestUserSearch(BaseTest):

    @pytest.fixture(autouse=True)
    def login_and_go_to_user_list(self, request):
        driver = request.cls.driver
        wait = request.cls.wait
        base_url = request.cls.base_url

        driver.get(f"{base_url}/login")

        login_page = LoginPage(driver, wait)
        login_page.login("Admin", "admin123")
        navigate_to_user_management(driver, wait)

    def test_search_exact_username(self):
        page = UserManagementSearch(self.driver, self.wait)
        page.search_user(username="Admin")
        assert page.verify_user_exists("Admin")

    def test_search_by_role_admin(self):
        page = UserManagementSearch(self.driver, self.wait)
        page.search_user(user_role="Admin")
        users = page.get_all_users()
        assert all("Admin" in user["role"] for user in users)

    def test_search_by_status_enabled(self):
        page = UserManagementSearch(self.driver, self.wait)
        page.search_user(status="Enabled")
        users = page.get_all_users()
        assert all("Enabled" in user["status"] for user in users)

    def test_search_non_existing_user(self):
        page = UserManagementSearch(self.driver, self.wait)
        page.search_user(username="non_existing_user_123")
        assert page.is_no_result_displayed()
