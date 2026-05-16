from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        #Locators
        #If site changes a selector fix it here
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"
        self.inventory_container = "#inventory_container"

    def login(self, username : str, password: str):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.inner_text(self.error_message)
    
    def is_logged_in(self):
        return self.page.is_visible(self.inventory_container)