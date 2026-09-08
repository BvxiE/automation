from base.appium_api import AppiumApi
from appium.webdriver.common.appiumby import AppiumBy as by
from base.newhome import NewHomePage
import time
import allure

username_input = (by.ID,"com.kuke:id/et_password_login_phone")
password_input = (by.ID,"com.kuke:id/et_password")
protocal_btn = (by.ID,"com.kuke:id/cb_privacy")
login_btn = (by.ID,"com.kuke:id/tv_password_login")
page_name = "密码登录界面"
@allure.step("账户密码登录，输入用户名")
class PasswordPage(AppiumApi):
    def user_input(self,content=""):
        time.sleep(2)
        self.input_ele(username_input,page_name,content)
        return self

    @allure.step("账户密码登录，输入密码")
    def password_input(self,content=""):
        time.sleep(2)
        self.input_ele(password_input,page_name,content)
        return self

    @allure.step("账户密码登录，勾选隐私协议")
    def user_protocal(self):
        time.sleep(5)
        self.click_ele(protocal_btn,page_name)
        return self

    @allure.step("账户密码登录，点击登录，登录成功")
    def login_success(self):
        time.sleep(5)
        self.click_ele(login_btn,page_name)
        return NewHomePage(self.driver)
#如果未勾选协议，部分 APP 登录按钮会被置为不可点击，此时`element_to_be_clickable`会超时，
    @allure.step("账户密码登录，点击登录，登录失败")
    def login_fail(self):
        time.sleep(5)
        self.click_ele(login_btn,page_name)
        return self
