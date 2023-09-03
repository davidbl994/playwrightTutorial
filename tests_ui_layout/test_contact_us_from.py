import time

from playwright.sync_api import Playwright, sync_playwright
import pytest
from pom.contact_us_page import ContactUsPage

def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("David", "123 Main", "test@email.com", "123-432-5434", "test_subject", "test message blah")

with sync_playwright() as sync_playwright:
    test_submit_form(playwright)
    time.sleep(5)
