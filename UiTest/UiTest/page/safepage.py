from base.appium_api import AppiumApi
from appium.webdriver.common.appiumby import AppiumBy as by
from page.homepage import HomePage
import time
safe_btn = (by.ID,"com.kuke:id/ok")
page_name = "安全弹窗"
class SafePage(AppiumApi):
    def goto_home(self):
        time.sleep(25)
        self.click_ele(safe_btn,page_name)
        return HomePage(self.driver)
