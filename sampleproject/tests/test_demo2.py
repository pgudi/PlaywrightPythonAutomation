from playwright.sync_api import Page,expect

def test_sgapp_validate(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://sgtestinginstituteapp.onrender.com/login")
    expect(page).to_have_title("S G Software Testing Institute")