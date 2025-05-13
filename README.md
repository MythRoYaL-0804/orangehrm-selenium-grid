# 🧪 OrangeHRM Selenium Grid Automation

Automation test project for [OrangeHRM](https://opensource-demo.orangehrmlive.com/) using **Selenium Grid**, **Docker**, **Pytest**, and **Allure Report**.

## 📁 Project Structure

```
orangehrm-selenium-grid/
├── base/                    # Base test setup & webdriver
├── common/                  # Common selectors & reusable functions
├── tests/                   # Organized test cases by feature/module
│   └── admin/
│       └── user_management/
│   └── test_login/
│       └──test_login_success.py
├── utils/                   # Browser, wait, screenshot utilities
├── assets/                  # Test data & images
├── .env                     # Environment config
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
├── run-tests.sh             # Shell script to run tests
└── docker-compose.yml       # Selenium Grid + test container
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- Docker + Docker Compose
- Git
- Google Chrome / Edge

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Test Locally

```bash
pytest -v tests/admin/user_management/test_user_search.py
```

### 🌐 Run on Selenium Grid via Docker

```bash
./run-tests.sh
```

---

## 📊 Generate Allure Report

```bash
allure serve allure-results
```

---

## ⚙️ Environment Variables (.env)

```env
ORANGEHRM_URL=https://opensource-demo.orangehrmlive.com/
ADMIN_USER=Admin
ADMIN_PASSWORD=admin123
ENVIRONMENT=docker
HEADLESS=false
```

---

## 📌 Notes

- Screenshots are saved in `/screenshot/` folder but are excluded from Git via `.gitignore`
- Project supports multi-browser via parameterized fixtures

---

## ✨ Credits

Maintained by Chuong. Contributions welcome!
