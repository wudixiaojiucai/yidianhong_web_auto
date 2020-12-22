import time

from common.base import Base
from pages.wework_admin_page.user_list_page import UserListPage


class IndexPage(Base):
    _index_btn_loc = ("id", "menu_index")
    _leave_page = ("link text", "离开此页")
    _mail_list_loc = ("id", "menu_contacts")  # 通讯录
    _mail_list_loc1 = ("xpath", '//*[text()="通讯录"]')  # 通讯录
    _cancel_btn = ("css selector", '[d_ck="cancel"]')  # 添加部门页-取消按钮

    def back_index(self):
        """添加成员页 返回首页"""
        self.click(self._index_btn_loc)
        self.click(self._leave_page)
        return IndexPage(self.driver)

    def add_depart_back(self):
        """添加部门输入页，返回首页"""
        self.click(self._cancel_btn)
        self.click(self._index_btn_loc)

    def to_user_list_page(self):
        """跳转通讯录页面"""
        self.click(self._mail_list_loc)
        return UserListPage(self.driver)
