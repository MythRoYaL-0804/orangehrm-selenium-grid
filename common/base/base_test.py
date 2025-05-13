import os
import pytest
import socket
import inspect
from dotenv import load_dotenv
from common.utils.logs.logger import setup_logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from common.utils.screenshots.screenshot_utils import take_screenshot

load_dotenv()
logger = setup_logger(__name__)
BASE_URL = os.getenv("ORANGEHRM_URL")

class BaseTest:
    
    @pytest.fixture(autouse=True)
    def setup_driver(self, request):
        """Setup WebDriver for Selenium Grid with configured browser and environment."""
        """Thiết lập WebDriver cho Selenium Grid với trình duyệt và môi trường đã được cấu hình."""
        
        browser = os.getenv("BROWSER", "chrome")
        
        environment = os.getenv("ENVIRONMENT", "local")
        
        grid_url = "http://selenium-hub:4444/wd/hub" if environment != "local" else "http://localhost:4444/wd/hub"
        wait_timeout = int(os.getenv("WAIT_TIMEOUT", "10"))
        
        self.browser_name = browser
        self.screenshot_dir = os.getenv("SCREENSHOT_DIR", "screenshots")
        
        # Tạo options tương ứng với browser (Chrome / Edge / Firefox)
        options = self._get_browser_options(browser)
        logger.info(f"🔧 Khởi tạo WebDriver [{browser.upper()}] cho môi trường [{environment.upper()}]")
        
        # Tạo Remote WebDriver kết nối tới Selenium Grid
        self.driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )
        
        # WebDriverWait giúp chờ các element hiệu quả
        self.wait = WebDriverWait(self.driver, wait_timeout)
        self.browser_name = browser
        self.base_url = os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com")
        # Gán vào request.cls để sử dụng trong test class
        # if hasattr(request, "cls"):
        #     request.cls = self
        #     request.cls.driver = self.driver
        #     request.cls.wait = self.wait
        #     request.cls.base_url = BASE_URL

        if request.cls is not None:
            request.cls.driver = self.driver
            request.cls.wait = self.wait
            request.cls.base_url = os.getenv("ORANGEHRM_URL")
            request.cls.browser_name = self.browser_name
            request.cls.screenshot_dir = self.screenshot_dir
                    
        yield
        
        # Nếu test bị fail → chụp ảnh màn hình
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                take_screenshot(self.driver, request.node.name, "fail", self.browser_name)
            except Exception as e:
                print(f"[⚠️] Không thể chụp screenshot: {e}")
        # Đóng browser sau khi chạy xong test
        self.driver.quit()
        
    
    def _get_browser_options(self, browser):
        """Tạo browser options phù hợp với từng trình duyệt (Chrome, Edge, Firefox)"""
        # Đọc biến HEADLESS từ môi trường để biết có cần chạy không giao diện
        headless_env = os.getenv("HEADLESS", "false").lower()  == "true" or not os.getenv("DISPLAY")
        
        hostname = socket.gethostname()

        if hostname.startswith("selenium"):
            headless_env = True
        
        # Tạo options tương ứng với trình duyệt
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "edge":
            options = EdgeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        else:
            raise ValueError(f"❌ Trình duyệt không được hỗ trợ: {browser}")
        
        # Các cấu hình chung cho mọi trình duyệt
        options.add_argument("--start-maximized")            # Phóng to màn hình
        options.add_argument("--disable-gpu")                # Tránh lỗi đồ họa trong môi trường CI
        options.add_argument("--no-sandbox")                 # Bắt buộc khi chạy trong Docker
        options.add_argument("--disable-dev-shm-usage")      # Tránh lỗi bộ nhớ chia s  ẻ thấp trong Docker
        
        # Chống bị detect automation (chỉ áp dụng cho Chrome & Edge)
        if browser in ["chrome", "edge"]:
            options.add_argument("--disable-infobars")       # Xóa thanh automation warning
            options.add_argument("--disable-extensions")     # Tắt tất cả extension
            options.add_argument("--disable-blink-features=AutomationControlled")  # Ngăn JS detect webdriver
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_argument(
                "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/90.0.4430.93 Safari/537.36"
            )
            
        if headless_env:
            if browser == "chrome":
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            elif browser == "edge":
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            elif browser == "firefox":
                options.add_argument("--headless")
        
        return options
    
    def capture_screenshot(self, status: str):
        """Tự động chụp screenshot cho test case hiện tại với trạng thái passed/failed/assert"""
        test_case_name = inspect.currentframe().f_back.f_code.co_name
        take_screenshot(self.driver, test_case_name, status, self.browser_name)