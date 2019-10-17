import time

from pages.base_page import BasePage


class qingjia_daixinshijia_page(BasePage):
    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)
    '''带薪事假成功申请'''
    def daixinshijia_zhengchang_success(self):
        # 点击请假
        qingjia_button = self.base_page.find_byID_('com.flashexpress.backyard:id/_leave')
        qingjia_button.click()
        # 切换到webview下
        view_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(view_now)
        cot = self.base_page.get_context()
        print(cot)
        print('点击请假类型前：')
        # 点击请假类型
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[1]/div/input').click()
        cots = self.base_page.get_context()
        print(cots)
        print('点击请假类型后：')
        # 点击带薪事假（带薪）按钮
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 1).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        print('还没有点击时间21')
        # 点击21号,如果后续日期更换，只更换对于的坐标就可以了
        ''' 位置信息 '''
        self.base_page.by_TouchAction_dingwei(100, 1700)
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
        self.base_page.by_TouchAction_dingwei(200, 1700)
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('带薪事假-请假的原因')
        time.sleep(2)
        # 浏览器页面需要向上滑动一下
        self.base_page.swipeUp()
        time.sleep(2)
        # 点击提交按钮
        # 提交按钮 = [90, 1695][990, 1830]
        self.base_page.by_TouchAction_dingwei(500, 1750)
        time.sleep(1)
        # 提交的确认弹框
        # 确定按钮 = [540,1245][1017,1365]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(3)