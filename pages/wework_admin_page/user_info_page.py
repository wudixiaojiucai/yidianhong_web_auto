from common.base import Base


class UserInfoPage(Base):
    # 成员详情页
    _detail_username = ("class name", "member_display_cover_detail_name")  # 姓名
    _detail_english = ("xpath", "//*[@class='member_display_cover_detail_bottom']")  # 索引 0别名
    _detail_acctid = ("xpath", "//*[@class='member_display_cover_detail_bottom']")  # 索引 1账号
    _detail_phone = ("xpath", "//*[@class='member_display_item member_display_item_Phone']")  # 手机号
    _detail_tel = ("xpath", "//*[@class='member_display_item member_display_item_Tel']")  # 座机号
    _detail_mail = ("xpath", "//*[@class='member_display_item member_display_item_Email']")  # 邮箱
    _detail_address = (
        "xpath", "//*[@class='member_display_item member_display_item_WxNickName']")  # 地址 索引0是微信,1是地址
    # 地址 索引 0部门，1职务，2身份，3微信插件，对外信息：4企业名称，5职务
    _detail_complex = ("xpath", "//*[@class='member_display_item']")

    def get_detail_username(self):
        """获取成员详情页 用户姓名"""
        return self.get_text(self._detail_username)

    def get_detail_english(self):
        """获取成员详情页 用户别名"""
        return self.get_texts(self._detail_english, 0)

    def get_detail_acctid(self):
        """获取成员详情页 用户账号"""
        return self.get_texts(self._detail_acctid, 1)

    def get_detail_phone(self):
        """获取成员详情页 用户手机号"""
        return self.get_innertext(self._detail_phone)

    def get_detail_tel(self):
        """获取成员详情页 用户座机号"""
        return self.get_innertext(self._detail_tel)

    def get_detail_mail(self):
        """获取成员详情页 用户邮箱"""
        return self.get_innertext(self._detail_mail)

    def get_detail_address(self):
        """获取成员详情页 用户地址"""
        return self.get_innertexts(self._detail_address, 1)

    def get_detail_department(self):
        """获取成员详情页 部门信息"""
        return self.get_innertexts(self._detail_complex, 0)

    def get_detail_position(self):
        """获取成员详情页 用户职务"""
        return self.get_innertexts(self._detail_complex, 1)

    def get_detail_identity(self):
        """获取成员详情页 用户身份"""
        return self.get_innertexts(self._detail_complex, 2)

    def get_detail_abbreviation(self):
        """获取成员详情页 企业简称"""
        return self.get_innertexts(self._detail_complex, 4)

    def get_detail_external_duties(self):
        """获取成员详情页 对外职务"""
        return self.get_innertexts(self._detail_complex, 5)
