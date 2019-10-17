import time

from common.read_yaml import read_yaml_file
from pages.base_page import BasePage


class qingjia_peixunjia_page(BasePage):
    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)
    '''培训假（带薪）成功申请   过去时间的7.5天   2019/9/12-2019/9/19
        12：[618,1191][768,1326]  (700,1200)
        19：[618,1332][768,1467]  (700,1400)
    '''
    def peixunjia_zhengchang_success(self):
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
        # 点击公司培训假（带薪）按钮,修改请假类型，只需要更改后边的li的下标
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 11).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        print('还没有点击时间21')
        # 点击24号,如果后续日期更换，只更换对于的坐标就可以了
        ''' 位置信息 '''
        a = read_yaml_file('peixunjia_zhengchang_success', 'startTime')
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

        # 点击25号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [18,1473][165,1608]
        ''' 位置信息 '''
        b = read_yaml_file('peixunjia_zhengchang_success', 'endTime')
        self.base_page.by_TouchAction_dingwei(b[0], b[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('培训假（带薪）两天-请假的原因')
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
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        qingjia_button_text = self.base_page.find_byandroid_text('请假').text
        print('打卡页面的 请假按钮文字')
        print(qingjia_button_text)
        print('打卡页面的 请假按钮文字')
        return qingjia_button_text

    '''
    培训假（带薪）申请失败   过去时间的8.5天   2019/9/17-2019/9/25
    17： [318,1332][465,1467](400,1400)
    25:[468,1473][615,1608]  (550,1500)
    '''

    def peixunjia_9day_fail(self):
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
        # 点击公司培训假（带薪）按钮,修改请假类型，只需要更改后边的li的下标
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 11).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        print('还没有点击时间21')
        # 点击24号,如果后续日期更换，只更换对于的坐标就可以了
        ''' 位置信息 '''
        a = read_yaml_file('peixunjia_9day_fail', 'startTime')
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

        # 点击25号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [18,1473][165,1608]
        ''' 位置信息 '''
        b = read_yaml_file('peixunjia_zhengchang_success', 'endTime')
        self.base_page.by_TouchAction_dingwei(b[0], b[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('培训假（带薪）两天-请假的原因')
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
        # self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        # 获取点击提交按钮后的提示  请假余额已用完
        a_text = self.base_page.find_byxpath('/html/body/div[2]/div/div[2]/div[1]').text
        print('texttexttexttexttexttexttexttext')
        print(a_text)
        print('texttexttexttexttexttexttexttext')
        # 点击请假余额已用完确认提示
        self.base_page.find_byxpath('/html/body/div[2]/div/div[3]/button[2]').click()
        # 将context设置成原生app
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(5)
        # 点击返回按钮
        # self.base_page.find_byID_('com.flashexpress.backyard:id/iv_back').click()
        self.base_page.by_touchAction_uiautomator2(100, 100)
        return a_text

        '''
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
        # 点击带薪事假（带薪）按钮,修改请假类型，只需要更改后边的li的下标
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 11).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        print('还没有点击时间21')
        # 点击17号,如果后续日期更换，只更换对于的坐标就可以了 [921,1332][1068,1467]
        #位置信息 
        a = read_yaml_file('peixunjia_9day_fail', 'startTime')
        self.base_page.by_TouchAction_dingwei(a[0],a[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        print('点击了确定按钮')
        time.sleep(3)
        # 点击结束时间按钮
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 2, 0).click()
        time.sleep(2)

        # 点击25 号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [168,1614][315,1749]
        #位置信息 
        b = read_yaml_file('peixunjia_9day_fail', 'endTime')
        self.base_page.by_TouchAction_dingwei(b[0],b[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('培训假（带薪）8.5天-请假的原因')
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
        # self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        # 获取点击提交按钮后的提示  请假余额已用完
        a_text = self.base_page.find_byxpath('/html/body/div[2]/div/div[2]/div[1]').text
        print('texttexttexttexttexttexttexttext')
        print(a_text)
        print('texttexttexttexttexttexttexttext')
        # 点击请假余额已用完确认提示
        self.base_page.find_byxpath('/html/body/div[2]/div/div[3]/button[2]').click()
        # 将context设置成原生app
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(5)
        # 点击返回按钮
        self.base_page.find_byID_('com.flashexpress.backyard:id/iv_back').click()
        return a_text
        
        :return: 
        '''



