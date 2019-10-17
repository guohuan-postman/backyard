import time
import unittest
from appium import webdriver
from pages.backyard_login_page import backyard_login
from pages.case_fail_chexiao_qingjia_page import case_fail
from pages.chexiao_shenqing_page import chexiaoshenqing
from pages.login_to_exit_page import login_to_exit_page
from pages.qingjia_chanjia_2day_page import qingjia_chanjia_2day_page
from pages.qingjia_chanjia_zaiciqingjia_page import qingjia_chanjia_zaiciqingjia_page



class Test_qingjia_chanjia_zaiciqingjia(unittest.TestCase):

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
            "recreateChromeDriverSessions": "true"  #切换webview和native时，必须加上此句话，才能定位到webview元素 appium API上说的是每次切换到非chrome-Driver时kill掉session
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
            #由于有时候会用例失败，造成上次的请假没有被撤销
            #增加查看是否有需要撤销的请假
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
            #退出登入账号
            self.exit_.to_exit()
            time.sleep(3)
            self.login.login_to_index_page(zhanghao=22399)
        #撤销请假
        self.cxqj = chexiaoshenqing(self.driver)
        self.chanjia_2day = qingjia_chanjia_2day_page(self.driver)
        self.zaiciqingjia = qingjia_chanjia_zaiciqingjia_page(self.driver)

    def tearDown(self):
        self.driver.quit()

    '''
    先申请产假带薪 2天，
    再次申请，查看提示文案
    取消产假
    '''
    '''产检申请，取消，再次申请，再次取消'''

    def test_chanjia2day_zhengchang_success(self):
        self.chanjia_2day.chanjia2day_zhengchang_success()
        time.sleep(2)
        text_tishi = self.zaiciqingjia.chanjia2day_zaiciqingjia()
        self.assertEqual(text_tishi, '请假余额已用完', msg='断言失败，再次申请产假时。提交时没有给出相应的提示')
        time.sleep(2)
        self.cxqj.shenpi_chexiaoshenqing()



    def test_chanjia2day_zhengchang_success_zaici_shenqing(self):
        self.chanjia_2day.chanjia2day_zhengchang_success()
        time.sleep(2)
        text_tishi = self.zaiciqingjia.chanjia2day_zaiciqingjia()
        self.assertEqual(text_tishi, '请假余额已用完', msg='断言失败，再次申请产假时。提交时没有给出相应的提示')
        time.sleep(2)
        self.cxqj.shenpi_chexiaoshenqing()
        #再次申请时，需要点击打卡按钮进入打卡页面后，再进行成功申请
        #点击打卡按钮
        time.sleep(3)
        self.chanjia_2day.click_daka()
        #进入打卡页面后，进行申请操作
        self.chanjia_2day.chanjia2day_zhengchang_success()
        time.sleep(2)
        text_tishi = self.zaiciqingjia.chanjia2day_zaiciqingjia()
        self.assertEqual(text_tishi, '请假余额已用完', msg='断言失败，再次申请产假时。提交时没有给出相应的提示')
        time.sleep(2)
        self.cxqj.shenpi_chexiaoshenqing()


