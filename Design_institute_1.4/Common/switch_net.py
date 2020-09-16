from selenium.webdriver.common.keys import Keys
from Common.basepage import BasePage
from PageLocators.biandian_locator import IndexBianPageLocator as IBP
import time
class Switch(BasePage):
    def switch_net(self,name,passw,projectname,yesorno):
        self.clear_text(IBP.h_name,doc="清空用户名输入框")
        self.input_text(IBP.h_name,name,doc="输入用户名")
        self.clear_text(IBP.h_pass,doc="清空用户名输入框")
        self.input_text(IBP.h_pass,passw,doc="输入密码")
        self.click(IBP.h_loginbutton,doc="点击登陆按钮")
        time.sleep(4)
        self.click(IBP.h_systemmanager,doc="点击系统管理")
        self.click_by_js(IBP.h_daymanager,doc="点击工日管理")
        self.driver.switch_to.frame("div_grgl")
        self.click_by_js(IBP.h_zhiliang,doc="点击质量评定管理")
        self.click(IBP.h_projectchoice,doc="点击项目类型下拉框")
        self.input_text(IBP.h_projectinput,projectname,doc="输入工程名称")
        self.input_text(IBP.h_enter,Keys.ENTER,doc="输入框点回车键")
        self.click(IBP.h_ifcanyu,doc="点击是否参与")
        self.input_text(IBP.h_ifcanyuinput,yesorno)
        self.input_text(IBP.h_ifcanyuenter,Keys.ENTER,doc="输入框点回车键")
        self.click(IBP.h_savebutton,doc="点击保存按钮")
        self.driver.switch_to.default_content()
        text_1 = self.get_element_text(IBP.h_savesucinfo,doc="获取保存成功提示语")
        self.driver.refresh()
        self.click(IBP.h_systemmanager,doc="点击系统管理")
        self.click_by_js(IBP.h_daymanager, doc="点击工日管理")
        self.driver.switch_to.frame("div_grgl")
        self.click_by_js(IBP.h_zhiliang, doc="点击质量评定管理")
        self.click(IBP.h_projectchoice,doc="点击项目类型下拉框")
        self.input_text(IBP.h_projectinput,projectname,doc="输入工程名称")
        self.input_text(IBP.h_enter,Keys.ENTER,doc="输入框点回车键")
        time.sleep(2)
        text_2 = self.get_element_text(IBP.h_ifcanyutext,doc="获取是否参与提示文本")
        return text_1,text_2