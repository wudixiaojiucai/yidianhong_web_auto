import time
import yaml
from selenium import webdriver
from common.base import Base
from common.file_path import cookie_file


class ContactsPage(Base):
    # 部门页
    mail_list_loc = ("id", "menu_contacts")  # 通讯录
    add_user_btn_loc = ("link text", "添加成员")  # 添加成员
    username_loc = ("id", "username")  # 姓名
    english_name_loc = ("id", "memberAdd_english_name")  # 别名
    memberAdd_acctid_loc = ("id", "memberAdd_acctid")  # 账号
    sex_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 性别 value 1男 2女
    memberAdd_phone_loc = ("id", "memberAdd_phone")  # 手机号
    memberAdd_telephone_loc = ("id", "memberAdd_telephone")  # 座机号
    memberAdd_mail_loc = ("id", "memberAdd_mail")  # 邮箱
    memberEdit_address_loc = ("id", "memberEdit_address")  # 地址
    memberAdd_title_loc = ("id", "memberAdd_title")  # 职务
    identity_stat_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 身份 普通 上级
    extern_position_set_loc = ("xpath", '//label[@class="ww_label ww_label_Middle"]//span')  # 同步公司内职务 自定义
    extern_position_loc = ("name", "extern_position")  # 自定义公司职务输入框
    sendInvite_loc = ("name", "sendInvite")  # 通过邮件或短信发送企业邀请复选框
    save_continue_btn_loc = ("link text", "保存并继续添加")  # 保存并继续添加按钮
    save_btn_loc = ("link text", "保存")  # 保存按钮
    cancel_btn_loc = ("link text", "取消")  # 取消按钮
    all_user_loc = ("xpath", '//*[@id="member_list"]/tr')  # 表格所有行

    # 成员详情页
    detail_username_loc = ("class name", "member_display_cover_detail_name")  # 姓名
    detail_english_loc = ("xpath", "//*[@class='member_display_cover_detail_bottom']")  # 索引 0别名
    detail_acctid_loc = ("xpath", "//*[@class='member_display_cover_detail_bottom']")  # 索引 1账号
    detail_phone_loc = ("xpath", "//*[@class='member_display_item member_display_item_Phone']")  # 手机号
    detail_tel_loc = ("xpath", "//*[@class='member_display_item member_display_item_Tel']")  # 座机号
    detail_mail_loc = ("xpath", "//*[@class='member_display_item member_display_item_Email']")  # 邮箱
    detail_address_loc = ("xpath", "//*[@class='member_display_item member_display_item_WxNickName']")  # 地址 索引0是微信,1是地址
    # 地址 索引 0部门，1职务，2身份，3微信插件，对外信息：4企业名称，5职务
    detail_complex_loc = ("xpath", "//*[@class='member_display_item']")

    def login(self):
        url_login = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
        url_index = "https://work.weixin.qq.com/wework_admin/frame#index"
        self.open(url_login)
        with open(cookie_file, encoding="utf-8") as f:
            cookie_data = yaml.safe_load(f)
            for cookie in cookie_data:
                self.driver.add_cookie(cookie)
        self.open(url_index)

    def to_mail_list(self):
        self.click(self.mail_list_loc)

    def to_add_user(self):
        self.click(self.add_user_btn_loc)

    def input_username(self, text=""):
        """输入用户名"""
        self.send(self.username_loc, text)

    def input_english_name(self, text=""):
        """输入别名"""
        self.send(self.english_name_loc, text)

    def input_memberAdd_acctid(self, text=""):
        """输入账号"""
        self.send(self.memberAdd_acctid_loc, text)

    def choose_sex(self, text):
        """选择性别"""
        self.radio_choose_text(self.sex_loc, text)

    def input_phone(self, text=""):
        """输入手机号"""
        self.send(self.memberAdd_phone_loc, text)

    def input_telephone(self, text=""):
        """输入座机号"""
        self.send(self.memberAdd_telephone_loc, text)

    def input_mail(self, text=""):
        """输入邮箱"""
        self.send(self.memberAdd_mail_loc, text)

    def input_address(self, text=""):
        """输入地址"""
        self.send(self.memberEdit_address_loc, text)

    def input_title(self, text=""):
        """输入职务"""
        self.send(self.memberAdd_title_loc, text)

    def choose_identity(self, text):
        """选择身份"""
        self.radio_choose_text(self.identity_stat_loc, text)

    def choose_extern_position(self, text):
        """选择公司职务"""
        self.radio_choose_text(self.extern_position_set_loc, text)

    def input_extern_position(self, text=""):
        """输入自定义公司职务"""
        self.send(self.extern_position_loc, text)

    def choose_sendInvite(self, value):
        """发送邀请勾选框"""
        self.choose_selected(self.sendInvite_loc, value)

    def click_save_continue_btn(self):
        """点击保存并继续按钮"""
        self.click(self.save_continue_btn_loc)

    def click_save_btn(self):
        """点击保存按钮"""
        self.click(self.save_btn_loc)

    def click_cancel_btn(self):
        """点击取消按钮"""
        self.click(self.cancel_btn_loc)

    def get_userinfo(self):
        """获取表格用户相关信息"""
        return self.get_list_texts(self.all_user_loc)

    def enter_detail_page(self, index):
        """进入用户详情页"""
        self.click_index(self.all_user_loc, index)

    def get_detail_username(self):
        """获取成员详情页 用户姓名"""
        return self.get_text(self.detail_username_loc)

    def get_detail_english(self):
        """获取成员详情页 用户别名"""
        return self.get_texts(self.detail_english_loc, 0)

    def get_detail_acctid(self):
        """获取成员详情页 用户账号"""
        return self.get_texts(self.detail_acctid_loc, 1)

    def get_detail_phone(self):
        """获取成员详情页 用户手机号"""
        return self.get_innertext(self.detail_phone_loc)

    def get_detail_tel(self):
        """获取成员详情页 用户座机号"""
        return self.get_innertext(self.detail_tel_loc)

    def get_detail_mail(self):
        """获取成员详情页 用户邮箱"""
        return self.get_innertext(self.detail_mail_loc)

    def get_detail_address(self):
        """获取成员详情页 用户地址"""
        return self.get_innertexts(self.detail_address_loc, 1)

    def get_detail_department(self):
        """获取成员详情页 部门信息"""
        return self.get_innertexts(self.detail_complex_loc, 0)

    def get_detail_position(self):
        """获取成员详情页 用户职务"""
        return self.get_innertexts(self.detail_complex_loc, 1)

    def get_detail_identity(self):
        """获取成员详情页 用户身份"""
        return self.get_innertexts(self.detail_complex_loc, 2)

    def get_detail_abbreviation(self):
        """获取成员详情页 企业简称"""
        return self.get_innertexts(self.detail_complex_loc, 4)

    def get_detail_external_duties(self):
        """获取成员详情页 对外职务"""
        return self.get_innertexts(self.detail_complex_loc, 5)


if __name__ == '__main__':
    loc = ("xpath", '//*[@id="member_list"]/tr')
    member_username_info_loc = ("xpath", '//*[@class="member_display_cover_detail_bottom"]')
    driver = webdriver.Chrome()
    web = ContactsPage(driver)
    web.login()
    web.to_mail_list()
    # print(web.get_userinfo())
    web.click_index(loc, 0)
    print(web.get_texts(member_username_info_loc, 1))
    time.sleep(5)
    web.quit_close()
