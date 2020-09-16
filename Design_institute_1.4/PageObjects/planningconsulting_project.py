from PageLocators.planconsult_locator import IndexPlanPageLocator as IPL
from PageLocators.login_page_locator import LoginPageLocator as LP
from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep
class IndexPlanConsultPage(BasePage):
    # '规划咨询'特殊字段
    def check_planconsult_field(self):
        self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IPL.projecttype_checkbox,doc='选择项目类型')
        self.click(IPL.planconsult_loc,doc="项目类型选择'规划咨询'")
        # 返回'生产部门'字段 和 '计划时间'字段数量
        return self.get_element_text(IPL.projecttypechoice_loc,doc="获取工程类型选项"),\
               self.get_element_text(IPL.constructnature_loc,doc="获取建设性质"),\
               self.get_element_text(IPL.planarea_loc,doc="获取规划面积"),\
               self.get_element_text(IPL.kv_loc,doc="获取10kv线路")

    def create_photovoltaic_project(self,projectname,projectno):
        self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
            # num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        # self.click(IPL.add_member, doc="点击'添加成员'")
        # self.input_text(IPL.name_input,"张无忌",doc="输入'张无忌'")
        # self.click(IPL.zhangwuji_gouxuan,doc="勾选张无忌")
        # self.click(IPL.sure_button,doc="点击'确定'按钮")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.clear_text(IPL.planarea_input,doc="清空规划面积默认值")
        self.input_text(IPL.planarea_input,"100",doc="规划面积输入100")
        self.clear_text(IPL.kv_input, doc="清空10kv线路默认值")
        self.input_text(IPL.kv_input, "400", doc="10kv线路输入400")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_photovoltaic_project66(self,projectname,projectno):
        # self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
            # num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        # self.click(IPL.add_member, doc="点击'添加成员'")
        # self.input_text(IPL.name_input,"张无忌",doc="输入'张无忌'")
        # self.click(IPL.zhangwuji_gouxuan,doc="勾选张无忌")
        # self.click(IPL.sure_button,doc="点击'确定'按钮")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.clear_text(IPL.kv_input, doc="清空10kv线路默认值")
        self.input_text(IPL.kv_input, "400", doc="10kv线路输入400")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name


    def create_photovoltaic_project22(self,name,password,projectname,projectno):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.zhuantiyanjiu,doc="工程类型选择'专题研究'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.tour_design, doc="点击'规划专业设计人'按钮")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.xuhonglei, doc="勾选'徐鸿磊'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.plan_fuzeren, doc="点击'专业规划负责人'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.wanglu_gouxuan, doc="勾选'王路'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_photovoltaic_project33(self,projectname,projectno):
        # self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.gouxuan_xinjianqu,doc="勾选'新建区'")
        self.click(IPL.zhuantiyanjiu,doc="工程类型选择'专题研究'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.tour_design, doc="点击'规划专业设计人'按钮")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.xuhonglei, doc="勾选'徐鸿磊'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.plan_fuzeren, doc="点击'专业规划负责人'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.wanglu_gouxuan, doc="勾选'王路'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def jixiaoguanli(self,name,password,rate):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")
        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        huiluxishu = self.get_element_text(IPL.huilu_xishu,doc="提取回路系数")
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days,doc="提取项目标准总工日")
        tibao_rate = self.get_element_text(IPL.tibaobili,doc="提取提报比例")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days,doc="提取标准工日")
        return huiluxishu,zuizhongxishu,project_zonggongri,tibao_rate,biaozhun_days

    def jixiaoguanli11(self,rate):
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")
        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(2)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        huiluxishu = self.get_element_text(IPL.huilu_xishu,doc="提取回路系数")
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days,doc="提取项目标准总工日")
        tibao_rate = self.get_element_text(IPL.tibaobili,doc="提取提报比例")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days,doc="提取标准工日")
        return huiluxishu,zuizhongxishu,project_zonggongri,tibao_rate,biaozhun_days

    def jixiaoguanli5(self,rate):
        # self.click(IPL.projectmanager_loc,doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")
        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days,doc="提取项目标准总工日")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days,doc="提取标准工日")
        tibao_days = self.get_element_text(IPL.tibao_days,doc="提取提报工日")
        return zuizhongxishu,project_zonggongri,biaozhun_days,tibao_days

    def jixiaoguanli6(self,rate):
        # self.click(IPL.projectmanager_loc,doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")
        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days,doc="提取项目标准总工日")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days,doc="提取标准工日")
        tibao_days = self.get_element_text(IPL.tibao_days,doc="提取提报工日")
        return zuizhongxishu,project_zonggongri,biaozhun_days,tibao_days


    def create_photovoltaic_project2(self,projectname,projectno):
        # self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
            # num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.gouxuan_xinjianqu,doc="勾选'新建区'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        # self.click(IPL.add_member, doc="点击'添加成员'")
        # self.input_text(IPL.name_input,"张无忌",doc="输入'张无忌'")
        # self.click(IPL.zhangwuji_gouxuan,doc="勾选张无忌")
        # self.click(IPL.sure_button,doc="点击'确定'按钮")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.tour_design, doc="点击'规划专业设计人'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.huangbo,doc="勾选黄渤")
        self.click(IPL.sure_button, doc="点击'确定'按钮")

        self.click(IPL.plan_fuzeren,doc="点击'规划专业负责人'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.xuhonglei,doc="勾选'徐红雷'")

        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.clear_text(IPL.planarea_input,doc="清空规划面积默认值")
        self.input_text(IPL.planarea_input,"123",doc="规划面积输入123")
        self.clear_text(IPL.kv_input, doc="清空10kv线路默认值")
        self.input_text(IPL.kv_input, "400", doc="10kv线路输入400")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_photovoltaic_project6(self,projectname,projectno):
        # self.click(IPL.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPL.nulldatas, doc="项目台账为空提示语")
            num_text_1 = 0
            # num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        self.click(IPL.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPL.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IPL.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IPL.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IPL.planconsult_loc,doc="选择'规划咨询'")
        self.click(IPL.gouxuan_xinjianqu,doc="勾选'新建区'")
        self.click(IPL.choose_member,doc="点击'选择成员'")
        self.click(IPL.project_manager,doc="点击'项目经理'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.haiqing_chooose,doc="勾选海清")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.zixunshi,doc="点击'咨询师'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.tour_design, doc="点击'规划专业设计人'")
        self.click(IPL.add_member, doc="点击'添加成员'")
        self.click(IPL.huangbo,doc="勾选黄渤")
        self.click(IPL.sure_button, doc="点击'确定'按钮")

        self.click(IPL.plan_fuzeren,doc="点击'规划专业负责人'")
        self.click(IPL.add_member,doc="点击'添加成员'")
        self.click(IPL.xuhonglei,doc="勾选'徐红雷'")

        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.sure_button, doc="点击'确定'按钮")
        self.click(IPL.setnode_button,doc="点击'设置节点'")
        self.click(IPL.planreport,doc="勾选'规划咨询报告'")
        self.click(IPL.planreport_choosebutton,doc="点击'规划咨询报告--选择'")
        self.click(IPL.planreport_hairuomeng_choosebutton,doc="勾选'海若梦'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.click(IPL.plan_sure_button,doc="点击'确定'")
        self.clear_text(IPL.planarea_input,doc="清空规划面积默认值")
        self.input_text(IPL.planarea_input,"123",doc="规划面积输入123")
        self.click(IPL.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IPL.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IPL.level_1,doc="选择1级别")
        self.click_by_js(IPL.diyubiaozhun,doc="可低于标准级别")
        self.click_by_js(IPL.huiqianjieduan,doc="跳过会签阶段")
        self.click(IPL.start_time,doc="点击'开始时间'")
        self.click(IPL.start_time_sure,doc="点击'确定'")
        self.click(IPL.end_time,doc="点击'结束时间'")
        self.click(IPL.end_time_sure,doc="点击'确定'")
        self.click(IPL.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IPL.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def jixiaoguanli2(self,rate):
        # self.click(IPL.projectmanager_loc,doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击规划咨询名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")
        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        mianjixishu = self.get_element_text(IPL.mianji_xishu,doc="提取面积系数")
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu2,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days2,doc="提取项目标准总工日")
        tibao_rate = self.get_element_text(IPL.tibaobili2,doc="提取提报比例")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days2,doc="提取标准工日")
        return mianjixishu,zuizhongxishu,project_zonggongri,tibao_rate,biaozhun_days

    def jixiaoguanli23(self,name,password,rate):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IPL.guangfuname,doc="点击光伏项目名称")
        self.click(IPL.faqi_shenpi,doc="点击发起审批")
        self.clear_text(IPL.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate,rate,doc="输入提报比例")

        self.click(IPL.tibao_sure,doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link,doc="点击提报比例按钮")
        sleep(3)
        mianjixishu = self.get_element_text(IPL.mianji_xishu,doc="提取面积系数")
        zuizhongxishu = self.get_element_text(IPL.zuizhong_xishu2,doc="提取最终系数")
        project_zonggongri = self.get_element_text(IPL.project_all_days2,doc="提取项目标准总工日")
        tibao_rate = self.get_element_text(IPL.tibaobili2,doc="提取提报比例")
        biaozhun_days = self.get_element_text(IPL.biaozhun_days2,doc="提取标准工日")
        return mianjixishu,zuizhongxishu,project_zonggongri,tibao_rate,biaozhun_days

    def jixiaoguanli24(self,rate):
        self.click(IPL.projectmanager_loc, doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc, doc="点击绩效管理")
        self.click(IPL.guangfuname, doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi, doc="点击发起审批")
        self.clear_text(IPL.tibao_rate, doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate, rate, doc="输入提报比例")
        self.click(IPL.tibao_sure, doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link, doc="点击提报比例按钮")
        sleep(6)
        text = self.get_element_text(IPL.zhiliang4, doc="获取成品质量系数")
        if text != '1.05':
            self.driver.refresh()
            sleep(4)
            text = self.get_element_text(IPL.zhiliang4, doc="获取成品质量系数")
        return text

    def jixiaoguanli30(self,rate):
        self.click(IPL.projectmanager_loc, doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc, doc="点击绩效管理")
        self.click(IPL.guangfuname, doc="点击规划咨询项目名称")
        self.click(IPL.faqi_shenpi, doc="点击发起审批")
        self.clear_text(IPL.tibao_rate, doc="清空'填报比例输入框'")
        self.input_text(IPL.tibao_rate, rate, doc="输入提报比例")
        self.click(IPL.tibao_sure, doc="点击确定")
        sleep(3)
        self.click(IPL.tibaobili_link, doc="点击提报比例按钮")
        sleep(6)
        text = self.get_element_text(IPL.zhiliang4, doc="获取成品质量系数")
        if text != '1.04':
            self.driver.refresh()
            sleep(4)
            text = self.get_element_text(IPL.zhiliang4, doc="获取成品质量系数")
        return text

    def jixiaoguanli25(self,rate):
        self.click(IPL.projectmanager_loc, doc="点击项目管理")
        self.click(IPL.jixiaoguanli_loc, doc="点击绩效管理")
        self.click(IPL.guangfuname, doc="点击规划咨询项目名称")
        sleep(1)
        text = self.get_element_text(IPL.zhiliangs, doc="获取成品质量系数")
        return text

    def faqijiaoshen(self):
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IPL.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPL.faqiliucheng_list)
        self.click(IPL.faqiliucheng,doc="点击'发起流程'")
        self.click(IPL.project_choose,doc="点击'所属项目'")
        self.click(IPL.choose_planproject,doc="选择'规划咨询工程'")
        self.click(IPL.project_sure_button,doc="点击'确定'")
        self.click(IPL.choose_file_button,doc="点击'选择卷则'")
        self.click(IPL.planconsultgouxuan,doc="勾选规划咨询报告")
        self.click(IPL.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IPL.surebutton,doc="点击'确定'")
        self.click(IPL.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IPL.time_sure,doc="点击'确定'")
        self.click(IPL.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IPL.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IPL.sureperson_choose,doc="点击'确认人选择'")
        self.click(IPL.haiqing,doc="选择'海清'")
        self.click(IPL.person_sure_button,doc="点击'确定'")
        self.click(IPL.huiqian_new,doc="跳过'会签'")
        self.click(IPL.wushen_choosebutton,doc="选择'五审人'")
        self.click(IPL.wushen_hairuomeng,doc="五审'海若梦'")
        self.click(IPL.wushen_sure_button,doc="点击'确定'")
        self.click(IPL.jiaoshenfile_add,doc="添加校审文件")
        self.click(IPL.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IPL.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IPL.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IPL.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IPL.faqiliucheng_list)
        project_name = self.get_element_text(IPL.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPL.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen2(self,name,password):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IPL.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPL.faqiliucheng_list)
        self.click(IPL.faqiliucheng,doc="点击'发起流程'")
        self.click(IPL.project_choose,doc="点击'所属项目'")
        self.click(IPL.choose_planproject6,doc="选择'规划咨询工程6'")
        self.click(IPL.project_sure_button,doc="点击'确定'")
        self.click(IPL.choose_file_button,doc="点击'选择卷则'")
        self.click(IPL.planconsultgouxuan,doc="勾选规划咨询报告")
        # self.click(IPL.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click_by_js(IPL.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click_by_js(IPL.surebutton,doc="点击'确定'")
        self.click(IPL.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IPL.time_sure,doc="点击'确定'")
        self.click(IPL.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IPL.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IPL.sureperson_choose,doc="点击'确认人选择'")
        self.click(IPL.haiqing,doc="选择'海清'")
        self.click(IPL.person_sure_button,doc="点击'确定'")
        self.click(IPL.huiqian_new,doc="跳过'会签'")
        self.click(IPL.wushen_choosebutton,doc="选择'五审人'")
        self.click(IPL.wushen_hairuomeng,doc="五审'海若梦'")
        self.click(IPL.wushen_sure_button,doc="点击'确定'")
        self.click(IPL.jiaoshenfile_add,doc="添加校审文件")
        self.click(IPL.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IPL.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IPL.file_sure_button,doc="点击'确定'")
        sleep(2)
        # self.click(IPL.faqi_liucheng,doc="发起流程")
        self.click_by_js(IPL.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IPL.faqiliucheng_list)
        project_name = self.get_element_text(IPL.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPL.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen3(self,name,password):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IPL.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPL.faqiliucheng_list)
        self.click(IPL.faqiliucheng,doc="点击'发起流程'")
        self.click(IPL.project_choose,doc="点击'所属项目'")
        self.click(IPL.choose_planproject6,doc="选择'规划咨询工程6'")
        self.click(IPL.project_sure_button,doc="点击'确定'")
        self.click(IPL.choose_file_button,doc="点击'选择卷则'")
        self.click(IPL.planconsultgouxuan,doc="勾选规划咨询报告")
        self.click_by_js(IPL.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click_by_js(IPL.surebutton,doc="点击'确定'")
        self.click(IPL.plan_finish_time,doc="点击'计划完成时间'")
        current_month = self.get_element_text(IPL.current_month, doc="获取当前月份")
        # self.click(IPL.time_sure,doc="点击'确定'")
        sleep(2)
        future_date = self.future_oneday(5).split("-")[-1]
        if int(future_date) < 10:
            future_date = future_date[-1]
            print(future_date)
        if int(self.future_oneday(5)[5:7]) > int(current_month[0:2]):
            self.click(IPL.lastmonth, doc="切换至下一月份")
        locator = '//span[text()="{}"]'.format(future_date)
        date_loc = (By.XPATH,locator)
        self.click(date_loc,doc="点击时间")
        self.click(IPL.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IPL.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IPL.sureperson_choose,doc="点击'确认人选择'")
        self.click(IPL.haiqing,doc="选择'海清'")
        self.click_by_js(IPL.person_sure_button,doc="点击'确定'")
        self.click(IPL.huiqian_new,doc="跳过'会签'")
        self.click(IPL.wushen_choosebutton,doc="选择'五审人'")
        self.click(IPL.wushen_hairuomeng,doc="五审'海若梦'")
        self.click(IPL.wushen_sure_button,doc="点击'确定'")
        self.click(IPL.jiaoshenfile_add,doc="添加校审文件")
        self.click(IPL.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IPL.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IPL.file_sure_button,doc="点击'确定'")
        sleep(2)
        # self.click(IPL.faqi_liucheng,doc="发起流程")
        self.click_by_js(IPL.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IPL.faqiliucheng_list)
        project_name = self.get_element_text(IPL.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPL.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state,future_date

    def faqijiaoshen4(self):
        # self.click(IPL.mywork_loc,doc="点击'我的工作'")
        # self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        # sleep(2)
        # try:
        #     self.get_element_text(IPL.liucheng_null, doc="流程为空提示语")
        #     num_1 = 0
        # except:
        #     num_1 = self.get_list_length(IPL.faqiliucheng_list)
        self.click(IPL.guihua,doc="点击'规划咨询报告'")
        self.click(IPL.faqiwushen,doc="点击'发起五审批'")
        self.click(IPL.clickinput,doc="点击'回复输入框'")
        self.input_text(IPL.huifutext,"好好学习，天天向上",doc="回复文本款输入'好好学习天天向上'")
        self.click(IPL.biaoshixiala,doc="点击'标识符下拉框'")
        self.click(IPL.firstmark,doc="选择第一个标识符")
        self.click(IPL.save_button,doc="点击保存按钮")
        self.click(IPL.faqi,doc="点击发起按钮")
        sleep(6)
        project_name = self.get_element_text(IPL.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPL.wushenren_approvestate,doc="获取'五审'状态")
        return project_name,state

    def wushenren_loginapprove(self,name,password):
        self.click(IPL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IPL.ph_needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IPL.ph_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def sureren_checksuc(self,name,password):
        self.click(IPL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IPL.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IPL.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IPL.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IPL.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IPL.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IPL.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state

    def sureperson_faqiqueren_suc(self):
        self.click(IPL.ph_needdeal_button, doc="点击'待处理'")
        sleep(8)
        self.click(IPL.sfile, doc="点击'01设计输入资料'")
        self.click(IPL.s_surebutton, doc="点击'确认'")
        self.click(IPL.s_allpassbutton, doc="点击'全部通过'")
        self.click(IPL.s_sure_button, doc="点击'确定'按钮")
        sleep(2)
        self.click(IPL.ph_dealed_button, doc="点击'已处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IPL.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IPL.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IPL.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IPL.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IPL.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IPL.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state


    def wushenren_approvesucess(self):
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IPL.ph_file,doc="点击'规划咨询报告'进入详情")
        self.click(IPL.ph_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IPL.ph_all_pass,doc="点击'全部通过'")
        sleep(1)
        self.click(IPL.ph_wushen_sure,doc="点击'确定'")
        self.click(IPL.ph_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        sleep(1)
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IPL.ph_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IPL.ph_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IPL.ph_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_approvesucess2(self):
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IPL.ph_file,doc="点击'规划咨询报告'进入详情")
        self.click(IPL.ph_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IPL.ph_all_pass,doc="点击'全部通过'")
        self.click(IPL.clickinput, doc="点击'意见输入框'")
        self.input_text(IPL.yijiantext, "好的可以啦", doc="意见文本款输入'好的可以啦'")
        self.click(IPL.surebiaoshixiala, doc="点击'标识符下拉框'")
        self.click(IPL.firstmarks, doc="选择第一个标识符")
        self.click(IPL.save_button, doc="点击保存按钮")
        sleep(2)
        self.click(IPL.ph_wushen_sure,doc="点击'确定'")
        self.click(IPL.ph_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        sleep(1)
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IPL.ph_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IPL.ph_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IPL.ph_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_tuihuisucess(self):
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IPL.ph_needdeal_button,doc="点击'待处理'")
        self.click(IPL.ph_file,doc="点击'规划咨询报告'进入详情")
        self.click(IPL.ph_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IPL.addadvoice,doc="点击'添加意见'")
        self.input_text(IPL.tuhao,'北斗七星',doc="图号输入'北斗七星'")
        self.input_text(IPL.yijian,'春暖花开好好干',doc="意见输入'春暖花开好好干'")
        self.click(IPL.yijian_sure,doc="点击'确定'按钮")
        sleep(3)
        self.click(IPL.ph_wushen_sure,doc="点击'确定'")
        self.click(IPL.ph_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        sleep(3)
        self.click(IPL.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IPL.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IPL.ph_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IPL.ph_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IPL.ph_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def faqiren_check_returedproject(self,name,password):
        self.click(IPL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        faqi_jiaoshenname = self.get_element_text(IPL.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPL.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPL.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IPL.ph_faqi_liushen_state,doc="获取六审状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def faqiren_check_returedproject2(self,name,password):
        self.click(IPL.ph_logout,doc="退出系统")
        sleep(2)
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        sleep(4)
        faqi_jiaoshenname = self.get_element_text(IPL.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPL.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPL.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IPL.ph_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state

    def faqiren_check_returedproject3(self,name,password):
        self.click(IPL.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPL.mywork_loc,doc="点击'我的工作'")
        self.click(IPL.jiaoshen_loc,doc="点击'校审'")
        sleep(5)
        faqi_jiaoshenname = self.get_element_text(IPL.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPL.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPL.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IPL.ph_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state

    def delete_1(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete1_loc, doc="删除'测试_规划咨询工程'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text

    def delete_5(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete5_loc, doc="删除'测试_规划咨询工程5'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text

    def delete_6(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete6_loc, doc="删除'测试_规划咨询工程6'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(5)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text


    def delete_2(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete2_loc, doc="删除'测试_规划咨询工程2'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text

    def delete_3(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete3_loc, doc="删除'测试_规划咨询工程3'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text

    def delete_4(self):
        self.click(IPL.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPL.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IPL.project_list_num)
        except:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPL.delete4_loc, doc="删除'测试_规划咨询工程4'")
        self.click(IPL.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IPL.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IPL.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPL.project_list_num)
        return num_1, num_2, success_text

    def faqiren_faqisure_suc(self):
        self.click(IPL.bfile,doc="点击'规划咨询报告'")
        self.click(IPL.b_faqisure,doc="点击'发起确认'")
        self.click(IPL.b_faqi,doc="点击'发起按钮'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IPL.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPL.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPL.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IPL.ph_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state




