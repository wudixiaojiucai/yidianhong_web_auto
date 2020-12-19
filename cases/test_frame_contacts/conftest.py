import pytest
from selenium import webdriver
from pages.wework_admin.frame_contacts import ContactsPage


@pytest.fixture(scope="function")
def login_fixture():
    driver = ContactsPage(webdriver.Chrome())
    driver.set_window()
    driver.login()
    yield driver
    driver.quit_close()
