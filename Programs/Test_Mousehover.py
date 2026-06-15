from playwright.sync_api import Page

def test_mouse_hover(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_role("button", name="Point Me").hover()

    page.get_by_role("link", name="Mobiles").hover()

    page.wait_for_timeout(3000)

    @pytest.mark.skip
    def test_mouse_rightclick(page: Page):
        page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

        button = page.locator(".context-menu-one")
        button.click(button="right")  # performs right click action - right , left, middle

        page.wait_for_timeout(5000)

    def test_mouse_doubleclick(page: Page):
        page.goto("https://testautomationpractice.blogspot.com/")

        btncopy = page.locator("button[ondblclick='myFunction1()']")
        btncopy.dblclick()  # performs double click action

        filed2 = page.locator("#field2")
        expect(filed2).to_have_value("Hello World!")

        page.wait_for_timeout(5000)

        def test_mouse_draganddrop(page: Page):
            page.goto("https://testautomationpractice.blogspot.com/")

            source = page.locator("#draggable")
            target = page.locator("droppable")

            # Approach1 : manual drag using hover()

            source.hover()
            page.mouse.down()
            target.hover()
            page.mouse.up()

            # source().drag_to(target)

            page.wait_for_timeout(5000