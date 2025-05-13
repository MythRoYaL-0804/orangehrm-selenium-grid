import os
import pytest
import inspect
from dotenv import load_dotenv
from common.base.base_test import BaseTest
from pages.login_page import *
from common.exceptions.exception_handler import handle_exceptions
from common.utils.logs.logger import setup_logger
from common.utils.waits.wait_loading_disappear import *
from common.utils.screenshots.screenshot_utils import take_screenshot

load_dotenv()

# Đọc biến từ file .env
URL = os.getenv("ORANGEHRM_URL")
USERNAME = os.getenv("ADMIN_USER")
PASSWORD = os.getenv("ADMIN_PASSWORD")

logger = setup_logger(__name__)

class TestLoginSuccess(BaseTest):
    
    @handle_exceptions
    def test_login_success(self):
        logger.info("🧪 Test: Đăng nhập với thông tin hợp lệ")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.login(USERNAME, PASSWORD)
        # Wait for Dashboard to load completely
        wait_for_dashboard_to_stabilize(self.driver)
        # Verify dashboard header
        dashboard_element =  login_page.verify_login_success()
        assert dashboard_element.is_displayed(), "⚠️ Dashboard header not visible after login"

        logger.info("✅ Login successful, dashboard is visible")
        self.capture_screenshot("passed")

