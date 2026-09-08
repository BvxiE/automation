#Page Object Model，页面对象模型，UI 自动化经典设计模式，核心思想：把页面元素、页面业务操作 和 测试用例彻底分离。
#`page`文件夹就是 PO 层；`base/appium_api.py`是底层公共操作封装；`tests`是测试用例层。
from base.appium_api import AppiumApi
from appium.webdriver.common.appiumby import AppiumBy as by
from base.loginpage import LoginPage
from base.mypage import MyPage
import time
import allure

login_icon = (by.ID,"com.kuke:id/tv_login")
my_btn =  (by.ID,"")
page_name = "首页"
class HomePage(AppiumApi):
    @allure.step("未登录状态，点击首页登录，进入登录")
    def goto_login(self):
        time.sleep(3)
        self.click_ele(login_icon,page_name)
        return LoginPage(self.driver)

    @allure.step("未登录状态，点击我的按钮，进入我的")
    def goto_mypage(self):
        self.click_ele(my_btn,page_name)
        return MyPage(self.driver)
