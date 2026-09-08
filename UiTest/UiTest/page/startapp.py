import os
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver import webdriver
from base.appium_api import AppiumApi
from page.safepage import SafePage
import allure
class StartAPP(AppiumApi):
    @allure.step("连接设备和Appium")
    def start(self):
        if self.driver is None:
            android_options = UiAutomator2Options()
            android_options.set_capability("automationName", "UiAutomator2")
            android_options.set_capability("platformName", "Android")
            android_options.set_capability("deviceName", "M461Q")
            android_options.set_capability("appPackage", "com.kuke")
            android_options.set_capability("appActivity", "com.kuke.module_business_splash.ui.SplashActivity")
            android_options.set_capability("noReset", True)
            android_options.set_capability("platformVersion", "9")
            android_options.set_capability("chromedriverExecutableDir", "E:\\Python310\\chromedriver.exe")
            android_options.set_capability("unicodeKeyboard", True)
            android_options.set_capability("resetKeyboard", True)
            android_options.set_capability("app", "C:\\Users\\Dell\\Downloads\\kuke-kkwx_744_jiagu_sign.apk")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=android_options)
            #self.driver.implicitly_wait(20)#作用全局，每一秒轮询，超过设置时间会报错（显性等待）
        else:
            os.system("adb shell am start com.kuke /.module_business_splash.ui.SplashActivity")
        return self

    @allure.step("弹出安全界面")
    def goto_safe(self):
        return SafePage(self.driver)

