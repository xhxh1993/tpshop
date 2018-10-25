from base import initDriver
from page.page import Page

class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_auto_intohome(self):
        #滑动屏幕
        self.page.inithomepageaction().auto_enter_home()
        #进入首页
