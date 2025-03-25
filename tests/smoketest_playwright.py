import os
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            ss_path = os.path.join(os.path.dirname(
                __file__), f"example-{browser_type.name}.png")
            print(ss_path)
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://playwright.dev')
            await page.screenshot(path=ss_path)
            await browser.close()

asyncio.run(main())
