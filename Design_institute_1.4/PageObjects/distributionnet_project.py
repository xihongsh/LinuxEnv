from PageLocators.netdistribution_locator import IndexNetPageLocator as IP
from PageLocators.login_page_locator import LoginPageLocator as LP
from Common.basepage import BasePage
from time import sleep
class IndexNetPage(BasePage):
    # '配网工程'特殊字段
    def check_network_field(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IP.projecttype_checkbox,doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        # 返回'生产部门'字段 和 '计划时间'字段数量
        return self.get_element_text(IP.productdepartment_loc,doc="获取'生产部门：'文本信息"),self.get_list_length(IP.time_loc,doc="获取'计划时间数量'")

    def create_network_project(self,projectname,projectno):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        sleep(2)
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sixapprovechoice_loc,doc="点击'HD六审-选择'")
        self.click(IP.xuexuangangcheck_loc,doc="六审选择薛选刚")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'成都'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        sleep(3)
        num_2 = self.get_list_length(IP.project_list_num)
        first_project_name = self.get_element_text(IP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def create_network_project_r(self,projectname,projectno):
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        sleep(2)
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sixapprovechoice_loc,doc="点击'HD六审-选择'")
        self.click(IP.xuexuangangcheck_loc,doc="六审选择薛选刚")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'成都'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        sleep(3)
        num_2 = self.get_list_length(IP.project_list_num)
        first_project_name = self.get_element_text(IP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name


    def to_upload_file(self):
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.design_file,doc="点击'设计卷册'进入项目云盘")
        sleep(3)
        self.click(IP.two_time,doc="点击'二次'进入文件夹上传文件")
        self.input_text_uploadfile(IP.uploadfile2_send,r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        self.input_text_uploadfile(IP.uploadfile2_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        filename = self.get_element_text(IP.uploadedfilename, doc="获取已经上传的文件名称")
        fileversion = self.get_element_text(IP.file_version, doc="获取文件版本号")
        self.click(IP.file_version,doc="点击版本号")
        first_filename = self.get_element_text(IP.alter_first_filename,doc="获取弹框首条文件名称")
        first_author = self.get_element_text(IP.alter_first_author,doc="获取弹框首条创建者")
        first_version = self.get_element_text(IP.alter_first_version,doc="获取弹框首条文件版本号")
        second_filename = self.get_element_text(IP.alter_second_filename,doc="获取弹框第二条文件名称")
        second_author = self.get_element_text(IP.alter_second_author,doc="获取弹框第二条创建者")
        second_version = self.get_element_text(IP.alter_second_version,doc="获取弹框第二条文件版本号")
        return filename,fileversion,first_filename,first_author,first_version,second_filename,second_author,second_version

    def to_upload_file2(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.design_file,doc="点击'设计卷册'进入项目云盘")
        sleep(1)
        self.click(IP.two_time,doc="点击'二次'进入文件夹上传文件")
        self.input_text_uploadfile(IP.uploadfile2_send,r"/root/测试上传脚本用4.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        filename = self.get_element_text(IP.uploadedfilename, doc="获取已经上传的文件名称")
        fileversion = self.get_element_text(IP.file_version, doc="获取文件版本号")
        return filename,fileversion

    def addrole_m(self,phone,phone2,phone3,phone4):
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.project_member,doc="点击'项目成员'")
        self.click(IP.peidian, doc="点击'配电'")
        self.click(IP.addmember, doc="点击'添加人员'")
        self.input_text(IP.inputname,phone4, doc="输入手机号")
        self.click(IP.searchbutton, doc="点击搜索")
        self.click(IP.zhangwuji, doc="勾选'张无忌'")
        self.click(IP.addbutton, doc="点击'添加'")
        self.click(IP.jiaohe,doc="点击'HD校核'")
        sleep(2)
        if self.get_element_text(IP.null_per) == '到第\n页':
            length_1 = 0
        else:
            length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # try:
        #     length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # except:
        #     length_1 = 0
        self.click(IP.addmember,doc="点击'添加人员'")
        self.input_text(IP.inputname,phone,doc="输入手机号")
        self.click(IP.searchbutton,doc="点击搜索")
        self.click(IP.zhangsan,doc="勾选'张三'")
        self.click(IP.addbutton,doc="点击'添加'")
        self.click(IP.addmember, doc="点击'添加人员'")
        self.input_text(IP.inputname,phone2,doc="输入手机号")
        self.click(IP.searchbutton,doc="点击搜索")
        self.click(IP.xiaojingteng,doc="勾选'萧敬腾'")
        self.click(IP.addbutton, doc="点击'添加'")
        self.click(IP.addmember, doc="点击'添加人员'")
        self.input_text(IP.inputname, phone3, doc="输入手机号")
        self.click(IP.searchbutton, doc="点击搜索")
        self.click(IP.zhangsanfeng, doc="勾选'张三丰'")
        self.click(IP.addbutton, doc="点击'添加'")
        sleep(1)
        length_2= self.get_list_length(IP.list_loc,doc="获取列表长度")
        phonenumber = self.get_elements_text_value(IP.getphone,doc="获取手机号")
        return length_1,length_2,phonenumber

    def addroles(self,phone):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.project_member,doc="点击'项目成员'")
        self.click(IP.peidian,doc="点击'配电'")
        sleep(2)
        if self.get_element_text(IP.null_per) == '到第\n页':
            length_1 = 0
        else:
            length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # try:
        #     length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # except:
        #     length_1 = 0
        self.click(IP.addmember,doc="点击'添加人员'")
        self.input_text(IP.inputname,phone,doc="输入手机号")
        self.click(IP.searchbutton,doc="点击搜索")
        self.click(IP.zhangwuji,doc="勾选'张无忌'")
        self.click(IP.addbutton,doc="点击'添加'")
        length_2= self.get_list_length(IP.list_loc,doc="获取列表长度")
        phonenumber = self.get_element_text(IP.getphone,doc="获取手机号")
        da_1 = self.get_element_text(IP.null_per)
        return length_1,length_2,phonenumber

    def addrole2(self,phone):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.project_member,doc="点击'项目成员'")
        self.click(IP.peidian,doc="点击'配电'")
        sleep(2)
        if self.get_element_text(IP.null_per) == '到第\n页':
            length_1 = 0
        else:
            length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # try:
        #     length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # except:
        #     length_1 = 0
        self.click(IP.addmember,doc="点击'添加人员'")
        self.input_text(IP.inputname,phone,doc="输入手机号")
        self.click(IP.searchbutton,doc="点击搜索")
        self.click(IP.zhangwuji,doc="勾选'张无忌'")
        self.click(IP.addbutton,doc="点击'添加'")
        length_2= self.get_list_length(IP.list_loc,doc="获取列表长度")
        phonenumber = self.get_element_text(IP.getphone,doc="获取手机号")
        return length_1,length_2,phonenumber

    def addrole3(self,phone):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        self.click(IP.first_project_name,doc="点击项目名称进入项目详情")
        self.click(IP.project_member,doc="点击'项目成员'")
        self.click(IP.peidian,doc="点击'配电'")
        sleep(2)
        if self.get_element_text(IP.null_per) == '到第\n页':
            length_1 = 0
        else:
            length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # try:
        #     length_1 = self.get_list_length(IP.list_loc, doc="获取列表长度")
        # except:
        #     length_1 = 0
        self.click(IP.addmember,doc="点击'添加人员'")
        self.input_text(IP.inputname,phone,doc="输入手机号")
        self.click(IP.searchbutton,doc="点击搜索")
        self.click(IP.zhangwuji,doc="勾选'张无忌'")
        self.click(IP.addbutton,doc="点击'添加'")
        length_2= self.get_list_length(IP.list_loc,doc="获取列表长度")
        phonenumber = self.get_element_text(IP.getphone,doc="获取手机号")
        return length_1,length_2,phonenumber

    def jiaoshenren(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        # self.click(IP.huiqian_new,doc="勾选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        sleep(3)
        self.click(IP.file_sure_button,doc="点击确定按钮")
        sleep(3)
        return self.get_element_text(IP.wushen_mizhaohui,doc="获取五审人"),self.get_element_text(IP.shejijiaoshen_fileinfo,doc="获取校审文件信息")

    def faqiliucheng(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        # self.click(IP.huiqian_new, doc="勾选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        # self.click(IP.jiaoshen_addfile,doc="添加校审文件")
        # self.click(IP.uploadfile,doc="点击'上传文件'")
        # self.input_text_uploadfile(IP.uploadfile_send,r"/root/测试上传脚本用.txt",doc="通过send_keys方法上传文件")
        # sleep(1)
        # self.click(IP.uploadfile_sure,doc="点击确定按钮")
        self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        sleep(2)
        num_2 = self.get_list_length(IP.faqiliucheng_list)
        project_name = self.get_element_text(IP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IP.wushen_zhuangtai,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqiliucheng_three(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程7'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        self.click(IP.huiqian_new, doc="取选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.tongbujiaoshen_gouxuan,doc="勾选同步校审")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        # self.click(IP.quxuan_huiqian,doc="取选会签")
        self.click(IP.jiaoheren_choice,doc="选择校核人")
        self.click(IP.jiaohe_zhangsanfeng,doc="选择校核人张三丰")
        self.click(IP.jiaohe_zhangsan,doc="选择校核人张三")
        self.click(IP.jiaohe_xiaojingteng,doc="选择校核人萧敬腾")
        self.click(IP.jiaohe_sure,doc="点击确定")
        # self.click(IP.jiaoshen_addfile, doc="添加校审文件")
        # self.click(IP.uploadfile,doc="点击'上传文件'")
        # self.input_text_uploadfile(IP.uploadfile2_send,r"/root/测试上传脚本用4.txt",doc="通过send_keys方法上传文件")
        # sleep(1)
        # self.click(IP.uploadfile_sure,doc="点击确定按钮")
        sleep(1)
        self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        sleep(6)
        num_2 = self.get_list_length(IP.faqiliucheng_list)
        project_name = self.get_element_text(IP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IP.jiaohe_state,doc="获取'校核'状态")
        return num_1,num_2,project_name,state

    def faqiliucheng_secondproject(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        # self.click(IP.huiqian_new, doc="勾选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        self.click(IP.jiaoshen_addfile,doc="添加校审文件")
        self.click(IP.uploadfile,doc="点击'上传文件'")
        self.input_text_uploadfile(IP.uploadfile_send,r"/root/测试上传脚本用.txt",doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IP.uploadfile_sure,doc="点击确定按钮")
        self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        sleep(6)
        num_2 = self.get_list_length(IP.faqiliucheng_list)
        project_name = self.get_element_text(IP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IP.wushen_zhuangtai,doc="获取'五审'状态")
        return num_1,num_2,project_name,state

    def faqiliucheng_third(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        # self.click(IP.huiqian_new, doc="勾选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        self.click(IP.jiaoshen_addfile,doc="添加校审文件")
        self.click(IP.uploadfile,doc="点击'上传文件'")
        self.input_text_uploadfile(IP.uploadfile_send,r"/root/测试上传脚本用.txt",doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IP.uploadfile_sure,doc="点击确定按钮")
        self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        sleep(6)
        num_2 = self.get_list_length(IP.faqiliucheng_list)
        project_name = self.get_element_text(IP.suoshuxiangmu,doc="获取'所属项目'名称")
        state = self.get_element_text(IP.wushen_zhuangtai,doc="获取'五审'状态")
        return num_1,num_2,project_name,state


    def faqiliucheng2(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        empty_fileinfo = self.get_element_text(IP.empty_file,doc="设计校审文件为空信息")
        self.click(IP.jiaoshen_addfile,doc="添加校审文件")
        self.click(IP.uploaded_check,doc="勾选'已上传文件'")
        sleep(2)
        tishiyu1 = self.get_element_text(IP.tishiyu,"获取提示语")
        # # sleep(6)
        # self.click(IP.uploadfile, doc="点击'上传文件'")
        # self.input_text_uploadfile(IP.uploadfile_send,r"/root/测试上传脚本用.txt",doc="通过send_keys方法上传文件")
        # sleep(2)
        # self.click(IP.uploadfile_sure,doc="点击确定按钮")
        # sleep(2)
        # self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        # tishiyu2 = self.get_element_text(IP.tishiyu, "获取提示语")
        return empty_fileinfo,tishiyu1

    def faqiliucheng3(self):
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(2)
        try:
            self.get_element_text(IP.liucheng_null, doc="流程为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.faqiliucheng_list)
        self.click(IP.faqiliucheng,doc="点击'发起流程'")
        self.click(IP.project_choose,doc="点击'选择'")
        self.click(IP.choose_netproject,doc="选择'测试_配网工程5'")
        self.click(IP.sure_button,doc="点击'确定按钮'")
        # self.click(IP.huiqian_new, doc="勾选'跳过会签阶段'")
        self.click(IP.choose_file,doc="点击'选择卷册'")
        self.click(IP.ercigouxuan,doc="勾选二次")
        self.click(IP.file_sure_button,doc="点击确定按钮")
        self.click(IP.surepeopel_choice,doc="选择'确认人'")
        self.click(IP.wanglu,doc="选择王路")
        self.click(IP.wanglu_surebutton,doc="点击'确定'按钮")
        self.click(IP.jiaoshen_addfile,doc="添加校审文件")
        self.click(IP.uploadfile, doc="点击'上传文件'")
        sleep(1)
        self.input_text_uploadfile(IP.uploadfile_send,r"/root/测试上传脚本用.txt",doc="通过send_keys方法上传文件")
        sleep(6)
        self.click(IP.uploadfile_sure,doc="点击确定按钮")
        sleep(2)
        self.click(IP.faqiliucheng_button,doc="点击'发起流程'")
        sleep(6)
        num_2 = self.get_list_length(IP.faqiliucheng_list)
        project_name = self.get_element_text(IP.suoshuxiangmu,doc="获取'所属项目'名称")
        approvelevel = self.get_element_text(IP.approve_level,doc="获取审批级别")
        state = self.get_element_text(IP.wushen_zhuangtai,doc="获取'五审'状态")
        return num_1,num_2,project_name,approvelevel,state

    def wushenren_loginapprove(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IP.needdeal_projectname,doc="获取待处理'项目名称'")
        wushenren_state = self.get_element_text(IP.wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,wushenren_state

    def jiaohe_loginapprove(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IP.needdeal_projectname,doc="获取待处理'项目名称'")
        jiaohe_state = self.get_element_text(IP.jiaohe_state,doc="获取校核人审批状态")
        return needdealproject_name,jiaohe_state


    def wushenren_loginapprove2(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealproject_name = self.get_element_text(IP.needdeal_projectname,doc="获取待处理'项目名称'")
        approvelevel = self.get_element_text(IP.approve_level, doc="获取审批级别")
        wushenren_state = self.get_element_text(IP.wushenren_approvestate,doc="获取五审人审批状态")
        return needdealproject_name,approvelevel,wushenren_state

    def wushenren_approvesucess(self):
        # self.click(IP.logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IP.mywork_loc,doc="点击'我的工作'")
        # self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci,doc="点击'二次'进入详情")
        self.click(IP.wushen_button,doc="点击'五审'进入审批详情")
        self.click(IP.all_pass,doc="点击'全部通过'")
        self.click(IP.wushen_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IP.dealed_wushen_state,doc="获取'已处理'五审状态")
        dealed_liushen_state = self.get_element_text(IP.dealed_liushen_state,doc="获取'已处理'六审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state,dealed_liushen_state

    def jiaohe_approvesucess_s(self):
        # self.click(IP.logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IP.mywork_loc,doc="点击'我的工作'")
        # self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button, doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button, doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button, doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci, doc="点击'二次'进入详情")
        zhiding_jiaoheren = self.get_element_text(IP.zhiding_jiaohe, doc="获取指定校核人")
        return num_text_1, num_text_2, zhiding_jiaoheren

    def wushenren_approvesucess3(self):
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci,doc="点击'二次'进入详情")
        self.click(IP.wushen_button,doc="点击'五审'进入审批详情")
        self.click(IP.all_pass,doc="点击'全部通过'")
        self.click(IP.wushen_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        approvelevel = self.get_element_text(IP.approve_level, doc="获取审批级别")
        dealed_wushen_state = self.get_element_text(IP.dealed_wushen_state,doc="获取'已处理'五审状态")
        dealed_liushen_state = self.get_element_text(IP.dealed_liushen_state,doc="获取'已处理'六审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state,dealed_liushen_state,approvelevel

    def wushenren_approvesucess2(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci,doc="点击'二次'进入详情")
        self.click(IP.wushen_button,doc="点击'五审'进入审批详情")
        self.click(IP.all_pass,doc="点击'全部通过'")
        self.click(IP.wushen_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_wushen_state = self.get_element_text(IP.dealed_wushen_state,doc="获取'已处理'五审状态")
        dealed_liushen_state = self.get_element_text(IP.dealed_liushen_state,doc="获取'已处理'六审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_wushen_state,dealed_liushen_state


    def liushenren_loginapprove(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealjiaoshen_name = self.get_element_text(IP.liushen_jiaoshen_name,doc="获取'六审'待处理项目校审名称")
        liushen_suoshu_project = self.get_element_text(IP.liushen_suoshu_project,doc="获取'六审'待处理项目所属项目")
        wushenzhuangtai = self.get_element_text(IP.wushenzhuangtai,doc="获取'五审审批状态'")
        liushen_shenpi_state = self.get_element_text(IP.liushen_shenpi_state,doc="获取六审审批状态")
        return needdealjiaoshen_name,liushen_suoshu_project,wushenzhuangtai,liushen_shenpi_state

    def liushenren_approvesucess(self):
        # self.click(IP.logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IP.mywork_loc,doc="点击'我的工作'")
        # self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci,doc="点击'二次'进入详情")
        self.click(IP.liushen_button,doc="点击'六审'进入审批详情")
        self.click(IP.six_all_pass,doc="点击'全部通过'")
        self.click(IP.liushen_sure,doc="点击'确定'")
        sleep(3)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_liushen_state = self.get_element_text(IP.dealed_liushen_station,doc="获取'已处理'六审状态")
        dealed_qishen_state = self.get_element_text(IP.dealed_qishen_station,doc="获取'已处理'七审状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_liushen_state,dealed_qishen_state

    def qishenren_loginapprove(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        needdealjiaoshen_name = self.get_element_text(IP.qishen_jiaoshen_name,doc="获取'七审'待处理项目校审名称")
        liushen_suoshu_project = self.get_element_text(IP.qishen_suoshu_project,doc="获取'七审'待处理项目所属项目")
        wushenzhuangtai = self.get_element_text(IP.wushenapprove_zhuangtai,doc="获取'五审审批状态'")
        liushen_shenpi_state = self.get_element_text(IP.liushenapprove_zhuangtai,doc="获取六审审批状态")
        qishen_shenpi_state = self.get_element_text(IP.qishen_shenpi_state,doc="获取七审审批状态")
        return needdealjiaoshen_name,liushen_suoshu_project,wushenzhuangtai,liushen_shenpi_state,qishen_shenpi_state

    def qishenren_approvesucess(self):
        # self.click(IP.logout,doc="退出系统")
        # self.input_text(LP.user_loc,name,doc="输入用户名")
        # self.input_text(LP.password_loc,password,doc="输入密码")
        # self.click(LP.login_button_loc,doc="登陆")
        # self.click(IP.mywork_loc,doc="点击'我的工作'")
        # self.click(IP.jiaoshen_loc,doc="点击'校审'")
        self.click(IP.needdeal_button,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.needdeal_button, doc="点击'待处理'")
        sleep(8)
        self.click(IP.erci,doc="点击'二次'进入详情")
        self.click(IP.qishen_button,doc="点击'七审'进入审批详情")
        self.click(IP.qi_all_pass,doc="点击'全部通过'")
        self.click(IP.qishen_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_qishen_state = self.get_element_text(IP.dealed_qishen_station,doc="获取'已处理'七审状态")
        dealed_sure_state = self.get_element_text(IP.sure_station,doc="获取'确认'状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_qishen_state,dealed_sure_state

    def create_network2_project(self,projectname,projectno):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sixapprovechoice_loc,doc="点击'HD六审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="六审也选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'成都'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        sleep(3)
        num_2 = self.get_list_length(IP.project_list_num)
        first_project_name = self.get_element_text(IP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def faqiren_check_returedproject(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IP.faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IP.faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_wushen_state = self.get_element_text(IP.faqi_wushen_state,doc="获取五审状态")
        faqi_liushen_state = self.get_element_text(IP.faqi_liushen_state,doc="获取六审状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,faqi_liushen_state

    def faqiren_check_returedproject3(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IP.faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IP.faqi_suoshuxiangmu,doc="获取所属项目")
        faqi_queren_state = self.get_element_text(IP.sure_state,doc="获取确认状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_queren_state

    def faqiren_check_returedproject2(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IP.faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IP.faqi_suoshuxiangmu,doc="获取所属项目")
        approvelevel = self.get_element_text(IP.approve_level, doc="获取审批级别")
        faqi_wushen_state = self.get_element_text(IP.faqi_wushen_state,doc="获取五审状态")
        sure_state = self.get_element_text(IP.sure_state,doc="获取确认状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,sure_state,approvelevel

    def querenren_approvesuccess(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.mywork_loc,doc="点击'我的工作'")
        self.click(IP.jiaoshen_loc,doc="点击'校审'")
        sleep(3)
        faqi_jiaoshenname = self.get_element_text(IP.faqi_jiaoshenmingcheng,doc="获取校审名称")
        faqi_suoshuproject = self.get_element_text(IP.faqi_suoshuxiangmu,doc="获取所属项目")
        approvelevel = self.get_element_text(IP.approve_level, doc="获取审批级别")
        faqi_wushen_state = self.get_element_text(IP.faqi_wushen_state,doc="获取五审状态")
        sure_state = self.get_element_text(IP.sure_state,doc="获取确认状态")
        return faqi_jiaoshenname,faqi_suoshuproject,faqi_wushen_state,sure_state,approvelevel

    def create_network3_project(self,projectname,projectno):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        mizhaohuitext = self.get_element_text(IP.mizhaohuitext_loc, doc="获取米照辉文本值")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        tianjingbo = self.get_element_text(IP.tianjingbotext_loc, doc="获取田景博文本值")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'配网设计中心'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        sleep(3)
        num_2 = self.get_list_length(IP.project_list_num)
        first_project_name = self.get_element_text(IP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name,mizhaohuitext,tianjingbo

    def create_network4_project(self,projectname,projectno):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        mizhaohuitext = self.get_element_text(IP.mizhaohuitext_loc, doc="获取米照辉文本值")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        tianjingbo = self.get_element_text(IP.tianjingbotext_loc, doc="获取田景博文本值")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'配网设计中心'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        sleep(5)
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        self.click(IP.guidang_guanli,doc="点击归档管理")
        self.click(IP.faqi_guidang,doc="点击发起归档")
        self.click(IP.choice, doc="所属项目后的'选择'")
        sleep(3)
        self.click(IP.guidang_filename,doc="点击项目名称")
        text_1 = self.get_element_text(IP.guidang_tishi,doc="获取归档提示语")
        self.click(IP.closebutton, doc="点击'X'关闭弹框")
        text_2 = self.get_element_text(IP.guidang_person1,doc="获取审批人员")
        return text_1,text_2

    def delete_1(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete1_loc,doc="删除'测试_配网工程'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_2(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete2_loc,doc="删除'测试_配网工程2'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_1(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete1_loc,doc="删除'测试_配网工程'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_s(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(3)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete7_loc,doc="删除'测试_配网工程7'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_3(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete3_loc,doc="删除'测试_配网工程3'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_4(self):
        # self.click(IP.projectmanager_loc, doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(4)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete4_loc,doc="删除'测试_配网工程4'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def delete_5(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        sleep(2)
        try:
            num_1 = self.get_list_length(IP.project_list_num)
        except:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        self.click(IP.delete5_loc,doc="删除'测试_配网工程5'")
        self.click(IP.delete_sure_loc,doc="确定删除")
        success_text = self.get_element_text(IP.delete_success,doc="获取'删除成功'")
        sleep(2)
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_2 = 0
        except:
            num_2 = self.get_list_length(IP.project_list_num)
        return num_1,num_2,success_text

    def guidang(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.guidang_guanli,doc="点击归档管理")
        self.click(IP.faqi_guidang,doc="点击发起归档")
        self.click(IP.choice, doc="所属项目后的'选择'")
        sleep(3)
        self.click(IP.guidang_filename,doc="点击项目名称")
        text_1 = self.get_element_text(IP.guidang_tishi,doc="获取归档提示语")
        return text_1

    def guidang2(self):
        self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        # self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.click(IP.first_project_name, doc="点击项目名称进入项目详情")
        self.click(IP.design_file, doc="点击'设计卷册'进入项目云盘")
        sleep(1)
        self.click(IP.two_time, doc="点击'二次'进入文件夹上传文件")
        self.input_text_uploadfile(IP.uploadfile2_send, r"/root/测试上传脚本用.txt", doc="通过send_keys方法上传文件")
        sleep(6)
        uploadfilename = self.get_element_text(IP.uploadedfilename, doc="获取已经上传的文件名称")
        fileversion = self.get_element_text(IP.file_version, doc="获取文件版本号")
        self.click(IP.guidang_guanli,doc="点击归档管理")
        sleep(3)
        self.click(IP.faqi_guidang,doc="点击发起归档")
        self.click(IP.choice, doc="所属项目后的'选择'")
        sleep(3)
        self.click(IP.guidang_filename1, doc="点击项目名称")
        self.click(IP.guidang_sure, doc="归档确定按钮")
        sleep(4)
        # jianguanren = self.get_element_text(IP.jianguan_person, doc="获取监管人员")
        self.click(IP.faqiguidang, doc="点击'发起归档'按钮")
        sleep(3)
        filename = self.get_element_text(IP.first_guidang_name,doc="获取第一条归档记录项目名称")
        version = self.get_element_text(IP.first_guidang_version,doc="获取第一条归档版本")
        approver = self.get_element_text(IP.first_guidang_approver,doc="获取第一条归档审批人")
        state = self.get_element_text(IP.first_guidang_state,doc="获取第一条归档审批状态")
        return uploadfilename,fileversion,filename,version,approver,state

    def create_network5_project(self,projectname,projectno):
        # self.click(IP.projectmanager_loc,doc="首页_点击'项目管理'")
        # self.click(IP.projectplatform_loc,doc="首页_点击'项目台账'")
        try:
            self.get_element_text(IP.null_datas, doc="项目台账为空提示语")
            num_1 = 0
        except:
            num_1 = self.get_list_length(IP.project_list_num)
        self.click(IP.addproject_loc,doc="首页_点击'添加项目'")
        self.input_text(IP.projectname_loc,projectname,doc="输入项目名称")
        self.input_text(IP.projectno_loc,projectno,doc="输入项目编号")
        self.click(IP.projecttype_checkbox, doc='选择项目类型')
        self.click(IP.netproject_loc,doc="项目类型选择'配网工程'")
        self.click(IP.designphasetype_loc,doc="选择设计阶段")
        self.click(IP.preliminary_design,doc="设计阶段选择'初步设计'")
        self.click(IP.volumetemplatetype_loc,doc="选择卷册模板")
        self.click(IP.network_engineering_template,doc="卷册模板选择'配网工程卷册模板'")
        self.click(IP.set_node,doc="点击'设置节点'")
        self.click(IP.twotimes_loc,doc="勾选'二次'")
        self.click(IP.secondcommunication_loc,doc="点击'二次通信-选择'")
        self.click(IP.wanglucheck_loc,doc="'二次通信'选择'王路'")
        self.click(IP.twotimessurebutton_loc,doc="点击确定按钮")
        self.click(IP.fiveapprovechoice_loc,doc="点击'HD五审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="五审选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sixapprovechoice_loc,doc="点击'HD六审-选择'")
        self.click(IP.mizhaohuicheck_loc,doc="六审也选择米照辉")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.sevenapprovechoice_loc,doc="点击'HD七审-选择'")
        self.click(IP.tianjingbocheck_loc,doc="七审选择田景博")
        self.click(IP.twotimessurebutton_loc, doc="点击确定按钮")
        self.click(IP.setnode_sure_button,doc="点击确定按钮")
        self.click(IP.productdepartment_choice_loc,doc="选择生产部门")
        self.click(IP.netdesigncenter_loc,doc="生产部门选择'成都'")
        self.click(IP.departmentsurebutton_loc,doc="选择好生产部门点'确定'按钮")
        self.click(IP.jiaoshen_jibie,doc="点击设计校审级别勾选框")
        self.click(IP.yiji,doc="选择一级")
        self.click(IP.time_loc,doc="选择计划时间")
        self.click(IP.time_sure_button,doc="选择默认时间点'确定'按钮")
        self.click(IP.create_button,doc="点击'创建'按钮创建项目")
        sleep(3)
        num_2 = self.get_list_length(IP.project_list_num)
        first_project_name = self.get_element_text(IP.first_project_name,doc="获取第一个项目名称")
        return num_1,num_2,first_project_name

    def faqiren_sure(self):
        self.click(IP.f_erci,doc="点击'二次'")
        self.click(IP.faqiqueren_button,doc="点击'发起确认'")
        text = self.get_element_text(IP.queren_person,doc="获取确认人信息")
        self.click(IP.faqi_button,doc="点击'发起'")
        first_project_name = self.get_element_text(IP.project_name, doc="获取第一个项目名称")
        sure_state = self.get_element_text(IP.surestate, doc="获取确认状态")
        return text,first_project_name,sure_state

    def wanglu_approvesucess(self,name,password):
        self.click(IP.logout,doc="退出系统")
        self.input_text(LP.user_loc,name,doc="输入用户名")
        self.input_text(LP.password_loc,password,doc="输入密码")
        self.click(LP.login_button_loc,doc="登陆")
        self.click(IP.w_mywork_loc,doc="点击'我的工作'")
        self.click(IP.w_jiaoshen_loc,doc="点击'校审'")
        self.click(IP.w_daichuli,doc="点击'待处理'")
        sleep(8)
        try:
            num_text_1 = self.get_element_text(IP.w_all_datas, doc="获取共XX行")
        except:
            num_text_1 = 0
        self.click(IP.w_yichuli,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_2 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_2 = 0
        self.click(IP.w_daichuli, doc="点击'待处理'")
        sleep(8)
        self.click(IP.w_erci,doc="点击'二次'进入详情")
        self.click(IP.w_sure,doc="点击确认")
        self.click(IP.w_all_pass,doc="点击'全部通过'")
        self.click(IP.w_allpass_sure,doc="点击'确定'")
        sleep(2)
        try:
            num_text_3 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_3 = 0
        self.click(IP.dealed_button,doc="点击'已处理'")
        sleep(8)
        try:
            num_text_4 = self.get_element_text(IP.all_datas, doc="获取共XX行")
        except:
            num_text_4 = 0
        dealed_jiaoshen_name = self.get_element_text(IP.dealed_jiaoshen_name,doc="获取'已处理'校审名称")
        dealed_suoshu_project = self.get_element_text(IP.dealed_suoshu_project,doc="获取'已处理'所属项目")
        dealed_approvejibie = self.get_element_text(IP.approvel_jibie,doc="获取审批级别")
        dealed_sure_state = self.get_element_text(IP.w_queren_state,doc="获取'确认'状态")
        return num_text_1,num_text_2,num_text_3,num_text_4,dealed_jiaoshen_name,dealed_suoshu_project,dealed_approvejibie,dealed_sure_state














