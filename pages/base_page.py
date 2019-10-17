import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from lxml.html import tostring
from lxml import etree


class BasePage(object):

    def __init__(self, appium_driver):
        self.driver: WebDriver = appium_driver


    def swipeUp(self, t=1000, n=1):
        '''向上滑动屏幕'''

        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
            time.sleep(1)

    def swipeDown(self, t=1000, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=1000, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=1000, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
    def find_byID_(self,id):

        '''根据id定位元素'''
        return self.driver.find_element_by_id(id)
    def return_elements_num(self,text):
        return self.driver.find_elements_by_xpath('//*[contains(@text,"%s")]'%text)

    def find_bytext(self,find_text):
        '''根据名称定位,然后点击'''
        loc_text = 'new UiSelector().text("%s")'%(find_text)
        # ele = self.driver.find_element_by_android_uiautomator(loc_text)
        # ele.click()
        # return ele
        return self.driver.find_element_by_android_uiautomator(loc_text)


    def click_tap(self, shuzu):
        self.driver.tap(shuzu)

    def by_className(self, classname):
        # reid = 'newUiSelector().resourceId("%s")'%resourceId
        # self.driver.find_element_by_android_uiautomator(reid).click()
        #clss = 'newUiSelector().className("%s")'%resourceId
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%classname).click()
    def by_index_android_instance(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText").instance(2)').send_keys('可以了吧？？？？')
    def find_byandroid_text(self,text):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%text)

    def find_byH5_className(self, class_name, num):
        return self.driver.find_elements_by_class_name(class_name)[num]
    def find_byH5class(self,classN):
        return self.driver.find_element_by_class_name(classN)
    def find_byxpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)
    def find_by_H5_name(self,H5_text):
        return self.driver.find_element_by_name(H5_text)
    def find_byClassAndTag(self,clsname,tagname,num,num2):
        return self.driver.find_elements_by_class_name(clsname)[num].find_elements_by_tag_name(tagname)[num2]
    def find_classtag(self):
        self.driver.find_element_by_class_name('dialog-body').find_element_by_tag_name('textarea').send_keys('121323123')
        # print('cla'*9)
        # print(cla)
        # print('cla'*9)

    def get_context(self):
        get_contexts = self.driver.contexts
        return get_contexts
    def to_now_context(self,context):
        return self.driver.switch_to.context(context)
    def back_(self):
        return self.driver.back()
    def by_TouchAction_dingwei(self,x,y):

        action1 = TouchAction(self.driver)
        #点击21
        #li = action1.press(x=950, y=1400).wait(300).release().wait(300).perform()
        # return action1.press(x=x, y=y).wait(300).release().wait(300).perform()
        return action1.press(x=x, y=y).release().perform()
    def by_touchAction_uiautomator2(self, x, y):
        action2 = TouchAction(self.driver)
        return action2.press(x=x, y=y).release().perform()
    def touchAction_point_to_point(self,x1,y1,x2,y2):
        TouchAction(self.driver).press(x=x1, y=y1).wait(300).move_to(x=x2, y=y2).wait(300).perform()

    def js_to_block(self):
        '''
               通过js 将display 设置为block 可见模式
               display="block";  修改样式的display="block" ,表示可见。
               '''
        t1 = time.time()
        js = 'document.querySelectorAll("div").display="block";'
        self.driver.execute_script(js)

    def return_all_handles(self):
        ''' 返回所有的window_handles'''
        return self.driver.window_handles
    def return_current_window_handle(self):
        '''返回当前的window_handle'''
        return self.driver.current_window_handle

    def get_current_context(self):
        return self.driver.current_context

    def js_input_textarea(self):
        # css = "document.querySelector('.mt-item-textarea');"
        css = "sum = document.querySelectorAll('.mt-item-textarea')[0];sum.value='驳回的原因';"
        return self.driver.execute_script(css)

    def js_return_html(self):
        js = "document.querySelector('html')"
        self.driver.execute_script(js)

    def classname_(self, cls_name):
        return self.driver.find_elements_by_class_name(cls_name)
    def css_select(self,css_select):
        # self.driver.find_elements_by_css_selector()
        return self.driver.find_elements_by_css_selector(css_select)
    def css_ele_select(self,css_select):
        return self.driver.find_element_by_css_selector(css_select)

    def to_alert(self):
        # self.driver.switch_to_alert()
        self.driver.switch_to.alert

    def F5(self):
        self.driver.refresh()

    def return_page(self):

        return self.driver.page_source

    def a_m(self):
        return self.driver.find_elements_by_android_uiautomator('new UiSelector().className("mt-item-textarea")')
        return self.driver.find_element_by_android_uiautomator('new UiSelector().className("mt-item-textarea"))') #.childSelector(newUiSelector().index("3")


















