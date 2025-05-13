# 🔢 OrangeHRM Selenium Automation Project

This is a professional-grade automated testing framework for the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) application, supporting **E2E**, **BDD**, and **TDD** testing using **Selenium Grid**, **Pytest**, and **Behave**.

---

## 🏠 Project Structure

```
orangehrm-selenium/
|-- src/                        # Business logic for TDD
|   |-- login/
|   |   |-- login_logic.py
|   |-- admin/
|       |-- user_management/
|           |-- user_validator.py
|
|-- pages/                     # Page Objects (shared by all test types)
|   |-- login/
|   |   |-- login_page.py
|   |-- admin/
|       |-- user_management_page.py
|
|-- tests/
|   |-- e2e/                   # Classic Pytest Selenium UI test
|   |   |-- login/
|   |   |   |-- test_login_success.py
|   |   |-- admin/
|   |       |-- user_management/
|   |           |-- test_add_user.py
|
|   |-- bdd/                   # BDD using Behave
|   |   |-- login/
|   |   |   |-- login.feature
|   |   |   |-- steps/
|   |   |       |-- login_steps.py
|   |   |-- admin/
|   |       |-- user_management/
|   |           |-- user_management.feature
|   |           |-- steps/
|   |               |-- user_steps.py
|
|   |-- tdd/                   # Unit logic test (Test-Driven Development)
|       |-- login/
|       |   |-- test_login_logic.py
|       |-- admin/
|           |-- user_management/
|               |-- test_user_validation.py
|
|-- common/                   # Base classes, wait utils, logger, exceptions
|-- docker/                   # Docker & Selenium Grid setup (optional)
|-- .env
|-- pytest.ini
|-- behave.ini
|-- requirements.txt
|-- run-tests.sh
|-- README.md
```

---

## 🧭 Module Test Mapping

| Module             | E2E Test Path                              | BDD Feature Path                                  | TDD Unit Test Path                               |
|--------------------|---------------------------------------------|---------------------------------------------------|--------------------------------------------------|
| Login              | `tests/e2e/login/test_login_success.py`     | `tests/bdd/login/login.feature`                   | `tests/tdd/login/test_login_logic.py`            |
| Admin - Users      | `tests/e2e/admin/user_management/*.py`      | `tests/bdd/admin/user_management/*.feature`       | `tests/tdd/admin/user_management/*.py`           |

---

## 🧪 Test Types

### 🔹 TDD (Test-Driven Development)
- Unit test for business logic.
- Framework: **Pytest**
- Location: `tests/tdd/`

> Viết test cho logic trước khi code thật. Kiểm tra xử lý đúng/sai của đầu vào.

### 🔸 BDD (Behavior-Driven Development)
- End-to-end behavior testing using **Gherkin syntax**
- Framework: **Behave**
- Location: `tests/bdd/`

> Viết test theo ngôn ngữ Gherkin: Given - When - Then. Giao tiếp tốt với tester, BA, PO.

### 🔹 E2E (End-to-End Testing)
- UI Automation using Selenium Grid and Pytest.
- Location: `tests/e2e/`

> Kiểm tra tổng quan theo flow người dùng thật từ giao diện.

---

## 🔄 Run Tests By Module

Chạy E2E cho module Login:
```bash
pytest tests/e2e/login/
```

Chạy BDD cho module User Management:
```bash
behave tests/bdd/admin/user_management/
```

Chạy TDD cho module Leave:
```bash
pytest tests/tdd/leave/
```

---

## 🚀 How to Run Tests

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run TDD tests
```bash
pytest tests/tdd/
```

### 3️⃣ Run BDD tests
```bash
behave tests/bdd/
```

### 4️⃣ Run E2E tests
```bash
pytest tests/e2e/
```

---

## 📊 Environments

File `.env` sample:
```env
ORANGEHRM_URL=https://opensource-demo.orangehrmlive.com/
ADMIN_USER=Admin
ADMIN_PASSWORD=admin123
```

---

## ⚙️ CI/CD Support (Optional)

Project is designed to support:
- GitHub Actions
- Allure Reports
- Docker + Selenium Grid

---

## 📌 Author

Project created by **Nguyễn Chương** – QA Automation Engineer 
Built for OrangeHRM test coverage training & demonstration.

---

## ✅ License

This project is for **educational & demonstration** purposes.
