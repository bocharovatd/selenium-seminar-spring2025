from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators

class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = 'https://education.vk.company/?#auth'

    def login(self, email, password):
        self.click(self.locators.CONTINUE_BUTTON)
        self.find(self.locators.EMAIL_FIELD).send_keys(email)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)
        self.wait().until(lambda d: 'auth' not in d.current_url)
