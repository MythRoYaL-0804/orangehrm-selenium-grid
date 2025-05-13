# XPATH_CONFIRM_DELETE_BUTTON ="//button[contains(@class, 'ConfirmGroupModal-module') and normalize-space() = '削除']"
# XPATH_CONFIRM_CANCEL_BUTTON ="//button[contains(@class, 'ConfirmGroupModal-module') and normalize-space() = 'キャンセル']"


# =====================
# ✅ CSS Selectors
# =====================
CSS_LOGIN_USERNAME_INPUT = "input[name='username']"
CSS_LOGIN_PASSWORD_INPUT = "input[name='password']"
CSS_LOGIN_SUBMIT_BUTTON = "button[type='submit']"
CSS_LOGIN_FORM_CONTAINER = "div.orangehrm-login-form"
# =====================
# ✅ XPath Selectors
# =====================
XPATH_LOGIN_ERROR = "//p[text()='Invalid credentials']"
XPATH_USERNAME_REQUIRED_ERROR = "//input[@name='username']/following::span[text()='Required']"
XPATH_PASSWORD_REQUIRED_ERROR = "//input[@name='password']/following::span[text()='Required']"
XPATH_DASHBOARD_HEADER = "//h6[text()='Dashboard']"
XPATH_LOADING_SPINNER = "//div[contains(@class, 'oxd-loading-spinner')]"