from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import PeoplePageLocators


class PeoplePage(BasePage):
    locators = PeoplePageLocators()
    url = 'https://education.vk.company/people/'

    def search_user(self, query):
        search_field = self.find(self.locators.INPUT_TEXT)
        search_field.clear()
        search_field.send_keys(query)
        self.click(self.locators.INPUT_SUBMIT)

    def get_all_users(self):
        return self.find_all(self.locators.USER_CARDS)

    def get_user_full_name(self, user_card):
        return self.wait().until(
            EC.visibility_of(user_card.find_element(*self.locators.FULL_NAME))
            ).text.strip()

    def get_user_description(self, user_card):
        return self.wait().until(
            EC.visibility_of(user_card.find_element(*self.locators.USER_DESCRIPTION))
            ).text.strip()

