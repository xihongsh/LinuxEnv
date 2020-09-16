from selenium.webdriver.common.by import By
class IndexpPhotovoltaicPageLocator:
    """
    首页添加光伏项目元素定位
    """
    # 首页'工作台'菜单定位
    workplatform_loc = (By.XPATH, '//span[contains(text(),"工作台")]')
    # '项目管理'定位
    projectmanager_loc = (By.XPATH,'//span[contains(text(),"项目管理")]/parent::a')
    # '项目台账'定位
    projectplatform_loc = (By.XPATH,'//span[contains(text(),"项目台账")]/parent::a')
    # '项目台账'第一个项目名称
    first_project_name = (By.XPATH,'//ul[@class="clearfix prlist-top"]//span[@class="fs-16 c-1 font-w cp it-name txt-ep"]')
    # '项目台账'--'无匹配数据！'
    null_datas = (By.XPATH,'//div[@class="nodatap"]')
    # '项目台账'列表
    project_list_num = (By.XPATH,'//div[@class="pjlist-box mt-10"]')
    # '+添加项目'定位
    addproject_loc = (By.XPATH,'//span[contains(text(),"添加项目")]')
    # '项目名称'输入框定位
    projectname_loc = (By.XPATH,'//label[contains(text(),"项目名称")]/following-sibling::div//input')
    # '项目编号'输入框定位
    projectno_loc = (By.XPATH,'//label[contains(text(),"项目编号")]/following-sibling::div//input')
    # 项目类型下拉框
    projecttype_checkbox = (By.XPATH,'//label[text()="项目类型："]/following-sibling::div//div[@class="su_form_control su_select_box"]')
    # 光伏工程
    guangfu_gongcheng = (By.XPATH,'//a[@title="光伏工程"]/parent::li')
    # 工程类型所有选项
    gongchengtype_allchoices = (By.XPATH,'//label[contains(text(),"工程类型")]/parent::li/div')
    # 分布式勾选框
    fenbushi_gouxuan = (By.XPATH,'//label[text()="分布式"]/span')
    # 设计阶段下拉框
    shejijieduan_choose = (By.XPATH,'//label[contains(text(),"设计阶段")]/parent::li/div')
    # 施工图选项
    shigongtu = (By.XPATH,'//a[@title="施工图"]/parent::li')
    # 电压等级下拉框
    dianyadengji_choose = (By.XPATH,'//label[contains(text(),"电压等级")]/parent::li/div')
    # 35kv选项
    kv35_choose = (By.XPATH,'//a[@title="35kV"]/parent::li')
    # 建设性质所有选项
    jianshexingzhi_allchoices = (By.XPATH,'//label[contains(text(),"建设性质")]/parent::li/div')
    # 光伏区建设勾选框
    guangfuqujianshe_gouxuan = (By.XPATH,'//label[text()="光伏区建设"]/span')
    # 角色模板下拉框
    juesemoban_choose = (By.XPATH,'//label[contains(text(),"角色模板")]/parent::li/div')
    # 恒华光伏工程选项
    henghuaguangfu_choose = (By.XPATH,'//a[@title="恒华光伏工程"]/parent::li')
    # 选择成员按钮
    choose_member = (By.XPATH,'//button[text()="选择成员"]')
    # 总工
    zonggong = (By.XPATH,'//li[text()="总工"]')
    # 添加成员按钮
    addmember_button = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 总工输入框
    zonggong_input = (By.XPATH,'//input[@id="searchId"]')
    # 张无忌 勾选框
    zhangwuji_gouxuan = (By.XPATH,'//span[text()="张无忌"]/parent::a/parent::li/span[@class="button chk checkbox_false_full"]')
    # 海清 勾选框
    haiqing_chooose = (By.XPATH,'//span[@id="team-tree1_7_check"]')
    # 确定按钮
    sure_button = (By.XPATH,'//button[text()="确定"]')
    # 添加成员按钮
    addpeople = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 设总
    shezong = (By.XPATH,'//li[text()="设总"]')
    # 海若梦 勾选
    hairuomeng_choose = (By.XPATH,'//span[@id="team-tree1_8_check"]')

    # 角色模板下拉框
    juancemoban_choose = (By.XPATH,'//label[contains(text(),"卷册模板")]/parent::li//input')
    # 光伏工程_施工图_35kV
    guangfu_35kv_choose = (By.XPATH,'//a[@title="光伏工程_施工图_35kV"]/parent::li')
    # 设置节点按钮
    setnode_button = (By.XPATH,'//button[text()="设置节点"]')
    # 01-设计输入资料  勾选
    shejiinputfile = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 01-设计输入资料  选择按钮
    inputfile_choosebutton = (By.XPATH,'//a[@id="team-tree3_2_a"]//b')
    # 01-设计输入资料  选择'海清'
    inputfile_zhangwuji_choose = (By.XPATH,'//span[@id="team-tree1_3_check"]')
    # 确定按钮
    inputfile_sure_button = (By.XPATH,'//button[text()="确定"]')
    # 设置节点 确定按钮
    setnode_sure_button = (By.XPATH,'//button[text()="确定"]')
    # 工程规模中字段数量
    gongchengguimo_fieldsnum = (By.XPATH,'//label[text()="工程规模："]/parent::li//li')
    # 工程规模 容量
    rongliang = (By.XPATH,'//label[text()="工程规模："]/parent::li//li/span[1]')
    # 容量输入框
    rongliang_input = (By.XPATH,'//span[text()="容量："]/parent::li//input')
    # 工程投资中字段数量
    gongchengtouzi_fieldsnum = (By.XPATH,'//label[text()="工程投资："]/parent::li//li')
    # 工程投资字段文本值
    gongchengtouzi_fieldstext = (By.XPATH,'//label[text()="工程投资："]/parent::li//ul')
    # 勘察费输入框
    kanchafei_input = (By.XPATH,'//span[text()="勘察费："]/parent::li//input')
    # 设计费输入框
    shejifei_input = (By.XPATH,'//span[text()="设计费："]/parent::li//input')
    # 总投资输入框
    zongtouzi_input = (By.XPATH,'//span[text()="总投资："]/parent::li//input')
    # 设计校审 勾选
    shejijiaoshen = (By.XPATH,'//label[text()="设计校审"]/span')
    # 设计校审级别勾选框
    jiaoshenlevel = (By.XPATH,'//div[@id="children-span"]/div[@class="su_form_control su_select_box"]')
    # 1级
    level_1 = (By.XPATH,'//a[@title="1级"]')
    # 可低于标准级别 勾选
    diyubiaozhun = (By.XPATH,'//label[text()="可低于标准级别"]/span')
    # 跳过会签阶段 勾选
    huiqianjieduan = (By.XPATH,'//label[text()="可跳过会签阶段"]/span')
    # 开始时间
    start_time = (By.XPATH,'//span[text()="—"]/preceding-sibling::div')
    # 结束时间
    end_time = (By.XPATH,'//span[text()="—"]/following-sibling::div')
    # 时间确定按钮
    start_time_sure = (By.XPATH,'//span[text()="—"]/preceding-sibling::div//span[text()="确定"]')
    # 时间确定按钮
    end_time_sure = (By.XPATH,'//span[text()="—"]/following-sibling::div//span[text()="确定"]')
    # 监管人-选择按钮
    jianguanren = (By.XPATH,'//label[text()="监管人："]/following-sibling::button')
    # 徐蕾勾选
    xulei = (By.XPATH,'//span[text()="徐蕾"]/../../span[@class="button chk checkbox_false_full"]')
    # 监管确定
    jianguan_sure = (By.XPATH,'//div[@class="popup"]//span[text()="确定"]')
    # 创建按钮
    create_button = (By.XPATH,'//button[text()="创建"]')

    # '绩效管理'定位
    jixiaoguanli_loc = (By.XPATH,'//span[contains(text(),"绩效管理")]/parent::a')
    # 项目名称-测试_光伏名称
    guangfuname = (By.XPATH,'//tr[1]//span[contains(text(),"光伏工程")]/parent::td')
    # 发起审批
    faqi_shenpi = (By.XPATH,'//span[text()="发起审批"]')
    # 勾选 '01-设计输入资料'
    designfile = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 选择卷册确定按钮
    choose_file_surebutton = (By.XPATH,'//div[contains(text(),"标识")]/following-sibling::div/span[text()="确定"]')
    # 点击第一个卷册名称
    first_file_name = (By.XPATH,'//tr[@class][1]//td[2]')
    # 编辑按钮
    editbutton = (By.XPATH,'//span[text()="编辑"]')
    # 恢复初始
    huifuchushi = (By.XPATH,'//span[text()="恢复初始"]')
    # 确定按钮
    surebutton = (By.XPATH,'//div[@class="box box1 por"]//span[text()="确定"]')
    # 主设人-标准工日
    zhu_biao = (By.XPATH,'//td[@title="主设人"]/parent::tr/td[5]')
    # 设计人-标准工日
    she_biao = (By.XPATH,'//div[@class="list list1 bd-e"]//tr[@class][3]//td[5]')
    # 标准总共日
    biaozhun_zonggongri = (By.XPATH,'//span[contains(text(),"标准总工日")]/span')
    # 提报总共日
    tibao_zonggongri = (By.XPATH,'//span[contains(text(),"提报总工日")]/span')
    # 标准总共日
    biaozhun_zonggongri2 = (By.XPATH,'//b[contains(text(),"标准工日")]/following-sibling::span')
    # 提报总共日
    tibao_zonggongri2 = (By.XPATH,'//b[contains(text(),"提报工日")]/following-sibling::span')
    # 项目成员
    photovaltaicmember = (By.XPATH,'//span[text()="项目成员"]/parent::span/parent::li')

    """发起审批各个勾选框的属性"""
    # 01设计输入资料勾选框
    box_01 = (By.XPATH,'//a[@title="01-设计输入资料"]/parent::li//span[@id="team-tree3_2_check"]')
    # 04-前期阶段批复意见 勾选框
    box_pifu = (By.XPATH,'//a[@title="04-前期阶段批复意见"]/parent::li//span[@id="team-tree3_3_check"]')
    # 06-其他资料 勾选框
    box_06 = (By.XPATH,'//a[@title="06-其他资料"]/parent::li//span[@id="team-tree3_4_check"]')
    # 02-前期阶段收口文件 勾选框
    box_shoukou = (By.XPATH,'//a[@title="02-前期阶段收口文件"]/parent::li//span[@id="team-tree3_5_check"]')
    # 01-地质测量水文资料 勾选框
    box_dizhi = (By.XPATH,'//a[@title="01-地质测量水文资料"]/parent::li//span[@id="team-tree3_6_check"]')
    # 05-原始资料收集文件 勾选框
    box_yuanshi = (By.XPATH,'//a[@title="05-原始资料收集文件"]/parent::li//span[@id="team-tree3_7_check"]')
    # 03-前期阶段评审意见 勾选框
    box_pingshen = (By.XPATH,'//a[@title="03-前期阶段评审意见"]/parent::li//span[@id="team-tree3_8_check"]')
    # 取消按钮
    cancle = (By.XPATH,'//p[contains(text(),"已发起绩效")]/parent::div//span[text()="取消"]')


    """
    我的工作
    """
    # 我的工作
    mywork_loc = (By.XPATH, '//span[contains(text(),"我的工作")]/parent::a')
    # 校审
    jiaoshen_loc = (By.XPATH,'//span[text()="校审"]/parent::a')
    # 空数据
    liucheng_null = (By.XPATH,'//p[contains(text(),"无匹配")]')
    # 所属项目名称
    suoshuxiangmu = (By.XPATH,'//tr[@class]//td[3]')
    suoshuxiangmu2 = (By.XPATH,'//tr[@class]//td[3]')
    # 我发起的流程列表
    faqiliucheng_list = (By.XPATH,'//tr[@class]')
    # 发起流程
    faqiliucheng = (By.XPATH,'//span[contains(text(),"发起流程")]')
    # 选择所属项目
    project_choose = (By.XPATH,'//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择光伏工程
    choose_netproject = (By.XPATH,'//div[contains(text(),"测试_光伏工程")]/parent::td/parent::tr')
    # 确定按钮
    project_sure_button = (By.XPATH,'//button[@class="danger yes"]')
    # 选择卷册按钮
    choose_file_button = (By.XPATH,'//span[text()="选择卷册"]')
    # 01设计输入资料勾选
    designfilegouxuan = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 同步校审文件勾选
    tongbujiaoshen_gouxuan = (By.XPATH,'//label[text()="同步校审文件"]/span')
    # 确定按钮
    surebutton = (By.XPATH,'//label[text()="同步校审文件"]/following-sibling::span[text()="确定"]')
    # 计划完成时间
    plan_finish_time = (By.XPATH,'//label[text()="计划完成时间："]/following-sibling::div//input')
    # 时间确定按钮
    time_sure = (By.XPATH,'//span[text()="清空"]/following-sibling::span')
    # 校审设计说明输入框
    jishenshuoming = (By.XPATH,'//textarea[@placeholder="请输入说明"]')
    # 确认人选择按钮
    sureperson_choose = (By.XPATH,'//label[text()="确认人："]/following-sibling::div//span[text()="选择"]')
    # 海若梦选择
    hairuomeng = (By.XPATH,'//span[@id="managerTree_8_check"]')
    # 海清选择
    haiqing = (By.XPATH,'//span[@id="managerTree_3_check"]')
    # 海清选择
    haiqing2 = (By.XPATH,'//span[text()="海清"]/parent::a/parent::li/span[@class="button chk checkbox_false_full"]')
    # 确定按钮
    person_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]/span')
    huiqian_new = (By.XPATH,'//span[text()="跳过会签阶段"]/following-sibling::label/span')
    # 五审人选择按钮
    wushen_choosebutton = (By.XPATH,'//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    wushen_hairuomeng = (By.XPATH,'//span[@id="managerTree_9_check"]')
    # 五审确定按钮
    wushen_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 设计校审文件添加按钮
    jiaoshenfile_add = (By.XPATH,'//label[text()="设计校审文件："]/following-sibling::div//span[text()="+添加"]')
    # 上传文件按钮
    upload_file = (By.XPATH,'//button[text()="上传文件"]')
    # 上传文件send_keys方法
    uploadfile_send = (By.XPATH,'//input[@id="uploadFileFoot"]')
    # 确定按钮
    file_sure_button = (By.XPATH,'//button[text()="确定"]')
    # 发起流程
    faqi_liucheng = (By.XPATH,'//button[text()="发起流程"]')
    # 五审人的五审状态
    wushenren_approvestate = (By.XPATH,'//tr[@class]//td[12]')
    wushenren_approvestate2 = (By.XPATH,'//tr[@class]//td[12]')

    # 退出按钮
    ph_logout = (By.XPATH,'//span[text()="退出"]/parent::a')

    """
     五审人登陆元素定位
     """
    # 待处理按钮
    ph_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    ph_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    ph_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    ph_wushenren_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--01-设计输入资料"]
    ph_file = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 五审
    ph_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 全部通过
    ph_all_pass = (By.XPATH, '//button[text()="全部通过"]')
    # 五审审批通过确定
    ph_wushen_sure = (By.XPATH, '//button[text()="确定"]')
    # 待处理空数据
    ph_nulldatas = (By.XPATH, '//p[contains(text(),"无匹配数据")]')
    # 已处理
    ph_dealed_button = (By.XPATH, '//button[text()="已处理"]')
    # 已处理校审名称
    ph_dealed_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 已处理了所属项目
    ph_dealed_suoshu_project = (By.XPATH, '//tr[@class][1]//td[3]')
    # 已处理五审状态
    ph_dealed_wushen_state = (By.XPATH, '//tr[@class][1]//td[12]')
    # 共XX行
    all_datas = (By.XPATH,'//a[contains(text(),"共")]')

    # 项目详情中的'设计卷册'
    design_file = (By.XPATH,'//span[text()="设计卷册"]/parent::span/parent::li')
    # 点击'01设计输入资料'进入二次文件夹
    file_input = (By.XPATH,'//span[text()="01-设计输入资料"]')
    # 上传文件send_keys方法
    uploadfile2_send = (By.XPATH,'//input[@type="file"]')
    # 上传完文件 获取文件名称text
    uploadedfilename = (By.XPATH,'//span[contains(text(),"脚本")]')
    uploadedfilename2 = (By.XPATH,'//tr[2]//span[contains(text(),"脚本")]')
    # 设计卷册上传文件后，文件版本号
    file_version = (By.XPATH,'//tr[@class][1]/td[6]')
    file_version2 = (By.XPATH,'//tr[2]//td[6]')


    """
    我发起的 元素定位
    """
    # 校审名称
    ph_faqi_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    ph_faqi_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    ph_faqi_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    ph_faqi_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 确认人状态
    ph_sure_state = (By.XPATH,'//tr[@class][1]//td[13]')


    """发起人发起确认"""
    # 设计校审名称--01-设计输入资料"]
    bfile = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 发起确认按钮
    b_faqisure = (By.XPATH,'//span[text()="发起确认"]')
    # 发起按钮
    b_faqi = (By.XPATH,'//button[text()="发起"]')
    # 校审名称
    b_faqi_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    b_faqi_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    b_faqi_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    b_faqi_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 待处理按钮
    b_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 已处理
    b_dealed_button = (By.XPATH, '//button[text()="已处理"]')


    """确认人海清"""
    # 校审名称
    s_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    s_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    s_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    s_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 七审状态
    s_qishen_state = (By.XPATH,'//tr[@class][1]//td[14]')
    # 确认人
    s_sure_state = (By.XPATH,'//tr[@class][1]//td[15]')
    # 设计校审名称--01-设计输入资料"]
    sfile = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 确认按钮
    s_surebutton = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="确认"]')
    # 全部通过按钮
    s_allpassbutton = (By.XPATH,'//button[text()="全部通过"]')
    # 确定按钮
    s_sure_button = (By.XPATH,'//button[text()="确定"]')

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH,'//span[text()="测试_光伏工程"]/ancestor::ul//span[text()="删除"]')
    delete2_loc = (By.XPATH,'//span[text()="测试_光伏工程2"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH,'//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH,'//div[text()="删除成功！"]')


    """归档"""
    # 归档管理
    guidang_guanli = (By.XPATH,'//span[contains(text(),"归档管理")]/parent::a')
    # 发起归档
    faqi_guidang = (By.XPATH,'//span[contains(text(),"发起归档")]')
    # 归档：项目名称
    guidang_filename = (By.XPATH,'//tr[@class][1]/td[2]')
    # 归档项目名称
    guidang_filename2 = (By.XPATH,'//div[@id="popup_list_id"]//tr[@class][1]/td[2]')
    # 归档提示语
    guidang_tishi = (By.XPATH,'//div[@class="prompt"]/div')
    # 归档-审批人员
    guidang_person = (By.XPATH,'//div[@class="popup"]//div[@class="lh-30 mb-10"]')
    guidang_person1 = (By.XPATH,'//label[text()="审批人员："]/following-sibling::div//span')
    # 所属项目后的"选择"
    choice = (By.XPATH,'//label[text()="所属项目："]/following-sibling::div//span[text()="选择"]')
    # 弹框关闭按钮
    closebutton = (By.XPATH,'//span[text()="✕"]')
    # 归档项目勾选
    guidang_gouxuan = (By.XPATH,'//span[@class="cp su2-radio-left"]')
    guidang_gouxuan1 = (By.XPATH,'//span[text()="测试_光伏工程"]')
    # 确定按钮
    sureb = (By.XPATH,'//span[text()="确定"]')
    # 监管人员
    jianguan_person = (By.XPATH,'//div[@class="lh-30 mb-10"]')
    # 归档确定
    guidang_sure = (By.XPATH,'//span[text()="确定"]')
    # 发起归档按钮
    faqiguidang = (By.XPATH,'//span[text()="保存"]/following-sibling::span[text()="发起归档"]')
    # 归档第一条记录项目名称
    first_guidang_name = (By.XPATH,'//tr[@class][1]/td[2]')
    # 归档第一条记录归档版本
    first_guidang_version = (By.XPATH,'//tr[@class][1]/td[8]')
    # 归档第一条记录审批人
    first_guidang_approver = (By.XPATH,'//tr[@class][1]/td[10]')
    # 归档第一条记录归档状态
    first_guidang_state = (By.XPATH,'//tr[@class][1]/td[11]')

    # 提交审批按钮
    submit_approve = (By.XPATH,'//span[text()="提交审批"]')
    # 韩正勾选框
    hanzheng = (By.XPATH,'//span[text()="韩正"]/parent::a/parent::li/span[@class="button chk radio_false_full"]')
    # 选择人员确定按钮
    chooseperson_sure = (By.XPATH,'//div[@class="frameView-item txt-c"]//span[text()="确定"]')
    # 成功 提示语
    success_info = (By.XPATH,'//div[@class="prompt-txt"]')
    # 取消申请
    apply_cancle = (By.XPATH,'//span[text()="取消申请"]')


    """监管人"""
    # '我审批的'按钮
    s_myapprove_button = (By.XPATH, '//span[text()="我审批的"]')
    # 我审批的第一条记录项目名称
    s_myapprove_projectname = (By.XPATH, '//tr[@class][1]//td[2]')
    # 我审批的第一条记录项目归档版本
    s_myapprove_version = (By.XPATH, '//tr[@class][1]//td[8]')
    # 我审批的第一条记录提交人
    s_tijiaoren = (By.XPATH,'//tr[@class][1]//td[9]')
    # 我审批的第一条记录归档状态
    s_approvestate = (By.XPATH,'//tr[@class][1]//td[10]')
    # 我审批的第一条记录审批时间
    s_approvetime = (By.XPATH,'//tr[@class][1]//td[12]')

    # '我监管的'按钮
    j_myjianguan_button = (By.XPATH, '//span[text()="我监管的"]')
    # 我监管的第一条记录项目名称
    j_myjianguan_projectname = (By.XPATH, '//tr[@class][1]//td[2]')
    # 我监管的第一条记录提交人
    j_tijiaoren = (By.XPATH,'//tr[@class][1]//td[9]')
    # 我监管的第一条记录监管人
    j_jianguan = (By.XPATH,'//tr[@class][1]//td[10]')
    # 我监管的第一条记录归档状态
    j_approvestate = (By.XPATH,'//tr[@class][1]//td[11]')
    # 我监管的第一条记录审批时间
    j_approvetime = (By.XPATH,'//tr[@class][1]//td[13]')
    # 我监管的第一条记录归档版本
    j_version = (By.XPATH,'//tr[@class][1]//td[8]')

    """监管人审批"""
    # 通过
    approve_pass = (By.XPATH,'//span[text()="通过"]')
    # 确定
    approve_sure = (By.XPATH,'//button[text()="确定"]')
    # 我审批的 所有数据
    s_all_datas = (By.XPATH, '//tr[@class]')

    """取消流程"""
    # 设计校审名称
    shejijiaoshen_quxiao = (By.XPATH,'//span[text()="01-设计输入资料"]')
    # 取消
    quxiao_quxiao = (By.XPATH,'//span[text()="取消"]')
    # 确定
    queding_quxiao = (By.XPATH,'//button[text()="确定"]')
    # 取消成功文本值
    quxiaochenggong_text = (By.XPATH,'//div[@class="prompt-txt"]')
    # 重新发起流程文本值
    chongxin_wenbenzhi = (By.XPATH,'//span[text()="重新发起流程"]')
    # 发起流程
    faqi_liucheng2 = (By.XPATH,'//button[text()="发起流程"]')
    # 流程发起成功文本值
    liucheng_text = (By.XPATH,'//div[@class="prompt"]')
    # 我发起的 项目列表
    project_list = (By.XPATH,'//tr[@class]')






