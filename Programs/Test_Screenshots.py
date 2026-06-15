from playwright.sync_api import Page
import datetime


def test_screenshots_demo(page: Page):
    page.goto("https://www.osprey.com/")

    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Page screenshot (visible area)
    page.screenshot(
        path=f"screenshots/homepage_visible_{timestamp}.png"
    )

    # Full page screenshot
    page.screenshot(
        path=f"screenshots/homepage_full_{timestamp}.png",
        full_page=True
    )

    # Element screenshot - Logo
    logo = page.locator("img[alt='Osprey store logo']")
    logo.screenshot(
        path=f"screenshots/logo_{timestamp}.png"
    )

    # Element screenshot - Featured Product
    featured_products = page.locator('span.main-nav__link-0-level-text')

    featured_products.screenshot(
        path=f"screenshots/featured_products_{timestamp}.png"
    )