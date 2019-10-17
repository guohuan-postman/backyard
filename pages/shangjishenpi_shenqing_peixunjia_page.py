import time

from selenium.common.exceptions import NoSuchElementException

from common.read_yaml import read_yaml_file
from pages.base_page import BasePage


class shangjishenpi_shenqing_peixunjia_page(BasePage):
    def __init__(self,appium_driver):
        self.base_page = BasePage(appium_driver)

    def shenqing_peixunjia_bohui(self):
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        # 点击请假
        qingjia_button = self.base_page.find_byID_('com.flashexpress.backyard:id/_leave')
        qingjia_button.click()
        time.sleep(1)
        # 切换到webview下
        view_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(view_now)
        cot = self.base_page.get_context()
        time.sleep(3)
        print(cot)
        print('点击请假类型前：')
        # 点击请假类型
        try:
            elem = self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[1]/div/input')
        except:
            for i in range(3):
                elem.click()
                time.sleep(1)
        else:
            elem.click()

        cots = self.base_page.get_context()
        print(cots)
        print('点击请假类型后：')
        time.sleep(1)
        # 点击公司培训假（带薪）按钮,修改请假类型，只需要更改后边的li的下标
        self.base_page.find_byClassAndTag('date-list', 'li', 0, 11).click()
        time.sleep(3)
        self.base_page.to_now_context(view_now)
        time.sleep(3)
        # 点击开始时间按钮
        # self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[2]/div/input').click()
        # self.base_page.find_byClassAndTag('mt-item-field-inner', 'input', 1, 0).click()
        # self.base_page.css_select("document.querySelector('.mt-item-input')").click()
        self.base_page.css_select('.mt-item-input')[1].click()
        time.sleep(1)
        self.base_page.to_now_context(view_now)
        time.sleep(3)
        print(self.base_page.get_context())
        print('还没有点击时间25')
        # 点击24号,如果后续日期更换，只更换对于的坐标就可以了
        ''' 位置信息  [318,1473][465,1608]'''
        a = read_yaml_file('shenqing_peixunjia_bohui','startTime')
        self.base_page.by_touchAction_uiautomator2(a[0], a[1])
        time.sleep(1)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_touchAction_uiautomator2(800, 1300)
        print('点击了确定按钮')
        time.sleep(3)
        # 点击结束时间按钮
        self.base_page.css_select('.mt-item-input')[2].click()
        time.sleep(2)
        # 点击25号,如果后续日期更换，只更换对于的坐标就可以了
        # 坐标位置 =
        ''' 位置信息  [468,1473][615,1608]'''
        b = read_yaml_file('shenqing_peixunjia_bohui', 'endTime')
        self.base_page.by_touchAction_uiautomator2(b[0], b[1])
        # self.base_page.css_select('document.querySelectorAll(".box-message")[21]').click()
        time.sleep(3)
        # 点击确按钮
        # 确定按钮位置 = [540,1260][1080,1380]
        self.base_page.by_touchAction_uiautomator2(800, 1300)
        # self.base_page.css_select("document.querySelector('.picker-toolbar span.mint-datetime-action.mint-datetime-confirm')").click()
        time.sleep(2)
        # 输入请假原因
        self.base_page.find_byxpath('//*[@id="app"]/div/div[1]/div[6]/textarea').send_keys('年假两天-请假的原因')
        time.sleep(2)
        # 浏览器页面需要向上滑动一下
        self.base_page.swipeUp()
        time.sleep(2)
        # 点击提交按钮
        # 提交按钮 = [90, 1695][990, 1830]
        self.base_page.by_touchAction_uiautomator2(500, 1750)
        # self.base_page.css_select('document.querySelector(".mint-button-text")').click()
        time.sleep(2)
        # 提交的确认弹框
        # 确定按钮 = [540,1245][1017,1365]
        self.base_page.by_touchAction_uiautomator2(800, 1300)
        time.sleep(3)
        #请假成功后，退出账号22399，登入账号 22395
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        self.base_page.find_byandroid_text('我的').click()
        time.sleep(1)
        self.base_page.find_byandroid_text('退出').click()
        time.sleep(1)
        self.base_page.find_byandroid_text('确定').click()
        # 登入账号  22395
        usename = self.base_page.find_byID_('com.flashexpress.backyard:id/userName')
        usename.send_keys(22395)
        time.sleep(1)
        pwd = self.base_page.find_byID_('com.flashexpress.backyard:id/userPass')
        pwd.send_keys(123456)
        time.sleep(1)
        #点击确定按钮
        time.sleep(1)
        self.base_page.find_byID_('com.flashexpress.backyard:id/login').click()
        #点击审批按钮
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        '''
        底部导航栏是原生按钮
        如果当前页面在可见审批导航栏页面，需要点击审批按钮，进入审批页面
        点击我的申请按钮
        点击待审批按钮，进入请假申请页面
        页面向上滑动一次
        点击撤销按钮
        点击确认撤销提示的 确定按钮
        点击页面的返回按钮，页面返回至审批页面
        '''

        # 点击审批按钮
        try:
            ele = self.base_page.find_bytext('审批')
        except NoSuchElementException:
            for i in range(3):
                ele.click()
                time.sleep(1)
        else:
            ele.click()

        time.sleep(2)
        context_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(context_now)
        time.sleep(3)
        #点击我的审批按钮
        wodeshenpi = self.base_page.find_byxpath('//*[@id="app"]/div/a[1]')
        print(wodeshenpi)
        wodeshenpi.click()
        #点击待审批按钮
        '''[0,348][1080,822]'''
        self.base_page.to_now_context(context_now)
        time.sleep(5)
        self.base_page.by_touchAction_uiautomator2(500,500)
        # self.base_page.css_ele_select("div.mint-cell-value.is-link").click()
        time.sleep(1)
        self.base_page.to_now_context(context_now)
        time.sleep(5)
        #页面滑动一次
        self.base_page.swipeUp()
        #点击驳回按钮  //*[@id="pageTwo"]/div/div[1]/div[6]/span[1]   [60,1602][510,1740]
        # self.base_page.find_byClassAndTag('mt-page-footer', 'span', 0, 0).click()
        self.base_page.by_touchAction_uiautomator2(400,1700)
        time.sleep(3)
        self.base_page.to_now_context('WEBVIEW_com.flashexpress.backyard')
        time.sleep(5)
        #定位驳回原因输入框 //*[@id="pageTwo"]/div/div[1]/div[8]/div/div[2]/textarea [144,945][936,1248]
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        eles = self.base_page.find_byH5class("android.widget.EditText")
        eles.send_keys("培训假申请驳回的原因")
        time.sleep(1)
        #点击确定按钮
        self.base_page.by_touchAction_uiautomator2(700, 1380)
        time.sleep(2)


