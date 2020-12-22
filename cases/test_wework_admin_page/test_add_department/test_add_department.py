import time
import pytest
from pages.frame_index_page.frame_index_page import IndexPage
from common.file_path import read_yaml, add_department_yaml_path


class TestAddDepartment:
    normal_data = read_yaml(add_department_yaml_path)["normal_data"]
    normal_ids = read_yaml(add_department_yaml_path)["normal_ids"]

    @pytest.mark.parametrize("test_data", normal_data, ids=normal_ids)
    def test_add_department(self, faker, index_fixture: IndexPage, test_data):
        """
        正常添加二级部门
        正常添加三级部门
        """
        page = index_fixture
        department_name = faker.company()
        res = page.to_user_list_page().to_add_department_page().add_department_normal(
            department_name=department_name,
            belong_department_name=test_data["index_department_name"])

        assert test_data["expect"] in res

    # ----------------------------------------------------------------------------------
    @pytest.mark.parametrize("test_data", [{"belong_department_name": "碑山老革命",
                                            "expect": "请输入部门名称"}], ids=["部门名称输入为空"])
    def test_add_department_fail_name(self, index_fixture: IndexPage, test_data):
        """部门名称输入空"""
        page = index_fixture
        res = page.to_user_list_page().to_add_department_page().add_department_fail_name(
            test_data["belong_department_name"])

        assert test_data["expect"] == res

    # ----------------------------------------------------------------------------------

    @pytest.mark.parametrize("test_data", [{"department_name": "部门ABC",
                                            "expect": "请选择所属部门"}], ids=["部门归属未选择"])
    def test_add_department_fail_depart(self, index_fixture: IndexPage, test_data):
        """部门归属未选择"""
        page = index_fixture
        res = page.to_user_list_page().to_add_department_page().add_department_fail_depart(test_data["department_name"])

        assert test_data["expect"] == res
