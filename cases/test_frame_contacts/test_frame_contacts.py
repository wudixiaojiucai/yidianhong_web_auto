import pytest
from common.read_yaml import read_yaml
from common.file_path import frame_contacts_yaml_path


class TestContacts:
    case_data = read_yaml(frame_contacts_yaml_path)["case_data"]

    @pytest.mark.parametrize("full_input", case_data)
    def test_add_user(self, login_fixture, full_input):
        """添加成员 - 信息完整输入"""
        driver = login_fixture
        driver.to_mail_list()
        driver.to_add_user()
        driver.input_username(full_input["username"])
        driver.input_english_name(full_input["english_name"])
        driver.input_memberAdd_acctid(full_input["acctid"])
        driver.choose_sex(full_input["sex"])
        driver.input_phone(full_input["phone"])
        driver.input_telephone(full_input["telephone"])
        driver.input_mail(full_input["mail"])
        driver.input_address(full_input["address"])
        driver.input_title(full_input["title"])
        driver.choose_identity(full_input["identity"])
        driver.choose_extern_position(full_input["position"])
        driver.choose_sendInvite(full_input["sendInvite"])  # 勾、不勾
        driver.click_save_btn()
        table_user_info = driver.get_userinfo()

        """根据姓名获取列表的索引"""
        tr_index = driver.get_index_value(full_input["username"], table_user_info)

        """验证 - 通讯录 - 部门页 - 添加的用户信息是否保存，且在表格的同一行内"""
        pytest.assume(tr_index != None)
        pytest.assume(full_input["title"] in table_user_info[tr_index])
        pytest.assume(full_input["phone"] in table_user_info[tr_index])
        pytest.assume(full_input["mail"] in table_user_info[tr_index])
        pytest.assume(full_input["invtebtn"] in table_user_info[tr_index])

        """验证 - 通讯录 - 用户详情页信息与输入和选择的是否一致"""
        driver.enter_detail_page(tr_index)
        pytest.assume(full_input["username"] in driver.get_detail_username())
        pytest.assume(full_input["english_name"] in driver.get_detail_english())
        pytest.assume(full_input["acctid"] in driver.get_detail_acctid())
        pytest.assume(full_input["phone"] in driver.get_detail_phone())
        pytest.assume(full_input["telephone"] in driver.get_detail_tel())
        pytest.assume(full_input["mail"] in driver.get_detail_mail())
        pytest.assume(full_input["address"] in driver.get_detail_address())
        pytest.assume(full_input["title"] in driver.get_detail_position())
        pytest.assume(full_input["identity"] in driver.get_detail_identity())
        pytest.assume(full_input["out_title"] in driver.get_detail_external_duties())
