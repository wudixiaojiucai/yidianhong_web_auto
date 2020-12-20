import pytest
import yaml
from selenium import webdriver
from common.file_path import cookie_file


@pytest.fixture(scope="session", name="driver", autouse=True)
def login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url_login = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    url_index = "https://work.weixin.qq.com/wework_admin/frame#index"
    driver.get(url_login)
    with open(cookie_file, encoding="utf-8") as f:
        cookie_data = yaml.safe_load(f)
        for cookie in cookie_data:
            driver.add_cookie(cookie)
    driver.get(url_index)
    return driver


def pytest_collection_modifyitems(items):
    """解决控制台unicode编码，改为中文"""
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="session", autouse=True)
def faker_locale():
    return ("zh_CN")
