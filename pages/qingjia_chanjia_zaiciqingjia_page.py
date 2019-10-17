import time

from selenium.common.exceptions import NoSuchElementException

from common.read_yaml import read_yaml_file
from pages.base_page import BasePage


class qingjia_chanjia_zaiciqingjia_page(BasePage):
    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)
    '''产假成功申请'''
    def chanjia2day_zaiciqingjia(self):

        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(5)
        # 点击请假
        try:
            qingjia_button = self.base_page.find_byID_('com.flashexpress.backyard:id/_leave')
        except NoSuchElementException:
            for i in range(20):
                qingjia_button.click()
                time.sleep(1)
        else:
            qingjia_button.click()
        time.sleep(3)
        # 切换到webview下
        view_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(view_now)
        time.sleep(3)
        cot = self.base_page.get_context()
        print(cot)
        print('点击请假类型前：')
        # 点击请假类型
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[1]/div/input').click()
        time.sleep(2)
        cots = self.base_page.get_context()
        print(cots)
        print('点击请假类型后：')
        # 点击带薪事假（带薪）按钮,修改请假类型，只需要更改后边的li的下标
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 3).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        time.sleep(3)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        time.sleep(1)
        print('还没有点击时间21')
        # 点击27号,如果后续日期更换，只更换对于的坐标就可以了
        ''' 位置信息 '''
        a = read_yaml_file('chanjia2day_zaiciqingjia', 'startTime')
        self.base_page.by_TouchAction_dingwei(a[0], a[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        print('点击了确定按钮')
        time.sleep(3)
        # 点击结束时间按钮
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 2, 0).click()
        time.sleep(2)

        # 点击22号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [18,1473][165,1608]
        ''' 位置信息 '''
        b = read_yaml_file('chanjia2day_zaiciqingjia', 'endTime')
        self.base_page.by_TouchAction_dingwei(b[0], b[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(2)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('产假两天-请假的原因')
        time.sleep(2)
        # 浏览器页面需要向上滑动一下
        self.base_page.swipeUp()
        time.sleep(2)
        # 点击提交按钮
        # 提交按钮 = [90, 1695][990, 1830]
        self.base_page.by_TouchAction_dingwei(500, 1750)
        time.sleep(2)
        # 提交的确认弹框
        # 确定按钮 = [540,1245][1017,1365]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(2)
        # 获取点击提交按钮后的提示  请假余额已用完
        a_text = self.base_page.find_byxpath('/html/body/div[2]/div/div[2]/div[1]').text
        time.sleep(1)
        print('texttexttexttexttexttexttexttext')
        print(a_text)
        print('texttexttexttexttexttexttexttext')
        #点击请假余额已用完确认提示
        self.base_page.find_byxpath('/html/body/div[2]/div/div[3]/button[2]').click()
        time.sleep(2)
        #将context设置成原生app
        # self.base_page.to_now_context('NATIVE_APP')
        # time.sleep(5)
        #点击返回按钮
        # self.base_page.find_byID_('com.flashexpress.backyard:id/iv_back').click()
        self.base_page.by_touchAction_uiautomator2(100, 100)
        time.sleep(2)
        return a_text
