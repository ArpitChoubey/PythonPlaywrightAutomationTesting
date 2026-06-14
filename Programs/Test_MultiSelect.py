import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from teh dropdown - 3 ways

    #page.locator("#colors").select_option(["Red", "Blue", "Green"])   # by label
    #page.locator("#colors").select_option(label=["Red", "Blue", "Green"])  # by label

    #page.locator("#colors").select_option(value=["red", "white", "green"])  # by values
    page.locator("#colors").select_option(index=[4, 2])  # by index


    dropdown_options = page.locator("#colors>options")
    expect(dropdown_options).to_have_count()

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)

    page.wait_for_timeout(5000)