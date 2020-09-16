from PageLocators.route_locator import  IndexRoutePageLocator as IRP
from PageLocators.login_page_locator import LoginPageLocator as LP
from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
class IndexRoutePage(BasePage):
    # '线路工程'特殊字段
    def check_route_field(self):
        self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IRP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IRP.projecttype_checkbox,doc='选择项目类型')
        self.click(IRP.routeproject_loc,doc="项目类型选择'线路工程'")
        self.click(IRP.consult_choose_box,doc="点击建设性质选择框")
        # 返回'工程类型'字段 '建设性质'字段
        return self.get_element_text(IRP.projecttypechoice_loc,doc="获取工程类型选项"),\
               self.get_element_text(IRP.consult_xingzhi,doc="获取建设性质所有选项")

    def create_route_project(self,projectname,projectno):
        self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        self.click(IRP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IRP.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IRP.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IRP.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IRP.routeproject_loc,doc="选择'线路工程'")
        self.click(IRP.jiakong,doc="勾选'架空'")
        self.click(IRP.design_box,doc="设计阶段下拉框")
        self.click(IRP.shigongtu,doc="设计阶段选择施工图")
        self.click(IRP.dianya_choose_box,doc="电压等级下拉框")
        self.click(IRP.kv35,doc="电压等级选择35kv")
        self.click(IRP.consult_choose_box,doc="建设性质下拉框")
        self.click(IRP.xinban,doc="新版绩效建设性质")
        self.click(IRP.choose_member,doc="点击'选择成员'")
        self.click(IRP.shezong,doc="点击'设总'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.input_text(IRP.name_input,"张无忌",doc="输入'张无忌'")
        self.input_text(IRP.name_input, Keys.ENTER)
        self.click(IRP.zhangwuji_gouxuan,doc="勾选张无忌")
        self.click(IRP.sure_button,doc="点击'确定'按钮")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.haiqing_chooose,doc="勾选海清")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.zonggong,doc="点击'总工'")
        self.click(IRP.add_member,doc="点击'添加成员'")
        self.click(IRP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IRP.xuhonglei, doc="勾选徐鸿磊")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.setnode_button,doc="点击'设置节点'")
        self.click(IRP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IRP.design_input,doc="点击'01-设计输入资料--选择'")
        self.click(IRP.design_choice2,doc="勾选'海清'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.clear_text(IRP.design_cost,doc="清出设计费默认值")
        self.input_text(IRP.design_cost,"50",doc="设计费输入50")
        self.click(IRP.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IRP.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IRP.start_time,doc="点击'开始时间'")
        self.click(IRP.start_time_sure,doc="点击'确定'")
        self.click(IRP.end_time,doc="点击'结束时间'")
        self.click(IRP.end_time_sure,doc="点击'确定'")
        self.click(IRP.create_button,doc="点击'创建'")
        sleep(3)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IRP.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_route_project33(self, projectname, projectno):
        # self.click(IRP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc, doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        self.click(IRP.addproject_loc, doc="首页_点击'添加项目'")
        self.input_text(IRP.projectname_loc, projectname, doc="输入'项目名称'")
        self.input_text(IRP.projectno_loc, projectno, doc="输入'项目编号'")
        self.click(IRP.projecttype_checkbox, doc="点击项目类型下拉框")
        self.click(IRP.routeproject_loc, doc="选择'线路工程'")
        self.click(IRP.jiakong, doc="勾选'架空'")
        self.click(IRP.design_box, doc="设计阶段下拉框")
        self.click(IRP.shigongtu, doc="设计阶段选择施工图")
        self.click(IRP.dianya_choose_box, doc="电压等级下拉框")
        self.click(IRP.kv35, doc="电压等级选择35kv")
        self.click(IRP.consult_choose_box, doc="建设性质下拉框")
        self.click(IRP.xinban, doc="新版绩效建设性质")
        self.click(IRP.choose_member, doc="点击'选择成员'")
        self.click(IRP.shezong, doc="点击'设总'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.input_text(IRP.name_input, "张无忌", doc="输入'张无忌'")
        self.input_text(IRP.name_input, Keys.ENTER)
        self.click(IRP.zhangwuji_gouxuan, doc="勾选张无忌")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.haiqing_chooose, doc="勾选海清")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.zonggong, doc="点击'总工'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.hairuomeng_choose, doc="勾选'海若梦'")
        self.click(IRP.xuhonglei, doc="勾选徐鸿磊")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.setnode_button, doc="点击'设置节点'")
        self.click(IRP.input01_file, doc="勾选'01-设计输入资料'")
        self.click(IRP.design_input, doc="点击'01-设计输入资料--选择'")
        self.click(IRP.design_choice2, doc="勾选'海清'")
        self.click(IRP.water_sure_button, doc="点击'确定'")
        self.click(IRP.water_sure_button, doc="点击'确定'")
        self.clear_text(IRP.design_cost, doc="清出设计费默认值")
        self.input_text(IRP.design_cost, "50", doc="设计费输入50")
        self.click(IRP.shejijiaoshen, doc="勾选'设计校审'")
        self.click(IRP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IRP.null,doc="选择无")
        self.click(IRP.start_time, doc="点击'开始时间'")
        self.click(IRP.start_time_sure, doc="点击'确定'")
        self.click(IRP.end_time, doc="点击'结束时间'")
        self.click(IRP.end_time_sure, doc="点击'确定'")
        self.click(IRP.create_button, doc="点击'创建'")
        sleep(3)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IRP.first_project_name, doc="获取第一个项目名称")
        return num_text_1, num_text_2, project_name

    def create_route_project3(self,name,password,projectname,projectno):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        self.click(IRP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IRP.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IRP.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IRP.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IRP.routeproject_loc,doc="选择'线路工程'")
        self.click(IRP.jiakong,doc="勾选'架空'")
        self.click(IRP.design_box,doc="设计阶段下拉框")
        self.click(IRP.shigongtu,doc="设计阶段选择施工图")
        self.click(IRP.dianya_choose_box,doc="电压等级下拉框")
        self.click(IRP.kv35,doc="电压等级选择35kv")
        self.click(IRP.consult_choose_box,doc="建设性质下拉框")
        self.click(IRP.xinban,doc="新版绩效建设性质")
        self.click(IRP.choose_member,doc="点击'选择成员'")
        self.click(IRP.xinagmujingli,doc="点击'项目经理'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.zhengkai_chooose, doc="勾选'郑凯'")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.shezong,doc="点击'设总'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.longmeixin_choose,doc="勾选龙美心")
        self.click(IRP.haiqing_chooose,doc="勾选海清")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.zonggong,doc="点击'总工'")
        self.click(IRP.add_member,doc="点击'添加成员'")
        self.click(IRP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IRP.xuhonglei, doc="勾选徐鸿磊")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.setnode_button,doc="点击'设置节点'")
        self.click(IRP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IRP.design_input,doc="点击'01-设计输入资料--选择'")
        self.click(IRP.hairuomeng_choose2,doc="勾选'海若梦'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.clear_text(IRP.design_cost,doc="清出设计费默认值")
        self.input_text(IRP.design_cost,"50",doc="设计费输入50")
        self.click(IRP.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IRP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IRP.level_1,doc="选择1级别")
        self.click_by_js(IRP.diyubiaozhun,doc="可低于标准级别")
        self.click_by_js(IRP.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IRP.start_time,doc="点击'开始时间'")
        self.click(IRP.start_time_sure,doc="点击'确定'")
        self.click(IRP.end_time,doc="点击'结束时间'")
        self.click(IRP.end_time_sure,doc="点击'确定'")
        self.click(IRP.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IRP.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_route_project4(self,projectname,projectno):
        # self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        self.click(IRP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IRP.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IRP.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IRP.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IRP.routeproject_loc,doc="选择'线路工程'")
        self.click(IRP.jiakong,doc="勾选'架空'")
        self.click(IRP.design_box,doc="设计阶段下拉框")
        self.click(IRP.shigongtu,doc="设计阶段选择施工图")
        self.click(IRP.dianya_choose_box,doc="电压等级下拉框")
        self.click(IRP.kv35,doc="电压等级选择35kv")
        self.click(IRP.consult_choose_box,doc="建设性质下拉框")
        self.click(IRP.xinban,doc="新版绩效建设性质")
        self.click(IRP.choose_member,doc="点击'选择成员'")
        self.click(IRP.xinagmujingli,doc="点击'项目经理'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.zhengkai_chooose, doc="勾选'郑凯'")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.shezong,doc="点击'设总'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.longmeixin_choose,doc="勾选龙美心")
        self.click(IRP.haiqing_chooose,doc="勾选海清")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.zonggong,doc="点击'总工'")
        self.click(IRP.add_member,doc="点击'添加成员'")
        self.click(IRP.hairuomeng_choose,doc="勾选'海若梦'")
        self.click(IRP.xuhonglei, doc="勾选徐鸿磊")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.setnode_button,doc="点击'设置节点'")
        self.click(IRP.pifu04,doc="勾选'04前期阶段批复意见'")
        self.click(IRP.pifuchoose,doc="点击'04前期阶段批复意见--选择'")
        self.click(IRP.hairuomeng_choose2,doc="勾选'海若梦'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.click(IRP.design_input, doc="点击'01-设计输入资料--选择'")
        self.click(IRP.haiqing, doc="勾选'海清'")
        self.click(IRP.water_sure_button, doc="点击'确定'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.clear_text(IRP.design_cost,doc="清出设计费默认值")
        self.input_text(IRP.design_cost,"50",doc="设计费输入50")
        self.click(IRP.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IRP.jiaoshenlevel,doc="点击标准校审级别")
        self.click(IRP.level_1,doc="选择1级别")
        self.click_by_js(IRP.diyubiaozhun,doc="可低于标准级别")
        self.click_by_js(IRP.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IRP.start_time,doc="点击'开始时间'")
        self.click(IRP.start_time_sure,doc="点击'确定'")
        self.click(IRP.end_time,doc="点击'结束时间'")
        self.click(IRP.end_time_sure,doc="点击'确定'")
        self.click(IRP.create_button,doc="点击'创建'")
        sleep(5)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IRP.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def create_route_project2(self,projectname,projectno):
        sleep(1)
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_text_1 = 0
        except:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        self.click(IRP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IRP.projectname_loc,projectname,doc="输入'项目名称'")
        self.input_text(IRP.projectno_loc,projectno,doc="输入'项目编号'")
        self.click(IRP.projecttype_checkbox,doc="点击项目类型下拉框")
        self.click(IRP.routeproject_loc,doc="选择'线路工程'")
        self.click(IRP.jiakong,doc="勾选'架空'")
        self.click(IRP.design_box,doc="设计阶段下拉框")
        self.click(IRP.kexingxing_yanjiu,doc="设计阶段选择可行性研究")
        self.click(IRP.dianya_choose_box,doc="电压等级下拉框")
        self.click(IRP.kv110,doc="电压等级选择110kv")
        self.click(IRP.consult_choose_box,doc="建设性质下拉框")
        self.click(IRP.yitihua,doc="可研勘测设计一体化项目")
        self.click(IRP.choose_member,doc="点击'选择成员'")
        self.click(IRP.xianlu_shejiren,doc="点击'线路电器设计人'")
        self.click(IRP.add_member, doc="点击'添加成员'")
        self.click(IRP.wangzulan,doc="勾选王祖蓝")
        self.click(IRP.sunhonglei,doc="勾选孙红雷")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.sure_button, doc="点击'确定'按钮")
        self.click(IRP.setnode_button,doc="点击'设置节点'")
        self.click(IRP.input01_file,doc="勾选'01-设计输入资料'")
        self.click(IRP.design_input,doc="点击'01-设计输入资料--选择'")
        self.click(IRP.design_choice,doc="勾选'王祖蓝'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.click(IRP.water_sure_button,doc="点击'确定'")
        self.clear_text(IRP.design_cost,doc="清出设计费默认值")
        self.input_text(IRP.design_cost,"100",doc="设计费输入100")
        self.click(IRP.shejijiaoshen,doc="勾选'设计校审'")
        self.click(IRP.huiqianjieduan,doc="勾选'跳过会签'")
        self.click(IRP.biaozhunjibie,doc="勾选'可低于标准级别'")
        self.click(IRP.start_time,doc="点击'开始时间'")
        self.click(IRP.start_time_sure,doc="点击'确定'")
        self.click(IRP.end_time,doc="点击'结束时间'")
        self.click(IRP.end_time_sure,doc="点击'确定'")
        self.click(IRP.create_button,doc="点击'创建'")
        sleep(3)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        project_name = self.get_element_text(IRP.first_project_name,doc="获取第一个项目名称")
        return num_text_1,num_text_2,project_name

    def jixiaoguanli_1(self,name,password,rate):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi,doc="点击发起审批")
        self.click(IRP.yuzhi_gouxuan,doc="点击预支勾选框")
        self.clear_text(IRP.tibao_rate,doc="清空'填报比例输入框'")
        self.input_text(IRP.tibao_rate,rate,doc="输入提报比例")
        self.click(IRP.tibao_sure,doc="点击确定")
        self.click(IRP.tibaobili_link,doc="点击提报比例按钮")
        tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        self.click(IRP.tijiao_shenpi,doc="点击提交审批")
        self.click(IRP.hanzheng1,doc="勾选韩正")
        self.click(IRP.sure,doc="点击确定")
        success = self.get_element_text(IRP.success,doc="成功 文本")
        shenpi_liuhen = self.get_element_text(IRP.shenpi_liuhen,doc="审批留痕 文本")
        return tibaobili,zhuanyezhanbi,project_biaozhungongri,tibao_days,success,shenpi_liuhen

    def jixiaoguanli_19(self,rate):
        self.click(IRP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc, doc="点击绩效管理")
        self.click(IRP.xianlu, doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi, doc="点击发起审批")
        self.click(IRP.yuzhi_gouxuan, doc="点击预支勾选框")
        self.clear_text(IRP.tibao_rate, doc="清空'填报比例输入框'")
        self.input_text(IRP.tibao_rate, rate, doc="输入提报比例")
        self.click(IRP.tibao_sure, doc="点击确定")
        self.click(IRP.tibaobili_link, doc="点击提报比例按钮")
        self.click(IRP.edit_button,doc="点击编辑按钮")
        self.click(IRP.edit_xishu_button,doc="点击系数调整按钮")
        self.input_text(IRP.xishu_input,"10",doc="系数调整输入框输入10")
        self.click(IRP.sure_button_xishu,doc="点击确定按钮")
        text = self.get_element_text(IRP.prom_info,doc="获取提示语")
        self.click(IRP.cancle_button_xishu,doc="点击取消按钮")
        self.click(IRP.cancle_edit_button,doc="点击退出编辑按钮")
        self.click(IRP.tijiao_shenpi,doc="点击提交审批")
        self.click(IRP.hanzheng1,doc="勾选韩正")
        self.click(IRP.sure,doc="点击确定")
        return text


    def jixiaoguanli_11(self):
        self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi,doc="点击发起审批")
        # self.click(IRP.yuzhi_gouxuan,doc="点击预支勾选框")
        # self.clear_text(IRP.tibao_rate,doc="清空'填报比例输入框'")
        # self.input_text(IRP.tibao_rate,rate,doc="输入提报比例")
        self.click(IRP.tibao_sure,doc="点击确定")
        self.click(IRP.tibaobili_link,doc="点击提报比例按钮")
        sleep(6)
        tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        # chengpin = self.get_element_text(IRP.chengpinzhiliang, doc="提取成品质量系数")
        project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        # if chengpin != '成品质量系数： 项目经理：1.01、电气：1.01、结构：1.01' \
        #         and project_biaozhungongri != '411.9 （基本工日：315.32考核工日：96.58）' \
        #         and tibao_days != '411.9 （基本工日：315.32 考核工日：96.58）':
        #     chengpin = self.get_element_text(IRP.chengpinzhiliang, doc="提取成品质量系数")
        #     project_biaozhungongri = self.get_element_text(IRP.biaozhun_days, doc="提取项目标准工日")
        #     tibao_days = self.get_element_text(IRP.tibao_days, doc="提取提报工日")
        return tibaobili,zhuanyezhanbi,project_biaozhungongri,tibao_days


    def jixiaoguanli_33(self):
        # self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi,doc="点击发起审批")
        self.click(IRP.tibao_sure,doc="点击确定")
        self.click(IRP.tibaobili_link,doc="点击提报比例按钮")
        sleep(4)
        tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        return tibaobili,zhuanyezhanbi,project_biaozhungongri,tibao_days

    def jixiaoguanli_36(self):
        self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.tibaobili_link,doc="点击提报比例按钮")
        sleep(10)
        # self.click(IRP.refresh,doc="点击更新按钮")
        # self.click(IRP.tongbugengxin,doc="勾选同步更新")
        # sleep(10)
        # self.click(IRP.refresh_sure,doc="点击确定按钮")
        # sleep(10)
        tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        # chengpin = self.get_element_text(IRP.chengpinzhiliang,doc="提取成品质量系数")
        project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        # if chengpin != '成品质量系数： 项目经理：1.01、电气：1.01、结构：0.0' \
        #         and project_biaozhungongri != '213.04 （基本工日：176.12考核工日：36.92）' \
        #         and tibao_days != '213.04 （基本工日：176.12 考核工日：36.92）':
        #     self.driver.refresh()
        #     sleep(4)
        #     chengpin = self.get_element_text(IRP.chengpinzhiliang, doc="提取成品质量系数")
        #     project_biaozhungongri = self.get_element_text(IRP.biaozhun_days, doc="提取项目标准工日")
        #     tibao_days = self.get_element_text(IRP.tibao_days, doc="提取提报工日")
        return tibaobili,zhuanyezhanbi,project_biaozhungongri,tibao_days

    def jixiaoguanli_34(self,name,password):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc, doc="点击绩效管理")
        self.click(IRP.xianlu, doc="点击线路工程名称")
        self.click(IRP.tibaobili_link, doc="点击提报比例按钮")
        tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        # chengpin = self.get_element_text(IRP.chengpinzhiliang,doc="提取成品质量系数")
        project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        return tibaobili,zhuanyezhanbi,project_biaozhungongri,tibao_days


    def hanzheng_logincheck(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        sleep(3)
        s_project_name = self.get_element_text(IRP.s_projectname,doc="获取'项目名称'")
        s_tibao = self.get_element_text(IRP.s_rate,doc="获取'提报比例'")
        s_approve_state = self.get_element_text(IRP.s_approve_state,doc="获取'审批状态'")
        s_time = self.get_element_text(IRP.s_pass_time,doc="获取'审批时间'")
        self.click(IRP.jianguan,doc="点击'我监管的'")
        sleep(3)
        j_project_name = self.get_element_text(IRP.j_projectname,doc="获取'项目名称'")
        j_tibao = self.get_element_text(IRP.j_rate,doc="获取'提报比例'")
        j_approve_state = self.get_element_text(IRP.j_approve_state,doc="获取'审批状态'")
        j_time = self.get_element_text(IRP.j_pass_time,doc="获取'审批时间'")
        return s_project_name,s_tibao,s_approve_state,s_time,j_project_name,j_tibao,j_approve_state,j_time

    def hanzheng_logincheck00(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jianguan, doc="点击'我监管的'")
        self.click(IRP.route_project, doc="点击'项目名称'")
        sleep(1)
        self.click(IRP.tibaobili_link_shen, doc="点击'提报比例'")
        self.click(IRP.edit_button, doc="点击编辑按钮")
        self.click(IRP.i_know, doc="点击我知道了")
        self.click(IRP.edit_xishu_button, doc="点击系数调整按钮")
        self.input_text(IRP.xishu_input, "10", doc="系数调整输入框输入10")
        self.click(IRP.sure_button_xishu, doc="点击确定按钮")
        text = self.get_element_text(IRP.prom_info, doc="获取提示语")
        sleep(3)
        self.click(IRP.cancle_button_xishu, doc="点击取消按钮")
        self.clear_text(IRP.man_input,doc="清空输入框")
        self.input_text(IRP.man_input,"100",doc="输入框输入100")
        self.click(IRP.save_data_button,doc="点击保存数据按钮")
        text_2 = self.get_element_text(IRP.prom_info, doc="获取提示语")
        return text,text_2




    def hanzheng_approvesuccess(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jianguan,doc="点击'我监管的'")
        self.click(IRP.route_project,doc="点击'项目名称'")
        sleep(1)
        self.click(IRP.tibaobili_link_shen,doc="点击'提报比例'")
        self.click(IRP.pass_button,doc="点击'通过'")
        self.click(IRP.pass_sure,doc="点击'确定'")
        success = self.get_element_text(IRP.j_pass_success, doc="获取'成功'")
        sleep(2)
        project_name = self.get_element_text(IRP.j_projectname,doc="获取'项目名称'")
        tibao = self.get_element_text(IRP.j_rate,doc="获取'提报比例'")
        approve_state = self.get_element_text(IRP.j_approve_state, doc="获取'审批状态'")
        time = self.get_element_text(IRP.j_pass_time,doc="获取'审批时间'")
        self.click(IRP.my_approve, doc="点击'我审批的'")
        sleep(3)
        now_date = self.get_date()
        s_projectnames = self.get_elements_text_value(IRP.s_all_datas, doc="'我审批的'列表所有数据")
        return project_name,tibao,success,time,approve_state,now_date,s_projectnames

    def hanzheng_approvesuccess2(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jianguan,doc="点击'我监管的'")
        sleep(3)
        self.click(IRP.route_project,doc="点击'项目名称'")
        sleep(1)
        self.click(IRP.tibaobili_link_shen,doc="点击'提报比例'")
        self.click(IRP.pass_button,doc="点击'通过'")
        self.click(IRP.pass_sure,doc="点击'确定'")
        sleep(1)
        success = self.get_element_text(IRP.j_pass_success, doc="获取'成功'")
        sleep(2)
        project_name = self.get_element_text(IRP.j_projectname,doc="获取'项目名称'")
        tibao = self.get_element_text(IRP.j_rate,doc="获取'提报比例'")
        approve_state = self.get_element_text(IRP.j_approve_state, doc="获取'审批状态'")
        time = self.get_element_text(IRP.j_pass_time,doc="获取'审批时间'")
        self.click(IRP.my_approve, doc="点击'我审批的'")
        sleep(3)
        now_date = self.get_date()
        s_projectnames = self.get_elements_text_value(IRP.s_all_datas, doc="'我审批的'列表所有数据")
        return project_name,tibao,success,time,approve_state,now_date,s_projectnames

    def hanzheng_approvesuccess3(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jianguan,doc="点击'我监管的'")
        sleep(3)
        self.click(IRP.route_project,doc="点击'项目名称'")
        sleep(1)
        self.click(IRP.tibaobili_link_shen,doc="点击'提报比例'")
        self.click(IRP.pass_button,doc="点击'通过'")
        self.click(IRP.pass_sure,doc="点击'确定'")
        sleep(1)
        success = self.get_element_text(IRP.j_pass_success, doc="获取'成功'")
        sleep(4)
        project_name = self.get_element_text(IRP.j_projectname,doc="获取'项目名称'")
        tibao = self.get_element_text(IRP.j_rate,doc="获取'提报比例'")
        approve_state = self.get_element_text(IRP.j_approve_state, doc="获取'审批状态'")
        time = self.get_element_text(IRP.j_pass_time,doc="获取'审批时间'")
        self.click(IRP.my_approve, doc="点击'我审批的'")
        now_date = self.get_date()
        s_projectnames = self.get_elements_text_value(IRP.s_all_datas, doc="'我审批的'列表所有数据")
        return project_name,tibao,success,time,approve_state,now_date,s_projectnames

    def jixiaoguanli_2(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi,doc="点击发起审批")
        sleep(4)
        tibao = self.get_default_value(IRP.second_rate,doc="获取第二次默认提报比例")
        shuxingzhi = self.get_element_attribute(IRP.secondrate,'disabled')
        self.click(IRP.tibao_sure, doc="点击确定")
        self.click(IRP.tibaobili_link, doc="点击提报比例按钮")
        self.click(IRP.tijiao_shenpi,doc="点击提交审批")
        self.click(IRP.hanzheng1,doc="勾选韩正")
        self.click(IRP.sure,doc="点击确定")
        return tibao,shuxingzhi

    def hanzheng_approvesuccess2(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jianguan,doc="点击'我监管的'")
        sleep(3)
        self.click(IRP.route_project,doc="点击'项目名称'")
        sleep(1)
        self.click(IRP.tibaobili_link_shen,doc="点击'提报比例'")
        self.click(IRP.pass_button,doc="点击'通过'")
        self.click(IRP.pass_sure,doc="点击'确定'")
        sleep(2)
        success = self.get_element_text(IRP.j_pass_success, doc="获取'成功'")
        now_date = self.get_date()
        project_name = self.get_element_text(IRP.j_projectname,doc="获取'项目名称'")
        tibao = self.get_element_text(IRP.j_rate,doc="获取'提报比例'")
        approve_state = self.get_element_text(IRP.j_approve_state, doc="获取'审批状态'")
        time = self.get_element_text(IRP.j_pass_time,doc="获取'审批时间'")
        self.click(IRP.my_approve, doc="点击'我审批的'")
        s_projectnames = self.get_elements_text_value(IRP.s_all_datas, doc="'我审批的'列表所有数据")
        return project_name,tibao,success,time,approve_state,now_date,s_projectnames

    def jixiaoguanli_3(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        sleep(3)
        try:
            self.click(IRP.faqi_shenpi,doc="点击发起审批")
        except:
            text = "没有发起审批按钮"
            return text

    def faqijiaoshen(self):
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IRP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IRP.faqiliucheng_list)
        self.click(IRP.faqiliucheng,doc="点击'发起流程'")
        self.click(IRP.project_choose,doc="选择项目")
        self.click(IRP.r_choose_routeproject,doc="选择'线路工程'")
        self.click(IRP.project_sure_button,doc="点击'确定'")
        self.click(IRP.choose_file_button,doc="点击'选择卷则'")
        self.click(IRP.input_file,doc="勾选01设计输入资料")
        self.click(IRP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IRP.surebutton,doc="点击'确定'")
        self.click(IRP.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IRP.time_sure,doc="点击'确定'")
        self.click(IRP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IRP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IRP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IRP.haiqing_choose_new,doc="选择'海清'")
        self.click(IRP.person_sure_button,doc="点击'确定'")
        self.click(IRP.huiqian_new,doc="跳过'会签'")
        self.click(IRP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IRP.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IRP.wushen_sure_button,doc="点击'确定'")
        self.click(IRP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IRP.upload_file,doc="点击'上传文件按钮'")
        sleep(2)
        self.input_text_uploadfile(IRP.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IRP.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IRP.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IRP.faqiliucheng_list)
        project_name = self.get_element_text(IRP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IRP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen11(self,name,password):
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IRP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IRP.faqiliucheng_list)
        self.click(IRP.faqiliucheng,doc="点击'发起流程'")
        self.click(IRP.project_choose,doc="选择项目")
        self.click(IRP.r_choose_routeproject,doc="选择'线路工程'")
        self.click(IRP.project_sure_button,doc="点击'确定'")
        self.click(IRP.choose_file_button,doc="点击'选择卷则'")
        self.click(IRP.input_file,doc="勾选01设计输入资料")
        self.click(IRP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IRP.surebutton,doc="点击'确定'")
        self.click(IRP.plan_finish_time,doc="点击'计划完成时间'")
        self.click(IRP.time_sure,doc="点击'确定'")
        self.click(IRP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IRP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IRP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IRP.haiqing_choose,doc="选择'海清'")
        self.click(IRP.person_sure_button,doc="点击'确定'")
        self.click(IRP.huiqian,doc="跳过'会签'")
        self.click(IRP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IRP.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IRP.wushen_sure_button,doc="点击'确定'")
        self.click(IRP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IRP.upload_file,doc="点击'上传文件按钮'")
        sleep(2)
        self.input_text_uploadfile(IRP.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IRP.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IRP.faqi_liucheng,doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IRP.faqiliucheng_list)
        project_name = self.get_element_text(IRP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IRP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen77(self, name, password):
        self.input_text(LP.user_loc, name, doc="输入用户名")
        self.input_text(LP.password_loc, password, doc="输入密码")
        self.click(LP.login_button_loc, doc="登陆")
        self.click(IRP.mywork_loc, doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc, doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IRP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IRP.faqiliucheng_list)
        self.click(IRP.faqiliucheng, doc="点击'发起流程'")
        self.click(IRP.project_choose, doc="选择项目")
        self.click(IRP.r_choose_routeproject, doc="选择'线路工程'")
        self.click(IRP.project_sure_button, doc="点击'确定'")
        self.click(IRP.choose_file_button, doc="点击'选择卷则'")
        self.click(IRP.input_file, doc="勾选01设计输入资料")
        self.click(IRP.tongbujiaoshen_gouxuan, doc="勾选同步校审")
        self.click(IRP.surebutton, doc="点击'确定'")
        self.click(IRP.plan_finish_time, doc="点击'计划完成时间'")
        self.click(IRP.time_sure, doc="点击'确定'")
        self.click(IRP.jishenshuoming, doc="点击'校审说明'")
        self.input_text(IRP.jishenshuoming, "风月同天", doc="输入文本值")
        self.click(IRP.sureperson_choose, doc="点击'确认人选择'")
        self.click(IRP.haiqing_choose, doc="选择'海清'")
        self.click(IRP.person_sure_button, doc="点击'确定'")
        self.click(IRP.jiaoshenfile_add, doc="添加校审文件")
        self.click(IRP.upload_file, doc="点击'上传文件按钮'")
        sleep(2)
        self.input_text_uploadfile(IRP.uploadfile_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IRP.file_sure_button, doc="点击'确定'")
        sleep(2)
        self.click(IRP.faqi_liucheng, doc="发起流程")
        sleep(6)
        num_2 = self.get_list_length(IRP.faqiliucheng_list)
        project_name = self.get_element_text(IRP.suoshuxiangmu, doc="获取'所属项目'名称")
        state = self.get_element_text(IRP.sure_state, doc="获取'确认人'状态")
        return num_1, num_2, project_name, state


    def faqijiaoshen7(self):
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IRP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IRP.faqiliucheng_list)
        self.click(IRP.faqiliucheng,doc="点击'发起流程'")
        self.click(IRP.project_choose,doc="选择项目")
        self.click(IRP.r_choose_routeproject,doc="选择'线路工程'")
        self.click(IRP.project_sure_button,doc="点击'确定'")
        self.click(IRP.choose_file_button,doc="点击'选择卷则'")
        self.click(IRP.input_file,doc="勾选01设计输入资料")
        self.click(IRP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IRP.surebutton,doc="点击'确定'")
        self.click(IRP.plan_finish_time, doc="点击'计划完成时间'")
        current_month = self.get_element_text(IRP.current_month, doc="获取当前月份")
        future_date = self.future_oneday(1).split("-")[-1]
        if int(future_date) < 10:
            future_date = future_date[-1]
            print(future_date)
        if int(self.future_oneday(5)[5:7]) > int(current_month[0:2]):
            self.click(IRP.lastmonth, doc="切换至下一月份")
        locator = '//span[text()="{}"]'.format(future_date)
        date_loc = (By.XPATH, locator)
        self.click(date_loc, doc="点击时间")
        self.click(IRP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IRP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IRP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IRP.longmeixin,doc="确认人选择'龙美心'")
        self.click(IRP.person_sure_button,doc="点击'确定'")
        self.click(IRP.huiqian_new,doc="跳过'会签'")
        self.click(IRP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IRP.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IRP.wushen_sure_button,doc="点击'确定'")
        self.click(IRP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IRP.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IRP.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IRP.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IRP.faqi_liucheng,doc="发起流程")
        sleep(5)
        num_2 = self.get_list_length(IRP.faqiliucheng_list)
        project_name = self.get_element_text(IRP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IRP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqijiaoshen8(self):
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IRP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IRP.faqiliucheng_list)
        self.click(IRP.faqiliucheng,doc="点击'发起流程'")
        self.click(IRP.project_choose,doc="选择项目")
        self.click(IRP.r_choose_routeproject,doc="选择'线路工程'")
        self.click(IRP.project_sure_button,doc="点击'确定'")
        self.click(IRP.choose_file_button,doc="点击'选择卷则'")
        self.click(IRP.pifuyijian,doc="勾选04-前期阶段批复意见")
        self.click(IRP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IRP.surebutton,doc="点击'确定'")
        self.click(IRP.plan_finish_time, doc="点击'计划完成时间'")
        current_month = self.get_element_text(IRP.current_month, doc="获取当前月份")
        future_date = self.future_oneday(1).split("-")[-1]
        if int(future_date) < 10:
            future_date = future_date[-1]
            print(future_date)
        if int(self.future_oneday(5)[5:7]) > int(current_month[0:2]):
            self.click(IRP.lastmonth, doc="切换至下一月份")
        locator = '//span[text()="{}"]'.format(future_date)
        date_loc = (By.XPATH, locator)
        self.click(date_loc, doc="点击时间")
        self.click(IRP.jishenshuoming,doc="点击'校审说明'")
        self.input_text(IRP.jishenshuoming,"风月同天",doc="输入文本值")
        self.click(IRP.sureperson_choose,doc="点击'确认人选择'")
        self.click(IRP.longmeixin,doc="确认人选择'龙美心'")
        self.click(IRP.person_sure_button,doc="点击'确定'")
        self.click(IRP.huiqian_new,doc="跳过'会签'")
        self.click(IRP.wushen_choosebutton,doc="选择'五审人'")
        self.click(IRP.wushenhairuomeng_choose,doc="五审'海若梦'")
        self.click(IRP.wushen_sure_button,doc="点击'确定'")
        self.click(IRP.jiaoshenfile_add,doc="添加校审文件")
        self.click(IRP.upload_file,doc="点击'上传文件按钮'")
        self.input_text_uploadfile(IRP.uploadfile_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IRP.file_sure_button,doc="点击'确定'")
        sleep(2)
        self.click(IRP.faqi_liucheng,doc="发起流程")
        sleep(4)
        num_2 = self.get_list_length(IRP.faqiliucheng_list)
        project_name = self.get_element_text(IRP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IRP.wushenren_approvestate,doc="获取'五审'状态")
        return num_1,num_2,project_name,state



    def wushenren_loginapprove(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        needdealproject_name = self.get_element_text(IRP.w_needdeal_projectname,doc="获取待处理'项目名称'")
        surp_state = self.get_element_text(IRP.w_sure,doc="获取确认人审批状态")
        return needdealproject_name,surp_state

    def wushenren_loginapproveee(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        needdealproject_name = self.get_element_text(IRP.w_needdeal_projectname,doc="获取待处理'项目名称'")
        w_state = self.get_element_text(IRP.w_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,w_state

    def wushenren_loginapprove_nn(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        needdealproject_name = self.get_element_text(IRP.w_needdeal_projectname,doc="获取待处理'项目名称'")
        wu_state = self.get_element_text(IRP.w_wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wu_state

    def wushenren_loginapprove_b(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        needdealproject_name = self.get_element_text(IRP.w_needdeal_projectname,doc="获取待处理'项目名称'")
        wu_state = self.get_element_text(IRP.w_wushenren_approvestate,doc="获取确认人审批状态")
        return needdealproject_name,wu_state

    def wushenren_loginapprove88(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        needdealproject_name = self.get_element_text(IRP.w_needdeal_projectname,doc="获取待处理'项目名称'")
        wu_state = self.get_element_text(IRP.w_wushenren_approvestate,doc="获取确认人审批状态")
        return needdealproject_name,wu_state

    def wushenren_approvesucess(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        self.click(IRP.w_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IRP.w_sure_button,doc="点击'五审'进入审批详情")
        self.click(IRP.w_all_pass,doc="点击'全部通过'")
        self.click(IRP.w_wushen_sure,doc="点击'确定'")
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IRP.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IRP.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IRP.w_dealed_wushen_state,doc="获取'已处理'确认状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_approvesucess001(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        self.click(IRP.w_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IRP.w_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IRP.w_all_pass,doc="点击'全部通过'")
        self.click(IRP.w_wushen_sure,doc="点击'确定'")
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IRP.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IRP.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IRP.w_dealed_wushen_state,doc="获取'已处理'确认状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_approvesucess_ab(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        self.click(IRP.w_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IRP.w_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IRP.w_all_pass,doc="点击'全部通过'")
        self.click(IRP.w_wushen_sure,doc="点击'确定'")
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IRP.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IRP.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IRP.w_dealed_wushen_state,doc="获取'已处理'确认状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_approvesucess_320(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        self.click(IRP.w_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IRP.w_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IRP.w_all_pass,doc="点击'全部通过'")
        self.click(IRP.w_wushen_sure,doc="点击'确定'")
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IRP.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IRP.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IRP.w_dealed_wushen_state,doc="获取'已处理'确认状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state

    def wushenren_approvesucess_a(self):
        # self.click(IRP.ph_logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        self.click(IRP.w_file,doc="点击'01-设计输入资料'进入详情")
        self.click(IRP.w_wushen_button,doc="点击'五审'进入审批详情")
        self.click(IRP.w_all_pass,doc="点击'全部通过'")
        self.click(IRP.w_wushen_sure,doc="点击'确定'")
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_3 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IRP.w_dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IRP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IRP.w_dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IRP.w_dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IRP.w_dealed_wushen_state,doc="获取'已处理'确认状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state


    def faqiren_faqisure_suc(self):
        self.click(IRP.bfile,doc="点击'01设计输入资料'")
        self.click(IRP.b_faqisure,doc="点击'发起确认'")
        self.click(IRP.b_faqi,doc="点击'发起按钮'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IRP.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IRP.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IRP.w_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IRP.w_faqi_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state

    def faqiren_faqisure_suc2(self):
        self.click(IRP.bfile2,doc="点击'04-前期阶段批复意见'")
        self.click(IRP.b_faqisure,doc="点击'发起确认'")
        self.click(IRP.b_faqi,doc="点击'发起按钮'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IRP.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IRP.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IRP.w_faqi_wushen_state,doc="获取五审状态")
        faqi_sure_state = self.get_element_text(IRP.w_faqi_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_sure_state

    def sureren_checksuc(self, name, password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        self.click(IRP.w_needdeal_button,doc="点击'待处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IRP.s_jiaoshenmingcheng, doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IRP.s_suoshuxiangmu, doc="获取所属项目")
        s_wushen_state = self.get_element_text(IRP.s_wushen_state, doc="获取五审状态")
        s_liushen_state = self.get_element_text(IRP.s_liushen_state, doc="获取六审人状态")
        s_qishen_state = self.get_element_text(IRP.s_qishen_state, doc="获取七审人状态")
        s_sureperson_state = self.get_element_text(IRP.s_sure_state, doc="获取确认人状态")
        return s_jiaoshenname, s_suoshuproject, s_wushen_state, s_liushen_state, s_qishen_state, s_sureperson_state

    def sureperson_faqiqueren_suc(self):
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        self.click(IRP.sfile, doc="点击'01设计输入资料'")
        self.click(IRP.s_surebutton, doc="点击'确认'")
        self.click(IRP.s_allpassbutton, doc="点击'全部通过'")
        self.click(IRP.s_sure_button, doc="点击'确定'按钮")
        sleep(2)
        self.click(IRP.w_dealed_button, doc="点击'已处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IRP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IRP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IRP.s_wushen_state,doc="获取五审状态")
        s_sureperson_state = self.get_element_text(IRP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_sureperson_state

    def sureperson_faqiqueren_suc2(self):
        self.click(IRP.w_needdeal_button, doc="点击'待处理'")
        self.click(IRP.sfile2, doc="点击'04-前期阶段批复意见'")
        self.click(IRP.s_surebutton, doc="点击'确认'")
        self.click(IRP.s_allpassbutton, doc="点击'全部通过'")
        self.click(IRP.s_sure_button, doc="点击'确定'按钮")
        sleep(2)
        self.click(IRP.w_dealed_button, doc="点击'已处理'")
        sleep(8)
        s_jiaoshenname = self.get_element_text(IRP.s_jiaoshenmingcheng,doc="获取校审名称")
        s_suoshuproject = self.get_element_text(IRP.s_suoshuxiangmu,doc="获取所属项目")
        s_wushen_state = self.get_element_text(IRP.s_wushen_state,doc="获取五审状态")
        s_sureperson_state = self.get_element_text(IRP.s_sure_state,doc="获取确认人状态")
        return s_jiaoshenname,s_suoshuproject,s_wushen_state,s_sureperson_state

    def faqiren_check_returedproject(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(5)
        faqi_jiaoshenname = self.get_element_text(IRP.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IRP.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IRP.w_faqi_wushen_state,doc="获取五审状态")
        faqi_queren_state = self.get_element_text(IRP.w_faqi_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_queren_state

    def faqiren_check_returedproject55(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(5)
        faqi_jiaoshenname = self.get_element_text(IRP.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IRP.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_queren_state = self.get_element_text(IRP.w_faqi_sure_state2,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_queren_state

    def faqiren_check_returedproject2(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jixiaotongji_loc,doc="点击'绩效统计'")
        self.click(IRP.jixiaotongji_gouxuan,doc="绩效统计统计勾选")
        self.click(IRP.jixiao_sure,doc="绩效勾选确定")
        sleep(3)
        zongji = self.get_element_text(IRP.zongji,doc="获取总计工日")
        gongcheng_jixiao = self.get_element_text(IRP.gongcheng_jixiao,doc="获取工程绩效")
        return zongji,gongcheng_jixiao

    def faqiren_check_returedproject35(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.mywork_loc,doc="点击'我的工作'")
        self.click(IRP.jiaoshen_loc,doc="点击'校审'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IRP.w_faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IRP.w_faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IRP.w_faqi_wushen_state,doc="获取五审状态")
        faqi_queren_state = self.get_element_text(IRP.w_faqi_sure_state,doc="获取确认人状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_queren_state

    def faqiren_check_returedproject3(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc,doc="点击'项目管理'")
        self.click(IRP.jixiaoguanli_loc,doc="点击'绩效管理'")
        self.click(IRP.jixiaotongji_loc,doc="点击'绩效统计'")
        first_last_day = self.get_first_and_last_day()
        sleep(4)
        data_1 = self.get_default_value(IRP.submittime,doc="获取提交时间")
        data_2 = self.get_default_value(IRP.zhitime, doc="获取提交时间")
        return first_last_day, data_1, data_2

    def delete_1(self):
        self.click(IRP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IRP.project_list_num)
        except:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IRP.delete1_loc, doc="删除'测试_线路工程'")
        self.click(IRP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IRP.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IRP.project_list_num)
        return num_1, num_2, success_text

    def delete_110(self,name,password):
        self.click(IRP.ph_logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IRP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IRP.project_list_num)
        except:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IRP.delete1_loc, doc="删除'测试_线路工程'")
        self.click(IRP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IRP.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IRP.project_list_num)
        return num_1, num_2, success_text

    def delete_8(self):
        self.click(IRP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IRP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IRP.project_list_num)
        except:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IRP.delete1_loc3, doc="删除'测试_线路工程3'")
        self.click(IRP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IRP.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IRP.project_list_num)
        return num_1, num_2, success_text

    def delete_2(self):
        self.click(IRP.projectmanager_loc, doc="点击项目管理")
        self.click(IRP.projectplatform_loc, doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IRP.project_list_num)
        except:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IRP.delete1_loc2, doc="删除'测试_线路工程2'")
        self.click(IRP.delete_sure_loc, doc="确定删除")
        success_text = self.get_element_text(IRP.delete_success, doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IRP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IRP.project_list_num)
        return num_1, num_2, success_text

    def jixiaoguanli_4(self):
        # self.click(IRP.projectmanager_loc,doc="点击项目管理")
        self.click(IRP.jixiaoguanli_loc,doc="点击绩效管理")
        self.click(IRP.xianlu,doc="点击线路工程名称")
        self.click(IRP.faqi_shenpi,doc="点击发起审批")
        self.click(IRP.tibao_sure,doc="点击确定")
        self.click(IRP.tibaobili_link,doc="点击提报比例按钮")
        # tibaobili = self.get_element_text(IRP.tibaobili,doc="提取提报比例")
        # zhuanyezhanbi = self.get_element_text(IRP.zhuanye_zhanbi,doc="提取专业占比")
        # project_biaozhungongri = self.get_element_text(IRP.biaozhun_days,doc="提取项目标准工日")
        # tibao_days = self.get_element_text(IRP.tibao_days,doc="提取提报工日")
        self.click(IRP.tijiao_shenpi,doc="点击提交审批")
        self.click(IRP.hanzheng1,doc="勾选韩正")
        self.click(IRP.sure,doc="点击确定")
        success = self.get_element_text(IRP.success,doc="成功 文本")
        shenpi_liuhen = self.get_element_text(IRP.shenpi_liuhen,doc="审批留痕 文本")
        return success,shenpi_liuhen