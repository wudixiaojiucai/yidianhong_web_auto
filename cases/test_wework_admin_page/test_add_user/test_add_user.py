import pytest
from common.file_path import read_yaml, add_user_yaml_path
from pages.frame_index_page.frame_index_page import IndexPage


class TestContacts:
    normal_data = read_yaml(add_user_yaml_path)["user_normal_data"]
    normal_ids = read_yaml(add_user_yaml_path)["normal_ids"]

    @pytest.mark.parametrize("user_normal_data", normal_data, ids=normal_ids)
    def test_add_user(self, main: IndexPage, del_fixture, user_normal_data):
        """
        添加成员 - 信息正确输入
        """
        main.to_user_list_page().to_add_user_page().add_user_normal(
            user_normal_data["username"],
            user_normal_data["english_name"],
            user_normal_data["acctid"],
            user_normal_data["phone"])
        res = main.to_user_list_page().get_user_info()
        assert user_normal_data["expect"] in str(res)

    # ----------------------------------------------------------------------------------

    fail_data = read_yaml(add_user_yaml_path)["user_fail_data"]
    fail_ids = read_yaml(add_user_yaml_path)["fail_ids"]

    @pytest.mark.parametrize("user_fail_data", fail_data, ids=fail_ids)
    def test_add_user_fail(self, main: IndexPage, user_fail_data):
        """
        添加成员 - 输入已存在的账号
        添加成员 - 输入已存在的手机号
        """
        res = main.to_user_list_page().to_add_user_page().add_user_fail(
            user_fail_data["username"],
            user_fail_data["english_name"],
            user_fail_data["acctid"],
            user_fail_data["phone"])

        assert user_fail_data["expect"] in res
