from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click(timeout=3000)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("helloworld@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("happy123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden() # želim potvrditi da sam se loginao, a najbolji primjer je da ovog više nema jednom kad se logiram

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
