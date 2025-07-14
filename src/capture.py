from playwright.sync_api import sync_playwright

def capture_page(url: str, out_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=15000)
        page.screenshot(path=f"{out_path}/page.png", full_page=True)
        with open(f"{out_path}/page.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        browser.close()
