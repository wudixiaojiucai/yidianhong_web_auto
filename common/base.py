import time

import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.do_exception import LocatorTypeError, ElementNotFound
from common.file_path import cookie_file


class Base:

    def __init__(self, driver: webdriver, time=10):
        self.driver = driver
        self.time = time

    def open(self, url):
        self.driver.get(url)

    def quit_close(self):
        self.driver.quit()

    def set_window(self):
        self.driver.maximize_window()
        # self.driver.set_window_size(2560, 1600)

    def find(self, locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                ele = WebDriverWait(self.driver, self.time).until(
                    EC.visibility_of_element_located(locator))
                # presence_of_element_located
                # visibility_of_element_located
                return ele
            except TimeoutException as e:
                raise ElementNotFound("元素定位超时")

    def finds(self, locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                eles = WebDriverWait(self.driver, self.time).until(
                    EC.visibility_of_all_elements_located(locator))
                # presence_of_all_elements_located
                return eles
            except TimeoutException as e:
                raise ElementNotFound("元素定位超时")

    def send(self, locator, text=""):
        ele = self.find(locator)
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见、无法输入、或者不唯一")

    def click(self, locator):
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见、无法点击、或者不唯一")

    def click_index(self, locator, index):
        """列表，根据索引点击"""
        eles = self.finds(locator)
        if eles[index].is_displayed():
            eles[index].click()
        else:
            raise ElementNotVisibleException("元素不可见、无法点击、或者索引输入错误")

    def click_list_text(self, locator, text):
        """列表，根据内容点击"""
        res = self.finds(locator)
        try:
            for index, item in enumerate(res):
                if item.text == text:
                    self.click_index(locator, index)
        except:
            raise ElementNotFound("无法点击，或没获取到预期的文本内容")

    def select_by_value(self, locator, value):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            element = self.find(locator)
            Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def get_attribute(self, locator, name):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                element = self.find(locator)
                return element.get_attribute(name)
            except:
                print(f"获取%s属性失败，返回{name}")
                return ''

    def radio_choose_value(self, locator, value):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                eles = self.finds(locator)
                for radio in eles:
                    if radio.get_attribute("value") == str(value):
                        if not radio.is_selected():
                            radio.click()
            except:
                raise ElementNotVisibleException("元素不可见、无法点击、或者value错误")

    def radio_choose_text(self, locator, text):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                eles = self.finds(locator)
                for radio in eles:
                    if radio.text == text:
                        if not radio.is_selected():
                            radio.click()
            except:
                raise ElementNotVisibleException("元素不可见、无法点击、或者value错误")

    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        res = ele.is_selected()
        return res

    def choose_selected(self, locator, value):
        """默认勾选时，index==1,去掉勾,其他任意数勾选。
           默认不勾选时，0 勾上，其他任意数不勾"""
        ele = self.find(locator)
        res = ele.is_displayed
        if res:
            if value == "不勾":
                ele.click()
        else:
            if value == "勾":
                ele.click()

    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            content = self.find(locator).text
            return content
        except:
            print("获取text失败，返回内容为空")
            return ""

    def get_texts(self, locator, index):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            content = self.finds(locator)[index].text
            return content
        except:
            print("获取text失败，返回内容为空")
            return ""

    def get_innertext(self, locator):
        """通过attribute获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            ele = self.find(locator)
            res = ele.get_attribute("innerText")
            return res
        except:
            print("获取text失败，返回内容为空")
            return ""

    def get_innertexts(self, locator, index):
        """通过attribute获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            ele = self.finds(locator)[index]
            res = ele.get_attribute("innerText")
            return res
        except:
            print("获取text失败，返回内容为空")
            return ""

    def get_list_texts(self, locator):
        """获取表格的文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            eles = self.finds(locator)
            text_list = [item.text for item in eles]
            # print(text_list)
            return text_list
        except:
            print("获取text失败，返回内容为空")
            return ""

    def is_in_texts(self, locator, text):
        """获取表格的文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        try:
            eles = self.finds(locator)
            for item in eles:
                if item.text == text:
                    return True
            return False
        except:
            print("获取text失败，返回内容为空")
            return ""

    def get_index_value(self, var, current_list):
        """根据值，获取值在列表中的索引"""
        try:
            for index, value in enumerate(current_list):
                if var in value:
                    return index
        except:
            print(f"{var}不存在，或者{current_list}为空")
            return ""

    def is_not_visible(self, locator):
        if not isinstance(locator, tuple):
            raise LocatorTypeError("定位类型错误，locator必须是元祖")
        else:
            try:
                ele = WebDriverWait(self.driver, self.time).until_not(
                    EC.visibility_of_element_located(locator))
                # presence_of_element_located
                # visibility_of_element_located
                return ele
            except TimeoutException as e:
                raise ElementNotFound("元素定位超时")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url_login = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    url_index = "https://work.weixin.qq.com/wework_admin/frame#index"
    driver.get(url_index)
    with open(cookie_file, encoding="utf-8") as f:
        cookie_data = yaml.safe_load(f)
        for cookie in cookie_data:
            driver.add_cookie(cookie)
    driver.get(url_index)
    mail_list = ("css selector", ".frame_nav_item_title")
    driver.find_element_by_css_selector(".frame_nav_item_title").click()
    time.sleep(2)
    _index_btn_loc = ("id", "menu_index")
    driver.find_element("id", "menu_index").click()
    time.sleep(3)
