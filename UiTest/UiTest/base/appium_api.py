import logging
import datetime
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.webdriver import WebDriver

from tools.getpath import getdir_path

# 获取当前模块logger
log = logging.getLogger(__name__)

class AppiumApi():
    #: 类型注解，声明driver变量类型为Appium的WebDriver
    driver:WebDriver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver #显式等待对象，最长等待10秒
        self.wait = WebDriverWait(driver, 10)
    #find_ele 是底层封装方法，核心是显式等待定位页面元素；元素找不到的时候自动截图并且把截图放入 allure 报告；捕获异常之后重新抛出，不吞异常保证用例失败；查找成功返回元素对象，供点击、输入等上层方法调用
    def find_ele(self,locater,page_name):#,value=None
        """
            封装元素查找方法：显式等待定位元素，找不到自动截图并添加到allure报告，异常向上抛出
            :param locater: 元素定位元组，格式 (By.ID, "元素id值")
            :param page_name: 页面名称，用于截图文件名标记，方便区分哪一页失败
            :return: 定位到的element元素对象
        """
        try:
            # if isinstance(locater,tuple):
            # locater 格式 (by.ID, "xxx")，*解包元组
            element = self.wait.until(
                #presence_of_element_located只判断 DOM 存在，元素可能不可见
                EC.presence_of_element_located(locater)
            )
            # else:
            #     element = self.driver.find_element(locater,value)
        except NoSuchElementException as e:
            log.info('页面元素失败开始截图')
            #时间字符串里面 `15:13:25` 带冒号，Windows 不允许文件名有冒号，直接报错，**截图文件生成失败，所以 img 文件夹里面没有图片**
            img_path = getdir_path("img") +"\\"+ page_name + datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".png"
            self.driver.get_screenshot_as_file(img_path)
            with open(img_path,"rb") as f:
                allure.attach(f.read(),name="失败截图",attachment_type=allure.attachment_type.PNG)
            raise e
        # 关键！捕获异常后重新抛出，终止用例，不会返回None
        else:
            return element
    def click_ele(self,locater,page_name):
        """
             封装点击操作：先调用find_ele查找元素，再执行click点击
            :param locater: 元素定位元组
            :param page_name: 页面名称，截图标记用
        """
        self.find_ele(locater,page_name).click()
    def get_ele_text(self,locater,page_name):
        # 注意要return，你原来没有return
        return self.find_ele(locater,page_name).text
    def clear_ele(self,locater,page_name):
        """
            封装输入框清空操作
            :param locater: 元素定位元组
            :param page_name: 页面名称
        """
        self.find_ele(locater,page_name).clear()
    def input_ele(self,locater,page_name,content=None):
        """
            封装输入框输入内容
            :param locater: 元素定位元组
            :param page_name: 页面名称
            :param content: 需要输入的文本内容
        """
        self.find_ele(locater,page_name).send_keys(content)
