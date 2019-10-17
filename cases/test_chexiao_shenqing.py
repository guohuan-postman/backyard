import time
import unittest

from appium import webdriver

from pages.backyard_login_page import backyard_login
from pages.case_fail_chexiao_qingjia_page import case_fail
from pages.chexiao_shenqing_page import chexiaoshenqing
from pages.login_to_exit_page import login_to_exit_page
from pages.qingjia_nianjia_page import qingjia_nianjia_page


class Test_chexiaoshenqing(unittest.TestCase):

    def setUp(self):

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
            # 由于有时候会用例失败，造成上次的请假没有被撤销
            # 增加查看是否有需要撤销的请假
            case = case_fail(self.driver)
            case.to_wodeshenqing_page()
            ele = case.return_len_qingjialeixing()
            # if len(ele) == 1:
            if ele is not None:
                case.chexiaoshenqing_success()
            else:
                case.fanhuidao_daka_page()
        else:
            print('已登入成功，不需要重新登入了')
            # 由于有时候会用例失败，造成上次的请假没有被撤销
            # 增加查看是否有需要撤销的请假
            case = case_fail(self.driver)
            case.to_wodeshenqing_page()
            ele = case.return_len_qingjialeixing()
            # if len(ele) == 1:
            if ele is not None:
                case.chexiaoshenqing_success()
            else:
                case.fanhuidao_daka_page()
            # 退出登入账号
            self.exit_.to_exit()
            time.sleep(3)
            self.login.login_to_index_page(zhanghao=22399)
        self.cxshenqing = chexiaoshenqing(self.driver)
    def tearDown(self):
        self.driver.quit()

    ''' 审批撤销申请'''
    def shenpi_chexiaoshenqing(self):
        result = self.cxshenqing.shenpi_chexiaoshenqing()
        qingjialeixing = result[0]
        wodeshenqing_text = result[1]
        self.assertEqual(qingjialeixing, '请假类型', msg='请假类型文字没有找到，页面没有跳转到我的申请页面')
        self.assertEqual(wodeshenqing_text, '我的申请', msg='断言失败，我的申请撤销后，页面没有返回到审批页面')
        time.sleep(3)
