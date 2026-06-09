# Hybrid Test Framework — automationexercise.com

## Architecture

```
hybrid_framework/
│
├── POM/                        # Page Object Models (one class per page)
│   ├── login_page.py
│   ├── registration_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_page.py
│   └── product_page.py
│
├── tests/                      # Test suites (one file per feature)
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_contact.py
│
├── test_data/                  # Excel data files
│   ├── login_data.xlsx         — usernames & passwords
│   ├── registration_data.xlsx  — full registration forms
│   ├── contact_data.xlsx       — contact form inputs
│   ├── payment_data.xlsx       — card details for checkout
│   ├── search_data.xlsx        — product search keywords
│   └── locators.xlsx           — all element locators by page (reference)
│
├── utilities/
│   └── XLUtils.py              — Excel reader (openpyxl-based)
│
├── conftest.py                 — pytest fixtures (driver, data)
├── pytest.ini                  — test runner config
└── requirements.txt
```

## Three-Layer Hybrid Design

| Layer | Technology | Purpose |
|---|---|---|
| **POM** | Selenium + Page classes | Encapsulate locators and actions |
| **Data-Driven** | openpyxl + Excel | Drive tests with multiple datasets |
| **Test Runner** | pytest + fixtures | Parameterize, report, structure |

## Setup

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# Specific suite
pytest tests/test_login.py
pytest tests/test_cart.py

# With HTML report
pytest --html=reports/report.html --self-contained-html

# Headless (uncomment in conftest.py)
# opt.add_argument("--headless=new")
```

## Excel Data Files

| File | Sheet | Columns |
|---|---|---|
| `login_data.xlsx` | Sheet1 | Username, Password, Is_Valid, Description |
| `registration_data.xlsx` | Sheet1 | Name, Email, Password, Day, Month, Year, First_Name, Last_Name, Company, Address, Country, State, City, Zipcode, Mobile, Is_Valid, Description |
| `contact_data.xlsx` | Sheet1 | Name, Email, Subject, Message, Is_Valid, Description |
| `payment_data.xlsx` | Sheet1 | Name_On_Card, Card_Number, CVC, Expiry_Month, Expiry_Year, Description |
| `search_data.xlsx` | Sheet1 | Keyword, Expected_Min_Results, Description |
| `locators.xlsx` | Per-page sheets | Component_name, Locator_name, Locator_value |

## Test Coverage

| Suite | TCs | Highlights |
|---|---|---|
| Login | 5 | Valid, invalid, logout, data-driven multi-user, empty fields |
| Registration | 2 | Full valid flow, data-driven with xfail for invalid rows |
| Products | 5 | Page load, count, detail view, search × 3 keywords, Excel-driven search |
| Cart | 5 | Add, continue shopping, name check, delete, checkout (logged in) |
| Checkout | 3 | Address visible, full order, data-driven multi-card |
| Contact | 3 | Page load, submit, data-driven multi-row |
