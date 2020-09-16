from selenium.webdriver.common.by import By
class IndexWaterPageLocator:
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
    水利咨询元素定位
    """
    # 水利咨询
    waterconsult_loc = (By.XPATH,'//a[@title="水利咨询工程"]/parent::li')
    # 工程类型选项
    projecttypechoice_loc = (By.XPATH,'//label[contains(text(),"工程类型")]/following-sibling::div')
    # 工程规模文本框
    project_area = (By.XPATH,'//label[text()="工程规模："]/following-sibling::div//span')
    # 工程投资文本框
    project_touzi = (By.XPATH,'//label[text()="工程投资："]/following-sibling::div//span')
    # 选择成员
    choose_member = (By.XPATH,'//button[text()="选择成员"]')
    # 施工组织设计专业负责人
    shigong_fuze = (By.XPATH,'//li[text()="施工组织设计专业负责人"]')
    # 施工组织设计专业设计人
    shigong_sheji = (By.XPATH,'//li[text()="施工组织设计专业设计人"]')
    # 征地移民专业设计人
    zhengdi_sheji = (By.XPATH,'//li[text()="征地移民专业设计人"]')
    # 征地移民专业负责人
    zhengdi_fuze = (By.XPATH,'//li[text()="征地移民专业负责人"]')
    # 添加成员
    add_member = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 员工姓名/手机号输入框
    name_input = (By.XPATH, '//input[@id="searchId"]')
    # 张无忌 勾选框
    zhangwuji_gouxuan = (By.XPATH, '//span[@id="team-tree1_841_check"]')
    # 确定按钮
    sure_button = (By.XPATH, '//button[text()="确定"]')
    # 海清 勾选框
    haiqing_chooose = (By.XPATH, '//span[@id="team-tree1_7_check"]')
    # 黄渤
    huangbo = (By.XPATH,'//span[@id="team-tree1_9_check"]')
    # 海若梦 勾选
    hairuomeng_choose = (By.XPATH,'//span[@id="team-tree1_8_check"]')
    # 徐鸿磊勾选
    xuhonglei = (By.XPATH,'//span[@id="team-tree1_3_check"]')
    # 王路勾选框
    wanglu_gouxuan = (By.XPATH,'//span[@id="team-tree1_797_check"]')
    # 设置节点按钮
    setnode_button = (By.XPATH, '//button[text()="设置节点"]')
    # 01设计输入资料  勾选
    design_inputfile = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 01设计输入资料  选择按钮
    design_choosebutton = (By.XPATH, '//a[@id="team-tree3_2_a"]//b')
    #  选择张无忌
    zhangwuji_choosebutton = (By.XPATH, '//span[@id="team-tree1_5_check"]')
    # 确定按钮
    water_sure_button = (By.XPATH, '//button[text()="确定"]')
    # 设计校审 勾选
    shejijiaoshen = (By.XPATH,'//label[text()="设计校审"]/span')
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
    # 创建按钮
    create_button = (By.XPATH,'//button[text()="创建"]')

    # 共XX行
    all_datas = (By.XPATH,'//a[contains(text(),"共")]')
    # '项目台账'--'无匹配数据！'
    nulldatas = (By.XPATH,'//div[@class="nodatap"]')

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
    # 选择规划咨询工程2
    choose_waterproject = (By.XPATH,'//div[contains(text(),"水利咨询工程")]/parent::td/parent::tr')
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
    # 徐鸿磊选择
    xuhonglei_choose = (By.XPATH,'//span[@id="managerTree_3_check"]')
    # 确定按钮
    person_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]/span')
    huiqian_new = (By.XPATH, '//span[text()="跳过会签阶段"]/following-sibling::label/span')
    # 五审人选择按钮
    wushen_choosebutton = (By.XPATH,'//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    wushenhairuomeng_choose = (By.XPATH,'//span[@id="managerTree_4_check"]')
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
    # 退出按钮
    ph_logout = (By.XPATH,'//span[text()="退出"]/parent::a')
    """
    五审人登陆元素定位
    """
    # 待处理按钮
    w_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    w_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    w_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    w_wushenren_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--01设计输入资料
    w_file = (By.XPATH, '//tr[@class][1]//td[2]')
    # 五审
    w_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 全部通过
    w_all_pass = (By.XPATH, '//button[text()="全部通过"]')
    # 五审审批通过确定
    w_wushen_sure = (By.XPATH, '//button[text()="确定"]')
    # 待处理空数据
    w_nulldatas = (By.XPATH, '//p[contains(text(),"无匹配数据")]')
    # 已处理
    w_dealed_button = (By.XPATH, '//button[text()="已处理"]')
    # 已处理校审名称
    w_dealed_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 已处理了所属项目
    w_dealed_suoshu_project = (By.XPATH, '//tr[@class][1]//td[3]')
    # 已处理五审状态
    w_dealed_wushen_state = (By.XPATH, '//tr[@class][1]//td[12]')

    """
    我发起的 元素定位
    """
    # 校审名称
    w_faqi_jiaoshenmingcheng = (By.XPATH,'//tr[@class][1]//td[2]')
    # 所属项目
    w_faqi_suoshuxiangmu = (By.XPATH,'//tr[@class][1]//td[3]')
    # 五审状态
    w_faqi_wushen_state = (By.XPATH,'//tr[@class][1]//td[12]')
    # 六审状态
    w_faqi_liushen_state = (By.XPATH,'//tr[@class][1]//td[13]')

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH, '//span[text()="测试_水利咨询工程"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH, '//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH, '//div[text()="删除成功！"]')




