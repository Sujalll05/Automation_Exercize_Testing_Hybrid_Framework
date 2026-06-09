"""
tests/test_contact.py
Hybrid Framework — Contact Us test suite
Covers: page visibility, valid form submission, data-driven submissions.
"""
import pytest
from POM.contact_page import ContactPage


class TestContact:

    # ── TC-CT-01: Contact page loads correctly ────────────────────────────────
    def test_contact_page_visible(self, driver_at_home):
        page = ContactPage(driver_at_home)
        page.navigate_to_contact()
        assert page.is_contact_page_visible(), "'Get In Touch' header not found."

    # ── TC-CT-02: Valid form submission shows success ─────────────────────────
    def test_valid_contact_form_submission(self, driver_at_home, contact_data):
        row = contact_data[0]
        page = ContactPage(driver_at_home)
        page.navigate_to_contact()

        page.fill_contact_form(
            name    = row["Name"],
            email   = row["Email"],
            subject = row["Subject"],
            message = row["Message"],
        )
        page.click_submit()
        page.accept_alert()

        assert page.is_success_message_visible(), "Success message not displayed after form submit."

    # ── TC-CT-03: Data-driven — multiple contact submissions ──────────────────
    @pytest.mark.parametrize("row_index", [0, 1])
    def test_contact_form_multiple_rows(self, driver_at_home, contact_data, row_index):
        if row_index >= len(contact_data):
            pytest.skip(f"Row {row_index} not in contact data.")

        row = contact_data[row_index]
        page = ContactPage(driver_at_home)
        page.navigate_to_contact()

        page.fill_contact_form(
            name    = row["Name"],
            email   = row["Email"],
            subject = row["Subject"],
            message = row["Message"],
        )
        page.click_submit()
        page.accept_alert()

        success_text = page.get_success_message_text()
        assert "success" in success_text.lower(), (
            f"Unexpected success text for row {row_index}: '{success_text}'"
        )
