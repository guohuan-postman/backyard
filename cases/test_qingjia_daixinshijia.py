import time
import unittest

from appium import webdriver

from pages.backyard_login_page import backyard_login
from pages.case_fail_chexiao_qingjia_page import case_fail
from pages.chexiao_shenqing_page import chexiaoshenqing
from pages.login_to_exit_page import login_to_exit_page
from pages.qingjia_daixinshijia_page import qingjia_daixinshijia_page
from pages.qingjia_nianjia_page import qingjia_nianjia_page


class Test_qingjia_daixinshijia(unittest.TestCase):

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
        self.cxqj = chexiaoshenqing(self.driver)
        self.daixinSJ = qingjia_daixinshijia_page(self.driver)

    def tearDown(self):
        self.driver.quit()
    '''
    带薪事假请假成功
    取消带薪请假
    '''
    def test_daixinshijian_zhengchang_success(self):

        self.daixinSJ.daixinshijia_zhengchang_success()
        time.sleep(5)
        self.cxqj.shenpi_chexiaoshenqing()

