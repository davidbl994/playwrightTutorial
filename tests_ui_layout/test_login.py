import time

import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.mark.smoke
@pytest.mark.regression
@pytest.fixture()
def test_login(set_up) -> None:
    page = set_up

    # Act - When/And
    # page.click("button:has-text('Log In')", timeout=2000)
    # page.click("text=Log In")
    page.click("'Log In'", timeout=2000)
    page.click("[data-testid='signUp.switchToSignUp']")
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    page.press("[data-testid='siteMembers.container'] >>input[type='email']", "Tab")
    page.fill("input[type='password']", "test123")
    page.click("[data-testid='submit'] >> [data-testid='buttonElement']")
    page.click("[aria-label='symon.storozhenko account menu']")

    # Assert - Then
    assert page.is_visible("text=My Orders")
