from ui.fixtures import credentials
from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = self.login_page
        login_page.open()
        login_page.login(credentials['email'], credentials['password'])
        assert self.driver.current_url == self.feed_page.url, "Current page is not FeedPage"


class TestLK(BaseCase):
    authorize = True

    SEARCH_QUERY = "Даниил Мироненко"
    EXPECTED_DESCRIPTION = "МГТУ им. Н. Э. Баумана, ИУ6-63Б"

    SCHEDULE_SUBJECT = "Обеспечение качества в разработке ПО"
    SCHEDULE_LESSON_TYPE = "Семинар"
    SCHEDULE_LESSON_DATE = "3 апреля 2025"
    EXPECTED_LESSON_TITLE = "Семинар 2. End-to-End тесты на Python"

    def test_find_groupmate(self):
        feed_page = self.feed_page
        feed_page.open()
        people_page = feed_page.go_to_people_page()
        
        people_page.search_user(self.SEARCH_QUERY)
        users = people_page.get_all_users()
        
        assert users, f"No users found for the query: {self.SEARCH_QUERY}"
        
        found = False
        for user in users:
            full_name = people_page.get_user_full_name(user)
            if self.SEARCH_QUERY in full_name:
                description = people_page.get_user_description(user)
                assert description == self.EXPECTED_DESCRIPTION, \
                    f"Description does not match. Expected: {self.EXPECTED_DESCRIPTION}, got: {description}"
                found = True
                break
        
        assert found, f"User with name '{self.SEARCH_QUERY}' not found"

    def test_info_about_lesson(self):
        feed_page = self.feed_page
        feed_page.open()
        schedule_page = feed_page.go_to_schedule_page()
        
        schedule_page.set_interval_whole_semester()
        schedule_page.select_subject(self.SCHEDULE_SUBJECT)
        schedule_page.select_kind(self.SCHEDULE_LESSON_TYPE)
        
        lesson_page = schedule_page.get_lesson_page_by_date(self.SCHEDULE_LESSON_DATE)
        actual_title = lesson_page.get_title()
        
        assert actual_title == self.EXPECTED_LESSON_TITLE, \
            f"Lesson title mismatch. Expected: {self.EXPECTED_LESSON_TITLE}, got: {actual_title}"
