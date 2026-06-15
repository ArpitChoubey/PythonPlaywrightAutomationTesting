from playwright.sync_api import Playwright, expect


def test_hande_popups(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # Handle popup window
    page.on("popup", lambda popup: popup.wait_for_load_state())

    # Click button that opens popup
    page.locator("#PopUp").click()

    page.wait_for_timeout(5000)

    # Get all pages/windows in current context
    all_popups = context.pages

    print("Total number of popups/pages:", len(all_popups))

    # Iterate through all pages
    for pw in all_popups:

        print("Popup/Page URL =====>", pw.url)

        title = pw.title()
        print("Title =====>", title)

        # Switch to Playwright popup window
        if "Playwright" in title:

            pw.locator("text=Get started").click()

            pw.wait_for_timeout(3000)

            expect(pw).to_have_title("Installation | Playwright")

            print("Successfully navigated to Installation page")

            pw.close()

    page.wait_for_timeout(5000)

    context.close()
    browser.close()