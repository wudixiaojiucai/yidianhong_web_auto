from common.base import Base


class AddUserPage(Base):
    _username_loc = ("id", "username")  # 姓名
    _english_name_loc = ("id", "memberAdd_english_name")  # 别名
    _memberAdd_acctid_loc = ("id", "memberAdd_acctid")  # 账号
    _sex_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 性别 value 1男 2女
    _memberAdd_phone_loc = ("id", "memberAdd_phone")  # 手机号
    _memberAdd_telephone_loc = ("id", "memberAdd_telephone")  # 座机号
    _memberAdd_mail_loc = ("id", "memberAdd_mail")  # 邮箱
    _memberEdit_address_loc = ("id", "memberEdit_address")  # 地址
    _memberAdd_title_loc = ("id", "memberAdd_title")  # 职务
    _identity_stat_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 身份 普通 上级
    _extern_position_set_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 同步公司内职务 自定义
    _extern_position_loc = ("name", "extern_position")  # 自定义公司职务输入框
    _sendInvite_loc = ("name", "sendInvite")  # 通过邮件或短信发送企业邀请复选框
    _save_continue_btn_loc = ("link text", "保存并继续添加")  # 保存并继续添加按钮
    _save_btn_loc = ("link text", "保存")  # 保存按钮
    _cancel_btn_loc = ("link text", "取消")  # 取消按钮
    _tips_loc = ("css selector", ".ww_inputWithTips_tips")

    def add_user_normal(self, username, english_name, acctid, phone):
        """输入姓名"""
        self.send(self._username_loc, username)
        """输入别名"""
        self.send(self._english_name_loc, english_name)
        """输入账号"""
        self.send(self._memberAdd_acctid_loc, acctid)
        """输入手机号"""
        self.send(self._memberAdd_phone_loc, phone)
        self.click(self._save_btn_loc)
        # from pages.wework_admin_page.user_list_page import UserListPage
        # return UserListPage(self.driver)

    def add_user_fail(self, username, english_name, acctid, phone):
        """输入姓名"""
        self.send(self._username_loc, username)
        """输入别名"""
        self.send(self._english_name_loc, english_name)
        """输入账号"""
        self.send(self._memberAdd_acctid_loc, acctid)
        """输入手机号"""
        self.send(self._memberAdd_phone_loc, phone)
        self.click(self._save_btn_loc)
        return self.get_list_texts(self._tips_loc)
