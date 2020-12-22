from selenium import webdriver
from common.base import Base
from pages.wework_admin_page.add_department_page import AddDepartmentPage
from pages.wework_admin_page.add_user_page import AddUserPage
from pages.wework_admin_page.user_info_page import UserInfoPage


class UserListPage(Base):
    # 部门页
    _mail_list = ("id", "menu_contacts")  # 通讯录
    _add_user_btn = ("link text", "添加成员")  # 添加成员
    _all_user = ("xpath", '//*[@id="member_list"]/tr')  # 表格所有行
    _del_checkbox = ("xpath", '//*[@id="member_list"]//tr[last()]//input')  # 最后一行勾选框
    _del_btn = ("xpath", "//a[text()='删除']")  # 删除按钮
    _del_ok_btn = ("css selector", '[d_ck="submit"]')  # 弹框确认按钮
    _del_tips_success = ("xpath", '//*[text()="删除成功"]')  # 删除成功提示
    _add_icon = ("css selector", '.member_colLeft_top_addBtn')  # + 号图标
    _add_department = ("xpath", '//a[text()="添加部门"]')  # 添加部门按钮
    _left_departmentlist = ("css selector", "'.jstree-anchor a'")  # 左边部门列表

    def to_add_user_page(self):
        """进入添加成员页面"""
        self.click(self._add_user_btn)
        return AddUserPage(self.driver)

    def get_user_info(self):
        """获取表格用户相关信息"""
        return self.get_list_texts(self._all_user)

    def to_user_info_page(self, index):
        """进入用户详情页"""
        self.click_index(self._all_user, index)
        return UserInfoPage(self.driver)

    def del_user(self):
        """删除添加在最后一行的用户"""
        if "111嘿嘿" in str(self.get_user_info()):
            self.click(self._del_checkbox)
            self.click(self._del_btn)
            self.click(self._del_ok_btn)
            return self.get_text(self._del_tips_success)
        else:
            print("用户不存在，删除失败")
            return ""

    def to_add_department_page(self):
        """进入添加部门页面"""
        self.click(self._add_icon)
        self.click(self._add_department)
        return AddDepartmentPage(self.driver)


if __name__ == '__main__':
    loc = ("xpath", '//*[@id="member_list"]/tr')
    member_username_info = ("xpath", '//*[@class="member_display_cover_detail_bottom"]')
    driver = webdriver.Chrome()
    web = UserListPage(driver)
