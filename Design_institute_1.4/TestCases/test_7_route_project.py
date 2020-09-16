import unittest,os,re,time
from selenium import webdriver
from Common.switch_net import Switch
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.route_project import IndexRoutePage as IRP
from TestDatas.global_datas import GlobalDatas as GD
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestRouteIndex(unittest.TestCase):
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

    def test_a_check_route_fields(self):
        """
        线路工程：验证线路工程字段 工程类型：架空，电缆；建设性质：有'可研勘测设计一体化项目’选项；
        """
        retured_fields = IRP(self.driver).check_route_field()
        print(retured_fields)
        self.assertEqual(retured_fields[0],ID.add_route_datas["工程类型"]),\
        self.assertIn(ID.add_route_datas["建设性质"],retured_fields[1])


    def test_b_create_route_project(self):
        """
        线路工程：成功创建线路工程
        断言：项目台账列表数量增加1，且首个项目名称是'测试_线路工程'
        :return:
        """
        results = IRP(self.driver).create_route_project(ID.add_route_datas["project_name"],ID.add_route_datas["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_route_datas["project_name"])

    def test_c_switchnet(self):
        """
        线路工程：后台设置线路工程工程不参与绩效计算
        断言：出现'保存成功' 再次选中线路工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"线路工程 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_d_jixiao(self):
        """
        线路工程：提报比例：40% ；项目经理：10% (6工日） 电气：55% (33工日） 结构：35% (21工日）
        标准工日:43.5（基本工日：33.3考核工日：10.2）,提报工日:43.5（基本工日：33.3考核工日：10.2）
        提交审批成功：弹出'成功'并且出现'审批留痕'按钮
        :return:
        """
        self.driver.get(GD.login_url)
        results = IRP(self.driver).jixiaoguanli_1(GD.login_sucess[0],GD.login_sucess[1],ID.add_route_datas["rate"])
        print(results)
        new_date_1 = results[2].replace(" ","")
        new_date_2 = results[3].replace(" ","")
        self.assertEqual(results[0],ID.add_route_datas["提报比例"]),self.assertEqual(results[1],ID.add_route_datas["专业占比"]),\
        self.assertEqual(new_date_1,ID.add_route_datas["标准工日"]),self.assertEqual(new_date_2,ID.add_route_datas["提报工日"]),\
        self.assertEqual(results[4],"成功"),self.assertEqual(results[5],"审批留痕")

    def test_e_hanzheng_logincheck(self):
        """
        线路工程：韩正登陆系统检查绩效管理
        断言：
        '我审批的':第一条记录项目名称是'测试_线路工程'提报比例是'40%'审批状态是'待审批'审批时间是'--'
        '监管的':第一条记录项目名称是'测试_线路工程'提报比例是'40%'审批状态是'待审批'审批时间是'--'
        :return:
        """
        results = IRP(self.driver).hanzheng_logincheck(GD.hanzheng[0],GD.hanzheng[1])
        self.assertEqual(results[0],"测试_线路工程"),self.assertEqual(results[1],"40%(预支)"),\
        self.assertEqual(results[2],"待审批"),self.assertEqual(results[3],"--"),\
        self.assertEqual(results[4],"测试_线路工程"),self.assertEqual(results[5],"40%(预支)"),\
        self.assertEqual(results[6],"待审批"),self.assertEqual(results[7],"--")

    def test_f_hanzheng_approvesuccess(self):
        """
        线路工程：韩正审批通过
        断言：绩效管理-我监管的：第一条记录项目名称是'测试_线路工程'提报比例'40%（预支）'审批状态为'已通过'审批日期为当日
        且'我审批的'第一个审批状态为'已通过'的是'测试_线路工程'
        """
        results = IRP(self.driver).hanzheng_approvesuccess()
        print(results)
        for i in range(len(results[6])):
            if "已通过" in results[6][i]:
                self.assertIn("测试_线路工程",results[6][i])
                break
        self.assertEqual(results[0],'测试_线路工程'),self.assertEqual(results[1],'40%(预支)'),\
        self.assertEqual(results[2],'成功'),self.assertIn(results[5],results[3]),self.assertEqual(results[4],'已通过')

    def test_g_second_rate(self):
        """
        线路工程：第二次提报比例为60%且不可修改，但提交审批成功
        """
        results = IRP(self.driver).jixiaoguanli_2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"60"),self.assertEqual(results[1],"true")

    def test_h_hanzheng_approvesuccess2(self):
        """
        线路工程：韩正审批通过
        断言：绩效管理-我监管的：第一条记录项目名称是'测试_线路工程'提报比例'60%'审批状态为'已通过'审批日期为当日
        且'我审批的'第一个审批状态为'已通过'是'测试_线路工程'
        """
        results = IRP(self.driver).hanzheng_approvesuccess3(GD.hanzheng[0],GD.hanzheng[1])
        print(results)
        for i in range(len(results[6])):
            if "已通过" in results[6][i]:
                self.assertIn("测试_线路工程",results[6][i])
                break
        self.assertEqual(results[0],'测试_线路工程'),self.assertEqual(results[1],'60%'),\
        self.assertEqual(results[2],'成功'),self.assertIn(results[5],results[3]),self.assertEqual(results[4],'已通过')

    def test_i_jixiao(self):
        """
        线路工程：线路工程只能发起两次绩效审批，且两次之和为100%，第三次则没有'提交审批按钮'
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_3(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(results,"没有发起审批按钮")

    def test_j_faqiliucheng(self):
        """
        线路工程：线路工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_线路工程',五审状态是'进行中'
        """
        results = IRP(self.driver).faqijiaoshen()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_route_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_k_wushen_loginapprove(self):
        """
        线路工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_线路工程',五审状态是'进行中'
        """
        results = IRP(self.driver).wushenren_loginapprove88(GD.hairuomeng[0],GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0],ID.add_route_datas["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_l_wushen_approvesuccess(self):
        """
        线路工程：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程'
        """
        results = IRP(self.driver).wushenren_approvesucess_a()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_route_datas["project_name"])

    def test_m_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程'，五审状态是'已通过'六审是"--"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"--")

    def test_n_deleteproject(self):
        """
        线路工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IRP(self.driver).delete_1()
        print(results)
        self.assertEqual(results[0] - 1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_o_create_route_project(self):
        """
        线路工程：成功创建线路工程(测绩效统计用)
        断言：项目台账列表数量增加1，且首个项目名称是'测试_线路工程2'
        :return:
        """
        results = IRP(self.driver).create_route_project2(ID.add_route_datas2["project_name"],ID.add_route_datas2["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_route_datas2["project_name"])

    def test_p_jixiao(self):
        """
        线路工程：提报比例：100%
        提交审批成功：弹出'成功'并且出现'审批留痕'按钮
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_4()
        print(results)
        self.assertEqual(results[0],"成功"),self.assertEqual(results[1],"审批留痕")

    def test_q_hanzheng_approvesuccess(self):
        """
        线路工程：韩正审批通过
        断言：绩效管理-我监管的：第一条记录项目名称是'测试_线路工程2'提报比例'100%'审批状态为'已通过'审批日期为当日
        且'我审批的'第一个审批状态为'已通过'的是'测试_线路工程2'
        """
        results = IRP(self.driver).hanzheng_approvesuccess2(GD.hanzheng[0],GD.hanzheng[1])
        print(results)
        for i in range(len(results[6])):
            if "已通过" in results[6][i]:
                self.assertIn("测试_线路工程2",results[6][i])
                break
        self.assertEqual(results[0],'测试_线路工程2'),self.assertEqual(results[1],'100%'),\
        self.assertEqual(results[2],'成功'),self.assertIn(results[5],results[3]),self.assertEqual(results[4],'已通过')

    def test_r_faqiren_checkdate(self):
        """
        线路工程：韩正审批通过，发起人登陆检查该项目的项目绩效默认时间无误
        断言：提交月份：当月的第一天，至：当月的最后一天
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        list = []
        list.append(results[1])
        list.append(results[2])
        new_str = "-".join(list)
        print(new_str,results[0])
        self.assertEqual(new_str,results[0])

    def test_s_faqiren_checkjixiao(self):
        """
        线路工程：韩正审批通过，发起人登陆检查该项目的项目绩效正确无误
        断言：总计：150，工程绩效：150
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],'总计：150'),self.assertEqual(results[1],'工程绩效：150')

    def test_t_deleteproject(self):
        """
        线路工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IRP(self.driver).delete_2()
        self.assertEqual(results[0] - 1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_u_switchnet(self):
        """
        线路工程：后台设置线路工程工程不参与绩效计算
        断言：出现'保存成功' 再次选中线路工程，是否参与为'否'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"线路工程 ","否 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'否')

    def test_v_create_route_project(self):
        """
        线路工程：成功创建线路工程(单专业验证)
        断言：项目台账列表数量增加1，且首个项目名称是'测试_线路工程'
        :return:
        """
        self.driver.get(GD.login_url)
        results = IRP(self.driver).create_route_project3(GD.login_sucess[0],GD.login_sucess[1],ID.add_route_datas3["project_name"],ID.add_route_datas3["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_route_datas3["project_name"])

    def test_w_jixiao(self):
        """
        线路工程：提报比例：100% ；
        专业占比：专业占比 项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）标准工日： 108.78（基本工日：83.26考核工日：25.52）
        提报工日： 108.78（基本工日：83.26考核工日：25.52）
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_33()
        new_date_1 = results[2].replace(" ","")
        new_date_2 = results[3].replace(" ","")
        print(results)
        self.assertEqual(results[0],'100%'),self.assertEqual(results[1],ID.add_route_datas3["专业占比"]),\
        self.assertEqual(new_date_1,ID.add_route_datas3["标准工日"]),self.assertEqual(new_date_2,ID.add_route_datas3["提报工日"])

    def test_y_switchnet(self):
        """
        线路工程：后台设置线路工程工程参与绩效计算
        断言：出现'保存成功' 再次选中线路工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"线路工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_z_jixiao(self):
        """
        线路工程：提报比例：100%
                  专业占比：项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）
                  标准工日： 108.78（基本工日：83.26考核工日：25.52）
                  提报工日： 108.78（基本工日：83.26考核工日：25.52）
        :return:
        """
        self.driver.get(GD.login_url)
        results = IRP(self.driver).jixiaoguanli_34(GD.login_sucess[0],GD.login_sucess[1])
        new_date_1 = results[2].replace(" ", "")
        new_date_2 = results[3].replace(" ", "")
        print(results)
        self.assertEqual(results[0],'100%'),self.assertEqual(results[1],ID.add_route_datas3["专业占比"]),\
        self.assertEqual(new_date_1,ID.add_route_datas3["标准工日"]),self.assertEqual(new_date_2,ID.add_route_datas3["提报工日"])

    def test_za_faqiliucheng(self):
        """
        线路工程：线路工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).faqijiaoshen7()
        print(results)
        self.assertEqual(results[0] + 1, results[1]), self.assertEqual(results[2], ID.add_route_datas3['project_name']), \
        self.assertEqual(results[3], "进行中")

    def test_zb_wushen_loginapprove(self):
        """
        线路工程：五审人登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).wushenren_loginapprove_b(GD.hairuomeng[0], GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zc_wushen_approvesuccess(self):
        """
        线路工程：五审人审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'
        """
        results = IRP(self.driver).wushenren_approvesucess_320()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "01-设计输入资料"), self.assertEqual(results[5], ID.add_route_datas3["project_name"])

    def test_zd_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"--"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject(GD.login_sucess[0], GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "--")

    def test_ze_faqiren_faqisure(self):
        """
        线路工程：发起人发起确认成功
        断言：'校审-我发起的'首条记录校审名称是" "01设计输入资料""项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_zf_sureperson_checksuccess(self):
        """
        线路工程：确认人龙美心登陆，发起人发起审批传递过来的流程正确无误
        断言：'校审-待处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).sureren_checksuc(GD.longmeixin[0],GD.longmeixin[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")

    def test_zg_sureperson_approvesuccess(self):
        """
        线路工程：确认人龙美心发起确认成功
        断言：'校审-已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过',"确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")

    def test_zh_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject35(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")

    def test_zi_jixiao(self):
        """
        线路工程：预支比例：100%
        专业占比 项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）
        项目标准工日： 108.78 （基本工日：83.26考核工日：25.52）
        提报工日： 108.78 （基本工日：83.26 考核工日：25.52）
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_36()
        print(results)
        # expected = ('100%', '专业占比 项目经理：10% (56.25工日） 电气：55% (309.38工日） 结构：35% (196.88工日）',
        #             '成品质量系数： 项目经理：1.01、电气：1.01、结构：0.0', '213.04 （基本工日：176.12考核工日：36.92）',
        #             '213.04 （基本工日：176.12 考核工日：36.92）')
        expected = ('100%', '专业占比 项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）', '108.78 （基本工日：83.26考核工日：25.52）', '108.78 （基本工日：83.26 考核工日：25.52）')
        self.assertEqual(results,expected)

    def test_zj_deleteproject(self):
        """
        线路工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IRP(self.driver).delete_8()
        print(results)
        self.assertEqual(results[0] - 1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_zk_create_route_project(self):
        """
        线路工程：成功创建线路工程(双专业验证)
        断言：项目台账列表数量增加1，且首个项目名称是'测试_线路工程'
        :return:
        """
        results = IRP(self.driver).create_route_project4(ID.add_route_datas3["project_name"],ID.add_route_datas3["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_route_datas3["project_name"])

    def test_zl_faqiliucheng(self):
        """
        线路工程：线路工程发起校审流程(节点名称为01设计输入资料)
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).faqijiaoshen7()
        print(results)
        self.assertEqual(results[0] + 1, results[1]), self.assertEqual(results[2], ID.add_route_datas3['project_name']), \
        self.assertEqual(results[3], "进行中")

    def test_zm_wushen_loginapprove(self):
        """
        线路工程：五审人登陆成功，传递过来的待处理项目正确无误(节点名称为01设计输入资料)
        断言：'待处理'首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).wushenren_loginapprove_nn(GD.hairuomeng[0], GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zn_wushen_approvesuccess(self):
        """
        线路工程：五审人审批成功，成功传递给发起人(节点名称为01设计输入资料)
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'
        """
        results = IRP(self.driver).wushenren_approvesucess_ab()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "01-设计输入资料"), self.assertEqual(results[5], ID.add_route_datas3["project_name"])

    def test_zo_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误(节点名称为01设计输入资料)
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"--"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject(GD.login_sucess[0], GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "--")

    def test_zp_faqiren_faqisure(self):
        """
        线路工程：发起人发起确认成功(节点名称为01设计输入资料)
        断言：'校审-我发起的'首条记录校审名称是" "01设计输入资料""项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).faqiren_faqisure_suc()
        print(results)
        self.assertEqual(results[0], "01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"进行中")

    def test_zq_sureperson_checksuccess(self):
        """
        线路工程：确认人龙美心登陆，发起人发起审批传递过来的流程正确无误(节点名称为01设计输入资料)
        断言：'校审-待处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).sureren_checksuc(GD.longmeixin[0],GD.longmeixin[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"无"),self.assertEqual(results[4],"无"),self.assertEqual(results[5],"进行中")


    def test_zr_sureperson_approvesuccess(self):
        """
        线路工程：确认人龙美心发起确认成功(节点名称为01设计输入资料)
        断言：'校审-已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).sureperson_faqiqueren_suc()
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")

    def test_zs_faqiren_checksuccess(self):
        """
        线路工程工程：发起人登陆，五审审批传递过来的流程正确无误(节点名称为01设计输入资料)
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject35(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas3["project_name"]),\
        self.assertEqual(results[2],"已通过"),self.assertEqual(results[3],"已通过")

    def test_zt_faqiliucheng(self):
        """
        线路工程：线路工程发起校审流程(节点名称为04-前期阶段批复意见)
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).faqijiaoshen8()
        print(results)
        self.assertEqual(results[0] + 1, results[1]), self.assertEqual(results[2], ID.add_route_datas3['project_name']), \
        self.assertEqual(results[3], "进行中")

    def test_zu_wushen_loginapprove(self):
        """
        线路工程：五审人登陆成功，传递过来的待处理项目正确无误(节点名称为04-前期阶段批复意见)
        断言：'待处理'首条记录项目名称是'测试_线路工程3',五审状态是'进行中'
        """
        results = IRP(self.driver).wushenren_loginapproveee(GD.hairuomeng[0], GD.hairuomeng[1])
        print(results)
        self.assertEqual(results[0], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[1], "进行中")

    def test_zv_wushen_approvesuccess(self):
        """
        线路工程：五审人审批成功，成功传递给发起人(节点名称为04-前期阶段批复意见)
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"04-前期阶段批复意见"项目名称是'测试_线路工程3'
        """
        results = IRP(self.driver).wushenren_approvesucess001()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(results[4], "04-前期阶段批复意见"), self.assertEqual(results[5], ID.add_route_datas3["project_name"])

    def test_zw_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误(节点名称为04-前期阶段批复意见)
        断言：'校审-我发起的'首条记录校审名称是"04-前期阶段批复意见"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"--"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject(GD.login_sucess[0], GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0], "04-前期阶段批复意见"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "--")

    def test_zx_faqiren_faqisure(self):
        """
        线路工程：发起人发起确认成功(节点名称为04-前期阶段批复意见)
        断言：'校审-我发起的'首条记录校审名称是" "04-前期阶段批复意见""项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).faqiren_faqisure_suc2()
        print(results)
        self.assertEqual(results[0], "04-前期阶段批复意见"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "进行中")

    def test_zy_sureperson_checksuccess(self):
        """
        线路工程：确认人龙美心登陆，发起人发起审批传递过来的流程正确无误(节点名称为04-前期阶段批复意见)
        断言：'校审-待处理'首条记录校审名称是"04-前期阶段批复意见"项目名称是'测试_线路工程3'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"进行中"
        :return:
        """
        results = IRP(self.driver).sureren_checksuc(GD.longmeixin[0], GD.longmeixin[1])
        print(results)
        self.assertEqual(results[0], "04-前期阶段批复意见"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "无"), self.assertEqual(results[4],"无"), \
        self.assertEqual(results[5], "进行中")

    def test_zz_sureperson_approvesuccess(self):
        """
        线路工程：确认人龙美心发起确认成功(节点名称为04-前期阶段批复意见)
        断言：'校审-已处理'首条记录校审名称是"04-前期阶段批复意见"项目名称是'测试_线路工程3'，五审状态是'已通过',六审七审状态是'无'"确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).sureperson_faqiqueren_suc2()
        print(results)
        self.assertEqual(results[0], "04-前期阶段批复意见"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "已通过")

    def test_zza_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，五审审批传递过来的流程正确无误(节点名称为04-前期阶段批复意见)
        断言：'校审-我发起的'首条记录校审名称是"04-前期阶段批复意见"项目名称是'测试_线路工程3'，五审状态是'已通过'确认人状态是"已通过"
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject35(GD.login_sucess[0], GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0], "04-前期阶段批复意见"), self.assertEqual(results[1], ID.add_route_datas3["project_name"]), \
        self.assertEqual(results[2], "已通过"), self.assertEqual(results[3], "已通过")

    def test_zzb_jixiao(self):
        """
        线路工程：双节点
        断言：提报比例100%，专业占比：项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）
        成品质量系数： 项目经理：1.01、电气：1.01、结构：1.01', 项目标准工日：108.78 （基本工日：83.26考核工日：25.52）
        提报工日：109.84 （基本工日：84.08 考核工日：25.76）
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_11()
        print(results)
        # expect = ('100%', '专业占比 项目经理：10% (56.25工日） 电气：55% (309.38工日） 结构：35% (196.88工日）',
        #           '成品质量系数： 项目经理：1.01、电气：1.01、结构：1.01', '411.9 （基本工日：315.32考核工日：96.58）',
        #           '411.9 （基本工日：315.32 考核工日：96.58）')
        expect = ('100%', '专业占比 项目经理：10% (15工日） 电气：55% (82.5工日） 结构：35% (52.5工日）', '108.78 （基本工日：83.26考核工日：25.52）', '109.84 （基本工日：84.08 考核工日：25.76）')
        self.assertEqual(results,expect)

    def test_zzc_deleteproject(self):
        """
        线路工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IRP(self.driver).delete_8()
        print(results)
        self.assertEqual(results[0] - 1, results[1]), self.assertEqual(results[2], "删除成功！")

    def test_zzd_create_route_project(self):
        """
        线路工程：成功创建线路工程
        断言：项目台账列表数量增加1，且首个项目名称是'测试_线路工程'
        :return:
        """
        results = IRP(self.driver).create_route_project33(ID.add_route_datas["project_name"],ID.add_route_datas["project_no"])
        print(results)
        if type(results[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        else:
            num_1 = results[0]
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        print(num_1,num_2)
        self.assertEqual(num_1+1,num_2),self.assertEqual(results[2],ID.add_route_datas["project_name"])

    def test_zze_switchnet(self):
        """
        线路工程：后台设置线路工程工程不参与绩效计算
        断言：出现'保存成功' 再次选中线路工程，是否参与为'是'
        :return:
        """
        self.driver.get(GD.houtai_url)
        results = Switch(self.driver).switch_net(GD.zhanghao[0],GD.zhanghao[1],"线路工程 ","是 ")
        print(results)
        self.assertEqual(results[0],'保存成功！'),self.assertEqual(results[1],'是')

    def test_zzf_faqiliucheng(self):
        """
        线路工程：线路工程发起校审流程
        断言：'我发起的'列表数量增加1，且首条记录项目名称是'测试_线路工程',确认人状态是'进行中'
        """
        self.driver.get(GD.login_url)
        results = IRP(self.driver).faqijiaoshen77(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_route_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zzg_surep_loginapprove(self):
        """
        线路工程：确认人海清登陆成功，传递过来的待处理项目正确无误
        断言：'待处理'首条记录项目名称是'测试_线路工程',确认人状态是'进行中'
        """
        results = IRP(self.driver).wushenren_loginapprove(GD.haiqing[0],GD.haiqing[1])
        print(results)
        self.assertEqual(results[0],ID.add_route_datas["project_name"]),\
        self.assertEqual(results[1],"进行中")

    def test_zzh_surep_approvesuccess(self):
        """
        线路工程：确认人海清审批成功，成功传递给发起人
        断言：'待处理'数量减1，'已处理'数量加1，'已处理'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程'
        """
        results = IRP(self.driver).wushenren_approvesucess()
        print(results)
        num_1 = int(re.findall(r"\d+\.?\d*", results[0])[0])
        num_2 = int(re.findall(r"\d+\.?\d*", results[1])[0])
        num_3 = int(re.findall(r"\d+\.?\d*", results[2])[0])
        num_4 = int(re.findall(r"\d+\.?\d*", results[3])[0])
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(results[4],"01-设计输入资料"),self.assertEqual(results[5],ID.add_route_datas["project_name"])

    def test_zzi_faqiren_checksuccess(self):
        """
        线路工程：发起人登陆，确认人海清审批传递过来的流程正确无误
        断言：'校审-我发起的'首条记录校审名称是"01-设计输入资料"项目名称是'测试_线路工程'，确认人状态是'已通过'
        :return:
        """
        results = IRP(self.driver).faqiren_check_returedproject55(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0],"01-设计输入资料"),self.assertEqual(results[1],ID.add_route_datas["project_name"]),\
        self.assertEqual(results[2],"已通过")


    def test_zzj_jixiao(self):
        """
        线路工程：发起绩效时系数调整输入框不能大于4.05
        断言：输入10提示'调整系数不可大于4.05！'
        :return:
        """
        results = IRP(self.driver).jixiaoguanli_19(ID.add_route_datas["rate"])
        print(results)
        self.assertEqual(results,"调整系数不可大于4.05！")

    def test_zzk_hanzheng_approve(self):
        """
        线路工程：韩正修改系数调整和考核工日
        断言：系数调整输入10时提示"调整系数不可大于4.05！"，考核工日输入100时提示"同角色内人员的有效考核工日总和不可大于该角色标准考核工日2.25倍！"

        :return:
        """
        results = IRP(self.driver).hanzheng_logincheck00(GD.hanzheng[0],GD.hanzheng[1])
        print(results)
        self.assertEqual(results[0],"调整系数不可大于4.05！"),self.assertEqual(results[1],"同角色内人员的有效考核工日总和不可大于该角色标准考核工日2.25倍！")

    def test_zzl_deleteproject(self):
        """
        线路工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IRP(self.driver).delete_110(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0] - 1, results[1]), self.assertEqual(results[2], "删除成功！")


