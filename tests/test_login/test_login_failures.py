import os
import pytest
import inspect
from dotenv import load_dotenv
from common.base.base_test import BaseTest
from pages.login_page import *
from common.exceptions.exception_handler import handle_exceptions
from common.utils.logs.logger import setup_logger
from common.utils.screenshots.screenshot_utils import take_screenshot

load_dotenv()

URL = os.getenv("ORANGEHRM_URL")
INVALID_USERNAME = os.getenv("INVALID_USERNAME")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
SPECIAL_CHAR_PASSWORD = os.getenv("SPECIAL_CHAR_PASSWORD")

logger = setup_logger(__name__)

class TestLoginFailures(BaseTest):

    @handle_exceptions
    def test_login_empty_fields(self):
        logger.info("🧪 Test: Login với username và password để trống")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.click_submit()
        assert login_page.username_required_displayed()
        assert login_page.password_required_displayed()
        logger.info("✅ Hiển thị lỗi required cho cả username và password")
        self.capture_screenshot("passed")


    @handle_exceptions
    def test_login_invalid_credentials(self):
        logger.info("🧪 Test: Login với thông tin sai")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        assert login_page.invalid_credentials_displayed()
        logger.info("✅ Hiển thị lỗi đăng nhập không hợp lệ")
        self.capture_screenshot("passed")

        
    @handle_exceptions
    def test_login_invalid_email_format(self):
        logger.info("🧪 Test: Login với định dạng email không hợp lệ")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.login("invalid-email", "somepassword")
        assert login_page.invalid_credentials_displayed()
        logger.info("✅ Hiển thị lỗi cho định dạng email sai")
        self.capture_screenshot("passed")


    @handle_exceptions
    def test_login_special_characters_in_password(self):
        logger.info("🧪 Test: Login với password có ký tự đặc biệt")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.login("admin", SPECIAL_CHAR_PASSWORD)
        assert login_page.invalid_credentials_displayed()
        logger.info("✅ Hiển thị lỗi với password đặc biệt")
        self.capture_screenshot("passed")


    @handle_exceptions
    def test_login_only_password_filled(self):
        logger.info("🧪 Test: Chỉ nhập password")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.enter_password("admin123")
        login_page.click_submit()
        assert login_page.username_required_displayed()
        logger.info("✅ Hiển thị lỗi thiếu username")
        self.capture_screenshot("passed")


    @handle_exceptions
    def test_login_only_username_filled(self):
        logger.info("🧪 Test: Chỉ nhập username")
        login_page = LoginPage(self.driver, self.wait)
        self.driver.get(URL)
        login_page.wait_for_login_ready() 
        login_page.enter_username("admin")
        login_page.click_submit()
        assert login_page.password_required_displayed()
        logger.info("✅ Hiển thị lỗi thiếu password")
        self.capture_screenshot("passed")


compile