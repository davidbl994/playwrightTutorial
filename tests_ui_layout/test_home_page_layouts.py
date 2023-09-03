from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elemnts import HomePage


def test_about_us_section_verbiage(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # Open new page
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees
    assert page.is_visible(HomePage.celebrating_beauty_body)

    browser.close()