from playwright.sync_api import Page, expect


def test_static_web_table(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # Locate table
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # ====================================================
    # 1. Count total number of rows
    # ====================================================

    rows = table.locator("tr")
    expect(rows).to_have_count(7)

    row_count = rows.count()
    print("Number of rows in a table:", row_count)   # 7

    # ====================================================
    # 2. Count total number of columns/headers
    # ====================================================

    columns = rows.locator("th")
    expect(columns).to_have_count(4)

    column_count = columns.count()
    print("Number of columns/headers in a table:", column_count)   # 4

    # ====================================================
    # 3. Read all data from 2nd row
    # ====================================================

    second_row_cells = rows.nth(2).locator("td")
    second_row_texts = second_row_cells.all_inner_texts()

    print("2nd row data =====> :", second_row_texts)

    expect(second_row_cells).to_have_text(
        ['Learn Java', 'Mukesh', 'Java', '500']
    )

    print("Printing 2nd row data.......")

    for text in second_row_texts:
        print(text)

    # ====================================================
    # 4. Read all data from table (excluding header)
    # ====================================================

    all_row_data = rows.all()

    # Uncomment if you want to print complete table

    # print("Printing data from all the rows and columns.......")
    # for row in all_row_data[1:]:
    #     cols = row.locator("td").all_inner_texts()
    #     print(cols)

    # ====================================================
    # 5. Print books whose author is Mukesh
    # ====================================================

    print("Printing Books names written By Mukesh..........")

    for row in all_row_data[1:]:

        author_name = row.locator("td").nth(1).inner_text()

        if author_name == "Mukesh":

            book_name = row.locator("td").nth(0).inner_text()

            print(f"{author_name}\t{book_name}")

    # ====================================================
    # 6. Calculate total price of all books
    # ====================================================

    total_price = 0

    for row in all_row_data[1:]:

        price = row.locator("td").nth(3).inner_text()

        total_price += int(price)

    print("Total price:", total_price)   # 7100