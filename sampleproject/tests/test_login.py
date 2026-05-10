from playwirght.sync_api import Page,expect

def test_launch_login(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Login Action
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("//input[@name='password']").fill("pgudi")
    page.locator("//button[text()='Sign In']").click()
    page.wait_for_timeout(3000)
