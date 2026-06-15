from playwright.sync_api import Page, expect

def test_file_Upload(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#singleFileInput").set_input_files(
        r"Upload\File1.txt"
    )

    page.get_by_role(
        "button",
        name="Upload Single File"
    ).click()

    expect(
        page.locator("#singleFileStatus")
    ).to_contain_text("File1.txt")

    print("File upload successful......")

    page.wait_for_timeout(5000)
