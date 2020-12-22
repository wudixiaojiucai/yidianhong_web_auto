from common.base import Base


class AddUserPage(Base):
    _username = ("id", "username")  # 姓名
    _english_name = ("id", "memberAdd_english_name")  # 别名
    _memberAdd_acctid = ("id", "memberAdd_acctid")  # 账号
    _sex = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 性别 value 1男 2女
    _memberAdd_phone = ("id", "memberAdd_phone")  # 手机号
    _memberAdd_telephone = ("id", "memberAdd_telephone")  # 座机号
    _memberAdd_mail = ("id", "memberAdd_mail")  # 邮箱
    _memberEdit_address = ("id", "memberEdit_address")  # 地址
    _memberAdd_title = ("id", "memberAdd_title")  # 职务
    _identity_stat = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 身份 普通 上级
    _extern_position_set = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 同步公司内职务 自定义
    _extern_position = ("name", "extern_position")  # 自定义公司职务输入框
    _sendInvite = ("name", "sendInvite")  # 通过邮件或短信发送企业邀请复选框
    _save_continue_btn = ("link text", "保存并继续添加")  # 保存并继续添加按钮
    _save_btn = ("link text", "保存")  # 保存按钮
    _cancel_btn = ("link text", "取消")  # 取消按钮
    _tips = ("css selector", ".ww_inputWithTips_tips")

    def add_user_normal(self, username, english_name, acctid, phone):
        """输入姓名"""
        self.send(self._username, username)
        """输入别名"""
        self.send(self._english_name, english_name)
        """输入账号"""
        self.send(self._memberAdd_acctid, acctid)
        """输入手机号"""
        self.send(self._memberAdd_phone, phone)
        self.click(self._save_btn)
        # from pages.wework_admin_page.user_list_page import UserListPage
        # return UserListPage(self.driver)

    def add_user_fail(self, username, english_name, acctid, phone):
        """输入姓名"""
        self.send(self._username, username)
        """输入别名"""
        self.send(self._english_name, english_name)
        """输入账号"""
        self.send(self._memberAdd_acctid, acctid)
        """输入手机号"""
        self.send(self._memberAdd_phone, phone)
        self.click(self._save_btn)
        return self.get_list_texts(self._tips)
