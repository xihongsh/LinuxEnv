import unittest,os,re
from selenium import webdriver
from Common.switch_net import Switch
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.photovoltaic_project import IndexPhotovoltaicPage as IPP
from TestDatas.global_datas import GlobalDatas as GD
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestPhotovoltaicIndex(unittest.TestCase):
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

    def test_a_switchnet(self):
        """
        光伏工程：后台设置光伏工程参与绩效计算
        断言：出现'保存成功' 再次选中光伏工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"光伏工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_b_photovoltaic_field(self):
        '''
        光伏工程：验证'项目类型'选择'光伏工程'时，工程类型包括分布式和大棚，建设性质包括光伏区建设，工程规模只有容量一个字段，
        工程投资有勘察费/设计费/总投资三个字段
        '''
        self.driver.get(GD.login_url)
        photovoltaic_retured_field= IPP(self.driver).check_Photovoltaic_field(GD.login_sucess[0],GD.login_sucess[1])
        print(photovoltaic_retured_field)
        self.assertIn(ID.add_photevoltaic_datas["工程类型"],photovoltaic_retured_field[0]),\
        self.assertIn(ID.add_photevoltaic_datas["建设性质"],photovoltaic_retured_field[1]),\
        self.assertEqual(ID.add_photevoltaic_datas["工程规模数量"],photovoltaic_retured_field[2]),\
        self.assertEqual(ID.add_photevoltaic_datas["工程规模字段"],photovoltaic_retured_field[3]),\
        self.assertEqual(ID.add_photevoltaic_datas["工程投资"],photovoltaic_retured_field[4]),\
        self.assertIn(ID.add_photevoltaic_datas["工程投资项1"],photovoltaic_retured_field[5]),\
        self.assertIn(ID.add_photevoltaic_datas["工程投资项2"],photovoltaic_retured_field[5]),\
        self.assertIn(ID.add_photevoltaic_datas["工程投资项3"],photovoltaic_retured_field[5])

    def test_c_create_photevoltaic_project(self):
        '''
        光伏工程：成功创建'光伏工程'项目
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_光伏工程'
        '''
        return_value = IPP(self.driver).create_photovoltaic_project(ID.add_photevoltaic_datas['project_name'],ID.add_photevoltaic_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_photevoltaic_datas['project_name'])

    def test_d_guidang_fail(self):
        '''
        光伏工程：成功创建'光伏工程'项目没有在设计卷册中上传文件发起归档失败
        断言：归档时点击项目名称提示'此项目内无可归档文件，不可发起归档'，且此时没有把监管人带过来
        '''
        results = IPP(self.driver).guidang()
        print(results)
        self.assertEqual(results[0],'此项目内无可归档文件，不可发起归档'),self.assertEqual(results[1],'选择')

    def test_e_guidang_success(self):
        '''
        光伏工程：成功创建'光伏工程'项目并在设计卷册中上传文件发起归档成功
        断言：上传文件成功后显示文件名称和版本号，够选项目监管人显示'徐蕾'，归档成功后归档第一条记录项目名称是'测试光伏工程'
        归档版本为'第一版'，审批人为'徐蕾'，归档状态为'待审批'
        '''
        results = IPP(self.driver).guidang2()
        print(results)
        self.assertEqual(results[0],'测试上传脚本用.txt'),self.assertEqual(results[1],'1'),\
        self.assertEqual(results[2],'徐蕾\n×\n选择'),self.assertEqual(results[3],ID.add_photevoltaic_datas['project_name']),\
        self.assertEqual(results[4],'第一版'),self.assertEqual(results[5],'徐蕾'),self.assertEqual(results[6],'待审批')

    def test_f_thirdguidang_fail(self):
        '''
        光伏工程：成功创建'光伏工程'项目并发起归档成功后监管人还没有审批，不能再次发起审批
        断言：再次发起归档会提示'此项目正处于卷册归档流程中，不可发起归档'
        '''
        results = IPP(self.driver).guidang3()
        print(results)
        self.assertEqual(results,'此项目正处于卷册归档流程中，不可发起归档')

    def test_g_jianguan_checksuccess(self):
        '''
        光伏工程：监管人徐蕾账号登陆系统流程传递正确无误
        断言：'我审批的'第一条记录项目名称是'测试_光伏工程'归档版本是'第一版'，提交人是'张无忌'，归档状态是'待审批'，审批时间是'--'
        '我监管的'第一条记录项目名称是'测试_光伏工程'归档版本是'第一版'，提交人是'张无忌'，审批人是'徐蕾'，归档状态是'待审批'，审批时间是'--'
        '''
        results = IPP(self.driver).jianguanren_checksucess(GD.xulei[0],GD.xulei[1])
        print(results)
        self.assertEqual(results[0],ID.add_photevoltaic_datas["project_name"]),self.assertEqual(results[1],"第一版"), \
        self.assertEqual(results[2], "张无忌"),self.assertEqual(results[3],"待审批"),self.assertEqual(results[4],"--"),\
        self.assertEqual(results[5],ID.add_photevoltaic_datas["project_name"]),self.assertEqual(results[6],"张无忌"),\
        self.assertEqual(results[7],"徐蕾"),self.assertEqual(results[8],"待审批"),self.assertEqual(results[9],"--")
        self.assertEqual(results[10],"第一版")

    def test_h_jianguan_approvesuccess(self):
        '''
        光伏工程：监管人徐蕾账号登陆系统审批完成
        '''
        results = IPP(self.driver).jianguanren_approvesucess()
        print(results)
        for i in range(len(results[0])):
            if "已通过" in results[0][i]:
                self.assertIn("测试_光伏工程",results[0][i]),self.assertIn("已通过",results[0][i]),self.assertIn(results[4],results[0][i])
                break
        self.assertEqual(results[1],'测试_光伏工程'),self.assertEqual(results[2],'已通过'),\
        self.assertIn(results[4],results[3])

    def test_i_faqiguidang_failagain(self):
        """
        光伏工程：发起归档成功并且监管人审批通过后，如果项目的设计卷册没有文件则无法发起归档
        断言：归档点项目名称提示'此项目内无可归档文件，不可发起归档'
        :return:
        """
        results = IPP(self.driver).faqiguidang_failagain(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(results,'此项目内无可归档文件，不可发起归档')

    def test_j_faqiguidang_successagain(self):
        """
        光伏工程：第二次发起归档，上传新的文件'测试上传脚本用.txt'版本号为'1'归档成功
        断言：归档管理-我发起的：数量增加1，并且首条项目名称 '测试_光伏工程'归档版本 '第二版'监管人'徐蕾'归档状态'待审批'
        :return:
        """
        results = IPP(self.driver).guidang_successagain()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[7])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[8])[0])
        self.assertEqual(results[0],'测试上传脚本用2.txt'),self.assertEqual(results[1],'1'),self.assertEqual(num_1+1,num_2)
        self.assertEqual(results[2],'徐蕾\n×\n选择'),self.assertEqual(results[3],'测试_光伏工程'),\
        self.assertEqual(results[4],'第二版'),self.assertEqual(results[5],'徐蕾'),self.assertEqual(results[6], '待审批')

    def test_k_zonggongri(self):
        """
        光伏工程：绩效管理发起审批各个节点都是不可勾选（后台的光伏工程参与绩效计算）
        断言依据：没有发起过校审流程且后台不参与绩效计算，所以发起绩效审批各个节点不可勾选属性都是'button chk checkbox_false_disable'
        """
        attrs = IPP(self.driver).jixiao_manage2()
        print(attrs)
        expected = ('button chk checkbox_false_disable', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable')
        self.assertEqual(attrs,expected)

    def test_l_faqiliucheng(self):
        """
        光伏工程：光伏工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_光伏工程',五审状态是'进行中'
        """
        results = IPP(self.driver).faqijiaoshen()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_photevoltaic_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_m_wushen_loginapprove(self):
        """
        光伏工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_光伏工程',五审状态是'进行中'
        """
        results = IPP(self.driver).wushenren_loginapprove(GD.hairuomeng[0],GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0],ID.add_photevoltaic_datas["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_n_wushen_approvesuccess(self):
        """
        光伏工程：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'
        """
        results = IPP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_photevoltaic_datas["project_name"])

    def test_o_faqiren_checksuccess(self):
        """
        光伏工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'，五审状态是'已通过'确认人是"--"
        :return:
        """
        results = IPP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_photevoltaic_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_p_faqiren_faqisure(self):
        """
        光伏工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IPP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_photevoltaic_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_q_sureperson_checksuccess(self):
        """
        光伏工程：确认人海清人登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IPP(self.driver).sureperson_check_returedproject(GD.haiqing[0], GD.haiqing[1])
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"), self.assertEqual(results[1], ID.add_photevoltaic_datas["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "无"), self.assertEqual(results[4],"无"), \
        self.assertEqual(results[5], "进行中")

    def test_r_sureperson_approvesuccess(self):
        """
        光伏工程：确认人海清发起确认成功
        断言：'校审-已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IPP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"), self.assertEqual(results[1], ID.add_photevoltaic_datas["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "无"), self.assertEqual(results[4],"无"), \
        self.assertEqual(results[5], "已通过")

    def test_s_faqiren_checksuccess(self):
        """
        光伏工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_光伏工程'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IPP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0], GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"), self.assertEqual(results[1], ID.add_photevoltaic_datas["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "已通过")

    def test_t_jixiaobox(self):
        """
        光伏工程：绩效管理发起审批弹框正确无误（后台的光伏工程参与绩效计算）
        断言依据：只有发起过校审流程并且走完审批流程的01设计输入资料才可勾选，其他节点不可被勾选
        """
        attrs = IPP(self.driver).jixiao_manage3()
        print(attrs)
        expected = ('button chk checkbox_false_full', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable', 'button chk checkbox_false_disable',
                    'button chk checkbox_false_disable')
        self.assertEqual(attrs,expected)

    def test_u_zonggongri(self):
        """
        光伏工程：绩效管理：验证标准共日和提报共日都为12.09 （基本工日：8.81考核工日：3.28）
        """
        days_count = IPP(self.driver).jixiao_manage33()
        print(days_count)
        self.assertEqual(days_count[0],'12.09 （基本工日：8.81考核工日：3.28）'),self.assertEqual(days_count[1],'12.09 （基本工日：8.81 考核工日：3.28）')

    def test_v_deleteproject(self):
        """
        光伏工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IPP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_w_create_photevoltaic_project(self):
        '''
        光伏工程：成功创建'光伏工程'项目
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_光伏工程2'
        '''
        return_value = IPP(self.driver).create_photovoltaic_project2(ID.add_photevoltaic_datas2['project_name'],ID.add_photevoltaic_datas2['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_photevoltaic_datas2['project_name'])

    def test_x_faqiliucheng(self):
        """
        光伏工程：光伏工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_光伏工程2',五审状态是'进行中'
        """
        results = IPP(self.driver).faqijiaoshen2()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_photevoltaic_datas2['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_y_quxiaoliucheng(self):
        """
        光伏工程：发起流程成功后，在取消流程
        取消成功断言：出现'取消成功'文本值，并出现'重新发起流程'文本值

        :return:
        """
        results = IPP(self.driver).quxiaojiaoshen()
        print(results)
        self.assertEqual(results[0],"取消成功"),self.assertEqual(results[1],"重新发起流程")

    def test_z_zaicifaqiliucheng(self):
        """
        光伏工程：取消流程成功后，再次发起流程
        再次发起流程成功断言：出现提示语'流程发起成功'，且列表只有一条记录，项目名字是'测试_光伏工程2',
        五审状态是'进行中'
        :return:
        """
        results = IPP(self.driver).zaici_faqijiaoshen()
        print(results)
        self.assertEqual(results[0],'流程发起成功'),self.assertEqual(results[1],ID.add_photevoltaic_datas2['project_name']),\
        self.assertEqual(results[2],'进行中'),self.assertEqual(results[3],1)

    def test_za_deleteproject(self):
        """
        光伏工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IPP(self.driver).delete_2()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_zb_switchnet(self):
        """
        光伏工程：后台设置光伏工程不参与绩效计算
        断言：出现'保存成功' 再次选中光伏工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"光伏工程 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_zc_create_photevoltaic_project(self):
        '''
        光伏工程：成功创建'光伏工程'项目（后台光伏工程不参与绩效计算）
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_光伏工程'
        '''
        self.driver.get(GD.login_url)
        return_value = IPP(self.driver).create_photovoltaic_project4(GD.login_sucess[0],GD.login_sucess[1],ID.add_photevoltaic_datas['project_name'],ID.add_photevoltaic_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_photevoltaic_datas['project_name'])

    def test_zd_jixiao(self):
        """
        光伏工程：绩效管理发起审批弹框都是可勾选状态（后台光伏工程不参与绩效计算）
        断言依据：所有的勾选框属性都是'checkbox_false_full'
        """
        attrs = IPP(self.driver).jixiao_manage2()
        print(attrs)
        expected = ('button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full')
        self.assertEqual(attrs,expected)

    def test_ze_faqijiaoshen(self):
        """
        光伏工程：光伏工程发起绩效审批成功（后台光伏工程不参与绩效计算）
        断言：提示'成功'并且出现'取消申请'按钮
        """
        results = IPP(self.driver).jixiao_manage4()
        print(results)
        self.assertEqual(results[0],"成功"),self.assertEqual(results[1],"取消申请")

    def test_zf_jixiao(self):
        """
        光伏工程：绩效管理再次发起审批弹框除'01设计输入资料'外都是可勾选状态（后台光伏工程不参与绩效计算）
        断言依据：'01设计输入资料'勾选框属性是'checkbox_true_disable'其他勾选框属性都是'checkbox_false_full'
        """
        attrs = IPP(self.driver).jixiao_manage22()
        print(attrs)
        expected = ('button chk checkbox_true_disable', 'button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full', 'button chk checkbox_false_full', 'button chk checkbox_false_full',
                    'button chk checkbox_false_full')
        self.assertEqual(attrs,expected)

    def test_zg_deleteproject(self):
        """
        光伏工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IPP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")



