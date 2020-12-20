from common.base import Base
from pages.wework_admin_page.user_list_page import UserListPage


class IndexPage(Base):
    _index_btn_loc = ("id", "menu_index")
    _leave_page = ("link text", "离开此页")
    _mail_list_loc = ("id", "menu_contacts")  # 通讯录

    def back_index(self):
        """返回首页"""
        self.click(self._index_btn_loc)
        self.click(self._leave_page)
        return IndexPage(self.driver)

    def to_user_list_page(self):
        """跳转通讯录页面"""
        self.click(self._mail_list_loc)
        return UserListPage(self.driver)
