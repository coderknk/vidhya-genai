# File: pages/genaipinnacle_page.py
from playwright.sync_api import Page

class GenAIPinnaclePage:
    """Page Object Model for the GenAI Pinnacle Program page."""
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.analyticsvidhya.com/genaipinnacle"
        # Locators for form fields and buttons (assumed selectors)
        self.fullname_input = page.locator("input[placeholder='Full Name']")
        self.phone_input = page.locator("input[placeholder='Phone Number']")
        self.email_input = page.locator("input[placeholder='Email Id']")
        self.experience_select = page.locator("select#experience")
        self.terms_checkbox = page.locator("label:has-text('Terms & Conditions')")
        self.whatsapp_checkbox = page.locator("label:has-text('Send WhatsApp Updates')")
        self.join_button = page.locator("button:has-text('Join the program')")
        self.terms_link = page.locator("text=Terms & Conditions")
        self.brochure_button = page.locator("text=Download Brochure")

    def load(self):
        """Navigate to the GenAI Pinnacle page."""
        self.page.goto(self.url)

    def fill_contact_form(self, name: str, phone: str, email: str, experience: str):
        """Fill the contact/enroll form fields."""
        self.fullname_input.fill(name)
        self.phone_input.fill(phone)
        self.email_input.fill(email)
        self.experience_select.select_option(value=experience)  # e.g. "0-3yrs"
    
    def agree_terms(self):
        """Check the Terms & Conditions checkbox."""
        self.terms_checkbox.click()
    
    def opt_whatsapp(self, enable: bool):
        """Toggle the WhatsApp updates checkbox."""
        if enable:
            self.whatsapp_checkbox.click()
    
    def submit_form(self):
        """Click the Join/Submit button."""
        self.join_button.click()
