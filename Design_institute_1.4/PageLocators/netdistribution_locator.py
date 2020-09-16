from selenium.webdriver.common.by import By
class IndexNetPageLocator:
    """
    首页添加项目元素定位
    """
    # 首页'工作台'菜单定位
    workplatform_loc = (By.XPATH, '//span[contains(text(),"工作台")]')
    # '项目管理'定位
    projectmanager_loc = (By.XPATH,'//span[contains(text(),"项目管理")]/parent::a')
    # '项目台账'定位
    projectplatform_loc = (By.XPATH,'//span[contains(text(),"项目台账")]/parent::a')
    # '+添加项目'定位
    addproject_loc = (By.XPATH,'//span[contains(text(),"添加项目")]')
    # '项目名称'输入框定位
    projectname_loc = (By.XPATH,'//label[contains(text(),"项目名称")]/following-sibling::div//input')
    # '项目编号'输入框定位
    projectno_loc = (By.XPATH,'//label[contains(text(),"项目编号")]/following-sibling::div//input')
    # 项目类型下拉框
    projecttype_checkbox = (By.XPATH,'//label[text()="项目类型："]/following-sibling::div//div[@class="su_form_control su_select_box"]')

    """
    配网元素定位
    """
    # 项目类型:'配网工程'选项定位
    netproject_loc = (By.XPATH,'//a[@title="配网工程"]/parent::li')
    # 设计阶段下选框定位
    designphasetype_loc = (By.XPATH,'//label[text()="设计阶段："]/following-sibling::div//div[@class="su_form_control su_select_box"]')
    # 设计阶段:'初步设计'选项定位
    preliminary_design = (By.XPATH,'//a[@title="初步设计"]/parent::li')
    # 卷册模板下选框架定位
    volumetemplatetype_loc = (By.XPATH,'//label[text()="卷册模板："]/following-sibling::div//div[@class="su_form_control su_select_box"]')
    # '配网工程卷册模板'定位
    network_engineering_template = (By.XPATH,'//a[@title="配网工程卷册模板"]')

    # '设置节点'定位
    set_node = (By.XPATH,'//button[text()="设置节点"]')
    # '二次'勾选框定位
    twotimes_loc = (By.XPATH,'//span[@id="team-tree3_13_check"]')
    # '二次通信'--'选择'
    secondcommunication_loc = (By.XPATH,'//li[@id="team-tree3_14"]//b')
    # '王路'勾选框定位
    wanglucheck_loc = (By.XPATH,'//a[@title="王路"]/parent::li/span[@class="button chk radio_false_full"]')
    # 二次确定按钮
    twotimessurebutton_loc = (By.XPATH,'//button[text()="确定"]')
    # HD五审批--'选择'定位
    fiveapprovechoice_loc = (By.XPATH,'//a[@id="team-tree3_19_a"]//b')
    # 米照辉勾选框定位
    mizhaohuicheck_loc = (By.XPATH,'//a[@title="米照辉"]/parent::li/span[@class="button chk radio_false_full"]')
    # 薛选刚
    xuexuangang2 = (By.XPATH,'//a[@title="薛选刚"]/parent::li/span[@class="button chk radio_false_full"]')
    # 田景博
    tianjingbo_2 = (By.XPATH,'//a[@title="田景博"]/parent::li/span[@class="button chk radio_false_full"]')
    # 米照辉文本值定位
    mizhaohuitext_loc = (By.XPATH,'//span[@id="team-tree1_7_span"]')
    # HD六审--'选择'定位
    sixapprovechoice_loc = (By.XPATH,'//a[@id="team-tree3_20_a"]//b')
    # 薛选刚勾选框定位
    xuexuangangcheck_loc = (By.XPATH,'//a[@title="薛选刚"]/parent::li/span[@class="button chk radio_false_full"]')
    # 薛选刚文本值定位
    xuexuangangtext_loc = (By.XPATH,'//span[@id="team-tree1_8_span"]')
    # HD七审--'选择'定位
    sevenapprovechoice_loc = (By.XPATH,'//a[@id="team-tree3_21_a"]//b')
    # 田景博勾选框定位
    tianjingbocheck_loc = (By.XPATH,'//a[@title="田景博"]/parent::li/span[@class="button chk radio_false_full"]')
    # 田景博文本值定位
    tianjingbotext_loc = (By.XPATH,'//span[@id="team-tree1_9_span"]')
    # '设置节点'--'确定'按钮
    setnode_sure_button = (By.XPATH,'//button[text()="恢复默认"]/following-sibling::button[text()="确定"]')
    # '生产部门'定位
    productdepartment_loc = (By.XPATH,'//label[contains(text(),"生产部门")]')
    # '生产部门'--'选择'
    productdepartment_choice_loc = (By.XPATH,'//label[contains(text(),"生产部门")]//following-sibling::button')
    # '选择部门'--'成都'
    netdesigncenter_loc = (By.XPATH,'//a[@title="成都"]/parent::li/span[@class="button chk radio_false_full"]')
    # '选择部门'--'确定'按钮
    departmentsurebutton_loc = (By.XPATH,'//div[@class="frameView-item txt-c"]//span[text()="确定"]')
    # 设计校审级别勾选框
    jiaoshen_jibie = (By.XPATH,'//span[text()="标准校审级别"]//parent::div/following-sibling::div[@class="pull-left"]//div[@class="su_form_control su_select_box"]')
    # 一级选择
    yiji = (By.XPATH,'//a[@title="1级"]/parent::li')
    # '计划时间'定位
    time_loc = (By.XPATH,'//input[@class="form-control date-picker-head-input"]')
    # 默认时间'确定'按钮
    time_sure_button = (By.XPATH,'//span[text()="确定"]')
    # '创建'按钮
    create_button = (By.XPATH,'//button[text()="创建"]')


    # '项目台账'列表
    project_list_num = (By.XPATH,'//div[@class="pjlist-box mt-10"]')
    # '项目台账'第一个项目名称
    first_project_name = (By.XPATH,'//ul[@class="clearfix prlist-top"]//span[@class="fs-16 c-1 font-w cp it-name txt-ep"]')
    # '项目台账'--'无匹配数据！'
    null_datas = (By.XPATH,'//div[@class="nodatap"]')
    # 项目详情中的'设计卷册'
    design_file = (By.XPATH,'//span[text()="设计卷册"]/parent::span/parent::li')
    # 点击'二次'进入二次文件夹
    two_time = (By.XPATH,'//span[text()="二次"]')
    # 上传文件按钮
    uploadfile_button = (By.XPATH,'//button[text()="上传文件"]')
    # uploadfile_button = (By.XPATH,'//input[@type="file"]')
    # 项目详情中的'项目成员'
    project_member = (By.XPATH,'//span[text()="项目成员"]/parent::span/parent::li')
    # 配电
    peidian = (By.XPATH,'//span[text()="配电"]/parent::a/parent::li')
    jiaohe = (By.XPATH,'//span[text()="HD校核"]/parent::a/parent::li')
    # 人员空数据
    null_per = (By.XPATH,'//ul[@class="pagination su-grid-footer"]')
    # 添加人员
    addmember = (By.XPATH,'//button[text()="添加人员"]')
    # 输入框
    inputname = (By.XPATH,'//span[@id="userName"]//input[@type="text"]')
    # 搜索按钮
    searchbutton = (By.XPATH,'//span[@id="userName"]//i')
    # 张无忌勾选框
    zhangwuji = (By.XPATH,'//span[@id="managerTree_2_check"]')
    # 张三勾选框
    zhangsan = (By.XPATH,'//span[@id="managerTree_2_check"]')
    # 萧敬腾勾选框
    xiaojingteng = (By.XPATH, '//span[@id="managerTree_2_check"]')
    # 张三丰勾选框
    zhangsanfeng = (By.XPATH, '//span[@id="managerTree_2_check"]')
    # 添加按钮
    addbutton = (By.XPATH,'//button[text()=" 添 加 "]')
    # 列表
    list_loc = (By.XPATH,'//tr[@class]')
    # 获取手机号
    getphone = (By.XPATH,'//tr[@class]//td[3]')

    """
    我的工作
    """
    # 我的工作
    mywork_loc = (By.XPATH, '//span[contains(text(),"我的工作")]/parent::a')
    # 校审
    jiaoshen_loc = (By.XPATH,'//span[text()="校审"]/parent::a')
    # 发起流程
    faqiliucheng = (By.XPATH,'//span[contains(text(),"发起流程")]')
    # 选择所属项目
    project_choose = (By.XPATH,'//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择配网工程
    choose_netproject = (By.XPATH,'//div[contains(text(),"测试_配网工程")]/parent::td/parent::tr')
    # 确定按钮
    sure_button = (By.XPATH,'//button[@class="danger yes"]')
    # 选择卷册
    choose_file = (By.XPATH,'//span[text()="选择卷册"]')
    # 二次勾选框
    ercigouxuan = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 同步校审文件勾选
    tongbujiaoshen_gouxuan = (By.XPATH,'//label[text()="同步校审文件"]/span')
    # 确定按钮
    file_sure_button = (By.XPATH,'//div[@class="poa txt-c w-p100 h-50 pt-10 bt-c"]//span[text()="确定"]')
    # 五审人-米照辉
    wushen_mizhaohui = (By.XPATH,'//label[text()="五审人："]/following-sibling::div')
    # 设计校审文件名称和版本号
    shejijiaoshen_fileinfo = (By.XPATH,'//label[text()="设计校审文件："]/parent::li//div[@class="ml-110"]//li')
    # 空校审文件信息
    empty_file = (By.XPATH,'//label[text()="设计校审文件："]/parent::li')

    # 确认人选择
    surepeopel_choice = (By.XPATH,'//label[contains(text(),"确认人")]/following-sibling::div//span[text()="选择"]')
    # 选择人员
    wanglu = (By.XPATH,'//span[@id="managerTree_3_check"]')
    # 确定按钮
    wanglu_surebutton = (By.XPATH,'//span[text()="确定"]')
    # 取选 会签
    quxuan_huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]')
    # 会签
    huiqian_new = (By.XPATH,'//span[text()="跳过会签阶段"]/following-sibling::label/span')
    # 校审文件添加按钮
    jiaoshen_addfile = (By.XPATH,'//label[contains(text(),"校审文件")]/following-sibling::div//span[text()="+添加"]')
    # 校核人-选择
    jiaoheren_choice = (By.XPATH,'//label[contains(text(),"校核人")]/following-sibling::div//span[text()="选择"]')
    # 校核人-张三丰,张三，萧敬腾
    jiaohe_zhangsanfeng = (By.XPATH,'//span[@id="managerTree_41_check"]')
    jiaohe_zhangsan = (By.XPATH,'//span[@id="managerTree_42_check"]')
    jiaohe_xiaojingteng = (By.XPATH,'//span[@id="managerTree_43_check"]')
    # 校核确定
    jiaohe_sure = (By.XPATH,'//span[text()="确定"]')
    # 上传文件
    uploadfile = (By.XPATH,'//button[text()="上传文件"]')
    # 已上传文件勾选框
    uploaded_check = (By.XPATH,'//tr[@class]//span[@class="sufont-check"]')
    # 勾选文件弹出提示语
    tishiyu = (By.XPATH,'//div[@class="prompt"]')
    # 上传文件send_keys方法
    uploadfile_send = (By.XPATH,'//input[@id="uploadFileFoot"]')
    uploadfile2_send = (By.XPATH,'//input[@type="file"]')
    # 上传文件勾选框
    uploadedfilegouxuan = (By.XPATH,'//tr[@class]//span[@class="sufont-check"]')
    # 上传完文件 获取文件名称text
    uploadedfilename = (By.XPATH,'//span[contains(text(),"脚本")]')
    # 设计卷册上传文件后，文件版本号
    file_version = (By.XPATH,'//tr[@class]/td[6]')
    # 点击版本号 弹出列表框首条信息
    alter_first_filename = (By.XPATH,'//div[@class="popup_list"]//tr[@class][1]/td[1]')
    alter_first_author = (By.XPATH,'//div[@class="popup_list"]//tr[@class][1]/td[4]')
    alter_first_version = (By.XPATH,'//div[@class="popup_list"]//tr[@class][1]/td[6]')
    # 点击版本号 弹出列表框第二条信息
    alter_second_filename = (By.XPATH,'//div[@class="popup_list"]//tr[@class][2]/td[1]')
    alter_second_author = (By.XPATH,'//div[@class="popup_list"]//tr[@class][2]/td[4]')
    alter_second_version = (By.XPATH,'//div[@class="popup_list"]//tr[@class][2]/td[6]')
    # 确定按钮
    uploadfile_sure = (By.XPATH,'//button[text()="确定"]')
    # 发起流程按钮
    faqiliucheng_button = (By.XPATH,'//button[text()="发起流程"]')

    # 我发起的流程列表
    faqiliucheng_list = (By.XPATH,'//tr[@class]')
    # 空数据
    liucheng_null = (By.XPATH,'//p[contains(text(),"无匹配")]')
    # 所属项目名称
    suoshuxiangmu = (By.XPATH,'//tr[@class]//td[3]')
    # 五审状态
    wushen_zhuangtai = (By.XPATH,'//tr[@class]//td[12]')
    # 校核状态
    jiaohe_state = (By.XPATH,'//tr[@class]//td[8]')
    # 审批级别
    approve_level = (By.XPATH,'//tr[@class][1]//td[6]')

    # 退出按钮
    logout = (By.XPATH,'//span[text()="退出"]/parent::a')
    # 共XX行
    all_datas = (By.XPATH,'//a[contains(text(),"共")]')
    """
    五审人登陆元素定位
    """
    # 待处理按钮
    needdeal_button = (By.XPATH,'//button[text()="待处理"]')
    # 待处理数量
    needdeal_num = (By.XPATH,'//tr[@class]')
    # 待处理所属项目名称
    needdeal_projectname = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审人的五审状态
    wushenren_approvestate = (By.XPATH,'//tr[@class][1]//td[12]')
    # 校核人状态
    jiaohe_state = (By.XPATH,'//tr[@class][1]//td[8]')
    # 设计校审名称--二次
    erci = (By.XPATH,'//span[text()="二次"]')
    # 指定校核人
    zhiding_jiaohe = (By.XPATH,'//li[@class="clearfix mt-10"]//span[@class="mr-40"][1]')
    # 五审
    wushen_button = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 校核
    jiaohe_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="校核"]')
    # 全部通过
    all_pass = (By.XPATH,'//button[text()="全部通过"]')
    # 五审审批通过确定
    wushen_sure = (By.XPATH,'//button[text()="确定"]')
    # 待处理空数据
    nulldatas = (By.XPATH,'//p[contains(text(),"无匹配数据")]')
    # 已处理
    dealed_button = (By.XPATH,'//button[text()="已处理"]')
    # 已处理校审名称
    dealed_jiaoshen_name = (By.XPATH,'//tr[@class][1]//td[2]')
    # 已处理了所属项目
    dealed_suoshu_project = (By.XPATH,'//tr[@class][1]//td[3]')
    # 已处理五审状态
    dealed_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 已处理六审状态
    dealed_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')

    """
    六审人登陆元素
    """
    # 六审待处理项目
    liushen_needtodeal_count = (By.XPATH,'//tr[@class]')
    # 六审校审名称
    liushen_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 六审所属项目
    liushen_suoshu_project = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审审批状态
    wushenzhuangtai = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审审批状态
    liushen_shenpi_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 六审
    liushen_button = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="六审"]')
    # 六审全部通过
    six_all_pass = (By.XPATH,'//button[text()="全部通过"]')
    # 六审审批通过确定
    liushen_sure = (By.XPATH,'//button[text()="确定"]')
    # 已处理六审状态
    dealed_liushen_station = (By.XPATH, '//tr[@class][1]//td[13]')
    # 已处理七审状态
    dealed_qishen_station = (By.XPATH,'//tr[@class][1]//td[14]')
    # 审批级别
    approvel_jibie = (By.XPATH,'//tr[@class][1]//td[6]')
    """
    七审人登陆元素
    """
    # 七审待处理项目
    qishen_needtodeal_count = (By.XPATH,'//tr[@class]')
    # 七审校审名称
    qishen_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 七审所属项目
    qishen_suoshu_project = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审审批状态
    wushenapprove_zhuangtai = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审审批状态
    liushenapprove_zhuangtai = (By.XPATH, '//tr[@class][1]//td[13]')
    # 七审审批状态
    qishen_shenpi_state = (By.XPATH,'//tr[@class][1]//td[14]')
    # 七审
    qishen_button = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="七审"]')
    # 七审全部通过
    qi_all_pass = (By.XPATH,'//button[text()="全部通过"]')
    # 七审审批通过确定
    qishen_sure = (By.XPATH,'//button[text()="确定"]')
    # 已处理六审状态
    dealed_qishen_state = (By.XPATH, '//tr[@class][1]//td[13]')
    # 确认状态
    sure_station = (By.XPATH,'//tr[@class][1]//td[15]')

    """
    我发起的 元素定位
    """
    # 校审名称
    faqi_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    faqi_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    faqi_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    faqi_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 确认状态
    sure_state = (By.XPATH,'//tr[@class][1]//td[13]')

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH,'//span[text()="测试_配网工程"]/ancestor::ul//span[text()="删除"]')
    delete2_loc = (By.XPATH,'//span[text()="测试_配网工程2"]/ancestor::ul//span[text()="删除"]')
    delete3_loc = (By.XPATH,'//span[text()="测试_配网工程3"]/ancestor::ul//span[text()="删除"]')
    delete4_loc = (By.XPATH,'//span[text()="测试_配网工程4"]/ancestor::ul//span[text()="删除"]')
    delete5_loc = (By.XPATH,'//span[text()="测试_配网工程5"]/ancestor::ul//span[text()="删除"]')
    delete7_loc = (By.XPATH,'//span[text()="测试_配网工程7"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH,'//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH,'//div[text()="删除成功！"]')

    """归档"""
    # 归档管理
    guidang_guanli = (By.XPATH,'//span[contains(text(),"归档管理")]/parent::a')
    # 发起归档
    faqi_guidang = (By.XPATH,'//span[contains(text(),"发起归档")]')
    # 所属项目后的"选择"
    choice = (By.XPATH,'//label[text()="所属项目："]/following-sibling::div//span[text()="选择"]')
    # 归档：项目名称
    guidang_filename = (By.XPATH,'//tr[@class][1]/td[2]')
    guidang_filename1 = (By.XPATH,'//input[@type="radio"]/parent::span')
    # 归档提示语
    guidang_tishi = (By.XPATH,'//div[@class="prompt"]/div')
    # 弹框关闭按钮
    closebutton = (By.XPATH, '//span[text()="✕"]')
    # 归档-审批人员
    guidang_person = (By.XPATH,'//div[@class="popup"]//div[@class="lh-30 mb-10"]')
    guidang_person1 = (By.XPATH,'//label[text()="审批人员："]/parent::li')
    # 归档项目勾选
    guidang_gouxuan = (By.XPATH,'//input[@type="radio"]')
    guidang_gouxua_n = (By.XPATH,'//span[@class="cp su2-radio-left"]')
    # 监管人员
    jianguan_person = (By.XPATH,'//div[@class="lh-30 mb-10"]')
    # 发起归档按钮
    faqiguidang = (By.XPATH,'//span[text()="保存"]/following-sibling::span[text()="发起归档"]')
    # 归档确定
    guidang_sure = (By.XPATH,'//span[text()="确定"]')
    # 归档第一条记录项目名称
    first_guidang_name = (By.XPATH,'//tr[@class][1]/td[2]')
    # 归档第一条记录归档版本
    first_guidang_version = (By.XPATH,'//tr[@class][1]/td[8]')
    # 归档第一条记录审批人
    first_guidang_approver = (By.XPATH,'//tr[@class][1]/td[10]')
    # 归档第一条记录归档状态
    first_guidang_state = (By.XPATH,'//tr[@class][1]/td[11]')

    """发起人发起确认"""
    # 设计校审名称--二次
    f_erci = (By.XPATH,'//span[text()="二次"]')
    # 发起确认
    faqiqueren_button = (By.XPATH,'//span[text()="发起确认"]')
    # 确认人信息
    queren_person = (By.XPATH,'//label[text()="确认人："]/parent::li')
    # 发起按钮
    faqi_button = (By.XPATH,'//button[text()="发起"]')
    # 项目名称
    project_name = (By.XPATH,'//tr[@class][1]/td[3]')
    # 确认状态
    surestate = (By.XPATH,'//tr[@class][1]/td[13]')

    """王路确认"""
    # 我的工作
    w_mywork_loc = (By.XPATH, '//span[contains(text(),"我的工作")]/parent::a')
    # 校审
    w_jiaoshen_loc = (By.XPATH,'//span[text()="校审"]/parent::a')
    # 待处理
    w_daichuli = (By.XPATH,'//button[text()="待处理"]')
    # 共XX行
    w_all_datas = (By.XPATH,'//a[contains(text(),"共")]')
    # 已处理
    w_yichuli = (By.XPATH,'//button[text()="已处理"]')
    # 二次
    w_erci = (By.XPATH,'//span[text()="二次"]')
    # 确认
    w_sure = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="确认"]')
    # 全部通过
    w_all_pass = (By.XPATH,'//button[text()="全部通过"]')
    # 全部通过：确定
    w_allpass_sure = (By.XPATH,'//button[text()="确定"]')
    # 确认人状态
    w_queren_state = (By.XPATH,'//tr[@class][1]//td[13]')


