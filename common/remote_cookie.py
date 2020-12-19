import yaml
from selenium import webdriver


def remote_cookie():
    """启动复用浏览器，或者扫码登录成功后的cookie"""
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    """获取cookie"""
    cookie_data = driver.get_cookies()
    with open("cookie.yaml", "w", encoding="utf-8") as f:
        """yml文件序列化"""
        yaml.dump(cookie_data, f)
        print("cookie写入完成")
    driver.quit()


remote_cookie()
