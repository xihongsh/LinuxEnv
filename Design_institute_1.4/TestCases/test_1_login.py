import unittest,os
from selenium import webdriver
from  TestDatas.global_datas import GlobalDatas as GD
from PageObjects.login_page import LoginPage as LP
root = os.path.dirname(os.path.abspath(__file__))
class TestLogin(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('no-sandbox')
        option.add_argument('disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(GD.login_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_a_success(self):
        """
        18612356691/123456 登陆系统成功
        断言：出现首页元素'工作台'登陆系统成功
        :return:
        """
        success_info = LP(self.driver).login_success(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(success_info,GD.login_sucess[2])




