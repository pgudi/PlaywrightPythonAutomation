from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    url=page.url
    print("URL of Application :",url)
    title=page.title()
    print("Title of Application:",title)