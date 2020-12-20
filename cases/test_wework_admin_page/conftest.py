import time

import pytest
from pages.frame_index_page.frame_index_page import IndexPage


@pytest.fixture(scope="session")
def index_fixture(driver):
    page = IndexPage(driver)
    yield page
    page.to_user_list_page().del_user()
    driver.quit()
