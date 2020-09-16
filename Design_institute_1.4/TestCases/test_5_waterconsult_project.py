import unittest,os,re
from selenium import webdriver
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.waterconsult_project import IndexWaterConsultPage as IWP
from TestDatas.global_datas import GlobalDatas as GD
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestWaterConsultIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('no-sandbox')
        option.add_argument('disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(chrome_options=option)
        cls.driver.get(GD.login_url)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.find_element(*LP.user_loc).send_keys(GD.login_sucess[0])
        cls.driver.find_element(*LP.password_loc).send_keys(GD.login_sucess[1])
        cls.driver.find_element(*LP.login_button_loc).click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    def test_a_check_waterconsult_fields(self):
        """
        水利咨询工程：验证水利咨询工程字段
        断言：
        工程类型:专题类\规划类\项目咨询类
        工程规模和工程投资都是文本框
        """
        retured_fields = IWP(self.driver).check_waterconsult_field()
        print(retured_fields)
        self.assertEqual(retured_fields[0],ID.add_waterconsult_datas["工程类型"]),\
        self.assertEqual(retured_fields[1],ID.add_waterconsult_datas["工程规模"]),\
        self.assertEqual(retured_fields[2],ID.add_waterconsult_datas["工程投资"])

    def test_b_create_waterconsult_project(self):
        """
        水利咨询工程：成功创建水利咨询工程
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_水利咨询工程'
        :return:
        """
        results = IWP(self.driver).create_waterconsult_project(ID.add_waterconsult_datas["project_name"],ID.add_waterconsult_datas["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_waterconsult_datas["project_name"])

    def test_c_faqiliucheng(self):
        """
        水利咨询工程：水利咨询工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_水利咨询工程',五审状态是'进行中'
        """
        results = IWP(self.driver).faqijiaoshen()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_waterconsult_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_d_wushen_loginapprove(self):
        """
        水利咨询工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_水利咨询工程',五审状态是'进行中'
        """
        results = IWP(self.driver).wushenren_loginapprove(GD.hairuomeng[0],GD.hairuomeng[1])
        self.assertEqual(results[0],ID.add_waterconsult_datas["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_e_wushen_approvesuccess(self):
        """
        水利咨询工程：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_水利咨询工程'
        """
        results = IWP(self.driver).wushenren_approvesucess(GD.hairuomeng[0],GD.hairuomeng[1])
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        if type(results[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        else:
            num_2 = 0
        if type(results[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        else:
            num_3 = 0
        if type(results[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_waterconsult_datas["project_name"])

    def test_f_faqiren_checksuccess(self):
        """
        水利咨询工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_水利咨询工程'，五审状态是'已通过'六审是"--"
        :return:
        """
        results = IWP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_waterconsult_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_g_deleteproject(self):
        """
        水利咨询工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IWP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")