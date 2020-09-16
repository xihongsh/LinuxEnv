from PageLocators.biandian_locator import IndexBianPageLocator as IBP
from PageLocators.login_page_locator import LoginPageLocator as LP
from Common.basepage import BasePage
from time import sleep
class IndexBianPage(BasePage):
    # '变电工程'特殊字段
    def check_biandian_field(self):
        self.click(IBP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IBP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IBP.projecttype_checkbox,doc='选择项目类型')
        self.click(IBP.biandianproject_loc,doc="项目类型选择'变电工程'")
        # 返回工程类型和建设性质字段
        return self.get_element_text(IBP.projecttypechoice_loc,doc="获取'工程类型'文本信息"),\
               self.get_element_text(IBP.consult_choose_box,doc="获取'建设性质'所有文本")

    def create_biandian_project(self,projectname,projectno):
        self.click(IBP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.project_list_num)
        self.click(IBP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IBP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IBP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IBP.projecttype_checkbox, doc='选择项目类型')
        self.click(IBP.biandianproject_loc,doc="项目类型选择'变电工程'")
        self.click(IBP.hunei,doc="工程类型选择'户内'")
        self.click(IBP.design_box,doc="点击设计阶段下拉框")
        self.click(IBP.jungongtu,doc="设计阶段选择'施工图'")
        self.click(IBP.dianya_choose_box,doc="点击'电压等级'下拉框")
        self.click(IBP.kv35,doc="电压等级选择'35kv'")
        self.click(IBP.biandian,doc="建设性质选择'变电新建'")
        self.click(IBP.choose_member,doc="选择成员")
        self.click(IBP.zonggong,doc="点击'总工'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.haiqing_chooose,doc="勾选'海清'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.shezong,doc="点击'设总'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.setnode_button,doc="设置节点")
        self.click(IBP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IBP.design_input,doc="选择")
        self.click(IBP.design_choice,doc="选择'海清'")
        self.click_by_js(IBP.b_sure_button1,doc="确定")
        self.click(IBP.b_sure_button2,doc="确定")
        self.click(IBP.shejijiaoshen,doc="勾选设计校审")
        self.click(IBP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IBP.level_1,doc="选择1级别")
        self.click_by_js(IBP.diyubiaozhun,doc="可低于标准级别")
        self.click_by_js(IBP.huiqianjieduan,doc="跳过会签阶段")
        self.click(IBP.start_time,doc="开始时间")
        self.click(IBP.start_time_sure,doc="确定时间")
        self.click(IBP.end_time,doc="结束时间")
        self.click(IBP.end_time_sure,doc="确定时间")
        self.click(IBP.create_button,doc="创建")
        sleep(6)
        num_2 = self.get_list_length(IBP.project_list_num)
        first_project_name = self.get_element_text(IBP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def create_biandian_project00(self,projectname,projectno):
        # self.click(IBP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.project_list_num)
        self.click(IBP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IBP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IBP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IBP.projecttype_checkbox, doc='选择项目类型')
        self.click(IBP.biandianproject_loc,doc="项目类型选择'变电工程'")
        self.click(IBP.hunei,doc="工程类型选择'户内'")
        self.click(IBP.design_box,doc="点击设计阶段下拉框")
        self.click(IBP.jungongtu,doc="设计阶段选择'施工图'")
        self.click(IBP.dianya_choose_box,doc="点击'电压等级'下拉框")
        self.click(IBP.kv35,doc="电压等级选择'35kv'")
        self.click(IBP.biandian,doc="建设性质选择'变电新建'")
        self.click(IBP.choose_member,doc="选择成员")
        self.click(IBP.zonggong,doc="点击'总工'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.haiqing_chooose,doc="勾选'海清'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.shezong,doc="点击'设总'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.setnode_button,doc="设置节点")
        self.click(IBP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IBP.design_input,doc="选择")
        self.click(IBP.design_choice,doc="选择'海清'")
        sleep(2)
        self.click(IBP.b_sure_button1,doc="确定")
        self.click(IBP.b_sure_button1,doc="确定")
        self.click(IBP.shejijiaoshen,doc="勾选设计校审")
        self.click(IBP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IBP.null,doc="选择无")
        self.click(IBP.start_time,doc="开始时间")
        self.click(IBP.start_time_sure,doc="确定时间")
        self.click(IBP.end_time,doc="结束时间")
        self.click(IBP.end_time_sure,doc="确定时间")
        self.click(IBP.create_button,doc="创建")
        sleep(6)
        num_2 = self.get_list_length(IBP.project_list_num)
        first_project_name = self.get_element_text(IBP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name


    def create_biandian_project3(self,name,password,projectname,projectno):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.project_list_num)
        self.click(IBP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IBP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IBP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IBP.projecttype_checkbox, doc='选择项目类型')
        self.click(IBP.biandianproject_loc,doc="项目类型选择'变电工程'")
        self.click(IBP.hunei,doc="工程类型选择'户内'")
        self.click(IBP.design_box,doc="点击设计阶段下拉框")
        self.click(IBP.jungongtu,doc="设计阶段选择'施工图'")
        self.click(IBP.dianya_choose_box,doc="点击'电压等级'下拉框")
        self.click(IBP.kv35,doc="电压等级选择'35kv'")
        self.click(IBP.biandian,doc="建设性质选择'变电新建'")
        self.click(IBP.choose_member,doc="选择成员")
        self.click(IBP.zonggong,doc="点击'总工'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.haiqing_chooose,doc="勾选'海清'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.shezong,doc="点击'设总'")
        self.click(IBP.addpeople,doc="点击'添加成员'")
        self.click(IBP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.sure_button,doc="确定")
        self.click(IBP.setnode_button,doc="设置节点")
        self.click(IBP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IBP.design_input,doc="选择")
        self.click(IBP.design_choice,doc="选择'海清'")
        self.click(IBP.b_sure_button1,doc="确定")
        self.click(IBP.b_sure_button1,doc="确定")
        self.click(IBP.shejijiaoshen,doc="勾选设计校审")
        self.click(IBP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IBP.level_1,doc="选择1级别")
        self.click_by_js(IBP.diyubiaozhun,doc="可低于标准级别")
        self.click_by_js(IBP.huiqianjieduan,doc="跳过会签阶段")
        self.click(IBP.start_time,doc="开始时间")
        self.click(IBP.start_time_sure,doc="确定时间")
        self.click(IBP.end_time,doc="结束时间")
        self.click(IBP.end_time_sure,doc="确定时间")
        self.click(IBP.create_button,doc="创建")
        sleep(6)
        num_2 = self.get_list_length(IBP.project_list_num)
        first_project_name = self.get_element_text(IBP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def create_biandian_project2(self, projectname, projectno):
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.project_list_num)
        self.click(IBP.addproject_loc, doc="首页_点击'添加项目'")
        self.input_text(IBP.projectname_loc, projectname, doc="输入项目名称")
        self.input_text(IBP.projectno_loc, projectno, doc="输入项目编号")
        self.click(IBP.projecttype_checkbox, doc='选择项目类型')
        self.click(IBP.biandianproject_loc, doc="项目类型选择'变电工程'")
        self.click(IBP.hunei, doc="工程类型选择'户内'")
        self.click(IBP.design_box, doc="点击设计阶段下拉框")
        self.click(IBP.jungongtu, doc="设计阶段选择'施工图'")
        self.click(IBP.dianya_choose_box, doc="点击'电压等级'下拉框")
        self.click(IBP.kv35, doc="电压等级选择'35kv'")
        self.click(IBP.biandian, doc="建设性质选择'变电新建'")
        self.click(IBP.choose_member, doc="选择成员")
        self.click(IBP.zonggong, doc="点击'总工'")
        self.click(IBP.addpeople, doc="点击'添加成员'")
        self.click(IBP.haiqing_chooose, doc="勾选'海清'")
        self.click(IBP.sure_button, doc="确定")
        self.click(IBP.shezong, doc="点击'设总'")
        self.click(IBP.addpeople, doc="点击'添加成员'")
        self.click(IBP.hairuomeng_choose, doc="勾选'海若梦'")
        self.click(IBP.sure_button, doc="确定")
        self.click(IBP.sure_button, doc="确定")
        self.click(IBP.setnode_button, doc="设置节点")
        self.click(IBP.input01_file, doc="勾选'01-设计输入资料'")
        self.click(IBP.design_input, doc="选择")
        self.click(IBP.design_choice, doc="选择'海清'")
        self.click(IBP.b_sure_button1, doc="确定")
        self.click(IBP.b_sure_button1, doc="确定")
        self.click(IBP.shejijiaoshen, doc="勾选设计校审")
        self.click(IBP.huiqianjieduan, doc="跳过会签阶段")
        self.click(IBP.start_time, doc="开始时间")
        self.click(IBP.start_time_sure, doc="确定时间")
        self.click(IBP.end_time, doc="结束时间")
        self.click(IBP.end_time_sure, doc="确定时间")
        self.click(IBP.create_button, doc="创建")
        sleep(4)
        num_2 = self.get_list_length(IBP.project_list_num)
        first_project_name = self.get_element_text(IBP.first_project_name, doc="获取第一个项目名称")
        return num_1, num_2, first_project_name

    def jixiao_manage2(self,name,password):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        sleep(6)
        value_1 = self.get_element_attribute(IBP.box_01,"class",doc="获取元素属性")
        value_2 = self.get_element_attribute(IBP.box_pifu,"class",doc="获取元素属性")
        value_3 = self.get_element_attribute(IBP.box_06,"class",doc="获取元素属性")
        value_4 = self.get_element_attribute(IBP.box_shoukou,"class",doc="获取元素属性")
        value_5 = self.get_element_attribute(IBP.box_dizhi,"class",doc="获取元素属性")
        value_6 = self.get_element_attribute(IBP.box_yuanshi,"class",doc="获取元素属性")
        value_7 = self.get_element_attribute(IBP.box_pingshen,"class",doc="获取元素属性")
        self.click(IBP.cancle,doc="点击取消按钮")
        return value_1,value_2,value_3,value_4,value_5,value_6,value_7

    def jixiao_manage25(self):
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        sleep(4)
        value_1 = self.get_element_attribute(IBP.box_01,"class",doc="获取元素属性")
        value_2 = self.get_element_attribute(IBP.box_pifu,"class",doc="获取元素属性")
        value_3 = self.get_element_attribute(IBP.box_06,"class",doc="获取元素属性")
        value_4 = self.get_element_attribute(IBP.box_shoukou,"class",doc="获取元素属性")
        value_5 = self.get_element_attribute(IBP.box_dizhi,"class",doc="获取元素属性")
        value_6 = self.get_element_attribute(IBP.box_yuanshi,"class",doc="获取元素属性")
        value_7 = self.get_element_attribute(IBP.box_pingshen,"class",doc="获取元素属性")
        self.click(IBP.cancle,doc="点击取消按钮")
        return value_1,value_2,value_3,value_4,value_5,value_6,value_7

    def jixiao_manage22(self):
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        sleep(4)
        value_1 = self.get_element_attribute(IBP.box_01,"class",doc="获取元素属性")
        value_2 = self.get_element_attribute(IBP.box_pifu,"class",doc="获取元素属性")
        value_3 = self.get_element_attribute(IBP.box_06,"class",doc="获取元素属性")
        value_4 = self.get_element_attribute(IBP.box_shoukou,"class",doc="获取元素属性")
        value_5 = self.get_element_attribute(IBP.box_dizhi,"class",doc="获取元素属性")
        value_6 = self.get_element_attribute(IBP.box_yuanshi,"class",doc="获取元素属性")
        value_7 = self.get_element_attribute(IBP.box_pingshen,"class",doc="获取元素属性")
        self.click(IBP.cancle,doc="点击取消按钮")
        return value_1,value_2,value_3,value_4,value_5,value_6,value_7

    def jixiao_manage3(self):
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        sleep(4)
        value_1 = self.get_element_attribute(IBP.box_01,"class",doc="获取元素属性")
        value_2 = self.get_element_attribute(IBP.box_pifu,"class",doc="获取元素属性")
        value_3 = self.get_element_attribute(IBP.box_06,"class",doc="获取元素属性")
        value_4 = self.get_element_attribute(IBP.box_shoukou,"class",doc="获取元素属性")
        value_5 = self.get_element_attribute(IBP.box_dizhi,"class",doc="获取元素属性")
        value_6 = self.get_element_attribute(IBP.box_yuanshi,"class",doc="获取元素属性")
        value_7 = self.get_element_attribute(IBP.box_pingshen,"class",doc="获取元素属性")
        self.click(IBP.cancle,doc="点击取消按钮")
        return value_1,value_2,value_3,value_4,value_5,value_6,value_7


    def jixiao_manage(self):
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IBP.inputfile01,doc="勾选'01设计输入资料'")
        self.click(IBP.sure,doc="确定")
        self.click(IBP.file_name,doc="点击'第一个卷册'名称")
        sleep(4)
        ewaixishu = self.get_element_text(IBP.ewai_xishu,doc="提取'额外系数'")
        zuizhong_nanyi_xishu = self.get_element_text(IBP.zuizhong_nanyi_xishu,doc="提取'最终难易系数'")
        biaozhun_zonggongri = self.get_element_text(IBP.biaozhun_gongri,doc="获取'标准共日'")
        tibao_zonggongri = self.get_element_text(IBP.tibao_gongri,doc="获取'提报共日'")
        return ewaixishu,zuizhong_nanyi_xishu,biaozhun_zonggongri,tibao_zonggongri

    def jixiao_manage00(self):
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IBP.inputfile01,doc="勾选'01设计输入资料'")
        self.click(IBP.sure,doc="确定")
        self.click(IBP.file_name,doc="点击'第一个卷册'名称")
        sleep(4)
        self.click(IBP.edit_button, doc="点击编辑按钮")
        self.click(IBP.edit_xishu_button, doc="点击系数调整按钮")
        self.input_text(IBP.xishu_input, "10", doc="系数调整输入框输入10")
        sleep(2)
        self.click(IBP.sure_button_xishu, doc="点击确定按钮")
        text = self.get_element_text(IBP.prom_info, doc="获取提示语")
        self.click(IBP.cancle_button_xishu, doc="点击取消按钮")
        self.click(IBP.cancle_edit_button, doc="点击退出编辑按钮")
        self.click(IBP.tijiao_shenpi, doc="点击提交审批")
        self.click(IBP.hanzheng13, doc="勾选韩正")
        self.click(IBP.sure1, doc="点击确定")
        return text


    def faqijiaoshen(self):
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        try:
            self.get_element_text(IBP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.faqiliucheng_list)
        self.click(IBP.faqiliucheng,doc="点击'发起流程'")
        self.click(IBP.project_choose,doc="点击'所属项目'")
        self.click(IBP.choose_biandianproject,doc="选择'变电工程'")
        self.click(IBP.project_sure_button,doc="点击'确定'")
        self.click(IBP.choose_file_button,doc="点击'选择卷则'")
        self.click(IBP.input_file,doc="勾选设计输入资料'")
        self.click(IBP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IBP.surebutton,doc="点击'确定'")
        self.click(IBP.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IBP.time_sure,doc="点击'确定'")
        self.click(IBP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IBP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IBP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IBP.haiqing_choose,doc="选择'海清'")
        self.click(IBP.person_sure_button,doc="点击'确定'")
        self.click(IBP.huiqian_new,doc="跳过'会签'")
        self.click(IBP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IBP.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IBP.wushen_sure_button,doc="点击'确定'")
        self.click(IBP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IBP.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IBP.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(4)
        self.click(IBP.file_sure_button,doc="点击'确定'")
        sleep(6)
        self.click(IBP.faqi_liucheng,doc="发起流程")
        sleep(8)
        num_2 = self.get_list_length(IBP.faqiliucheng_list)
        project_name = self.get_element_text(IBP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IBP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen33(self, name, password):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IBP.mywork_loc, doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc, doc="点击'校审'")
        try:
            self.get_element_text(IBP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.faqiliucheng_list)
        self.click(IBP.faqiliucheng, doc="点击'发起流程'")
        self.click(IBP.project_choose, doc="点击'所属项目'")
        self.click(IBP.choose_biandianproject, doc="选择'变电工程'")
        self.click(IBP.project_sure_button, doc="点击'确定'")
        self.click(IBP.choose_file_button, doc="点击'选择卷则'")
        self.click(IBP.input_file, doc="勾选设计输入资料'")
        self.click(IBP.tongbujiaoshen_gouxuan, doc="勾选同步校审")
        self.click(IBP.surebutton, doc="点击'确定'")
        self.click(IBP.plan_finish_time, doc="点击'计划完成时间'")
        self.click(IBP.time_sure, doc="点击'确定'")
        self.click(IBP.jishenshuoming, doc="点击'校审说明'")
        self.input_text(IBP.jishenshuoming, "风月同天", doc="输入文本值")
        self.click(IBP.sureperson_choose, doc="点击'确认人选择'")
        self.click(IBP.haiqing_choose, doc="选择'海清'")
        self.click(IBP.person_sure_button, doc="点击'确定'")
        # self.click(IBP.huiqian, doc="跳过'会签'")
        # self.click(IBP.wushen_choosebutton, doc="选择'五审人'")
        # self.click(IBP.wushenhairuomeng_choose, doc="五审'海若梦'")
        # self.click(IBP.wushen_sure_button, doc="点击'确定'")
        self.click(IBP.jiaoshenfile_add, doc="添加校审文件")
        self.click(IBP.upload_file, doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IBP.uploadfile_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(4)
        self.click(IBP.file_sure_button, doc="点击'确定'")
        sleep(6)
        self.click(IBP.faqi_liucheng, doc="发起流程")
        sleep(8)
        num_2 = self.get_list_length(IBP.faqiliucheng_list)
        project_name = self.get_element_text(IBP.suoshuxiangmu, doc="获取'所属项目'名称")
        state = self.get_element_text(IBP.sure_state, doc="获取'确认人'状态")
        return num_1, num_2, project_name, state

    def faqijiaoshen2(self):
        self.click(IBP.mywork_loc, doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc, doc="点击'校审'")
        sleep(4)
        try:
            self.get_element_text(IBP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IBP.faqiliucheng_list)
        self.click(IBP.faqiliucheng, doc="点击'发起流程'")
        self.click(IBP.project_choose, doc="点击'所属项目'")
        self.click(IBP.choose_biandianproject, doc="选择'变电工程'")
        self.click(IBP.project_sure_button, doc="点击'确定'")
        self.click(IBP.choose_file_button, doc="点击'选择卷则'")
        self.click(IBP.input_file, doc="勾选设计输入资料'")
        self.click(IBP.tongbujiaoshen_gouxuan, doc="勾选同步校审")
        self.click(IBP.surebutton, doc="点击'确定'")
        self.click(IBP.plan_finish_time, doc="点击'计划完成时间'")
        self.click(IBP.time_sure, doc="点击'确定'")
        self.click(IBP.jishenshuoming, doc="点击'校审说明'")
        self.input_text(IBP.jishenshuoming, "风月同天", doc="输入文本值")
        self.click(IBP.sureperson_choose, doc="点击'确认人选择'")
        self.click(IBP.haiqing_choose, doc="选择'海清'")
        self.click(IBP.person_sure_button, doc="点击'确定'")
        self.click(IBP.huiqian_new, doc="跳过'会签'")
        self.click(IBP.wushen_choosebutton, doc="选择'五审人'")
        self.click(IBP.wushenhairuomeng_choose, doc="五审'海若梦'")
        self.click(IBP.wushen_sure_button, doc="点击'确定'")
        self.click(IBP.jiaoshenfile_add, doc="添加校审文件")
        self.click(IBP.upload_file, doc="点击'上传文件按钮'")
        sleep(2)
        self.input_text_uploadfile(IBP.uploadfile_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IBP.file_sure_button, doc="点击'确定'")
        sleep(2)
        self.click(IBP.faqi_liucheng, doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IBP.faqiliucheng_list)
        project_name = self.get_element_text(IBP.suoshuxiangmu, doc="获取'所属项目'名称")
        state = self.get_element_text(IBP.wushenren_approvestate, doc="获取'五审'状态")
        return num_1, num_2, project_name, state

    def wushenren_loginapprove(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IBP.b_needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IBP.b_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def wushenren_loginapprove2(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IBP.b_needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IBP.b_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def wushenren_approvesucess(self):
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IBP.b_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IBP.b_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IBP.b_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IBP.b_all_pass,doc="点击'全部通过'")
        self.click(IBP.b_wushen_sure,doc="点击'确定'")
        self.click(IBP.b_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IBP.b_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IBP.b_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IBP.b_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IBP.b_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_tuihuisucess(self):
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IBP.b_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        self.click(IBP.b_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IBP.b_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IBP.b_all_tuihui,doc="点击'全部退回'")
        self.click(IBP.b_wushen_sure,doc="点击'确定'")
        self.click(IBP.b_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IBP.b_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IBP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IBP.b_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IBP.b_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IBP.b_dealed_wushen_state,doc="获取'已处理'五审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def faqiren_check_returedproject2(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        sleep(4)
        faqi_jiaoshenname = self.get_element_text(IBP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IBP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IBP.b_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IBP.b_faqi_liushen_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def faqiren_check_returedproject25(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        sleep(4)
        faqi_jiaoshenname = self.get_element_text(IBP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IBP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IBP.b_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IBP.b_faqi_liushen_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def faqiren_check_returedproject26(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        sleep(4)
        faqi_jiaoshenname = self.get_element_text(IBP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IBP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_liushen_state = self.get_element_text(IBP.b_faqi_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_liushen_state

    def sureperson_check_returedproject(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        self.click(IBP.b_needdeal_button, doc="点击'待处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IBP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IBP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IBP.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IBP.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IBP.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IBP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state

    def sureperson_faqiqueren_suc(self):
        self.click(IBP.b_needdeal_button, doc="点击'待处理'")
        sleep(8)
        self.click(IBP.sfile, doc="点击'01设计输入资料'")
        self.click(IBP.s_surebutton, doc="点击'确认'")
        self.click(IBP.s_allpassbutton, doc="点击'全部通过'")
        self.click(IBP.s_sure_button, doc="点击'确定'按钮")
        sleep(2)
        self.click(IBP.b_dealed_button, doc="点击'已处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IBP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IBP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IBP.s_wushen_state,doc="获取五审状态")
        s_liushen_state = self.get_element_text(IBP.s_liushen_state,doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IBP.s_qishen_state,doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IBP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_liushen_state,s_qishen_state,s_sureperson_state


    def faqiren_faqisure_suc(self):
        self.click(IBP.bfile,doc="点击'01设计输入资料'")
        self.click(IBP.b_faqisure,doc="点击'发起确认'")
        self.click(IBP.b_faqi,doc="点击'发起按钮'")
        faqi_jiaoshenname = self.get_element_text(IBP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IBP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IBP.b_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IBP.b_faqi_liushen_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state



    def faqiren_check_returedproject2(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        faqi_jiaoshenname = self.get_element_text(IBP.b_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IBP.b_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IBP.b_faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IBP.b_faqi_liushen_state,doc="获取六审状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def delete_1(self):
        self.click(IBP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IBP.project_list_num)
        except:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IBP.delete1_loc, doc="删除'测试_变电工程'")
        self.click(IBP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IBP.delete_success, doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IBP.project_list_num)
        return num_1, num_2, success_text

    def delete_12(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IBP.project_list_num)
        except:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IBP.delete1_loc, doc="删除'测试_变电工程'")
        self.click(IBP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IBP.delete_success, doc="获取'删除成功'")
        sleep(4)
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IBP.project_list_num)
        return num_1, num_2, success_text


    def delete_2(self):
        self.click(IBP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IBP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IBP.project_list_num)
        except:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IBP.delete1_loc2, doc="删除'测试_变电工程2'")
        self.click(IBP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IBP.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IBP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IBP.project_list_num)
        return num_1, num_2, success_text

    def jixiao_manage4(self):
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.biandian_name,doc="点击'测试_变电工程'")
        self.click(IBP.faqi_shenpi,doc="点击'发起审批'")
        self.click(IBP.box_pifu,doc="点击'前期阶段批复意见'")
        self.click(IBP.sure,doc="点击'确定按钮'")
        self.click(IBP.file_name,doc="点击'第一个卷册名称'")
        self.click(IBP.submit_approve,doc="点击'提交审批'")
        self.click(IBP.hanzheng12,doc="勾选'韩正'")
        self.click(IBP.chooseperson_sure,doc="点击'确定'")
        text_1 = self.get_element_text(IBP.success_info,doc="获取成功提示语")
        text_2 = self.get_element_text(IBP.apply_cancle,doc="获取取消申请")
        return text_1,text_2



    def wushenren_loginapprove11(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.mywork_loc,doc="点击'我的工作'")
        self.click(IBP.jiaoshen_loc,doc="点击'校审'")
        self.click(IBP.b_needdeal_button,doc="点击'待处理'")
        sleep(4)
        self.click(IBP.b_file, doc="点击'01-设计输入资料'进入详情")
        self.click(IBP.b_sure_button, doc="点击'确认'进入审批详情")
        self.click(IBP.b_all_pass, doc="点击'全部通过'")
        self.click(IBP.b_wushen_sure, doc="点击'确定'")
        sleep(3)
        self.click(IBP.b_dealed_button, doc="点击'已处理'")
        sleep(5)
        dealed_jiaoshen_name = self.get_element_text(IBP.b_dealed_jiaoshen_name, doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IBP.b_dealed_suoshu_project, doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IBP.b_dealed_sure_state, doc="获取'已处理'确认人状态")
        return dealed_jiaoshen_name, dealed_suoshu_project, dealed_wushen_state

    def hanzheng_logincheck00(self,name,password):
        self.click(IBP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IBP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IBP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IBP.jianguan, doc="点击'我监管的'")
        self.click(IBP.route_project, doc="点击'项目名称'")
        sleep(1)
        self.click(IBP.file_01,doc="点击01设计输入资料")
        self.click(IBP.edit_button, doc="点击编辑按钮")
        self.click(IBP.i_know, doc="点击我知道了")
        self.click(IBP.edit_xishu_button, doc="点击系数调整按钮")
        self.input_text(IBP.xishu_input, "10", doc="系数调整输入框输入10")
        self.click(IBP.sure_button_xishu, doc="点击确定按钮")
        text = self.get_element_text(IBP.prom_info, doc="获取提示语")
        sleep(3)
        self.click(IBP.cancle_button_xishu, doc="点击取消按钮")
        self.clear_text(IBP.man_input,doc="清空输入框")
        self.input_text(IBP.man_input,"100",doc="输入框输入100")
        self.click(IBP.save_data_button,doc="点击保存数据按钮")
        text_2 = self.get_element_text(IBP.prom_info, doc="获取提示语")
        return text,text_2














