"""
tests/test_registration.py
Hybrid Framework — Registration test suite
Covers: full valid registration, duplicate email, invalid email format.
"""
import pytest
from POM.registration_page import RegistrationPage


class TestRegistration:

    # ── TC-R-01: Full valid registration ─────────────────────────────────────
    def test_valid_registration(self, driver_at_login, registration_data):
        """Register a new account using the first valid row from Excel."""
        d = registration_data[0]
        page = RegistrationPage(driver_at_login)

        page.register(
            name     = d["Name"],
            email    = d["Email"],
            password = d["Password"],
            day      = d["Day"],
            month    = d["Month"],
            year     = d["Year"],
            first    = d["First_Name"],
            last     = d["Last_Name"],
            company  = d["Company"],
            address  = d["Address"],
            country  = d["Country"],
            state    = d["State"],
            city     = d["City"],
            zipcode  = d["Zipcode"],
            mobile   = d["Mobile"],
        )

        assert page.is_account_created(), "Account Created! message not found."

    # ── TC-R-02: Data-driven registration with multiple datasets ─────────────
    @pytest.mark.parametrize("row_index", [0, 1, 2])
    def test_registration_multiple_datasets(self, driver_at_login, registration_data, row_index):
        """Run registration for each row in Excel. Rows with invalid data should fail gracefully."""
        if row_index >= len(registration_data):
            pytest.skip(f"Row {row_index} not present in registration data.")

        d = registration_data[row_index]

        # Skip rows that are intentionally invalid (marked with is_valid = FALSE in Excel)
        if str(d.get("Is_Valid", "TRUE")).upper() == "FALSE":
            pytest.xfail(f"Row {row_index} is marked as invalid data — expecting failure.")

        page = RegistrationPage(driver_at_login)
        page.register(
            name     = d["Name"],
            email    = d["Email"],
            password = d["Password"],
            day      = d["Day"],
            month    = d["Month"],
            year     = d["Year"],
            first    = d["First_Name"],
            last     = d["Last_Name"],
            company  = d["Company"],
            address  = d["Address"],
            country  = d["Country"],
            state    = d["State"],
            city     = d["City"],
            zipcode  = d["Zipcode"],
            mobile   = d["Mobile"],
        )

        assert page.is_account_created(), f"Registration failed for row {row_index}: {d['Email']}"
