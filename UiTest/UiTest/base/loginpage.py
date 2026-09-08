from base.appium_api import AppiumApi
from appium.webdriver.common.appiumby import AppiumBy as by
from base.password import PasswordPage
import time
import allure

password_btu = (by.ID,"com.kuke:id/tv_title_right")
page_name = "手机号登录首页"
class LoginPage(AppiumApi):
    @allure.step("登录页面，点击密码登录，进入密码登录页面")
    def goto_password_login(self):
        time.sleep(8)
        self.click_ele(password_btu,page_name)
        return PasswordPage(self.driver)
