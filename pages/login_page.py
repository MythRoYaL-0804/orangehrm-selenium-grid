from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.selectors.login_selectors import *
from common.waits.wait_utils import wait_until_visible, wait_until_clickable

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def wait_for_login_ready(self):
        """Chờ khung login hiển thị để đảm bảo trang sẵn sàng thao tác"""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CSS_LOGIN_FORM_CONTAINER)))

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, CSS_LOGIN_USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, CSS_LOGIN_PASSWORD_INPUT).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, CSS_LOGIN_SUBMIT_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def invalid_credentials_displayed(self):
        error = self.wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_LOGIN_ERROR)))
        return error.is_displayed()

    def username_required_displayed(self):
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_USERNAME_REQUIRED_ERROR)))
        return el.is_displayed()

    def password_required_displayed(self):
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_PASSWORD_REQUIRED_ERROR)))
        return el.is_displayed()
    
    def verify_login_success(self):
        return wait_until_visible(self.driver, (By.XPATH, XPATH_DASHBOARD_HEADER))

