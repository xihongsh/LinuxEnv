import unittest,os,re
from selenium import webdriver
from PageLocators.login_page_locator import LoginPageLocator as LP
from PageObjects.distributionnet_project import IndexNetPage as IP
from TestDatas.global_datas import GlobalDatas as GD
from TestDatas.index_datas import IndexDatas as ID
root = os.path.dirname(os.path.abspath(__file__))
class TestNetIndex(unittest.TestCase):
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

    def test_a_netproject_field(self):
        '''
        配网工程：验证'项目类型'选择'配网工程'时，会出现'生产部门'字段，'计划时间'只有开始时间
        '''
        department_info,time_num = IP(self.driver).check_network_field()
        print(department_info,time_num)
        self.assertEqual(department_info,ID.add_netproject_datas['配网工程验证字段']),self.assertEqual(time_num,ID.add_netproject_datas['计划时间数量'])

    def test_b_create_netproject(self):
        '''
        配网工程：成功创建'配网工程'项目
        断言成功依据：项目台账列表数量增加1，且第一个台账项目为'测试_配网工程'
        '''
        return_value = IP(self.driver).create_network_project(ID.add_netproject_datas['project_name'],ID.add_netproject_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_netproject_datas['project_name'])

    def test_c_upload_file(self):
        '''
        配网工程：设计卷册上传文件
        断言：上传成功后的文件名称与已知文件名称一致证明，上传两次版本号显示2，
        点击版本号弹出弹框，弹框首条记录名称作者版本号正确无误版本号是2，第二条记录名称作者版本号正确无误版本号是1
        '''
        results = IP(self.driver).to_upload_file()
        print(results)
        self.assertEqual(results[0],"测试上传脚本用.txt"),self.assertEqual(results[1],"2"),\
        self.assertEqual(results[2],"测试上传脚本用.txt"),self.assertEqual(results[3],"张无忌"),\
        self.assertEqual(results[4],"2"),self.assertEqual(results[5],"测试上传脚本用.txt"),\
        self.assertEqual(results[6],"张无忌"),self.assertEqual(results[7],"1")

    def test_d_addrole_to_net(self):
        """
        配网工程：配网工程增加角色
        断言成功依据：配电角色列表数量由0变成1，且配电角色手机号为新增手机号18612356691
        新需求：
        "新版3.5有改动"
        """
        results = IP(self.driver).addroles(GD.login_sucess[0])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],GD.login_sucess[0])

    def test_e_wushenren(self):
        """
        配网工程：创建配网项目五审人选择的是米照辉,设计校审文件正确无误
        断言成功依据：新建项目发起设计校审流程五审人只自动显示出米照辉，
        并且设计校审文件名称是'测试上传脚本用.txt',版本号是V2
        """
        results = IP(self.driver).jiaoshenren()
        print(results)
        pattern = re.compile('(.[\u4E00-\u9FA5_a-zA-Z]+)')
        cas_part_names = pattern.findall(results[0])
        print(cas_part_names)
        file_info = results[1].split("\n")
        print(file_info)
        self.assertEqual(cas_part_names,['米照辉', '选择']),self.assertEqual(file_info,['V2', '测试上传脚本用.txt'])

    def test_f_faqiliucheng1(self):
        """
        配网工程：发起流程
        断言依据：校审-我发起的：列表数量增加1并且第一条记录所属项目名称为新建项目名称'测试_配网工程'，五审人状态为进行中
        """
        results = IP(self.driver).faqiliucheng()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_netproject_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    # def test_g_faqiliucheng2(self):
    #     """
    #     配网工程：第二次发起流程查看校审文件是否显示
    #     断言依据：因为第一次发起流程自动带出来并且发起成功，第二次发起流程校审文件就不会自动带出了，
    #     且勾选已上传文件时会有提示语''重新上传文件发起流程会有提示语''
    #     """
    #     results = IP(self.driver).faqiliucheng2()
    #     print(results)

    def test_h_guidang(self):
        """
        配网工程：创建配网工程发起校审流程后不可归档
        断言：点击项目名称归档时提示'此项目内存在处于“设计校审”流程中的文件，不可发起归档'
        :return:
        """
        results = IP(self.driver).guidang()
        print(results)
        self.assertEqual(results,'此项目内存在处于“设计校审”流程中的文件，不可发起归档')

    def test_i_wushenren_loginsucess(self):
        """
        配网工程：五审人登陆成功，待处理项目正确无误（校审-待处理：第一个项目名称为新建项目'测试_配网工程'且五审人审批状态为‘进行中’）
        """
        needtodeal_results = IP(self.driver).wushenren_loginapprove(GD.wushenren[0],GD.wushenren[1])
        print(needtodeal_results)
        self.assertEqual(needtodeal_results[0],ID.add_netproject_datas['project_name']),\
        self.assertEqual(needtodeal_results[1],"进行中")

    def test_j_wushenren_approvesucess(self):
        """
        配网工程：五审人审批成功，顺利传给六审
        断言成功：待处理减少1，已处理增加1，校审-已处理：校审名称为二次；所属项目为'测试_配网工程'；五审状态为'已通过'；六审状态为'进行中'
        """
        approveresult = IP(self.driver).wushenren_approvesucess()
        if type(approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", approveresult[0])[0])
        else:
            num_1 = 0
        if type(approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", approveresult[1])[0])
        else:
            num_2 = 0
        if type(approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", approveresult[2])[0])
        else:
            num_3 = 0
        if type(approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(approveresult[4],"二次"),self.assertEqual(approveresult[5],ID.add_netproject_datas['project_name']),\
        self.assertEqual(approveresult[6],"已通过"),self.assertEqual(approveresult[7],"进行中")

    def test_k_liushenren_loginsuccess(self):
        """
        配网工程：六审人登陆成功，待处理项目正确无误
        断言成功：校审名称为二次；所属项目为'测试_配网工程'；五审状态为'已通过'；六审状态为'进行中'
        """
        liushen_needtodeal_results = IP(self.driver).liushenren_loginapprove(GD.liushenren[0],GD.liushenren[1])
        self.assertEqual(liushen_needtodeal_results[0],"二次"),self.assertEqual(liushen_needtodeal_results[1],ID.add_netproject_datas['project_name']),\
        self.assertEqual(liushen_needtodeal_results[2],"已通过"),self.assertEqual(liushen_needtodeal_results[3],"进行中")

    def test_l_liushenren_approvesuccess(self):
        """
        配网工程：六审人审批成功，顺利传给七审
        断言：待处理数量减少1已处理数量增加1
        且校审-已处理：第一条记录校审名称为二次；所属项目为'测试_配网工程'；六审状态为'已通过'；七审状态为'进行中'
        """
        liushen_approveresult = IP(self.driver).liushenren_approvesucess()
        if type(liushen_approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", liushen_approveresult[0])[0])
        else:
            num_1 = 0
        if type(liushen_approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", liushen_approveresult[1])[0])
        else:
            num_2 = 0
        if type(liushen_approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", liushen_approveresult[2])[0])
        else:
            num_3 = 0
        if type(liushen_approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", liushen_approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1-1,num_3),self.assertEqual(num_2+1,num_4),\
        self.assertEqual(liushen_approveresult[4],"二次"),self.assertEqual(liushen_approveresult[5],ID.add_netproject_datas['project_name']),\
        self.assertEqual(liushen_approveresult[6],"已通过"),self.assertEqual(liushen_approveresult[7],"进行中")

    def test_m_qishenren_loginsuccess(self):
        """
        配网工程：七审人登陆成功，待处理项目正确无误
        断言：校审-待处理：第一条记录校审名称为二次；所属项目为'测试_配网工程'；五审六审状态为'已通过'；七审状态为'进行中'
        """
        qishen_needtodeal_results = IP(self.driver).qishenren_loginapprove(GD.qishenren[0],GD.qishenren[1])
        self.assertEqual(qishen_needtodeal_results[0],"二次"),self.assertEqual(qishen_needtodeal_results[1],ID.add_netproject_datas['project_name']),\
        self.assertEqual(qishen_needtodeal_results[2],"已通过"),self.assertEqual(qishen_needtodeal_results[3],"已通过"),\
        self.assertEqual(qishen_needtodeal_results[4],"进行中")

    def test_n_qishenren_approvesuccess(self):
        """
        配网工程：七审人审批成功
        断言：七审人账号登陆，待处理数量减少1已处理数量增加1
        校审-已处理：第一条记录校审名称为二次；所属项目为'测试_配网工程'；七审状态为'已通过'
        """
        qishen_approveresult = IP(self.driver).qishenren_approvesucess()
        if type(qishen_approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", qishen_approveresult[0])[0])
        else:
            num_1 = 0
        if type(qishen_approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", qishen_approveresult[1])[0])
        else:
            num_2 = 0
        if type(qishen_approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", qishen_approveresult[2])[0])
        else:
            num_3 = 0
        if type(qishen_approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", qishen_approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(qishen_approveresult[4],"二次"),self.assertEqual(qishen_approveresult[5],ID.add_netproject_datas['project_name']),\
        self.assertEqual(qishen_approveresult[6],"已通过")

    def test_o_deleteproject(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_1(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_p_create_netproject(self):
        '''
        配网工程：创建'配网工程'项目 五审六审为同一人
        断言：项目台账列表数量增加1，且第一条记录项目名称是'测试_配网工程2'
        '''
        return_value = IP(self.driver).create_network2_project(ID.add_netproject2_datas['project_name'],ID.add_netproject2_datas['project_no'])
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_netproject2_datas['project_name'])

    def test_q_addrole_to_net(self):
        """
        配网工程：增加角色
        断言成功依据：配电角色列表列表数量由0变成1，且配电角色手机号为新增手机号18612356691
        """
        results = IP(self.driver).addrole2(GD.login_sucess[0])
        self.assertEqual(results[0] + 1, results[1]),self.assertEqual(results[2],GD.login_sucess[0])

    def test_r_faqiliucheng(self):
        """
        配网工程：发起流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称为'测试_配网工程2'和五审状态为'进行中'
        """
        results = IP(self.driver).faqiliucheng_secondproject()
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_netproject2_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_s_wushenren_loginsucess(self):
        """
        配网工程：五审人登陆成功，待处理项目正确无误（校审-待处理：第一条记录项目名称为'测试_配网工程2'和五审状态为'进行中'）
        """
        needtodeal_results = IP(self.driver).wushenren_loginapprove(GD.wushenren[0],GD.wushenren[1])
        self.assertEqual(needtodeal_results[0],ID.add_netproject2_datas['project_name']),\
        self.assertEqual(needtodeal_results[1],"进行中")

    def test_t_wushenren_approvesucess(self):
        """
        配网工程：五审人审批成功，返回给发起人
        断言：待处理数量减少1已处理数量增加1
        校审-已处理：第一条记录校审名称为'二次'项目名称为'测试_配网工程2'和五审状态为'已通过'六审状态为"--"
        """
        approveresult = IP(self.driver).wushenren_approvesucess()
        if type(approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", approveresult[0])[0])
        else:
            num_1 = 0
        if type(approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", approveresult[1])[0])
        else:
            num_2 = 0
        if type(approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", approveresult[2])[0])
        else:
            num_3 = 0
        if type(approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4),\
        self.assertEqual(approveresult[4],"二次"),self.assertEqual(approveresult[5],ID.add_netproject2_datas['project_name']),\
        self.assertEqual(approveresult[6],"已通过"),self.assertEqual(approveresult[7],"--")

    def test_u_faqiren_checkproject(self):
        """
        配网工程：五审六审为同一人，五审审核通过，返回给发起人的项目正确无误
        断言：发起人登陆系统，校审-我发起的：第一条记录校审名称为'二次'项目名称为'测试_配网工程2'和五审状态为'已通过'六审状态为"--"
        """
        faqiresult = IP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(faqiresult[0],"二次"),self.assertEqual(faqiresult[1],ID.add_netproject2_datas['project_name']),\
        self.assertEqual(faqiresult[2],"已通过"),self.assertEqual(faqiresult[3],"--")

    def test_v_delete2project(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_2()
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_w_create_netproject(self):
        '''
        配网工程：创建'配网工程'项目 六审没有人
        断言：项目台账列表数量增加1，且第一条记录项目名称为'测试_配网工程3'
        '''
        return_value = IP(self.driver).create_network3_project(ID.add_netproject3_datas['project_name'],ID.add_netproject3_datas['project_no'])
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_netproject3_datas['project_name'])

    def test_x_addrole_to_net(self):
        """
        配网工程：增加角色
        断言：配电角色列表数量增加1，且该角色手机号为新增角色手机号18612356691
        """
        results = IP(self.driver).addrole3(GD.login_sucess[0])
        self.assertEqual(results[0] + 1, results[1]), self.assertEqual(results[2], GD.login_sucess[0])

    def test_y_faqiliucheng(self):
        """
        配网工程：发起流程
        断言：校审-我发起的：列表数量增加1，且第一条记录项目名称是'测试_配网工程3',且五审状态是'进行中'
        """
        results = IP(self.driver).faqiliucheng_third()
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_netproject3_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_z_wushenren_approvesucess(self):
        """
        配网工程：五审人审批成功，返回给发起人
        断言：待处理数量减少1已处理数量增加1
        校审-已处理：第一条记录校审名称为'二次'，项目名称是'测试_配网工程3',且五审状态是'已通过'六审状态是'--'
        """
        approveresult = IP(self.driver).wushenren_approvesucess2(GD.wushenren[0],GD.wushenren[1])
        if type(approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", approveresult[0])[0])
        else:
            num_1 = 0
        if type(approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", approveresult[1])[0])
        else:
            num_2 = 0
        if type(approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", approveresult[2])[0])
        else:
            num_3 = 0
        if type(approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4),\
        self.assertEqual(approveresult[4],"二次"),self.assertEqual(approveresult[5],ID.add_netproject3_datas['project_name']),\
        self.assertEqual(approveresult[6],"已通过"),self.assertEqual(approveresult[7],"--")

    def test_za_faqiren_checkproject(self):
        """
        配网工程：五审六审为同一人，五审审核通过，返回给发起人的项目正确无误
        断言发起人登陆系统，校审-我发起的：第一条记录校审名称为'二次'，项目名称是'测试_配网工程3',且五审状态是'已通过'六审状态是'--'
        """
        faqiresult = IP(self.driver).faqiren_check_returedproject(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(faqiresult[0],"二次"),self.assertEqual(faqiresult[1],ID.add_netproject3_datas['project_name']),\
        self.assertEqual(faqiresult[2],"已通过"),self.assertEqual(faqiresult[3],"--")

    def test_zb_delete3project(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_3()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_zc_guidangf(self):
        """
        配网工程：创建项目没有上传文没有选择监管人发起归档
        断言：点击项目名称归档时提示"此项目内无可归档文件，不可发起归档",审批人员没有
        :return:
        """
        results = IP(self.driver).create_network4_project(ID.add_netproject4_datas['project_name'],ID.add_netproject4_datas['project_no'])
        print(results)
        self.assertEqual(results[0],'此项目内无可归档文件，不可发起归档'),self.assertEqual(results[1],'*审批人员：\n选择')

    def test_zd_guidangs(self):
        """
        配网工程：在项目云盘中上传文件后归档成功
        断言：归档成功依据上传文件成功显示文件名，和版本号'1'，归档记录第一条为新归档项目名称‘测试_配网工程4’，
        归档版本为'第一版'，审批人为'--'，归档状态为'已通过'
        :return:
        """
        results = IP(self.driver).guidang2()
        print(results)
        self.assertEqual(results[0],"测试上传脚本用.txt"),self.assertEqual(results[1],"1"),\
        self.assertEqual(results[2],ID.add_netproject4_datas['project_name']),self.assertEqual(results[3],"第一版"),\
        self.assertEqual(results[4],"--"),self.assertEqual(results[5],"已通过")

    def test_ze_delete4project(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_4()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_zf_create_netproject(self):
        '''
        配网工程：成功创建'配网工程'项目,设计校审级别为1级
        断言成功依据：项目台账列表数量增加1，且第一个台账项目为'测试_配网工程5'
        '''
        return_value = IP(self.driver).create_network5_project(ID.add_netproject5_datas['project_name'],ID.add_netproject5_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_netproject5_datas['project_name'])

    def test_zg_addrole2_to_net(self):
        """
        配网工程：配网工程增加角色
        断言成功依据：配电角色列表数量由0变成1，且配电角色手机号为新增手机号18612356691
        新需求：
        "新版3.5有改动"
        """
        results = IP(self.driver).addrole2(GD.login_sucess[0])
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],GD.login_sucess[0])

    def test_zh_faqiliucheng1(self):
        """
        配网工程：发起流程
        断言依据：校审-我发起的：列表数量增加1并且第一条记录所属项目名称为新建项目名称'测试_配网工程'，五审人状态为进行中
        """
        results = IP(self.driver).faqiliucheng3()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(results[3],"一级"),self.assertEqual(results[4],"进行中")

    def test_zi_wushenren_loginsucess(self):
        """
        配网工程：五审人登陆成功，待处理项目正确无误（校审-待处理：第一个项目名称为新建项目'测试_配网工程5'且审批级别为1级，五审人审批状态为‘进行中’）
        """
        needtodeal_results = IP(self.driver).wushenren_loginapprove2(GD.wushenren[0],GD.wushenren[1])
        print(needtodeal_results)
        self.assertEqual(needtodeal_results[0],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(needtodeal_results[1],"一级"),self.assertEqual(needtodeal_results[2],'进行中')

    def test_zj_wushenren2_approvesucess(self):
        """
        配网工程：五审人审批成功，流程发给发起人
        断言成功：待处理减少1，已处理增加1，校审-已处理：校审名称为二次；所属项目为'测试_配网工程5'；五审状态为'已通过'；六审状态为'无'，审批级别为'一级'
        """
        approveresult = IP(self.driver).wushenren_approvesucess3()
        if type(approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", approveresult[0])[0])
        else:
            num_1 = 0
        if type(approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", approveresult[1])[0])
        else:
            num_2 = 0
        if type(approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", approveresult[2])[0])
        else:
            num_3 = 0
        if type(approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1, num_2, num_3, num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4), \
        self.assertEqual(approveresult[4], "二次"), self.assertEqual(approveresult[5],ID.add_netproject5_datas['project_name']), \
        self.assertEqual(approveresult[6], "已通过"), self.assertEqual(approveresult[7], "无"),self.assertEqual(approveresult[8], "一级")

    def test_zk_faqiren_checkproject(self):
        """
        配网工程：配网工程设计校审级别为1级，五审审核通过，返回给发起人的项目正确无误
        断言：发起人登陆系统，校审-我发起的：第一条记录校审名称为'二次'项目名称为'测试_配网工程5'和五审状态为'已通过'确认状态为"--"
        """
        faqiresult = IP(self.driver).faqiren_check_returedproject2(GD.login_sucess[0],GD.login_sucess[1])
        self.assertEqual(faqiresult[0],"二次"),self.assertEqual(faqiresult[1],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(faqiresult[2],"已通过"),self.assertEqual(faqiresult[3],"--"),self.assertEqual(faqiresult[4],'一级')

    def test_zl_faqiren_faqiqueren(self):
        """
        配网工程：发起人发起确认成功
        断言：点发起确认按钮后，确认人自动获取'王路'，发起成功后，第一条项目名称是'测试_配网工程5'确认状态是'进行中'
        """
        results = IP(self.driver).faqiren_sure()
        print(results)
        self.assertEqual(results[0],'*确认人：\n王路'),self.assertEqual(results[1],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(results[2],'进行中')

    def test_zm_wanglu_approvesucess(self):
        """
        配网工程：王路审批成功，返回给发起人
        断言：待处理数量减少1已处理数量增加1
        校审-已处理：第一条记录校审名称为'二次'，项目名称是'测试_配网工程5',确认级别是1级，确认状态是'以通过'
        """
        approveresult = IP(self.driver).wanglu_approvesucess(GD.wanglu[0],GD.wanglu[1])
        print(approveresult)
        if type(approveresult[0]) == str:
            num_1 = int(re.findall(r"\d+\.?\d*", approveresult[0])[0])
        else:
            num_1 = 0
        if type(approveresult[1]) == str:
            num_2 = int(re.findall(r"\d+\.?\d*", approveresult[1])[0])
        else:
            num_2 = 0
        if type(approveresult[2]) == str:
            num_3 = int(re.findall(r"\d+\.?\d*", approveresult[2])[0])
        else:
            num_3 = 0
        if type(approveresult[3]) == str:
            num_4 = int(re.findall(r"\d+\.?\d*", approveresult[3])[0])
        else:
            num_4 = 0
        print(num_1,num_2,num_3,num_4)
        self.assertEqual(num_1 - 1, num_3), self.assertEqual(num_2 + 1, num_4),\
        self.assertEqual(approveresult[4],"二次"),self.assertEqual(approveresult[5],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(approveresult[6],"一级"),self.assertEqual(approveresult[7],"已通过")

    def test_zn_faqiren_checkproject(self):
        """
        配网工程：创建配网工程设计校审级别为1级，确认人王路确认通过后，；流程传递给发起人，发起人检查无误
        断言：发起人登陆系统，校审-我发起的：第一条记录校审名称为'二次'项目名称为'测试_配网工程5'和确认状态为'已通过'
        """
        faqiresult = IP(self.driver).faqiren_check_returedproject3(GD.login_sucess[0],GD.login_sucess[1])
        print(faqiresult)
        self.assertEqual(faqiresult[0],"二次"),self.assertEqual(faqiresult[1],ID.add_netproject5_datas['project_name']),\
        self.assertEqual(faqiresult[2],"已通过")

    def test_zo_deleteproject(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_5()
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")

    def test_zp_create_netproject(self):
        '''
        配网工程：成功创建'配网工程'项目
        断言成功依据：项目台账列表数量增加1，且第一个台账项目为'测试_配网工程7'
        '''
        return_value = IP(self.driver).create_network_project_r(ID.add_netproject7_datas['project_name'],ID.add_netproject7_datas['project_no'])
        print(return_value)
        self.assertEqual(return_value[0]+1,return_value[1]),self.assertEqual(return_value[2],ID.add_netproject7_datas['project_name'])

    def test_zq_addrole_to_net(self):
        """
        配网工程：配网工程增加角色
        断言成功依据：HD校核角色列表数量由0变成4，且HD校核角色角色手机号为新增手机号17088552222，17088552255，18612356692
        新需求：
        "新版3.5有改动"
        """
        results = IP(self.driver).addrole_m(GD.HD[0],GD.HD[1],GD.HD[2],GD.HD[3])
        print(results)
        self.assertEqual(results[0]+3,results[1]),self.assertEqual(results[2][0],GD.HD[0]), \
        self.assertEqual(results[2][1], GD.HD[1]),self.assertEqual(results[2][2],GD.HD[2])

    def test_zr_upload_file(self):
        '''
        配网工程：设计卷册上传文件
        断言：上传成功后
        点击版本号弹出弹框，弹框首条记录名称作者版本号正确无误版本号是1
        '''
        results = IP(self.driver).to_upload_file2()
        print(results)
        self.assertEqual(results[0],"测试上传脚本用4.txt"),self.assertEqual(results[1],"1")

    def test_zs_faqiliucheng1(self):
        """
        配网工程：发起流程
        断言依据：校审-我发起的：列表数量增加1并且第一条记录所属项目名称为新建项目名称'测试_配网工程7'，五审人状态为进行中
        """
        results = IP(self.driver).faqiliucheng_three()
        print(results)
        self.assertEqual(results[0]+1,results[1]),self.assertEqual(results[2],ID.add_netproject7_datas['project_name']),\
        self.assertEqual(results[3],"进行中")

    def test_zt_jiaoheren_check(self):
        """
        配网工程：校核人登陆流程传递过来正确无误
        断言：首条项目名称是'测试_配网工程7'，校核状态是'进行中'
        :return:
        """
        results = IP(self.driver).jiaohe_loginapprove(GD.jiaohe[0],GD.jiaohe[1])
        print(results)
        self.assertEqual(results[0],ID.add_netproject7_datas["project_name"]),self.assertEqual(results[1],'进行中')

    def test_zu_jiaohe_approvesucess(self):
        """
        配网工程：校核人张三丰登陆，指定校核人准确无误
        断言成功：指定校核人显示'张三丰','张三','萧敬腾'
        """
        approveresult = IP(self.driver).jiaohe_approvesucess_s()
        print(approveresult)
        self.assertEqual(approveresult[2],'指定校核人： 张三,张三丰,萧敬腾')

    def test_zv_deleteproject(self):
        """
        配网工程：删除项目成功
        断言：出现'删除成功'且项目台账列表数量减少1
        :return:
        """
        results = IP(self.driver).delete_s(GD.login_sucess[0],GD.login_sucess[1])
        print(results)
        self.assertEqual(results[0]-1,results[1]),self.assertEqual(results[2],"删除成功！")


































