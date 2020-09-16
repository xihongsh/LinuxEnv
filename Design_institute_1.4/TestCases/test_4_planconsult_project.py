import unittest,os,re
from selenium import webdriver
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.planningconsulting_project import IndexPlanConsultPage as IP
from TestDatas.global_datas import GlobalDatas as GD
from Common.switch_net import Switch
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestPlanConsult(unittest.TestCase):
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

    def test_a_check_planconsult_fields(self):
        """
        规划咨询工程：验证规划咨询工程字段
        断言：
        工程类型：常规规划\专项规划\专题研究\综合能源规划
        建设性质：建成区\新建区
        """
        retured_fields = IP(self.driver).check_planconsult_field()
        print(retured_fields)
        self.assertEqual(retured_fields[0],ID.add_planconsult_datas["工程类型"]),\
        self.assertEqual(retured_fields[1],ID.add_planconsult_datas["建设性质"]),\
        self.assertEqual(retured_fields[2],ID.add_planconsult_datas["工程规模_1"]),\
        self.assertEqual(retured_fields[3],ID.add_planconsult_datas["工程规模_2"])

    def test_b_create_planconsult_project(self):
        """
        规划咨询工程（建成区）：成功创建规划咨询工程（建成区）
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project(ID.add_planconsult_datas["project_name"],ID.add_planconsult_datas["project_no"])
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas["project_name"])

    def test_c_switchnet(self):
        """
        规划咨询工程：后台设置规划咨询工程不参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_d_jixiao(self):
        """
        规划咨询工程（建成区）：回路系数=2、最终系数=2、项目总标准工日=200、提报比例=20%，标准工日=34
        :return:
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).jixiaoguanli(GD.login_sucess[0],GD.login_sucess[1],ID.add_planconsult_datas["rate"])
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        print(num_1,num_2,num_3)
        self.assertEqual(num_1,2),self.assertEqual(num_2,2.0),self.assertEqual(num_3,200),\
        self.assertEqual(results[3],"20%"),self.assertEqual(results[4],"34")

    def test_e_deleteproject(self):
        """
        规划咨询工程（建成区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_f_create_planconsult_project(self):
        """
        规划咨询工程（新建区）：成功创建规划咨询工程（新建区）
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程2'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project2(ID.add_planconsult_datas2["project_name"],ID.add_planconsult_datas2["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas2["project_name"])

    def test_g_jixiao(self):
        """
        规划咨询工程（新建区）：面积系数=0.1、最终系数=0.1、项目总标准工日=10、提报比例=20%、标准工日=1.7
        :return:
        """
        results = IP(self.driver).jixiaoguanli2(ID.add_planconsult_datas2["rate"])
        print(results)
        num_1 = float(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        print(num_1,num_2,num_3)
        self.assertEqual(num_1,0.1),self.assertEqual(num_2,0.1),self.assertEqual(num_3,10),\
        self.assertEqual(results[3],"20%"),self.assertEqual(results[4],"1.7")

    def test_h_faqiliucheng(self):
        """
        规划咨询工程（新建区）：规划咨询工程发起校审流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称为'测试_规划咨询工程2'和五审状态为'进行中'
        """
        results = IP(self.driver).faqijiaoshen()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_planconsult_datas2['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_i_wushen_loginapprove(self):
        """
        规划咨询工程（新建区）：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_规划咨询工程2',五审状态是'进行中'
        """
        results = IP(self.driver).wushenren_loginapprove(GD.hairuomeng[0],GD.hairuomeng[1])
        self.assertEqual(results[0],ID.add_planconsult_datas2["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_j_wushen_approvesuccess(self):
        """
        规划咨询工程（新建区）：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程2'
        """
        results = IP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"规划咨询报告"),self.assertEqual(results[5],ID.add_planconsult_datas2["project_name"])

    def test_k_faqiren_checksuccess(self):
        """
        规划咨询工程（新建区）：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程2'，五审状态是'已通过'六审是"--"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas2["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_l_deleteproject(self):
        """
        规划咨询工程（新建区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_2()
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_m_switchnet(self):
        """
        规划咨询工程：后台设置规划咨询工程参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_n_create_planconsult_project(self):
        """
        规划咨询工程（建成区）：成功创建规划咨询工程（建成区）(创建项目时工程类型选择“专题研究)
        10kV线路=不需要输入，提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程3'
        :return:
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).create_photovoltaic_project22(GD.login_sucess[0],GD.login_sucess[1],ID.add_planconsult_datas3["project_name"],ID.add_planconsult_datas3["project_no"])
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas3["project_name"])

    def test_o_jixiao(self):
        """
        规划咨询工程（建成区）：(创建项目时工程类型选择“专题研究)
        10kV线路=不需要输入，提报比例=20%
        断言依据：最终系数:2.89、项目总标准工日:433.5、标准工日： 73.7、提报工日： 73.7
        :return:
        """
        results = IP(self.driver).jixiaoguanli5(ID.add_planconsult_datas3["rate"])
        print(results)
        num_1 = float(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1,2.89),self.assertEqual(num_2,433.5),\
        self.assertEqual(results[2],"73.7"),self.assertEqual(results[3],"73.7")

    def test_p_deleteproject(self):
        """
        规划咨询工程（建成区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_3()
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_q_create_planconsult_project(self):
        """
        规划咨询工程（新建区）：成功创建规划咨询工程（新建区）(创建项目时工程类型选择“专题研究)
        10kV线路=不需要输入，提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程4'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project33(ID.add_planconsult_datas4["project_name"],ID.add_planconsult_datas4["project_no"])
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas4["project_name"])

    def test_r_jixiao(self):
        """
        规划咨询工程（新建区）：(创建项目时工程类型选择“专题研究) 10kV线路=不需要输入，提报比例=20%
        最终系数:2.89、项目总标准工日:433.5、标准工日： 73.7、提报工日： 73.7
        :return:
        """
        results = IP(self.driver).jixiaoguanli6(ID.add_planconsult_datas4["rate"])
        print(results)
        num_1 = float(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1,2.89),self.assertEqual(num_2,433.5),\
        self.assertEqual(results[2],"73.7"),self.assertEqual(results[3],"73.7")

    def test_s_deleteproject(self):
        """
        规划咨询工程（建成区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_4()
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_t_create_planconsult_project(self):
        """
        规划咨询工程（建成区）：成功创建规划咨询工程（建成区）需要输入：10kV线路=400，提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程5'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project66(ID.add_planconsult_datas5["project_name"],ID.add_planconsult_datas5["project_no"])
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas5["project_name"])

    def test_u_jixiao(self):
        """
        规划咨询工程（建成区）：需要输入：10kV线路=400，提报比例=20%
        断言依据：回路系数=2、最终系数=2、项目总标准工日=200、提报比例=20%，标准工日=34
        :return:
        """
        results = IP(self.driver).jixiaoguanli11(ID.add_planconsult_datas["rate"])
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        print(num_1,num_2,num_3)
        self.assertEqual(num_1,2),self.assertEqual(num_2,2.0),self.assertEqual(num_3,200),\
        self.assertEqual(results[3],"20%"),self.assertEqual(results[4],"34")

    def test_v_deleteproject(self):
        """
        规划咨询工程（建成区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_5()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_w_create_planconsult_project(self):
        """
        规划咨询工程（新建区）：成功创建规划咨询工程（新建区）需要输入：规划面积=123、提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程6'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project6(ID.add_planconsult_datas6["project_name"],ID.add_planconsult_datas6["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas6["project_name"])

    def test_x_switchnet(self):
        """
        规划咨询工程（新建区）：后台设置规划咨询工程不参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_y_jixiao(self):
        """
        规划咨询工程（新建区）：需要输入：规划面积=123、提报比例=20%
        断言依据：面积系数=0.1、最终系数=0.1、项目总标准工日=10、提报比例=20%、标准工日=1.7
        :return:
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).jixiaoguanli23(GD.login_sucess[0],GD.login_sucess[1],ID.add_planconsult_datas6["rate"])
        print(results)
        num_1 = float(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = float(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        print(num_1,num_2,num_3)
        self.assertEqual(num_1,0.1),self.assertEqual(num_2,0.1),self.assertEqual(num_3,10),\
        self.assertEqual(results[3],"20%"),self.assertEqual(results[4],"1.7")

    def test_z_switchnet(self):
        """
        规划咨询工程（新建区）：后台设置规划咨询工程参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_za_faqiliucheng(self):
        """
        规划咨询工程（新建区）：规划咨询工程发起校审流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称为'测试_规划咨询工程6'和五审状态为'进行中'
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).faqijiaoshen2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_planconsult_datas6['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zb_wushen_loginapprove(self):
        """
        规划咨询工程（新建区）：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_规划咨询工程6',五审状态是'进行中'
        """
        results = IP(self.driver).wushenren_loginapprove(GD.hairuomeng[0], GD.hairuomeng[1])
        self.assertEqual(results[0], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zc_wushen_approvesuccess(self):
        """
        规划咨询工程（新建区）：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'
        """
        results = IP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "规划咨询报告"), self.assertEqual(results[5], ID.add_planconsult_datas6["project_name"])

    def test_zd_faqiren_checksuccess(self):
        """
        规划咨询工程（新建区）：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人是"--"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0], GD.login_sucess[1])
        self.assertEqual(results[0], "规划咨询报告"), self.assertEqual(results[1], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "--")

    def test_ze_faqiren_faqisure(self):
        """
        规划咨询工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是" "规划咨询报告""项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0], "规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_zf_sureperson_checksuccess(self):
        """
        规划咨询工程：确认人海清人登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).sureren_checksuc(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")

    def test_zg_sureperson_approvesuccess(self):
        """
        规划咨询工程：确认人海清发起确认成功
        断言：'校审-已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"已通过")

    def test_zh_faqiren_checksuccess(self):
        """
        规划咨询工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")


    def test_zi_jixiao(self):
        """
        规划咨询工程（新建区）：校审流程文件没有问题，没有延期,成品质量系数为1.7
        :return:
        """
        results = IP(self.driver).jixiaoguanli25(ID.add_planconsult_datas6["rate"])
        print(results)
        self.assertEqual(results,"1.7")

    def test_zj_deleteproject(self):
        """
        规划咨询工程（新建区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_6()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_zk_create_planconsult_project(self):
        """
        规划咨询工程（新建区）：成功创建规划咨询工程（新建区）需要输入：规划面积=123、提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程6'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project6(ID.add_planconsult_datas6["project_name"],ID.add_planconsult_datas6["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas6["project_name"])

    def test_zl_switchnet(self):
        """
        规划咨询工程（新建区）：后台设置规划咨询工程参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_zm_faqiliucheng(self):
        """
        规划咨询工程（新建区）：规划咨询工程发起校审流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称为'测试_规划咨询工程6'和五审状态为'进行中'
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).faqijiaoshen3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_planconsult_datas6['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zn_wushen_loginapprove(self):
        """
        规划咨询工程（新建区）：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_规划咨询工程6',五审状态是'进行中'
        """
        results = IP(self.driver).wushenren_loginapprove(GD.hairuomeng[0], GD.hairuomeng[1])
        self.assertEqual(results[0], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zo_wushen_approvesuccess(self):
        """
        规划咨询工程（新建区）：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'
        """
        results = IP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "规划咨询报告"), self.assertEqual(results[5], ID.add_planconsult_datas6["project_name"])

    def test_zp_faqiren_checksuccess(self):
        """
        规划咨询工程（新建区）：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人是"--"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0], GD.login_sucess[1])
        self.assertEqual(results[0], "规划咨询报告"), self.assertEqual(results[1], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "--")

    def test_zq_faqiren_faqisure(self):
        """
        规划咨询工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是" "规划咨询报告""项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0], "规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_zr_sureperson_checksuccess(self):
        """
        规划咨询工程：确认人海清人登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).sureren_checksuc(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")

    def test_zs_sureperson_approvesuccess(self):
        """
        规划咨询工程：确认人海清发起确认成功
        断言：'校审-已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"已通过")

    def test_zt_faqiren_checksuccess(self):
        """
        规划咨询工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")


    def test_zu_jixiao(self):
        """
        规划咨询工程（新建区）：校审流程文件没有问题，没有延期且提前5天完成,成品质量系数为1.05
        :return:
        """
        results = IP(self.driver).jixiaoguanli24(ID.add_planconsult_datas6["rate"])
        print(results)
        self.assertEqual(results,"1.05")

    def test_zv_deleteproject(self):
        """
        规划咨询工程（新建区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_6()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_zw_create_planconsult_project(self):
        """
        规划咨询工程（新建区）：成功创建规划咨询工程（新建区）需要输入：规划面积=123、提报比例=20%
        断言：台账列表数量增加1，且第一条记录项目名称是'测试_规划咨询工程6'
        :return:
        """
        results = IP(self.driver).create_photovoltaic_project6(ID.add_planconsult_datas6["project_name"],ID.add_planconsult_datas6["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_planconsult_datas6["project_name"])

    def test_zx_switchnet(self):
        """
        规划咨询工程（新建区）：后台设置规划咨询工程参与绩效计算
        断言：出现'保存成功' 再次选中规划咨询工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"规划咨询 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_zy_faqiliucheng(self):
        """
        规划咨询工程（新建区）：规划咨询工程发起校审流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称为'测试_规划咨询工程6'和五审状态为'进行中'
        """
        self.driver.get(GD.login_url)
        results = IP(self.driver).faqijiaoshen3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_planconsult_datas6['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zz_wushen_loginapprove(self):
        """
        规划咨询工程（新建区）：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_规划咨询工程6',五审状态是'进行中'
        """
        results = IP(self.driver).wushenren_loginapprove(GD.hairuomeng[0], GD.hairuomeng[1])
        self.assertEqual(results[0], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zza_wushen_tuihuisuccess(self):
        """
        规划咨询工程（新建区）：五审人退回成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'未通过'
        """
        results = IP(self.driver).wushenren_tuihuisucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "规划咨询报告"), self.assertEqual(results[5], ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[6],"未通过")

    def test_zzb_faqiren_checksuccess(self):
        """
        规划咨询工程（新建区）：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'未通过'确认人是"--"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0], GD.login_sucess[1])
        self.assertEqual(results[0], "规划咨询报告"), self.assertEqual(results[1], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[2], "未通过"), self.assertEqual(results[3], "--")

    def test_zzc_faqiliuchengagain(self):
        """
        规划咨询工程（新建区）：规划咨询工程再次发起校审流程
        断言：第一条记录项目名称为'测试_规划咨询工程6'和五审状态为'进行中'
        """
        results = IP(self.driver).faqijiaoshen4()
        print(results)
        self.assertEqual(results[0],ID.add_planconsult_datas6['project_name']),self.assertEqual(results[1],"进行中")

    def test_zzd_wushen_loginapprove(self):
        """
        规划咨询工程（新建区）：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_规划咨询工程6',五审状态是'进行中'
        """
        results = IP(self.driver).wushenren_loginapprove(GD.hairuomeng[0], GD.hairuomeng[1])
        self.assertEqual(results[0], ID.add_planconsult_datas6["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zze_wushen_approvesuccess(self):
        """
        规划咨询工程（新建区）：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'
        五审状态是'已通过'
        """
        results = IP(self.driver).wushenren_approvesucess2()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "规划咨询报告"), self.assertEqual(results[5], ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[6],"已通过")

    def test_zzf_faqiren_checksuccess(self):
        """
        规划咨询工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"--"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_zzg_faqiren_faqisure(self):
        """
        规划咨询工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是" "规划咨询报告""项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0], "规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_zzh_sureperson_checksuccess(self):
        """
        规划咨询工程：确认人海清人登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IP(self.driver).sureren_checksuc(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")

    def test_zzi_sureperson_approvesuccess(self):
        """
        规划咨询工程：确认人海清发起确认成功
        断言：'校审-已处理'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"已通过")

    def test_zzj_faqiren_checksuccess(self):
        """
        规划咨询工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"规划咨询报告"项目名称是'测试_规划咨询工程6'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"规划咨询报告"),self.assertEqual(results[1],ID.add_planconsult_datas6["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")


    def test_zzk_jixiao(self):
        """
        规划咨询工程（新建区）：校审流程提前5天完成但犯了一个一般性问题所以成品质量系数是1.04
        :return:
        """
        results = IP(self.driver).jixiaoguanli30(ID.add_planconsult_datas6["rate"])
        print(results)
        self.assertEqual(results,"1.04")

    def test_zzl_deleteproject(self):
        """
        规划咨询工程（新建区）：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_6()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

