from PageLocators.photovoltaic_locator import IndexpPhotovoltaicPageLocator as IPP
from PageLocators.login_page_locator import LoginPageLocator as LP
from selenium.webdriver.common.keys import Keys
from Common.basepage import BasePage
from time import sleep
class IndexPhotovoltaicPage(BasePage):
    # '光伏工程'特殊字段
    def check_Photovoltaic_field(self,name,password):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IPP.projecttype_checkbox,doc='选择项目类型')
        self.click(IPP.guangfu_gongcheng,doc="项目类型选择'光伏工程'")
        # 返回'生产部门'字段 和 '计划时间'字段数量
        return self.get_element_text(IPP.gongchengtype_allchoices,doc="获取'工程类型'文本信息"),\
               self.get_element_text(IPP.jianshexingzhi_allchoices,doc="获取'建设性质'所有文本"),\
               self.get_list_length(IPP.gongchengguimo_fieldsnum,doc="获取工程规模字段数量"),\
               self.get_element_text(IPP.rongliang,doc="获取工程规模唯一字段文本值"),\
               self.get_list_length(IPP.gongchengtouzi_fieldsnum,doc="获取工程投资字段数量"),\
               self.get_element_text(IPP.gongchengtouzi_fieldstext,doc="获取工程投资文本值")

    def create_photovoltaic_project(self,projectname,projectno):
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPP.project_list_num)
        self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IPP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IPP.projecttype_checkbox, doc='选择项目类型')
        self.click(IPP.guangfu_gongcheng,doc="项目类型选择'光伏工程'")
        self.click(IPP.fenbushi_gouxuan,doc="工程类型选择'分布式'")
        self.click(IPP.shejijieduan_choose,doc="点击设计阶段下拉框")
        self.click(IPP.shigongtu,doc="设计阶段选择'施工图'")
        self.click(IPP.dianyadengji_choose,doc="点击'电压等级'下拉框")
        self.click(IPP.kv35_choose,doc="电压等级选择'35kv'")
        self.click(IPP.guangfuqujianshe_gouxuan,doc="建设性质选择'光伏区建设'")
        self.click(IPP.juesemoban_choose,doc="点击'角色模板'下拉框")
        self.click(IPP.henghuaguangfu_choose,doc="角色模板选择'恒华光伏工程'")
        self.click(IPP.choose_member,doc="选择成员")
        self.click(IPP.zonggong,doc="点击'总工'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.haiqing_chooose,doc="勾选'海清'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.addpeople,doc="点击添加人员")
        self.input_text(IPP.zonggong_input,"张无忌",doc="总工输入'张无忌'")
        self.input_text(IPP.zonggong_input,Keys.ENTER)
        self.click(IPP.zhangwuji_gouxuan,doc="勾选'张无忌'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.shezong,doc="点击'设总'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.setnode_button,doc="设置节点")
        self.click(IPP.shejiinputfile,doc="勾选'01-设计输入资料'")
        self.click(IPP.inputfile_choosebutton,doc="选择")
        self.click(IPP.inputfile_zhangwuji_choose,doc="选择'张无忌'")
        self.click(IPP.inputfile_sure_button,doc="确定")
        self.click(IPP.setnode_sure_button,doc="确定")
        self.clear_text(IPP.rongliang_input,doc="清除默认文本值")
        self.input_text(IPP.rongliang_input,"100",doc="工程规模容量输入100")
        self.clear_text(IPP.kanchafei_input, doc="清除默认文本值")
        self.input_text(IPP.kanchafei_input,"101",doc="勘察费输入101")
        self.clear_text(IPP.shejifei_input, doc="清除默认文本值")
        self.input_text(IPP.shejifei_input,"102",doc="设计费输入102")
        self.clear_text(IPP.zongtouzi_input, doc="清除默认文本值")
        self.input_text(IPP.zongtouzi_input,"103",doc="总投资输入103")
        self.click(IPP.shejijiaoshen,doc="勾选设计校审")
        self.click(IPP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IPP.level_1,doc="选择1级别")
        self.click_by_js(IPP.diyubiaozhun,doc="勾选可低于标准级别")
        self.click_by_js(IPP.huiqianjieduan,doc="勾选可跳过会签阶段")
        self.click(IPP.start_time,doc="开始时间")
        self.click(IPP.start_time_sure,doc="确定时间")
        self.click(IPP.end_time,doc="结束时间")
        self.click(IPP.end_time_sure,doc="确定时间")
        self.click(IPP.jianguanren,doc="选择监管人")
        self.click(IPP.xulei,doc="勾选徐蕾")
        self.click(IPP.jianguan_sure,doc="点击确定按钮")
        self.click(IPP.create_button,doc="创建")
        sleep(4)
        num_2 = self.get_list_length(IPP.project_list_num)
        first_project_name = self.get_element_text(IPP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def create_photovoltaic_project4(self,name,password,projectname,projectno):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPP.project_list_num)
        self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IPP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IPP.projecttype_checkbox, doc='选择项目类型')
        self.click(IPP.guangfu_gongcheng,doc="项目类型选择'光伏工程'")
        self.click(IPP.fenbushi_gouxuan,doc="工程类型选择'分布式'")
        self.click(IPP.shejijieduan_choose,doc="点击设计阶段下拉框")
        self.click(IPP.shigongtu,doc="设计阶段选择'施工图'")
        self.click(IPP.dianyadengji_choose,doc="点击'电压等级'下拉框")
        self.click(IPP.kv35_choose,doc="电压等级选择'35kv'")
        self.click(IPP.guangfuqujianshe_gouxuan,doc="建设性质选择'光伏区建设'")
        self.click(IPP.juesemoban_choose,doc="点击'角色模板'下拉框")
        self.click(IPP.henghuaguangfu_choose,doc="角色模板选择'恒华光伏工程'")
        self.click(IPP.choose_member,doc="选择成员")
        self.click(IPP.zonggong,doc="点击'总工'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.haiqing_chooose,doc="勾选'海清'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.addpeople,doc="点击添加人员")
        self.input_text(IPP.zonggong_input,"张无忌",doc="总工输入'张无忌'")
        self.input_text(IPP.zonggong_input,Keys.ENTER)
        self.click(IPP.zhangwuji_gouxuan,doc="勾选'张无忌'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.shezong,doc="点击'设总'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.setnode_button,doc="设置节点")
        self.click(IPP.shejiinputfile,doc="勾选'01-设计输入资料'")
        self.click(IPP.inputfile_choosebutton,doc="选择")
        self.click(IPP.inputfile_zhangwuji_choose,doc="选择'张无忌'")
        self.click(IPP.inputfile_sure_button,doc="确定")
        self.click(IPP.setnode_sure_button,doc="确定")
        self.clear_text(IPP.rongliang_input,doc="清除默认文本值")
        self.input_text(IPP.rongliang_input,"100",doc="工程规模容量输入100")
        self.clear_text(IPP.kanchafei_input, doc="清除默认文本值")
        self.input_text(IPP.kanchafei_input,"101",doc="勘察费输入101")
        self.clear_text(IPP.shejifei_input, doc="清除默认文本值")
        self.input_text(IPP.shejifei_input,"102",doc="设计费输入102")
        self.clear_text(IPP.zongtouzi_input, doc="清除默认文本值")
        self.input_text(IPP.zongtouzi_input,"103",doc="总投资输入103")
        self.click(IPP.shejijiaoshen,doc="勾选设计校审")
        self.click(IPP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IPP.level_1,doc="选择1级别")
        button = self.driver.find_element_by_xpath('//label[text()="可低于标准级别"]/span')
        self.driver.execute_script("$(arguments[0]).click()", button)
        button = self.driver.find_element_by_xpath('//label[text()="可跳过会签阶段"]/span')
        self.driver.execute_script("$(arguments[0]).click()", button)
        self.click(IPP.start_time,doc="开始时间")
        self.click(IPP.start_time_sure,doc="确定时间")
        self.click(IPP.end_time,doc="结束时间")
        self.click(IPP.end_time_sure,doc="确定时间")
        self.click(IPP.jianguanren,doc="选择监管人")
        self.click(IPP.xulei,doc="勾选徐蕾")
        self.click(IPP.jianguan_sure,doc="点击确定按钮")
        self.click(IPP.create_button,doc="创建")
        sleep(4)
        num_2 = self.get_list_length(IPP.project_list_num)
        first_project_name = self.get_element_text(IPP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def create_photovoltaic_project2(self,projectname,projectno):
        self.click(IPP.projectplatform_loc, doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPP.project_list_num)
        self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IPP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IPP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IPP.projecttype_checkbox, doc='选择项目类型')
        self.click(IPP.guangfu_gongcheng,doc="项目类型选择'光伏工程'")
        self.click(IPP.fenbushi_gouxuan,doc="工程类型选择'分布式'")
        self.click(IPP.shejijieduan_choose,doc="点击设计阶段下拉框")
        self.click(IPP.shigongtu,doc="设计阶段选择'施工图'")
        self.click(IPP.dianyadengji_choose,doc="点击'电压等级'下拉框")
        self.click(IPP.kv35_choose,doc="电压等级选择'35kv'")
        self.click(IPP.guangfuqujianshe_gouxuan,doc="建设性质选择'光伏区建设'")
        self.click(IPP.juesemoban_choose,doc="点击'角色模板'下拉框")
        self.click(IPP.henghuaguangfu_choose,doc="角色模板选择'恒华光伏工程'")
        self.click(IPP.choose_member,doc="选择成员")
        self.click(IPP.zonggong,doc="点击'总工'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.haiqing_chooose,doc="勾选'海清'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.addpeople,doc="点击添加人员")
        self.input_text(IPP.zonggong_input,"张无忌",doc="总工输入'张无忌'")
        self.click(IPP.zhangwuji_gouxuan,doc="勾选'张无忌'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.shezong,doc="点击'设总'")
        self.click(IPP.addmember_button,doc="点击'添加成员'")
        self.click(IPP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.sure_button,doc="确定")
        self.click(IPP.setnode_button,doc="设置节点")
        self.click(IPP.shejiinputfile,doc="勾选'01-设计输入资料'")
        self.click(IPP.inputfile_choosebutton,doc="选择")
        self.click(IPP.inputfile_zhangwuji_choose,doc="选择'张无忌'")
        self.click(IPP.inputfile_sure_button,doc="确定")
        self.click(IPP.setnode_sure_button,doc="确定")
        self.clear_text(IPP.rongliang_input,doc="清除默认文本值")
        self.input_text(IPP.rongliang_input,"100",doc="工程规模容量输入100")
        self.clear_text(IPP.kanchafei_input, doc="清除默认文本值")
        self.input_text(IPP.kanchafei_input,"101",doc="勘察费输入101")
        self.clear_text(IPP.shejifei_input, doc="清除默认文本值")
        self.input_text(IPP.shejifei_input,"102",doc="设计费输入102")
        self.clear_text(IPP.zongtouzi_input, doc="清除默认文本值")
        self.input_text(IPP.zongtouzi_input,"103",doc="总投资输入103")
        self.click(IPP.shejijiaoshen,doc="勾选设计校审")
        self.click(IPP.huiqianjieduan,doc="跳过会签阶段")
        self.click(IPP.start_time,doc="开始时间")
        self.click(IPP.start_time_sure,doc="确定时间")
        self.click(IPP.end_time,doc="结束时间")
        self.click(IPP.end_time_sure,doc="确定时间")
        self.click(IPP.jianguanren,doc="选择监管人")
        self.click(IPP.xulei,doc="勾选徐蕾")
        self.click(IPP.jianguan_sure,doc="点击确定按钮")
        self.click(IPP.create_button,doc="创建")
        sleep(4)
        num_2 = self.get_list_length(IPP.project_list_num)
        first_project_name = self.get_element_text(IPP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def jixiao_manage3(self):
        self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname,doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        value_1 = self.get_element_attribute(IPP.box_01, "class")
        value_2 = self.get_element_attribute(IPP.box_pifu, "class")
        value_3 = self.get_element_attribute(IPP.box_06, "class")
        value_4 = self.get_element_attribute(IPP.box_shoukou, "class")
        value_5 = self.get_element_attribute(IPP.box_dizhi, "class")
        value_6 = self.get_element_attribute(IPP.box_yuanshi, "class")
        value_7 = self.get_element_attribute(IPP.box_pingshen, "class")
        self.click(IPP.cancle, doc="点击取消按钮")
        return value_1, value_2, value_3, value_4, value_5, value_6, value_7

    def jixiao_manage(self):
        # self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname,doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IPP.designfile,doc="勾选'01-设计输入资料'")
        self.click(IPP.choose_file_surebutton,doc="确定")
        sleep(2)
        self.click(IPP.first_file_name,doc="点击'第一个卷册'名称")
        sleep(4)
        zhu_biao = self.get_element_text(IPP.zhu_biao,doc="提取'主设人标准工日'")
        she_biao = self.get_element_text(IPP.she_biao,doc="提取'设计人标准工日'")
        biaozhunzonggongri = self.get_element_text(IPP.biaozhun_zonggongri,doc="获取'标准总共日'")
        tibaozonggongri = self.get_element_text(IPP.tibao_zonggongri,doc="获取'提报总共日'")
        return zhu_biao,she_biao,biaozhunzonggongri,tibaozonggongri


    def jixiao_manage33(self):
        self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname,doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IPP.designfile,doc="勾选'01-设计输入资料'")
        self.click(IPP.choose_file_surebutton,doc="确定")
        sleep(4)
        self.click(IPP.first_file_name,doc="点击'第一个卷册'名称")
        # self.click(IPP.editbutton,doc="点击'编辑'按钮")
        # self.click(IPP.huifuchushi,doc="点击'恢复初始'按钮")
        # self.click(IPP.surebutton,doc="点击'确定'按钮")
        sleep(4)
        # zhu_biao = self.get_element_text(IPP.zhu_biao,doc="提取'主设人标准工日'")
        # she_biao = self.get_element_text(IPP.she_biao,doc="提取'设计人标准工日'")
        biaozhunzonggongri = self.get_element_text(IPP.biaozhun_zonggongri2,doc="获取'标准共日'")
        tibaozonggongri = self.get_element_text(IPP.tibao_zonggongri2,doc="获取'提报共日'")
        return biaozhunzonggongri,tibaozonggongri

    def jixiao_manage2(self):
        # self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname,doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        value_1 = self.get_element_attribute(IPP.box_01, "class")
        value_2 = self.get_element_attribute(IPP.box_pifu, "class")
        value_3 = self.get_element_attribute(IPP.box_06, "class")
        value_4 = self.get_element_attribute(IPP.box_shoukou, "class")
        value_5 = self.get_element_attribute(IPP.box_dizhi, "class")
        value_6 = self.get_element_attribute(IPP.box_yuanshi, "class")
        value_7 = self.get_element_attribute(IPP.box_pingshen, "class")
        self.click(IPP.cancle, doc="点击取消按钮")
        return value_1, value_2, value_3, value_4, value_5, value_6, value_7

    def jixiao_manage4(self):
        self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname, doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IPP.box_01,doc="点击'01设计输入资料'")
        self.click(IPP.choose_file_surebutton,doc="点击'确定按钮'")
        self.click(IPP.first_file_name,doc="点击'第一个卷册名称'")
        self.click(IPP.submit_approve,doc="点击'提交审批'")
        self.click(IPP.hanzheng,doc="勾选'韩正'")
        self.click(IPP.chooseperson_sure,doc="点击'确定'")
        text_1 = self.get_element_text(IPP.success_info,doc="获取成功提示语")
        text_2 = self.get_element_text(IPP.apply_cancle,doc="获取取消申请")
        return text_1,text_2


    def jixiao_manage22(self):
        self.click(IPP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IPP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IPP.guangfuname,doc="点击'光伏项目'")
        self.click(IPP.faqi_shenpi,doc="点击'发起审批'")
        value_1 = self.get_element_attribute(IPP.box_01, "class")
        value_2 = self.get_element_attribute(IPP.box_pifu, "class")
        value_3 = self.get_element_attribute(IPP.box_06, "class")
        value_4 = self.get_element_attribute(IPP.box_shoukou, "class")
        value_5 = self.get_element_attribute(IPP.box_dizhi, "class")
        value_6 = self.get_element_attribute(IPP.box_yuanshi, "class")
        value_7 = self.get_element_attribute(IPP.box_pingshen, "class")
        self.click(IPP.cancle, doc="点击取消按钮")
        return value_1, value_2, value_3, value_4, value_5, value_6, value_7


    def faqijiaoshen(self):
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IPP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPP.faqiliucheng_list)
        self.click(IPP.faqiliucheng,doc="点击'发起流程'")
        self.click(IPP.project_choose,doc="点击'所属项目'")
        self.click(IPP.choose_netproject,doc="选择'光伏工程'")
        self.click(IPP.project_sure_button,doc="点击'确定'")
        self.click(IPP.choose_file_button,doc="点击'选择卷则'")
        self.click(IPP.designfilegouxuan,doc="勾选设计输入资料'")
        self.click(IPP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IPP.surebutton,doc="点击'确定'")
        self.click(IPP.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IPP.time_sure,doc="点击'确定'")
        self.click(IPP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IPP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IPP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IPP.haiqing2,doc="选择'海清'")
        self.click(IPP.person_sure_button,doc="点击'确定'")
        self.click(IPP.huiqian_new,doc="跳过'会签'")
        self.click(IPP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IPP.wushen_hairuomeng,doc="五审'海若梦'")
        self.click(IPP.wushen_sure_button,doc="点击'确定'")
        self.click(IPP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IPP.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IPP.uploadfile_send,r"/root/测试上传脚本用3.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IPP.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IPP.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IPP.faqiliucheng_list)
        project_name = self.get_element_text(IPP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen2(self):
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        try:
            self.get_element_text(IPP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IPP.faqiliucheng_list)
        self.click(IPP.faqiliucheng,doc="点击'发起流程'")
        self.click(IPP.project_choose,doc="点击'所属项目'")
        self.click(IPP.choose_netproject,doc="选择'光伏工程'")
        self.click(IPP.project_sure_button,doc="点击'确定'")
        self.click(IPP.choose_file_button,doc="点击'选择卷则'")
        self.click(IPP.designfilegouxuan,doc="勾选设计输入资料'")
        self.click(IPP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IPP.surebutton,doc="点击'确定'")
        self.click(IPP.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IPP.time_sure,doc="点击'确定'")
        self.click(IPP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IPP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IPP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IPP.haiqing,doc="选择'海清'")
        self.click(IPP.person_sure_button,doc="点击'确定'")
        self.click(IPP.huiqian_new,doc="跳过'会签'")
        self.click(IPP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IPP.wushen_hairuomeng,doc="五审'海若梦'")
        self.click(IPP.wushen_sure_button,doc="点击'确定'")
        self.click(IPP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IPP.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IPP.uploadfile_send,r"/root/测试上传脚本用3.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IPP.file_sure_button,doc="点击'确定'")
        sleep(3)
        self.click(IPP.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IPP.faqiliucheng_list)
        project_name = self.get_element_text(IPP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IPP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def wushenren_loginapprove(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        self.click(IPP.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IPP.ph_needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IPP.ph_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def wushenren_approvesucess(self):
        # self.click(IPP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IPP.mywork_loc,doc="点击'我的工作'")
        # self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        self.click(IPP.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IPP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IPP.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IPP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IPP.ph_needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IPP.ph_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IPP.ph_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IPP.ph_all_pass,doc="点击'全部通过'")
        self.click(IPP.ph_wushen_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IPP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        sleep(2)
        self.click(IPP.ph_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IPP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IPP.ph_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IPP.ph_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IPP.ph_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def faqiren_check_returedproject(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        faqi_jiaoshenname = self.get_element_text(IPP.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPP.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPP.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IPP.ph_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state

    def faqiren_faqisure_suc(self):
        self.click(IPP.bfile,doc="点击'01设计输入资料'")
        self.click(IPP.b_faqisure,doc="点击'发起确认'")
        self.click(IPP.b_faqi,doc="点击'发起按钮'")
        faqi_jiaoshenname = self.get_element_text(IPP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPP.b_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IPP.b_faqi_liushen_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def sureperson_check_returedproject(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        self.click(IPP.b_needdeal_button, doc="点击'待处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IPP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IPP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IPP.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IPP.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IPP.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IPP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state

    def sureperson_faqiqueren_suc(self):
        self.click(IPP.b_needdeal_button, doc="点击'待处理'")
        self.click(IPP.sfile, doc="点击'01设计输入资料'")
        self.click(IPP.s_surebutton, doc="点击'确认'")
        self.click(IPP.s_allpassbutton, doc="点击'全部通过'")
        self.click(IPP.s_sure_button, doc="点击'确定'按钮")
        sleep(2)
        self.click(IPP.b_dealed_button, doc="点击'已处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IPP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IPP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IPP.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IPP.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IPP.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IPP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state


    def faqiren_check_returedproject2(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.mywork_loc,doc="点击'我的工作'")
        self.click(IPP.jiaoshen_loc,doc="点击'校审'")
        faqi_jiaoshenname = self.get_element_text(IPP.ph_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IPP.ph_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IPP.ph_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IPP.ph_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def delete_1(self):
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IPP.project_list_num)
        except:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPP.delete1_loc,doc="删除'测试_光伏工程'")
        self.click(IPP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IPP.delete_success,doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPP.project_list_num)
        return num_1,num_2,success_text

    def delete_2(self):
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IPP.project_list_num)
        except:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IPP.delete2_loc,doc="删除'测试_光伏工程2'")
        self.click(IPP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IPP.delete_success,doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IPP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IPP.project_list_num)
        return num_1,num_2,success_text

    def guidang(self):
        self.click(IPP.guidang_guanli,doc="点击归档管理")
        self.click(IPP.faqi_guidang,doc="点击发起归档")
        sleep(4)
        self.click(IPP.choice,doc="所属项目后的'选择'")
        self.click(IPP.guidang_filename,doc="点击项目名称")
        text_1 = self.get_element_text(IPP.guidang_tishi,doc="获取归档提示语")
        self.click(IPP.closebutton,doc="点击'X'关闭弹框")
        text_2 = self.get_element_text(IPP.guidang_person1,doc="获取审批人员")
        return text_1,text_2

    def guidang2(self):
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        # self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IPP.first_project_name, doc="点击项目名称进入项目详情")
        self.click(IPP.design_file, doc="点击'设计卷册'进入项目云盘")
        sleep(1)
        self.click(IPP.file_input, doc="点击'01设计输入资料'进入文件夹上传文件")
        self.input_text_uploadfile(IPP.uploadfile2_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        uploadfilename = self.get_element_text(IPP.uploadedfilename, doc="获取已经上传的文件名称")
        fileversion = self.get_element_text(IPP.file_version, doc="获取文件版本号")
        self.click(IPP.guidang_guanli,doc="点击归档管理")
        self.click(IPP.faqi_guidang,doc="点击发起归档")
        self.click(IPP.choice, doc="所属项目后的'选择'")
        sleep(4)
        self.click(IPP.guidang_gouxuan,doc="勾选归档项目名称")
        self.click(IPP.sureb,doc="点击'确定按钮'")
        sleep(20)
        jianguanren = self.get_element_text(IPP.jianguan_person,doc="获取监管人员")
        self.click(IPP.faqiguidang,doc="点击'发起归档'按钮")
        sleep(4)
        filename = self.get_element_text(IPP.first_guidang_name,doc="获取第一条归档记录项目名称")
        version = self.get_element_text(IPP.first_guidang_version,doc="获取第一条归档版本")
        approver = self.get_element_text(IPP.first_guidang_approver,doc="获取第一条归档审批人")
        state = self.get_element_text(IPP.first_guidang_state,doc="获取第一条归档审批状态")
        return uploadfilename,fileversion,jianguanren,filename,version,approver,state

    def guidang3(self):
        self.click(IPP.faqi_guidang,doc="点击发起归档")
        self.click(IPP.choice, doc="所属项目后的'选择'")
        sleep(4)
        self.click(IPP.guidang_gouxuan1, doc="勾选归档项目名称")
        sleep(2)
        tishiyu = self.get_element_text(IPP.guidang_tishi,doc="获取归档提示语")
        return tishiyu

    def jianguanren_checksucess(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPP.guidang_guanli, doc="点击归档管理")
        self.click(IPP.s_myapprove_button,doc="点击'我审批的'")
        sleep(6)
        filename1 = self.get_element_text(IPP.s_myapprove_projectname,doc="我审批的第一条记录项目名称")
        banben1 = self.get_element_text(IPP.s_myapprove_version,doc="我审批的第一条记录归档版本")
        tijiaoren1 = self.get_element_text(IPP.s_tijiaoren,doc="我审批的第一条记录提交人")
        approvestate1 = self.get_element_text(IPP.s_approvestate,doc="我审批的第一条记录审批状态")
        approvetime1 = self.get_element_text(IPP.s_approvetime,doc="我审批的第一条记录审批时间")
        self.click(IPP.j_myjianguan_button, doc="点击'我监管的'")
        sleep(6)
        filename2 = self.get_element_text(IPP.j_myjianguan_projectname,doc="我监管的第一条记录项目名称")
        tijiaoren2 = self.get_element_text(IPP.j_tijiaoren,doc="我监管的第一条记录提交人")
        jianguanren2 = self.get_element_text(IPP.j_jianguan,doc="我监管的第一条记录监管人")
        approvestate2 = self.get_element_text(IPP.j_approvestate,doc="我监管的第一条记录审批状态")
        approvetime2 = self.get_element_text(IPP.j_approvetime,doc="我监管的第一条记录审批时间")
        version2 = self.get_element_text(IPP.j_version,doc="我监管的第一条记录归档版本")
        return filename1,banben1,tijiaoren1,approvestate1,approvetime1,filename2,tijiaoren2,jianguanren2,approvestate2,approvetime2,version2

    def jianguanren_approvesucess(self):
        self.click(IPP.s_myapprove_button,doc="点击'我审批的'")
        self.click(IPP.s_myapprove_projectname,doc="点击'我审批的'第一条项目名称")
        self.click(IPP.approve_pass,doc="点击'通过'")
        self.click(IPP.approve_sure,doc="点击'确定'")
        sleep(4)
        date = self.get_date()
        s_projectnames = self.get_elements_text_value(IPP.s_all_datas, doc="'我审批的'列表所有数据")
        self.click(IPP.j_myjianguan_button,doc="点击'我监管的'")
        sleep(2)
        file_name = self.get_element_text(IPP.j_myjianguan_projectname,doc="'我监管的'第一条记录名称")
        guidang_state = self.get_element_text(IPP.j_approvestate,doc="'我监管的'第一条记录归档状态")
        approve_time = self.get_element_text(IPP.j_approvetime,doc="'我监管的'第一条记录审批时间")
        return s_projectnames,file_name,guidang_state,approve_time,date

    def faqiguidang_failagain(self,name,password):
        self.click(IPP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IPP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IPP.guidang_guanli,doc="点击归档管理")
        self.click(IPP.faqi_guidang,doc="点击发起归档")
        self.click(IPP.choice, doc="所属项目后的'选择'")
        sleep(4)
        self.click(IPP.guidang_gouxuan1, doc="勾选归档项目名称")
        text = self.get_element_text(IPP.guidang_tishi,doc="获取提示语")
        return text

    def guidang_successagain(self):
        self.click(IPP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IPP.projectplatform_loc,doc="首页_点击'项目台账'")
        # self.click(IPP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IPP.first_project_name, doc="点击项目名称进入项目详情")
        self.click(IPP.design_file, doc="点击'设计卷册'进入项目云盘")
        sleep(1)
        self.click(IPP.file_input, doc="点击'01设计输入资料'进入文件夹上传文件")
        self.input_text_uploadfile(IPP.uploadfile2_send, r"/root/测试上传脚本用2.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        uploadfilename = self.get_element_text(IPP.uploadedfilename2, doc="获取已经上传的文件名称")
        fileversion = self.get_element_text(IPP.file_version2, doc="获取文件版本号")
        self.click(IPP.guidang_guanli,doc="点击归档管理")
        num_1 = self.get_element_text(IPP.all_datas,doc="获取共多少行")
        self.click(IPP.faqi_guidang,doc="点击发起归档")
        self.click(IPP.choice, doc="所属项目后的'选择'")
        sleep(2)
        self.click(IPP.guidang_gouxuan,doc="勾选归档项目名称")
        self.click(IPP.guidang_sure, doc="归档确定按钮")
        sleep(2)
        jianguanren = self.get_element_text(IPP.jianguan_person,doc="获取监管人员")
        self.click(IPP.faqiguidang, doc="点击'发起归档'按钮")
        sleep(2)
        num_2 = self.get_element_text(IPP.all_datas, doc="获取共多少行")
        filename = self.get_element_text(IPP.first_guidang_name,doc="获取第一条归档记录项目名称")
        version = self.get_element_text(IPP.first_guidang_version,doc="获取第一条归档版本")
        approver = self.get_element_text(IPP.first_guidang_approver,doc="获取第一条归档审批人")
        state = self.get_element_text(IPP.first_guidang_state,doc="获取第一条归档审批状态")
        return uploadfilename,fileversion,jianguanren,filename,version,approver,state,num_1,num_2

    def quxiaojiaoshen(self):
        self.click(IPP.shejijiaoshen_quxiao,doc="点击'设计校审流程'")
        self.click(IPP.quxiao_quxiao,doc="点击'取消'")
        self.click(IPP.queding_quxiao,doc="点击'确定'")
        text = self.get_element_text(IPP.quxiaochenggong_text,doc="获取'取消成功'文本值")
        text2 = self.get_element_text(IPP.chongxin_wenbenzhi,doc="获取'重新发起流程'文本值")
        return text,text2

    def zaici_faqijiaoshen(self):
        self.click(IPP.chongxin_wenbenzhi,doc="点击'再次发起流程'")
        self.click(IPP.faqi_liucheng2,doc="点击'发起流程'")
        success_text = self.get_element_text(IPP.liucheng_text,doc="获取'流程发起成功'文本值")
        project_name = self.get_element_text(IPP.suoshuxiangmu2, doc="获取'所属项目'名称")
        state = self.get_element_text(IPP.wushenren_approvestate2, doc="获取'五审'状态")
        length = self.get_list_length(IPP.project_list,doc="获取列表长度")
        return success_text,project_name,state,length



















