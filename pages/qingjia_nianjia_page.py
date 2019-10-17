import time

from selenium.common.exceptions import NoSuchElementException

from common.read_yaml import read_yaml_file
from pages.base_page import BasePage


class qingjia_nianjia_page(BasePage):


    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)

    '''
        年假正常时间范围，可以申请：选择2019/9/20-2019/9/21，如果修改脚本，只修改日期的  位置信息  就行
    '''
    def nianjia_zhengchang_success(self):
        #点击请假
        qingjia_button = self.base_page.find_byID_('com.flashexpress.backyard:id/_leave')
        qingjia_button.click()
        #切换到webview下
        view_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(view_now)
        cot = self.base_page.get_context()
        print(cot)
        print('点击请假类型前：')
        #点击请假类型
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[1]/div/input').click()
        cots = self.base_page.get_context()
        print(cots)
        print('点击请假类型后：')
        #点击年假（带薪）按钮
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 0).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        #点击开始时间按钮
        #self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        print('还没有点击时间26')
        #点击26号,如果后续日期更换，只更换对于的坐标就可以了 [618,1473][768,1608]
        ''' 位置信息 '''
        a = read_yaml_file('nianjia_zhengchang_success','startTime')
        self.base_page.by_TouchAction_dingwei(a[0],a[1])
        time.sleep(3)
        #点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800,1300)
        print('点击了确定按钮')
        time.sleep(3)
        #点击结束时间按钮
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 2, 0).click()
        time.sleep(2)

        # 点击28号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [921,1473][1068,1608]
        ''' 位置信息 '''
        b = read_yaml_file('nianjia_zhengchang_success','endTime')
        self.base_page.by_TouchAction_dingwei(b[0], b[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        #输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('请假的原因')
        time.sleep(2)
        #浏览器页面需要向上滑动一下
        self.base_page.swipeUp()
        time.sleep(2)
        #点击提交按钮
        # 提交按钮 = [90, 1695][990, 1830]
        self.base_page.by_TouchAction_dingwei(500,1750)
        # 提交的确认弹框
        # 确定按钮 = [540,1245][1017,1365]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(3)

    '''
    年假超出时间范围：选择2019/9/18-2019/9/30，如果修改脚本，只修改日期的  位置信息  就行
    10.12 = [921,1755][1068,1890]  (1000,1800)
    9.30 = [168,1614][315,1749]   (250,1700)
    '''
    def nianjia_chaochu_time_tishi(self):
        # 点击请假
        qingjia_button = self.base_page.find_byID_('com.flashexpress.backyard:id/_leave')
        qingjia_button.click()
        time.sleep(1)
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
        # 点击年假（带薪）按钮
        try:
            ele = self.base_page.find_byClassAndTag('date-list', 'li', 0, 0)
        except:
            for i in range(3):
                ele.click()
                time.sleep(1)
        else:
            ele.click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        # 点击开始时间按钮
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        time.sleep(2)
        print('还没有点击时间18')
        ''' 位置信息 '''
        # 点击9.30号,如果后续日期更换，只更换对于的坐标就可以了 [18,1614][165,1749]
        c = read_yaml_file('nianjia_chaochu_time_tishi','startTime')
        self.base_page.by_TouchAction_dingwei(c[0],c[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        print('点击了确定按钮')
        time.sleep(3)
        # 点击结束时间按钮
        self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 2, 0).click()
        time.sleep(2)
        # 点击10.12号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 = [168,1614][315,1749]
        ''' 位置信息 '''
        d = read_yaml_file('nianjia_chaochu_time_tishi', 'endTime')
        self.base_page.by_TouchAction_dingwei(d[0], d[1])
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_TouchAction_dingwei(800, 1300)
        time.sleep(1)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('请假的原因')
        time.sleep(2)
        # 浏览器页面需要向上滑动一下
        self.base_page.swipeUp()
        time.sleep(2)
        # 点击提交按钮
        # 提交按钮 = [90, 1695][990, 1830]
        self.base_page.by_TouchAction_dingwei(500, 1750)
        #请您确认请假时间确认弹框提示
        # 确认 = [540,1245][1017,1365]
        self.base_page.by_TouchAction_dingwei(800,1300)
        time.sleep(3)
        #获取点击提交按钮后的提示
        text = self.base_page.find_byxpath('/html/body/div[2]/div/div[2]/div[1]').text
        print('texttexttexttexttexttexttexttext')
        print(text)
        print('texttexttexttexttexttexttexttext')
        time.sleep(2)
        return text


