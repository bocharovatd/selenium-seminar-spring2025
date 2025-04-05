from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage
from ui.locators.basic_locators import FeedPageLocators


class FeedPage(BasePage):
    locators = FeedPageLocators()
    url = 'https://education.vk.company/feed/'

    def go_to_people_page(self):
        self.click(self.locators.PEOPLE_PAGE_LINK)
        return PeoplePage(self.driver)

    def go_to_schedule_page(self):
        self.click(self.locators.SCHEDULE_PAGE_LINK)
        return SchedulePage(self.driver)
        