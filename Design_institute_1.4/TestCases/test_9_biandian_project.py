import unittest,os,re
from selenium import webdriver
from Common.switch_net import Switch
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.biandian_project import IndexBianPage as IBP
from TestDatas.global_datas import GlobalDatas as GD
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestBiandianIndex(unittest.TestCase):
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

    def test_a_biandian_field(self):
        '''
        变电工程：验证'项目类型'选择'变电工程'时，工程类型包括户内和户外，建设性质包括变电新建，主变新建，主变增容，间隔扩建，
        全站改造，综自改造，大修技改，其他
        '''
        retured_field= IBP(self.driver).check_biandian_field()
        print(retured_field)
        self.assertEqual(retured_field[0],ID.add_biandian_datas['工程类型']),\
        self.assertEqual(retured_field[1],ID.add_biandian_datas['建设性质'])


    def test_b_create_biandian_project(self):
        '''
        变电工程：成功创建'变电工程'项目
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_光伏工程'
        '''
        return_value = IBP(self.driver).create_biandian_project(ID.add_biandian_datas['project_name'],ID.add_biandian_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_biandian_datas['project_name'])

    def test_c_switchnet(self):
        """
        变电工程：后台设置变电工程参与绩效计算
        断言：出现'保存成功' 再次选中变电工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"变电工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_d_jixiao(self):
        """
        变电工程：绩效管理发起审批弹框都是不可勾选状态
        断言依据：所有的勾选框属性都是'checkbox_false_disable'
        """
        self.driver.get(GD.login_url)
        attrs = IBP(self.driver).jixiao_manage2(GD.login_sucess[0],GD.login_sucess[1])
        print(attrs)
        for attr in attrs:
            self.assertIn("checkbox_false_disable",attr)

    def test_e_faqijiaoshen(self):
        """
        变电工程：变电工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_变电工程',五审状态是'进行中'
        """
        results = IBP(self.driver).faqijiaoshen()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_biandian_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_f_wushen_loginapprove(self):
        """
        变电工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_变电工程',五审状态是'进行中'
        """
        results = IBP(self.driver).wushenren_loginapprove(GD.hairuomeng[0],GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_g_wushen_approvesuccess(self):
        """
        变电工程：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'
        """
        results = IBP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_biandian_datas["project_name"])

    def test_h_faqiren_checksuccess(self):
        """
        变电工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，五审状态是'已通过'确认人状态是"--"
        :return:
        """
        results = IBP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_i_faqiren_faqisure(self):
        """
        变电工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IBP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_j_sureperson_checksuccess(self):
        """
        变电工程：确认人海清人登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IBP(self.driver).sureperson_check_returedproject(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")

    def test_k_sureperson_approvesuccess(self):
        """
        变电工程：确认人海清发起确认成功
        断言：'校审-已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IBP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"已通过")

    def test_l_faqiren_checksuccess(self):
        """
        变电工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IBP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")

    def test_m_jixiao(self):
        """
        变电工程：卷册验证
        断言依据：01-设计输入资料 勾选框可勾选，其他勾选框不可勾选
        """
        results = IBP(self.driver).jixiao_manage3()
        print(results)
        self.assertEqual(results,ID.juance_boxs)


    def test_n_jixiao(self):
        """
        变电工程：绩效验证：
        额外系数：1
        最终难易系数：1   标准总工日：8 （基本工日：5.4考核工日：2.6）
        提报总工日：8 （基本工日：5.4 考核工日：2.6）
        """
        days_count = IBP(self.driver).jixiao_manage()
        print(days_count)
        self.assertEqual(days_count[0],"1"),self.assertEqual(days_count[1],"1"),\
        self.assertEqual(days_count[2],"8 （基本工日：5.4考核工日：2.6）"),self.assertEqual(days_count[3],'8 （基本工日：5.4 考核工日：2.6）')

    def test_o_deleteproject(self):
        """
        变电工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IBP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_p_create_biandian_project(self):
        '''
        变电工程：成功创建'变电工程'项目
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_变电工程2'
        '''
        return_value = IBP(self.driver).create_biandian_project2(ID.add_biandian_datas2['project_name'],ID.add_biandian_datas2['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_biandian_datas2['project_name'])

    def test_q_faqijiaoshen(self):
        """
        变电工程：变电工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_变电工程2',五审状态是'进行中'
        """
        results = IBP(self.driver).faqijiaoshen2()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_biandian_datas2['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_r_wushen_loginapprove(self):
        """
        变电工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_变电工程2',五审状态是'进行中'
        """
        results = IBP(self.driver).wushenren_loginapprove2(GD.hairuomeng[0],GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0],ID.add_biandian_datas2["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_s_wushen_tuihuisuccess(self):
        """
        变电工程：五审退回成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程2'
        五审状态是未通过
        """
        results = IBP(self.driver).wushenren_tuihuisucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_biandian_datas2["project_name"]),\
        self.assertEqual(results[6],"未通过")

    def test_t_faqiren_checksuccess(self):
        """
        变电工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程2'，五审状态是'未通过'六审是"--"
        :return:
        """
        results = IBP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas2["project_name"]),\
        self.assertEqual(results[2],"未通过"),self.assertEqual(results[3],"--")

    def test_u_deleteproject2(self):
        """
        变电工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IBP(self.driver).delete_2()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_v_switchnet(self):
        """
        变电工程：后台设置变电工程不参与绩效计算
        断言：出现'保存成功' 再次选中变电工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"变电工程 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_w_create_biandian_project(self):
        '''
        变电工程：成功创建'变电工程'项目（后台变电工程不参与绩效计算）
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_变电工程'
        '''
        self.driver.get(GD.login_url)
        return_value = IBP(self.driver).create_biandian_project3(GD.login_sucess[0],GD.login_sucess[1],ID.add_biandian_datas['project_name'],ID.add_biandian_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_biandian_datas['project_name'])

    def test_x_jixiao(self):
        """
        变电工程：绩效管理发起审批弹框都是可勾选状态（后台变电工程不参与绩效计算）
        断言依据：所有的勾选框属性都是'checkbox_false_full'
        """
        attrs = IBP(self.driver).jixiao_manage25()
        print(attrs)
        for attr in attrs:
            self.assertIn("checkbox_false_full",attr)

    def test_y_faqijiaoshen(self):
        """
        变电工程：变电工程发起绩效审批成功（后台变电工程不参与绩效计算）
        断言：提示'成功'并且出现'取消申请'按钮
        """
        results = IBP(self.driver).jixiao_manage4()
        print(results)
        self.assertEqual(results[0],"成功"),self.assertEqual(results[1],"取消申请")


    def test_z_jixiao(self):
        """
        变电工程：绩效管理再次发起审批弹框除04前提阶段批复意见外都是可勾选状态（后台变电工程不参与绩效计算）
        断言依据：所有的勾选框属性都是'checkbox_false_full'04前提阶段批复意见
        """
        attrs = IBP(self.driver).jixiao_manage22()
        print(attrs)
        expected = ('button chk checkbox_false_full', 'button chk checkbox_true_disable', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full', 'button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full')
        self.assertEqual(attrs,expected)

    def test_za_deleteproject(self):
        """
        变电工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IBP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_zc_create_biandian_project(self):
        '''
        变电工程：成功创建'变电工程'项目
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_光伏工程'
        '''
        return_value = IBP(self.driver).create_biandian_project00(ID.add_biandian_datas['project_name'],ID.add_biandian_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_biandian_datas['project_name'])

    def test_zd_switchnet(self):
        """
        变电工程：后台设置变电工程参与绩效计算
        断言：出现'保存成功' 再次选中变电工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"变电工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_ze_faqijiaoshen(self):
        """
        变电工程：变电工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_变电工程',确认状态是'进行中'
        """
        self.driver.get(GD.login_url)
        results = IBP(self.driver).faqijiaoshen33(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_biandian_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zf_surep_loginapprove(self):
        """
        变电工程：确认人登陆审批成功
        断言：已处理项目"测试_变电工程" 确认人状态为"已通过"
        """
        results = IBP(self.driver).wushenren_loginapprove11(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas['project_name']),self.assertEqual(results[2],"已通过")

    def test_zg_faqiren_checksuccess(self):
        """
        变电工程：发起人登陆，确认人审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_变电工程'，确认人状态是"已通过"
        :return:
        """
        results = IBP(self.driver).faqiren_check_returedproject26(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_biandian_datas["project_name"]),\
        self.assertEqual(results[2],"已通过")

    def test_zh_jixiao(self):
        """
        变电工程：验证系数调整
        断言：调整系数输入10提示'调整系数不可大于5.67！'
        """
        results = IBP(self.driver).jixiao_manage00()
        print(results)
        self.assertEqual(results,"调整系数不可大于5.67！")

    def test_zi_hanzheng_approve(self):
        """
        线路工程：韩正修改系数调整和考核工日
        断言：调整系数输入10提示"调整系数不可大于5.67！"考核工日输入100提示"同角色内人员的有效考核工日总和不可大于该角色标准考核工日4.56倍！"
        :return:
        """
        results = IBP(self.driver).hanzheng_logincheck00(GD.hanzheng[0],GD.hanzheng[1])
        print(results)
        self.assertEqual(results[0],"调整系数不可大于5.67！"),self.assertEqual(results[1],"同角色内人员的有效考核工日总和不可大于该角色标准考核工日4.56倍！")

    def test_zj_deleteproject(self):
        """
        变电工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IBP(self.driver).delete_12(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]-1, results[1]), self.assertEqual(results[2], "删除成功！")







