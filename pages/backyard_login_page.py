import time
import string

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage

class backyard_login(BasePage):


    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)

    def login_to_index_page(self,zhanghao = None):
        #self.base_page.find_bytext('同意并继续')
        time.sleep(1)
        usename = self.base_page.find_byID_('com.flashexpress.backyard:id/userName')
        usename.send_keys(zhanghao)
        time.sleep(1)
        pwd = self.base_page.find_byID_('com.flashexpress.backyard:id/userPass')
        pwd.send_keys(123456)
        time.sleep(1)
        self.base_page.find_byID_('com.flashexpress.backyard:id/login').click()
        time.sleep(3)
        return self

    def login_success_tishi(self):

        try:
            element = self.base_page.find_bytext('同意并继续')
            if len(element)==1:
                self.base_page.find_bytext('同意并继续').click()
        except NoSuchElementException:
            print('没有出现  同意并继续按钮 不需要任何操作')

        time.sleep(3)
        #查找输入工号是否这个elements存在，如果存在，证明没有登入成功，返回elements=1
        tishi = self.base_page.return_elements_num('输入工号')
       #如果返回胡elements=1 ，证明找到了，输入工号输入框，此时需要进行登入操作了，否则证明登入成功，只会打印 ‘已登入成功’
        if len(tishi) == 1:
            return True
        else:
            return False




