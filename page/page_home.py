import time
from selenium.webdriver.common.by import By
from base.baseaction import Baseaction

class HomePageAction(Baseaction):
    into_btn_feature = By.ID,"com.tpshop.malls:id/start_Button"
    home_btn_feature = By.XPATH, ("text,首页,1", "resource-id,com.tpshop.malls:id/tab_txtv,1")

    def auto_enter_home(self):

        #通过强制等待让界面消失
        time.sleep(10)
        try:
            self.find_element(self.home_btn_feature)
        except Exception:
            #进行滑动的动作
            for i in range(3):
                self.swipe_left()
                time.sleep(1)
            #点击进入主界面
            self.click(self.into_btn_feature)