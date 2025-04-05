from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LessonPageLocators


class LessonPage(BasePage):
    locators = LessonPageLocators()
    
    def get_title(self):
        return self.find(self.locators.LESSON_TITLE).text
