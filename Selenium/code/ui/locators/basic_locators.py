from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class FeedPageLocators:
    PEOPLE_PAGE_LINK = (By.CSS_SELECTOR, "a[href='/people/']")
    SCHEDULE_PAGE_LINK = (By.CSS_SELECTOR, "a[href='/schedule/']")


class LoginPageLocators:
    CONTINUE_BUTTON = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'gtm-login-btn')


class PeoplePageLocators:
    INPUT_TEXT = (By.CLASS_NAME, 'input-text')
    INPUT_SUBMIT = (By.CLASS_NAME, 'input-submit')
    USER_CARDS = (By.CSS_SELECTOR, "td.cell-name")
    FULL_NAME = (By.CSS_SELECTOR, "p.realname")
    USER_DESCRIPTION = (By.CLASS_NAME, "user-desc")


class SchedulePageLocators:
    WHOLE_SEMESTER_BUTTON = (By.XPATH, "//a[text()='Весь семестр']")
    SUBJECTS_DROP_DOWN_BUTTON = (By.XPATH, "//span[contains(text(), 'дисциплины')]/following-sibling::div[contains(@class, 'r-icon-arrow_down')]")
    SUBJECT_ELEM = lambda self, subject: (By.XPATH, f"//div[@class='option']/span[text()='{subject}']")
    KINDS_DROP_DOWN_BUTTON = (By.XPATH, "//span[contains(text(), ' типы')]/following-sibling::div[contains(@class, 'r-icon-arrow_down')]")
    KIND_ELEM = lambda self, kind: (By.XPATH, f"//div[@class='option']/span[text()='{kind}']")
    LESSON_HREF_BY_DATE = lambda self, date: (By.XPATH, f"//tr[.//nobr[contains(.//text(), '{date}')]]//a[@class='schedule-show-info']")
    SCHEDULE_TABLE_ROWS = (By.CSS_SELECTOR, 'tr.schedule-timetable__item')


class LessonPageLocators:
    LESSON_TITLE = (By.XPATH, "//h1[contains(@class, 'styleslesson__SLessonHeaderTitle')]")
