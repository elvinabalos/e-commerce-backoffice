from playwright.sync_api import Page, expect


def test_login(page: Page):

    # Navigate (use base-url if configured)
    page.goto("/")

    # Login
    page.locator("input[placeholder='Enter Username']").fill("superadmin")
    page.locator("input[placeholder='Enter Password']").fill("superadmin031819")
    page.get_by_role("button", name="Login").click()

    # Assert successful login
    expect(page).to_have_url("/control-panel")
    expect(page.locator("div.module-header").get_by_text("Control Panel")).to_be_visible()

    # Logout
    page.locator("div[title='User Menu']").click()
    page.get_by_text("Logout").click()

    # Confirm logout modal
    expect(page.get_by_text("Are you sure you want to logout?")).to_be_visible()
    page.get_by_role("button", name="Ok").click()

    # Verify redirect to login page
    expect(page).to_have_url("/")
    expect(page.locator("input[placeholder='Enter Username']")).to_be_visible()