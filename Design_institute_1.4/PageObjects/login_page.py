from PageLocators.login_page_locator import LoginPageLocator as loc
from PageLocators.planconsult_locator import IndexPlanPageLocator as IP
from Common.basepage import BasePage
class LoginPage(BasePage):

    def login_success(self,username,password):
        self.input_text(loc.user_loc,username,doc="登陆页面_输入用户名")
        self.input_text(loc.password_loc,password,doc="登陆页面_输入密码")
        self.click(loc.login_button_loc,doc="登陆页面_点击登录按钮")
        return self.get_element_text(IP.workplatform_loc,doc="获取首页角标信息")







