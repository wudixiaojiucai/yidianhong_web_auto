import pytest


@pytest.fixture(scope="class")
def del_fixture(main):
    yield
    """删除最后一行 添加的姓名为111嘿嘿的用户"""
    res = main.to_user_list_page().del_user()
    print(res)
