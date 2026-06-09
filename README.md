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
