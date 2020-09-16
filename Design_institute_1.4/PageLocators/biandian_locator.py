from selenium.webdriver.common.by import By
class IndexBianPageLocator:
    """
    首页添加项目元素定位
    """
    # 首页'工作台'菜单定位
    workplatform_loc = (By.XPATH, '//span[contains(text(),"工作台")]')
    # '项目管理'定位
    projectmanager_loc = (By.XPATH,'//span[contains(text(),"项目管理")]/parent::a')
    # '项目台账'定位
    projectplatform_loc = (By.XPATH,'//span[contains(text(),"项目台账")]/parent::a')
    # '项目台账'第一个项目名称
    first_project_name = (By.XPATH,'//div[@class="pjlist-box mt-10"][1]//div[@class="left"]//span[@class="prls-icon"]/following-sibling::span[1]')
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
    """
    变电工程元素定位
    """
    # 变电工程
    biandianproject_loc = (By.XPATH,'//a[@title="变电工程"]/parent::li')
    # 工程类型选项
    projecttypechoice_loc = (By.XPATH,'//label[contains(text(),"工程类型")]/following-sibling::div')
    # 建设性质选择框
    consult_choose_box = (By.XPATH,'//label[text()="建设性质："]/following-sibling::div')
    # 建设性质选项
    consult_xingzhi = (By.XPATH,'//label[text()="建设性质："]/parent::li//ul')
    # 工程类型-户内勾选框
    hunei = (By.XPATH,'//label[text()="户内"]/span')
    # 设计阶段-下拉框
    design_box = (By.XPATH,'//label[text()="设计阶段："]/following-sibling::div')
    # 设计阶段-竣工图选项
    jungongtu = (By.XPATH,'//a[@title="竣工图"]/parent::li')
    # 电压等级选择框
    dianya_choose_box = (By.XPATH,'//label[text()="电压等级："]/following-sibling::div')
    # 电压等级-35kv选项
    kv35 = (By.XPATH,'//a[@title="35kV"]/parent::li')
    # 建设性质-变电新建勾选框
    biandian = (By.XPATH,'//label[text()="变电新建"]/span')
    # 选择成员
    choose_member = (By.XPATH,'//button[text()="选择成员"]')
    # 设总
    shezong = (By.XPATH,'//li[text()="设总"]')
    # 添加成员
    add_member = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 员工姓名/手机号输入框
    name_input = (By.XPATH, '//input[@id="searchId"]')
    # 张无忌 勾选框
    zhangwuji_gouxuan = (By.XPATH, '//span[@id="team-tree1_812_check"]')
    # 确定按钮
    sure_button = (By.XPATH, '//button[text()="确定"]')
    # 海清 勾选框
    haiqing_chooose = (By.XPATH, '//span[@id="team-tree1_7_check"]')
    # 总工
    zonggong = (By.XPATH,'//li[text()="总工"]')
    # 项目经理
    project_manager = (By.XPATH,'//li[text()="项目经理"]')
    # 添加成员
    addpeople = (By.XPATH,'//span[text()="添加成员"]')
    # 海若梦 勾选
    hairuomeng_choose = (By.XPATH,'//span[@id="team-tree1_8_check"]')
    # 徐鸿磊勾选
    xuhonglei = (By.XPATH,'//span[@id="team-tree1_3_check"]')
    # 设置节点按钮
    setnode_button = (By.XPATH, '//button[text()="设置节点"]')
    # 01-设计输入资料  勾选
    input01_file = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 01-设计输入资料 选择按钮
    design_input = (By.XPATH,'//a[@id="team-tree3_2_a"]//b')
    # 01-设计输入资料  选择海清
    design_choice = (By.XPATH,'//span[@id="team-tree1_6_check"]')
    # 确定按钮
    b_sure_button1 = (By.XPATH, '//button[text()="确定"]')
    # 设计校审 勾选
    shejijiaoshen = (By.XPATH,'//label[text()="设计校审"]/span')
    # 设计校审级别勾选框
    jiaoshenlevel = (By.XPATH,'//div[@id="children-span"]/div[@class="su_form_control su_select_box"]')
    # 1级
    level_1 = (By.XPATH,'//a[@title="1级"]')
    # 无
    null = (By.XPATH,'//a[@title="无"]')
    # 跳过会签阶段 勾选
    huiqianjieduan = (By.XPATH,'//label[text()="可跳过会签阶段"]/span')
    # 可低于标准级别 勾选
    diyubiaozhun = (By.XPATH,'//label[text()="可低于标准级别"]/span')
    # 开始时间
    start_time = (By.XPATH,'//span[text()="—"]/preceding-sibling::div')
    # 结束时间
    end_time = (By.XPATH,'//span[text()="—"]/following-sibling::div')
    # 时间确定按钮
    start_time_sure = (By.XPATH,'//span[text()="—"]/preceding-sibling::div//span[text()="确定"]')
    # 时间确定按钮
    end_time_sure = (By.XPATH,'//span[text()="—"]/following-sibling::div//span[text()="确定"]')
    # 创建按钮
    create_button = (By.XPATH,'//button[text()="创建"]')
    # 共XX行
    all_datas = (By.XPATH,'//a[contains(text(),"共")]')
    """
    绩效管理
    """
    # '绩效管理'定位
    jixiaoguanli_loc = (By.XPATH, '//span[contains(text(),"绩效管理")]/parent::a')
    # 项目名称-测试_变电工程
    biandian_name = (By.XPATH, '//tr[1]//span[contains(text(),"变电工程")]/parent::td')
    # 发起审批
    faqi_shenpi = (By.XPATH, '//span[text()="发起审批"]')
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

    # 前期阶段批复意见
    pifu_gouxuan = (By.XPATH,'//span[@id="team-tree3_3_check"]')
    # 01设计输入资料
    inputfile01 = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 确定按钮
    sure = (By.XPATH,'//p[contains(text(),"已发起绩效")]/parent::div//span[text()="确定"]')
    sure1 = (By.XPATH,'//div[@id="selectRolePersonTree"]/following-sibling::div/span[text()="确定"]')
    # 取消按钮
    cancle = (By.XPATH,'//p[contains(text(),"已发起绩效")]/parent::div//span[text()="取消"]')
    # 卷册名称
    file_name = (By.XPATH,'//tr[@class][1]/td[2]')
    # 额外系数
    ewai_xishu = (By.XPATH,'//span[text()="额外系数："]/span')
    # 最终难易系数
    zuizhong_nanyi_xishu = (By.XPATH,'//span[text()="最终难易系数："]/span')
    # 标准总工日
    biaozhun_zonggongri = (By.XPATH,'//span[text()="标准总工日："]/span')
    # 标准工日
    biaozhun_gongri = (By.XPATH,'//b[text()="标准工日："]/../span')
    # 提报总工日
    tibao_zonggongri = (By.XPATH,'//span[text()="提报总工日："]/span')
    # 提报工日
    tibao_gongri = (By.XPATH,'//b[text()="提报工日："]/../span')

    # 编辑按钮
    edit_button = (By.XPATH, '//span[text()="编辑"]')
    # 我知道了
    i_know = (By.XPATH, '//span[text()="我知道了"]')
    # 调整系数按钮
    edit_xishu_button = (By.XPATH, '//div//span[text()="恢复初始"]/following-sibling::span[text()="系数调整"]')
    # 保存数据按钮
    save_data_button = (By.XPATH, '//div//span[text()="恢复初始"]/following-sibling::span[text()="保存数据"]')
    # 退出编辑按钮
    cancle_edit_button = (By.XPATH, '//div//span[text()="恢复初始"]/following-sibling::span[text()="退出编辑"]')
    # 提交审批按钮
    tijiao_shenpi = (By.XPATH,'//span[text()="提交审批"]')
    # 韩正
    hanzheng1 = (By.XPATH,'//a[@title="韩正"]/preceding-sibling::span[@class="button chk radio_false_full"]')
    hanzheng13 = (By.XPATH,'//a[@title="韩正"]/preceding-sibling::span[@class="button chk radio_false_full"]')
    hanzheng12 = (By.XPATH,'//span[text()="韩正"]/../preceding-sibling::span[@treenode_check]')
    # 系数调整输入框
    xishu_input = (By.XPATH, '//div[@style="height: 240px;"]//input')
    # 确定按钮
    sure_button_xishu = (By.XPATH, '//div[@style="height: 240px;"]//span[text()="确定"]')
    # 提示语
    prom_info = (By.XPATH, '//div[@class="prompt-txt"]')
    # 取消按钮
    cancle_button_xishu = (By.XPATH, '//div[@style="height: 240px;"]//span[text()="取消"]')
    # 项目经理输入框
    man_input = (By.XPATH, '//table[@class="text-left table table-hover su-grid"]//tr[2]/td[8]/input')


    """"""
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
    suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 我发起的流程列表
    faqiliucheng_list = (By.XPATH,'//tr[@class]')
    # 发起流程
    faqiliucheng = (By.XPATH,'//span[contains(text(),"发起流程")]')
    # 选择所属项目
    project_choose = (By.XPATH,'//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择变电工程
    choose_biandianproject = (By.XPATH,'//div[contains(text(),"变电工程")]/parent::td/parent::tr')
    # 确定按钮
    project_sure_button = (By.XPATH,'//button[@class="danger yes"]')
    # 选择卷册
    choose_file_button = (By.XPATH,'//span[text()="选择卷册"]')
    # 01设计输入资料
    input_file = (By.XPATH,'//span[@id="team-tree3_2_check"]')
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
    # 海清选择
    haiqing_choose = (By.XPATH,'//span[@id="managerTree_6_check"]')
    # 确定按钮
    person_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]/span')
    huiqian_new = (By.XPATH,'//span[text()="跳过会签阶段"]/following-sibling::label//span')
    # 五审人选择按钮
    wushen_choosebutton = (By.XPATH,'//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    wushenhairuomeng_choose = (By.XPATH,'//span[@id="managerTree_16_check"]')
    # 五审确定按钮
    wushen_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 设计校审文件添加按钮
    jiaoshenfile_add = (By.XPATH,'//label[text()="设计校审文件："]/following-sibling::div//span[text()="+添加"]')
    # 上传文件按钮
    upload_file = (By.XPATH,'//button[text()="上传文件"]')
    # 上传文件send_keys方法
    uploadfile_send = (By.XPATH, '//input[@id="uploadFileFoot"]')
    # 确定按钮
    file_sure_button = (By.XPATH,'//button[text()="确定"]')
    # 发起流程
    faqi_liucheng = (By.XPATH,'//button[text()="发起流程"]')
    # 五审人的五审状态
    wushenren_approvestate = (By.XPATH,'//tr[@class][1]//td[12]')
    # 确认人状态
    sure_state = (By.XPATH,'//tr[@class][1]//td[8]')
    # 退出按钮
    ph_logout = (By.XPATH,'//span[text()="退出"]/parent::a')
    """
    五审人登陆元素定位
    """
    # 待处理按钮
    b_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    b_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    b_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    b_wushenren_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--01-设计输入资料
    b_file = (By.XPATH, '//tr[@class][1]//td[2]')
    # 五审
    b_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 确认
    b_sure_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="确认"]')
    # 确认
    b_sure_button2 = (By.XPATH, '//button[text()="确定"]')
    # 全部通过
    b_all_pass = (By.XPATH, '//button[text()="全部通过"]')
    # 全部退回
    b_all_tuihui = (By.XPATH, '//button[text()="全部退回"]')
    # 五审审批通过确定
    b_wushen_sure = (By.XPATH, '//button[text()="确定"]')
    # 待处理空数据
    b_nulldatas = (By.XPATH, '//p[contains(text(),"无匹配数据")]')
    # 已处理
    b_dealed_button = (By.XPATH, '//button[text()="已处理"]')
    # 已处理校审名称
    b_dealed_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 已处理了所属项目
    b_dealed_suoshu_project = (By.XPATH, '//tr[@class][1]//td[3]')
    # 已处理五审状态
    b_dealed_wushen_state = (By.XPATH, '//tr[@class][1]//td[12]')
    # 已处理确认人状态
    b_dealed_sure_state = (By.XPATH, '//tr[@class][1]//td[15]')

    """
    我发起的 元素定位
    """
    # 校审名称
    b_faqi_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    b_faqi_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    b_faqi_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    b_faqi_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')
    # 确认人状态
    b_faqi_sure_state = (By.XPATH,'//tr[@class][1]//td[8]')

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
    审批人'韩正'元素定位
    """
    # 我监管的
    jianguan = (By.XPATH,'//span[text()="我监管的"]')
    # 项目名称'测试线路工程'
    route_project = (By.XPATH,'//tr[@class][1]/td[2]')
    # 提报比例链接
    tibaobili_link_shen = (By.XPATH, '//tr[@class][1]//td[2]/span')
    # 01设计输入资料
    file_01 = (By.XPATH,'//span[text()="01-设计输入资料"]')
    # 通过 按钮
    pass_button = (By.XPATH,'//span[text()="通过"]')
    # 确定按钮
    pass_sure = (By.XPATH,'//span[contains(text(),"通过后")]/parent::div/following-sibling::div/span[text()="确定"]')
    # 成功
    """我监管的"""
    b_pass_success = (By.XPATH,'//div[@class="prompt-txt"]')
    # 审批时间
    b_pass_time = (By.XPATH,'//tr[@class][1]/td[13]')
    # 所属项目名称
    b_projectname = (By.XPATH,'//tr[@class][1]/td[2]')
    # 参审卷册/所属比例
    b_rate = (By.XPATH,'//tr[@class][1]/td[3]')
    # 审批状态
    b_approve_state = (By.XPATH,'//tr[@class][1]/td[11]')

    """我审批的"""
    # 我审批的
    my_approve = (By.XPATH,'//span[text()="我审批的"]')
    # 审批时间
    s_pass_time = (By.XPATH, '//tr[@class][1]/td[12]')
    # 所属项目名称
    s_projectname = (By.XPATH, '//tr[@class][1]/td[2]')
    # 参审卷册/所属比例
    s_rate = (By.XPATH, '//tr[@class][1]/td[3]')
    # 审批状态
    s_approve_state = (By.XPATH, '//tr[@class][1]/td[10]')

    # 线路工程_已通过
    passed = (By.XPATH,"//span[contains(text(),'测试_线路工程')]/parent::td/parent::tr/td[10]")
    # 序号
    num = (By.XPATH,"//span[contains(text(),'测试_线路工程')]/parent::td/parent::tr/td[1]")
    # 第二次提报比例
    second_rate = (By.XPATH,'//input[@disabled="disabled"]')
    # 第二次提报比例属性框
    secondrate = (By.XPATH,'//b[text()="提报比例："]/following-sibling::input')

    """
    我的工作
    """
    # 我的工作
    b_mywork_loc = (By.XPATH, '//span[contains(text(),"我的工作")]/parent::a')
    # 校审
    b_jiaoshen_loc = (By.XPATH, '//span[text()="校审"]/parent::a')
    # 空数据
    b_liucheng_null = (By.XPATH, '//p[contains(text(),"无匹配")]')
    # 所属项目名称
    b_suoshuxiangmu = (By.XPATH, '//tr[@class]//td[3]')
    # 我发起的流程列表
    b_faqiliucheng_list = (By.XPATH, '//tr[@class]')
    # 发起流程
    b_faqiliucheng = (By.XPATH, '//span[contains(text(),"发起流程")]')
    # 选择所属项目
    b_project_choose = (By.XPATH, '//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择线路工程
    b_choose_routeproject = (By.XPATH, '//div[contains(text(),"测试_线路工程")]/parent::td/parent::tr')
    # 确定按钮
    b_project_sure_button = (By.XPATH, '//button[@class="danger yes"]')
    # 选择卷册按钮
    b_choose_file_button = (By.XPATH, '//span[text()="选择卷册"]')
    # 01设计输入资料勾选
    b_designfilegouxuan = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 同步校审文件勾选
    b_tongbujiaoshen_gouxuan = (By.XPATH, '//label[text()="同步校审文件"]/span')
    # 确定按钮
    b_surebutton = (By.XPATH, '//label[text()="同步校审文件"]/following-sibling::span[text()="确定"]')
    # 计划完成时间
    b_plan_finish_time = (By.XPATH, '//label[text()="计划完成时间："]/following-sibling::div//input')
    # 时间确定按钮
    b_time_sure = (By.XPATH, '//span[text()="清空"]/following-sibling::span')
    # 校审设计说明输入框
    b_jishenshuoming = (By.XPATH, '//textarea[@placeholder="请输入说明"]')
    # 确认人选择按钮
    b_sureperson_choose = (By.XPATH, '//label[text()="确认人："]/following-sibling::div//span[text()="选择"]')
    # 海若梦选择
    b_hairuomeng = (By.XPATH, '//span[@id="managerTree_7_check"]')
    # 海清选择
    b_haiqing = (By.XPATH, '//span[@id="managerTree_3_check"]')
    # 确定按钮
    b_person_sure_button = (By.XPATH, '//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    b_huiqian = (By.XPATH, '//label[text()="跳过会签阶段"]/span')
    # 五审人选择按钮
    b_wushen_choosebutton = (By.XPATH, '//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    b_wushen_hairuomeng = (By.XPATH, '//span[@id="managerTree_9_check"]')
    # 五审确定按钮
    b_wushen_sure_button = (By.XPATH, '//center/span[text()="确定"]')
    # 设计校审文件添加按钮
    b_jiaoshenfile_add = (By.XPATH, '//label[text()="设计校审文件："]/following-sibling::div//span[text()="+添加"]')
    # 上传文件按钮
    b_upload_file = (By.XPATH, '//button[text()="上传文件"]')
    # 确定按钮
    b_file_sure_button = (By.XPATH, '//button[text()="确定"]')
    # 发起流程
    b_faqi_liucheng = (By.XPATH, '//button[text()="发起流程"]')
    # 五审人的五审状态
    b_wushenrenapprovestate = (By.XPATH, '//tr[@class]//td[12]')
    # 退出按钮
    b_logout = (By.XPATH, '//span[text()="退出"]/parent::a')
    # 发起确认按钮
    b_faqisure = (By.XPATH,'//span[text()="发起确认"]')
    # 发起按钮
    b_faqi = (By.XPATH,'//button[text()="发起"]')

    """
    五审人登陆元素定位
    """
    # 待处理按钮
    b_needdealbutton = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    b_needdealnum = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    b_needdealprojectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    b_wushen_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--01-设计输入资料"]
    bfile = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 五审
    b_wu_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 全部通过
    b_allpass = (By.XPATH, '//button[text()="全部通过"]')
    # 五审审批通过确定
    b_wu_sure = (By.XPATH, '//button[text()="确定"]')
    # 待处理空数据
    b_null_datas = (By.XPATH, '//p[contains(text(),"无匹配数据")]')
    # 已处理
    b_dealedbutton = (By.XPATH, '//button[text()="已处理"]')
    # 已处理校审名称
    b_dealedjiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 已处理了所属项目
    b_dealedsuoshu_project = (By.XPATH, '//tr[@class][1]//td[3]')
    # 已处理五审状态
    b_dealedwushen_state = (By.XPATH, '//tr[@class][1]//td[12]')
    # 共XX行
    b_alldatas = (By.XPATH, '//a[contains(text(),"共")]')

    # 提交审批按钮
    submit_approve = (By.XPATH,'//span[text()="提交审批"]')
    # 韩正勾选框
    hanzheng = (By.XPATH,'//span[@id="selectRolePersonTree_22_check"]')
    hanzheng1 = (By.XPATH,'//span[@id="selectRolePersonTree_22_check"]')
    # 选择人员确定按钮
    chooseperson_sure = (By.XPATH,'//div[@class="frameView-item txt-c"]//span[text()="确定"]')
    # 成功 提示语
    success_info = (By.XPATH,'//div[@class="prompt-txt"]')
    # 取消申请
    apply_cancle = (By.XPATH,'//span[text()="取消申请"]')

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH, '//span[text()="测试_变电工程"]/ancestor::ul//span[text()="删除"]')
    delete1_loc2 = (By.XPATH, '//span[text()="测试_变电工程2"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH, '//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH, '//div[text()="删除成功！"]')

    """后台系统"""
    # 用户名输入框
    h_name = (By.XPATH, '//input[@id="loginName"]')
    # 密码输入框
    h_pass = (By.XPATH, '//input[@id="password"]')
    # 登陆按钮
    h_loginbutton = (By.XPATH,'//span[@id="button"]')
    # 系统管理
    h_systemmanager = (By.XPATH,'//span[text()="系统管理"]')
    # 工日管理
    h_daymanager = (By.XPATH,'//a[text()="工日管理"]')
    # 质量评定管理
    h_zhiliang = (By.XPATH,'//label[text()="质量评定管理"]')
    # iframe
    h_iframeid = "div_grgl"
    # 项目类型选择框
    h_projectchoice = (By.XPATH,'//div[@id="projectType_chosen"]//b')
    # 项目类型输入框
    h_projectinput = (By.XPATH,'//div[@id="projectType_chosen"]//div[@class="chosen-search"]//input[@type="text"]')
    # 项目类型输入Enter
    h_enter = (By.XPATH,'//div[@id="projectType_chosen"]//div[@class="chosen-search"]//input[@type="text"]')
    # 是否参与选择框
    h_ifcanyu = (By.XPATH,'//select[@id="yesOrNo"]/following-sibling::div//b')
    # 是否参与输入框
    h_ifcanyuinput = (By.XPATH,'//div[@id="yesOrNo_chosen"]//input')
    # 是否参与回车
    h_ifcanyuenter = (By.XPATH,'//div[@id="yesOrNo_chosen"]//input')
    # 保存按钮
    h_savebutton = (By.XPATH,'//span[text()="保存"]')
    # 保存成功提示语
    h_savesucinfo = (By.XPATH,'//span[@class="label label-warning"]')
    # 是否参与文本
    h_ifcanyutext = (By.XPATH,'//div[@id="yesOrNo_chosen"]//a[@class="chosen-single"]')







