from playwright.async_api import async_playwright


async def get_titles_and_links(page):
    # Find all the li elements with class 'ais-Hits-item'
    items = page.locator('li.ais-Hits-item').all()
    results = []
    for item in items:
        # Get the title (text content of the h3 inside the post div)
        title = item.locator('div.post h3.title strong').inner_text()

        # Get the href attribute from the anchor tag
        href = item.locator('a').get_attribute('href')
        results.append((title, href))
    return results


class A16zDataFetcher:
    def __init__(self):
        self.browser_ctx = async_playwright()

    async def execute(self):
        async with self.browser_ctx as p:
            b_type = p.chromium
            browser = await b_type.launch()
            page = await browser.new_page()
            await page.goto('https://a16z.com/search/?query=investing')
            print(await get_titles_and_links(page))
            await browser.close()
