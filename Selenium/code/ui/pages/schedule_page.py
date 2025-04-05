from ui.pages.base_page import BasePage
from ui.pages.lesson_page import LessonPage
from ui.locators.basic_locators import SchedulePageLocators
from selenium.webdriver.support import expected_conditions as EC

class SchedulePage(BasePage):
    locators = SchedulePageLocators()
    url = 'https://education.vk.company/schedule/'

    def set_interval_whole_semester(self):
        self.click(self.locators.WHOLE_SEMESTER_BUTTON)

    def select_subject(self, subject):
        self.click(self.locators.SUBJECTS_DROP_DOWN_BUTTON)
        rows = self.find_all(self.locators.SCHEDULE_TABLE_ROWS)
        self.click(self.locators.SUBJECT_ELEM(subject))
        self.wait_for_filters_applied(rows)

    def select_kind(self, kind):
        self.click(self.locators.KINDS_DROP_DOWN_BUTTON)
        rows = self.find_all(self.locators.SCHEDULE_TABLE_ROWS)
        self.click(self.locators.KIND_ELEM(kind))
        self.wait_for_filters_applied(rows)
    
    def get_lesson_page_by_date(self, date):
        self.click_and_switch_to_new_window(self.locators.LESSON_HREF_BY_DATE(date))
        return LessonPage(self.driver)

    def wait_for_filters_applied(self, rows, timeout=10):
        self.wait(timeout).until(
            lambda d: len(d.find_elements(*self.locators.SCHEDULE_TABLE_ROWS)) != len(rows)
        )
