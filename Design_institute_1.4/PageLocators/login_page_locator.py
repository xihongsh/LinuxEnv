from selenium.webdriver.common.by import By
class LoginPageLocator:
    """
    登录页面基本元素定位封装
    """
    # 用户输入框定位
    user_loc = (By.XPATH, '//input[@id="loginName"]')
    # 密码输入框定位
    password_loc = (By.XPATH, '//input[@id="password"]')
    # 登陆按钮
    login_button_loc = (By.XPATH, '//li[@class="cp"]')