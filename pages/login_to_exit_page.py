import time

from pages.base_page import BasePage


class login_to_exit_page(BasePage):
    def __init__(self,appiumdriver):
        self.base_page = BasePage(appiumdriver)

    def to_exit(self):
        self.base_page.to_now_context('NATIVE_APP')
        time.sleep(3)
        self.base_page.find_byandroid_text('我的').click()
        time.sleep(1)
        self.base_page.find_byandroid_text('退出').click()
        time.sleep(1)
        self.base_page.find_byandroid_text('确定').click()
