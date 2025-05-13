from selenium.webdriver.common.by import By

# === Navigation ===
XPATH_ADMIN_MENU_BUTTON = "//span[text()='Admin']"
XPATH_USER_MANAGEMENT_SUBMENU = "//span[normalize-space()='User Management']"
XPATH_USER_MANAGEMENT_NAV_LINK = "//a[normalize-space()='Users']"

# === Search ===
XPATH_SEARCH_USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
XPATH_SEARCH_USER_ROLE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'oxd-select-wrapper')]")
USER_ROLE_OPTION = lambda role: (By.XPATH, f"//div[@role='option']//span[text()='{role}']")

STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class,'dropdown')]")
STATUS_OPTION = lambda status: (By.XPATH, f"//div[@role='option']//span[text()='{status}']")


XPATH_SEARCH_BUTTON = (By.XPATH,"//button[normalize-space()='Search']")
XPATH_RESET_BUTTON = (By.XPATH,"//button[normalize-space()='Reset']")

USER_TABLE_USERNAME_CELLS = (By.XPATH, "//div[@role='table']//div[@class='oxd-table-cell' and text()]")
NO_RECORD_FOUND = (By.XPATH, "//span[normalize-space()='No Records Found']")
USER_TABLE_ROWS = (By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card")