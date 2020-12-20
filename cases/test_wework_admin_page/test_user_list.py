import pytest
from common.read_yaml import read_yaml
from common.file_path import frame_contacts_yaml_path


class TestContacts:
    normal_data = read_yaml(frame_contacts_yaml_path)["user_normal_data"]
    normal_ids = read_yaml(frame_contacts_yaml_path)["normal_ids"]
    fail_data = read_yaml(frame_contacts_yaml_path)["user_fail_data"]
    fail_ids = read_yaml(frame_contacts_yaml_path)["fail_ids"]

    @pytest.mark.parametrize("user_normal_data", normal_data, ids=normal_ids)
    def test_add_user(self, index_fixture, user_normal_data):
        """
        添加成员 - 信息正确输入
        """
        page = index_fixture
        page.to_user_list_page().to_add_user_page().add_user_normal(user_normal_data["username"],
                                                                    user_normal_data["english_name"],
                                                                    user_normal_data["acctid"],
                                                                    user_normal_data["phone"])
        res = page.to_user_list_page().get_user_info()
        assert user_normal_data["expect"] in str(res)

    @pytest.mark.parametrize("user_fail_data", fail_data, ids=fail_ids)
    def test_add_user_fail(self, index_fixture, user_fail_data):
        """
        添加成员 - 输入已存在的账号
        添加成员 - 输入已存在的手机号
        """
        page = index_fixture
        res = page.to_user_list_page().to_add_user_page().add_user_fail(user_fail_data["username"],
                                                                        user_fail_data["english_name"],
                                                                        user_fail_data["acctid"],
                                                                        user_fail_data["phone"])

        assert user_fail_data["expect"] in res
