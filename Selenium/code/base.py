from contextlib import contextmanager
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.feed_page import FeedPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        authorize = False
        self.driver = driver
        self.config = config

        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.feed_page: FeedPage = (request.getfixturevalue('feed_page'))
        if self.authorize:
            credentials = request.getfixturevalue("credentials")
            login_page = self.login_page
            login_page.open()
            login_page.login(credentials['email'], credentials['password'])
        
