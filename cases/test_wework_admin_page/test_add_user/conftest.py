import pytest
from pages.frame_index_page.frame_index_page import IndexPage


@pytest.fixture(scope="class")
def del_fixture(driver):
    yield
    """删除最后一行 添加的姓名为111嘿嘿的用户"""
    page = IndexPage(driver)
    res = page.to_user_list_page().del_user()
    print(res)
