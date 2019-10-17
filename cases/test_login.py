import time
import unittest

from appium import webdriver

from pages.backyard_login_page import backyard_login
from pages.login_to_exit_page import login_to_exit_page


class Test_login(unittest.TestCase):

    def setUp(self):
        '''
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '2395072134057ece',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'noReset': 'True',
            'automationname': 'UiAutomator2',
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }
        :return:
        '''

        desired_caps = {
            "deviceName": "KVYPIZPZ99999999",
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "appPackage": "com.flashexpress.backyard",
            "appActivity": "com.flashexpress.express.welcome.WelcomeActivity",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            "recreateChromeDriverSessions": "true"
            # 切换webview和native时，必须加上此句话，才能定位到webview元素 appium API上说的是每次切换到非chrome-Driver时kill掉session
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.hide_keyboard()  # 关闭安卓手机的键盘
        self.login = backyard_login(self.driver)
        self.exit_ = login_to_exit_page(self.driver)
        tishi = self.login.login_success_tishi()
        # print('test:'+tishi)
        # 如果为True证明找到了登入账号的id，需要登入
        # else证明已登入可直接操作其他
        if tishi == True:
            self.login.login_to_index_page(zhanghao=22399)
        else:
            print('已登入成功，不需要重新登入了')
            # 退出登入账号
            self.exit_.to_exit()
            time.sleep(1)
            self.login.login_to_index_page(zhanghao=22399)
        #self.driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        self.login = backyard_login(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        tishi = self.login.login_success_tishi()
        # print('test:'+tishi)
        #如果为True证明找到了登入账号的id，需要登入
        #else证明已登入可直接操作其他
        if tishi  == True:
            self.login.login_to_index_page(zhanghao=22400)
        else:
            print('已登入成功，不需要重新登入了')

