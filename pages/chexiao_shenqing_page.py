import time

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class chexiaoshenqing(BasePage):

    def __init__(self,appium_driver):
        self.base_page = BasePage(appium_driver)
    ''' 审批撤销申请'''
    def shenpi_chexiaoshenqing(self):
        result = []
        # con = self.base_page.get_context()
        #
        # print('审批页面的context:开始输出')
        # print(con)
        # print('审批页面的context：输出结束')
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

        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(8)
        # 点击审批按钮
        try:
            ele = self.base_page.find_bytext('审批')
            time.sleep(1)
        except NoSuchElementException:
            print(NoSuchElementException)
            for i in range(3):
                ele.click()
                time.sleep(1)
        else:
            ele.click()
        time.sleep(2)
        print(self.base_page.return_page())
        context_now = 'WEBVIEW_com.flashexpress.backyard'
        self.base_page.to_now_context(context_now)
        time.sleep(5)
        #点击我的申请
        wodeshenqing  = self.base_page.find_byxpath('//*[@id="app"]/div/a[2]')
        print(wodeshenqing)
        wodeshenqing.click()
        print(self.base_page.return_page())
        print('点了我的申请')
        time.sleep(3)
        # print('我的申请页面当前的handle')
        # #print(self.base_page.return_current_window_handle())
        # print('我的申请页面当前的handle')
        # print('我的申请页面所有的handle')
        # #print(self.base_page.return_all_handles())
        # print('我的申请页面所有的handle')
        # #获取我的申请页面的请假类型文字

        # time.sleep(8)
        self.base_page.to_now_context('NATIVE_APP')
        # self.base_page.to_now_context('WEBVIEW_com.flashexpress.backyard')
        time.sleep(5)
        print('当前contexct'*9)
        print(self.base_page.get_current_context())
        print('当前contexct' * 9)
        page = self.base_page.return_page()
        print(page)
        try:
            qingjia = self.base_page.find_byH5_className('android.view.View', 12)
        except NoSuchElementException:
            print(NoSuchElementException)
            # 点击返回按钮，页面返回到审批页面，但是back方法不可使用，
            # self.base_page.back_()
            # 返回按钮 =[30,54][174,198]
            self.base_page.by_TouchAction_dingwei(100, 150)
            time.sleep(2)
            # self.base_page.to_now_context('NATIVE_APP')
            # time.sleep(8)
            self.base_page.to_now_context('WEBVIEW_com.flashexpress.backyard')
            time.sleep(5)
            wodeshenqing_text = self.base_page.find_byxpath('//*[@id="app"]/div/a[2]').text
            result.append(wodeshenqing_text)
            print('result+' * 8)
            print(result)
            return result
        else:
            # qingjia = self.base_page.find_byxpath('//*[@id="pageOne"]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]')
            print('请假' * 9)
            print(qingjia)
            print('请假' * 9)
            qingjialeixing = qingjia.text
            print('请假类型' * 8)
            print(qingjialeixing)
            print('请假类型' * 8)
            result.append(qingjialeixing)
            time.sleep(1)
            # print('点击前待审批页面的context')
            # print(self.base_page.get_context())
            # print('点击前待审批页面的context')
            self.base_page.to_now_context('NATIVE_APP')
            time.sleep(5)
            #各种方法定位不到，只能通过模拟点击事件 [837,378][963,429] 考虑兼容性。进来靠右边一些
            self.base_page.by_touchAction_uiautomator2(x=800, y=400)
            # print('点击后待审批页面的context')
            # #print(self.base_page.get_context())
            # print('点击后待审批页面的context')
            time.sleep(3)
            self.base_page.swipeUp()
            time.sleep(3)
            #无法获取撤销按钮，改用模拟点击事件  [315,1602][765,1740]
            # self.base_page.find_by_H5_name('撤销').click()
            self.base_page.by_touchAction_uiautomator2(x=500, y=1700)
            time.sleep(2)
            #无法获取确定按钮，改用模拟点击事件[546, 1353][1005, 1473]
            # self.base_page.find_by_H5_name('确定').click()
            self.base_page.by_touchAction_uiautomator2(x=900, y=1400)
            time.sleep(2)
            #点击返回按钮，页面返回到审批页面，但是back方法不可使用，
            # self.base_page.back_()
            #返回按钮 =[30,54][174,198]
            self.base_page.by_TouchAction_dingwei(100, 150)
            time.sleep(2)
            # self.base_page.to_now_context('NATIVE_APP')
            # time.sleep(8)
            self.base_page.to_now_context('WEBVIEW_com.flashexpress.backyard')
            time.sleep(2)
            wodeshenqing_text = self.base_page.find_byxpath('//*[@id="app"]/div/a[2]').text
            result.append(wodeshenqing_text)
            print('result+'*8)
            print(result)
            return result




