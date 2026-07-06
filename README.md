# Tichi Test Automation

## Project Overview

This project automates the **Login** and **Signup** functionalities of the **Tichi Web Application** using **Python, Selenium WebDriver, and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern to organize the automation code and improve maintainability.

---

## Tools Used

- Python
- Selenium WebDriver
- Pytest
- ChromeDriver
- VS Code

---

## Project Structure

```
Tichi_Test_Automation
│
├── pages/
│   ├── login_page.py
│   └── signup_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_signup.py
│
├── utilities/
│   └── driver_factory.py
│
├── report.pdf
├── Defect_Report.docx
├── QA_Test_Cases_Tichi.xlsx
├── requirements.txt
└── README.md
```

---

## Test Scenarios

### Login Module

- Empty Email
- Invalid Email
- Invalid Email (Missing @)
- Invalid Email (Missing Domain)
- Valid Login
- Empty Password
- Incorrect Password
- Page Title Validation
- URL Validation

### Signup Module

- Empty Email
- Invalid Email
- Valid Email
- Empty First Name
- Empty Password
- Password Mismatch
- Invalid Mobile Number
- Terms & Conditions Checkbox Validation

---

## Test Execution Summary

- Total Test Cases : **17**
- Passed : **17**
- Failed : **0**

---

## Documents Included

- Test Cases
- Defect Report
- Test Execution Report

---

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run all test cases:

```bash
pytest
```

Generate HTML Report:

```bash
pytest --html=report.html --self-contained-html
```

---

## Author

**Keerthana**

Python | Selenium | Pytest
