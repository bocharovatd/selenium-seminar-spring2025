import pytest
from ui.fixtures import credentials
from base import BaseCase

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = self.login_page
        login_page.open()
        login_page.login(credentials['username'], credentials['password'])
        assert self.driver.current_url == self.feed_page.url, "Current page is not FeedPage"


class TestLK(BaseCase):
    authorize = True

    def test_find_groupmate(self):
        feed_page = self.feed_page
        feed_page.open()
        people_page = feed_page.go_to_people_page()
        search_query = "Даниил Мироненко"
        expected_description = "МГТУ им. Н. Э. Баумана, ИУ6-63Б" 
        people_page.search_user(search_query)

        users = people_page.get_all_users()
        assert users, "No users found for the query"
        
        found = False
        for user in users:
            full_name = people_page.get_user_full_name(user)
            if search_query in full_name:
                description = people_page.get_user_description(user)
                assert description == expected_description, "Description does not match"
                found = True
                break
        
        assert found, "User with the specified name not found"

    def test_info_about_lesson(self):
        feed_page = self.feed_page
        feed_page.open()
        schedule_page = feed_page.go_to_schedule_page()
        schedule_page.set_interval_whole_semester()
        schedule_page.select_subject("Обеспечение качества в разработке ПО")
        schedule_page.select_kind("Семинар")
        lesson_page = schedule_page.get_lesson_page_by_date("3 апреля 2025")
        assert lesson_page.get_title() == "Семинар 2. End-to-End тесты на Python"
