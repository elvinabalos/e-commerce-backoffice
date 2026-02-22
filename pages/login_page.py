from playwright.sync_api import expect
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("input[placeholder='Enter Username']")
        self.password_input = page.locator("input[placeholder='Enter Password']")
        self.login_button = page.get_by_role("button", name="Login")
        self.user_menu = page.locator("div[title='User Menu']")
        self.logout_button = page.get_by_text("Logout")
        self.confirm_logout_button = page.get_by_role("button", name="Ok")
        self.error_message = page.locator("div.error-message")  # Adjust selector to your app

    # Login action
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # Logout action
    def logout(self):
        self.user_menu.click()
        self.logout_button.click()
        expect(self.page.get_by_text("Are you sure you want to logout?")).to_be_visible()
        self.confirm_logout_button.click()

    # Positive assertion
    def assert_login_success(self):
        expect(self.page).to_have_url("/control-panel")
        expect(self.page.locator("div.module-header").get_by_text("Control Panel")).to_be_visible()

    # Negative assertion
    def assert_login_failed(self):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(
            "These credentials do not match"
        )
        expect(self.page).to_have_url("/")