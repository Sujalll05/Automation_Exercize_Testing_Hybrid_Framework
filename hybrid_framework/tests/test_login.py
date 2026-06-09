
import pytest
from POM.login_page import LoginPage


class TestLogin:


    def test_valid_login(self, driver_at_login, login_data):
        user = login_data[0]
        page = LoginPage(driver_at_login)
        page.login(user["Username"], user["Password"])

        assert page.is_login_successful(), (
            f"Expected 'Logged in as' banner, but login failed for {user['Username']}."
        )


    def test_invalid_credentials_show_error(self, driver_at_login):
        """Wrong email/password should show the error message."""
        page = LoginPage(driver_at_login)

        page.login("notareal@email.com", "WrongPass@99")

        error = page.get_error_message()
        assert error != "", "Expected error message but none appeared."
        assert "incorrect" in error.lower(), f"Unexpected error text: '{error}'"


    def test_logout_after_valid_login(self, driver_at_login, login_data):
        """User should be redirected and logout link should disappear."""
        user = login_data[0]
        page = LoginPage(driver_at_login)

        page.login(user["Username"], user["Password"])
        assert page.is_login_successful(), "Pre-condition: login must succeed."

        page.click_logout()

        assert not page.is_logout_visible(), "Logout link still visible — logout may have failed."


    @pytest.mark.parametrize("row_index", [0, 1])
    def test_login_multiple_users(self, driver_at_login, login_data, row_index):
        """Run login test for each valid-credential row in Excel."""
        if row_index >= len(login_data):
            pytest.skip(f"Row {row_index} not found in login data file.")

        user = login_data[row_index]
        page = LoginPage(driver_at_login)

        page.login(user["Username"], user["Password"])

        assert page.is_login_successful(), (
            f"Login failed for row {row_index}: {user['Username']}"
        )


    def test_login_empty_fields(self, driver_at_login):
        """Submitting blank fields should not log the user in."""
        page = LoginPage(driver_at_login)

        page.login("", "")

        assert not page.is_login_successful(), "Expected login to fail with empty fields."
