from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

# =========================
# 🔐 Thông tin đăng nhập
# =========================
VALID_EMAIL = os.getenv("VALID_EMAIL")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
INVALID_USERNAME = os.getenv("INVALID_USERNAME")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
SPECIAL_CHAR_PASSWORD = os.getenv("SPECIAL_CHAR_PASSWORD")

# =========================
# 🌐 Base URL và các route quan trọng
# =========================
BASE_URL = os.getenv("ORANGEHRM_URL", "").rstrip("/")  # Xóa dấu "/" cuối nếu có

LOGIN_URL = f"{BASE_URL}/login"
DASHBOARD_URL = f"{BASE_URL}/dashboard"
USER_MANAGEMENT_URL = f"{BASE_URL}/admin/viewSystemUsers"
ADD_USER_URL = f"{BASE_URL}/admin/saveSystemUser"
