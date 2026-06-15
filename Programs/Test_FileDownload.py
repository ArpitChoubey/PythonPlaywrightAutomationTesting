import os

from playwright.sync_api import sync_playwright, expect, Page

def test_download_file(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()  # this will generate a link to download file

    # Approach 1: register an event
    # def handle_download(download):
    #     download.save_as("downloads/testfile.txt")
    #
    # page.on("download", handle_download)

    # Approach 2: lambda
    page.on(
        "download",
        lambda download: download.save_as("downloads/testfile.txt")
    )

    page.locator("#txtDownloadLink").click()

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File not exist")