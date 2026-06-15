from playwright.sync_api import Page, expect

def test_file_Multiple_Upload(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # uploading multiple files
    files = ["Upload\\File1.txt", "Upload\\File2.txt"]

    page.locator("#multipleFilesInput").set_input_files(files)

    page.get_by_text("Upload Multiple Files").click()

    # validation
    msgloc = page.locator("#multipleFilesStatus")

    expect(msgloc).to_contain_text("File1.txt")
    expect(msgloc).to_contain_text("File2.txt")

    page.wait_for_timeout(5000)

    print("Multiple files are uploaded successfully.......")