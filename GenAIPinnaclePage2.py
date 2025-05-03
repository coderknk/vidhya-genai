# File: tests/test_pinnacle_form.py
import pytest
from playwright.sync_api import sync_playwright
from pages.genaipinnacle_page import GenAIPinnaclePage

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def test_valid_form_submission(page):
    """Test filling and submitting the contact form with valid data."""
    pinnacle = GenAIPinnaclePage(page)
    pinnacle.load()
    # Fill form with sample data
    pinnacle.fill_contact_form(name="Alice Test", phone="9876543210", email="alice@example.com", experience="0-3yrs")
    pinnacle.agree_terms()
    pinnacle.opt_whatsapp(True)
    pinnacle.submit_form()
    # Verify successful submission (example: check URL or success message)
    assert page.url != pinnacle.url, "Form did not submit or redirect as expected."

def test_title_and_banners(page):
    """Test that key banners and headings are visible."""
    pinnacle = GenAIPinnaclePage(page)
    pinnacle.load()
    # Check main title
    assert page.text_content("h1") == "GenAI Pinnacle Program"
    # Check discount badge
    assert page.is_visible("text=25% Off"), "Discount badge not visible"
    # Check countdown timer presence
    assert page.is_visible("text=Enrollment closes in"), "Countdown text not visible"

def test_terms_link(page):
    """Verify Terms & Conditions link navigates correctly."""
    pinnacle = GenAIPinnaclePage(page)
    pinnacle.load()
    pinnacle.terms_link.click()
    # After click, expect the terms page
    assert "terms" in page.url
    assert page.text_content("h1").startswith("Terms"), "Terms page did not load"
