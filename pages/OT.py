import time

from common.read_yaml import read_yaml_file
from pages.base_page import BasePage


class OT_page(BasePage):
    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)
    '''申请OT'''
    def shenqing_ot(self):
        page = self.base_page.return_page()
        print(page)
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        # 点击审批按钮
        self.base_page.find_bytext('审批').click()
        time.sleep(1)

        #触摸考勤的框框 固定的位置，不用抽取
        self.base_page.by_touchAction_uiautomator2(200, 800)
        time.sleep(2)
        print('触摸点击申请OT按钮 +' * 8)
        # page = self.base_page.return_page()
        # print(page)
        print('触摸点击申请OT按钮 +' * 8)
        #触摸点击申请OT按钮
        self.base_page.by_touchAction_uiautomator2(745, 654)
        time.sleep(4)
        print('申请OT +' * 8)
        page = self.base_page.return_page()
        print(page)
        print('申请OT +' * 8)
        #点击OT日期
        self.base_page.by_touchAction_uiautomator2(500, 300)
        time.sleep(1)
        #OT日期
        a = read_yaml_file('shenqing_ot', 'OTtime')
        self.base_page.by_touchAction_uiautomator2(a[0], a[1])
        time.sleep(1)
        #申请OT
        self.base_page.by_touchAction_uiautomator2(800, 450)
        time.sleep(1)
        #申请OT确定按钮
        self.base_page.by_touchAction_uiautomator2(800, 1300)
        time.sleep(1)
        #开始时间
        self.base_page.by_touchAction_uiautomator2(800, 600)
        time.sleep(1)
        #开始时间日期
        b = read_yaml_file('shenqing_ot', 'startTime')
        self.base_page.by_touchAction_uiautomator2(b[0], b[1])
        time.sleep(2)
        #选择时间
        c = read_yaml_file('shenqing_ot', 'select_time')
        #选择申请OT得开始时间，0-24，在yaml文件中修改
        for i in range(c[0]):
            self.base_page.touchAction_point_to_point(267, 1650, 267, 1542)
            time.sleep(1)

        #点击确定按钮
        self.base_page.by_touchAction_uiautomator2(800, 1100)
        #点击时长
        time.sleep(1)
        self.base_page.by_touchAction_uiautomator2(800, 800)
        time.sleep(1)
        #点击确定
        self.base_page.by_touchAction_uiautomator2(800, 1300)
        time.sleep(2)
        # ele = self.base_page.find_byH5class('android.widget.EditText')
        ele = self.base_page.find_byH5_className('android.widget.EditText', 4)
        ele.send_keys('申请OT原因')
        time.sleep(1)
        self.base_page.swipeUp()
        time.sleep(1)
        self.base_page.swipeUp()
        time.sleep(1)
        #点击提交按钮
        self.base_page.by_touchAction_uiautomator2(500, 1600)
        time.sleep(5)

    def to_shenpi_page(self):
        self.base_page.by_touchAction_uiautomator2(800, 1500)
        time.sleep(1)








