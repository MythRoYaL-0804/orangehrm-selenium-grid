from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.selectors.admin.user_management_selectors import *

class UserManagementSearch:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
    def search_user(self, username=None, user_role=None, status=None):
        if username:
            username_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_SEARCH_USERNAME_INPUT)))
            username_input.clear()
            username_input.send_keys(username)

        if user_role:
            self.wait.until(EC.element_to_be_clickable(XPATH_SEARCH_USER_ROLE_DROPDOWN)).click()
            self.wait.until(EC.element_to_be_clickable(USER_ROLE_OPTION(user_role))).click()

        if status:
            self.wait.until(EC.element_to_be_clickable(STATUS_DROPDOWN)).click()
            self.wait.until(EC.element_to_be_clickable(STATUS_OPTION(status))).click()

        self.wait.until(EC.element_to_be_clickable(XPATH_SEARCH_BUTTON)).click()
        
    def verify_user_exists(self, expected_username):
        elements = self.wait.until(EC.presence_of_all_elements_located(USER_TABLE_USERNAME_CELLS))
        return any(expected_username in el.text for el in elements)

    def is_no_result_displayed(self):
        return self.wait.until(EC.presence_of_element_located(NO_RECORD_FOUND)).is_displayed()

    def get_all_users(self):
        rows = self.driver.find_elements(*USER_TABLE_ROWS)
        user_data = []
        for row in rows:
            cells = row.find_elements(By.XPATH, "./div")
            if len(cells) >= 6:
                user_data.append({
                    "username": cells[1].text,
                    "role": cells[2].text,
                    "status": cells[5].text,
                })
        return user_data
