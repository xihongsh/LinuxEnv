from PageLocators.waterconsult_locator import IndexWaterPageLocator as IWL
from PageLocators.login_page_locator import LoginPageLocator as LP
from selenium.webdriver.common.keys import Keys
from Common.basepage import BasePage
from time import sleep
class IndexWaterConsultPage(BasePage):
    # '水利咨询'特殊字段
    def check_waterconsult_field(self):
        self.click(IWL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IWL.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IWL.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IWL.projecttype_checkbox,doc='选择项目类型')
        self.click(IWL.waterconsult_loc,doc="项目类型选择'水利咨询'")
        # 返回'工程类型'字段 和 '工程规模和工程投资'文本框
        return self.get_element_text(IWL.projecttypechoice_loc,doc="获取工程类型选项"),\
               self.get_element_text(IWL.project_area,doc="获取工程规模文本框"),\
               self.get_element_text(IWL.project_touzi,doc="获取工程投资文本框")

    def create_waterconsult_project(self,projectname,projectno):
        self.click(IWL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IWL.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IWL.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 =  self.get_element_text(IWL.all_datas, doc="获取共XX行")
        self.click(IWL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IWL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IWL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IWL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IWL.waterconsult_loc,doc="选择'水利咨询工程'")
        self.click(IWL.choose_member,doc="点击'选择成员'")
        self.click(IWL.shigong_fuze,doc="点击'施工组织设计专业负责人'")
        self.click(IWL.add_member, doc="点击'添加成员'")
        self.input_text(IWL.name_input,"张无忌",doc="输入'张无忌'")
        self.input_text(IWL.name_input,Keys.ENTER)
        self.click(IWL.zhangwuji_gouxuan,doc="勾选张无忌")
        self.click(IWL.sure_button,doc="点击'确定'按钮")
        self.click(IWL.add_member, doc="点击'添加成员'")
        self.click(IWL.haiqing_chooose,doc="勾选海清")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.shigong_sheji,doc="点击'施工组织设计专业设计人'")
        self.click(IWL.add_member,doc="点击'添加成员'")
        self.click(IWL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.zhengdi_sheji, doc="点击'征地移民专业设计人'")
        self.click(IWL.add_member, doc="点击'添加成员'")
        self.click(IWL.huangbo, doc="勾选黄渤")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.zhengdi_fuze, doc="点击'征地移民专业负责人'")
        self.click(IWL.add_member, doc="点击'添加成员'")
        self.click(IWL.xuhonglei, doc="勾选徐鸿磊")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.add_member, doc="点击'添加成员'")
        self.click(IWL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.sure_button, doc="点击'确定'按钮")
        self.click(IWL.setnode_button,doc="点击'设置节点'")
        self.click(IWL.design_inputfile,doc="勾选'01设计输入资料'")
        self.click(IWL.design_choosebutton,doc="点击'01设计输入资料--选择'")
        self.click(IWL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IWL.water_sure_button,doc="点击'确定'")
        self.click(IWL.water_sure_button,doc="点击'确定'")
        self.click(IWL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IWL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IWL.start_time,doc="点击'开始时间'")
        self.click(IWL.start_time_sure,doc="点击'确定'")
        self.click(IWL.end_time,doc="点击'结束时间'")
        self.click(IWL.end_time_sure,doc="点击'确定'")
        self.click(IWL.create_button,doc="点击'创建'")
        sleep(4)
        try:
            num_text_2 = self.get_element_text(IWL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IWL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def faqijiaoshen(self):
        self.click(IWL.mywork_loc,doc="点击'我的工作'")
        self.click(IWL.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IWL.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IWL.faqiliucheng_list)
        self.click(IWL.faqiliucheng,doc="点击'发起流程'")
        self.click(IWL.project_choose,doc="点击'所属项目'")
        self.click(IWL.choose_waterproject,doc="选择'水利咨询工程'")
        self.click(IWL.project_sure_button,doc="点击'确定'")
        self.click(IWL.choose_file_button,doc="点击'选择卷则'")
        self.click(IWL.input_file,doc="勾选01设计输入资料")
        self.click(IWL.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IWL.surebutton,doc="点击'确定'")
        self.click(IWL.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IWL.time_sure,doc="点击'确定'")
        self.click(IWL.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IWL.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IWL.sureperson_choose,doc="点击'确认人选择'")
        self.click(IWL.xuhonglei_choose,doc="选择'徐鸿磊'")
        self.click(IWL.person_sure_button,doc="点击'确定'")
        self.click(IWL.huiqian_new,doc="跳过'会签'")
        self.click(IWL.wushen_choosebutton,doc="选择'五审人'")
        self.click(IWL.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IWL.wushen_sure_button,doc="点击'确定'")
        self.click(IWL.jiaoshenfile_add,doc="添加校审文件")
        self.click(IWL.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IWL.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IWL.file_sure_button,doc="点击'确定'")
        sleep(1)
        self.click(IWL.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IWL.faqiliucheng_list)
        project_name = self.get_element_text(IWL.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IWL.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def wushenren_loginapprove(self,name,password):
        self.click(IWL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IWL.mywork_loc,doc="点击'我的工作'")
        self.click(IWL.jiaoshen_loc,doc="点击'校审'")
        self.click(IWL.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IWL.w_needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IWL.w_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def wushenren_approvesucess(self,name,password):
        # self.click(IWL.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IWL.mywork_loc,doc="点击'我的工作'")
        # self.click(IWL.jiaoshen_loc,doc="点击'校审'")
        self.click(IWL.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IWL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IWL.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IWL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IWL.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IWL.w_file,doc="点击'1设计输入资料'进入详情")
        self.click(IWL.w_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IWL.w_all_pass,doc="点击'全部通过'")
        sleep(1)
        self.click(IWL.w_wushen_sure,doc="点击'确定'")
        self.click(IWL.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IWL.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        sleep(4)
        self.click(IWL.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IWL.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IWL.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IWL.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IWL.w_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def faqiren_check_returedproject(self,name,password):
        self.click(IWL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IWL.mywork_loc,doc="点击'我的工作'")
        self.click(IWL.jiaoshen_loc,doc="点击'校审'")
        faqi_jiaoshenname = self.get_element_text(IWL.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IWL.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IWL.w_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IWL.w_faqi_liushen_state,doc="获取六审状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def delete_1(self):
        self.click(IWL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IWL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IWL.project_list_num)
        except:
            self.get_element_text(IWL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IWL.delete1_loc, doc="删除'测试_水利咨询工程'")
        self.click(IWL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IWL.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IWL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IWL.project_list_num)
        return num_1, num_2, success_text
