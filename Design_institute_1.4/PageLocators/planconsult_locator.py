from selenium.webdriver.common.by import By
class IndexPlanPageLocator:
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
    规划咨询元素定位
    """
    # 规划咨询
    planconsult_loc = (By.XPATH,'//a[@title="规划咨询"]/parent::li')
    # 专题研究勾选框
    zhuantiyanjiu = (By.XPATH,'//label[text()="专题研究"]/span')
    # 新建区勾选
    gouxuan_xinjianqu = (By.XPATH,'//label[text()="新建区"]//span')
    # 工程类型选项
    projecttypechoice_loc = (By.XPATH,'//label[contains(text(),"工程类型")]/following-sibling::div')
    # 设计阶段--规划阶段
    designpro_log = (By.XPATH,'//label[contains(text(),"设计阶段")]/parent::li/div')
    # 建设性质选项
    constructnature_loc = (By.XPATH,'//label[contains(text(),"建设性质")]/following-sibling::div')
    # 选择成员
    choose_member = (By.XPATH,'//button[text()="选择成员"]')
    # 项目经理
    project_manager = (By.XPATH,'//li[text()="项目经理"]')
    # 项目经理
    zixunshi = (By.XPATH,'//li[text()="咨询师"]')
    # 规划专业设计人
    tour_design = (By.XPATH,'//li[text()="规划专业设计人"]')
    # 规划专业负责人
    plan_fuzeren = (By.XPATH,'//li[text()="规划专业负责人"]')
    # 添加成员
    add_member = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 员工姓名/手机号输入框
    name_input = (By.XPATH, '//input[@id="searchId"]')
    # 张无忌 勾选框
    zhangwuji_gouxuan = (By.XPATH, '//span[@id="team-tree1_814_check"]')
    # 确定按钮
    sure_button = (By.XPATH, '//button[text()="确定"]')
    # 海清 勾选框
    haiqing_chooose = (By.XPATH, '//a[@title="海清"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 黄渤
    huangbo = (By.XPATH,'//a[@title="黄渤"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 海若梦 勾选
    hairuomeng_choose = (By.XPATH,'//a[@title="海若梦"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 徐鸿磊勾选
    xuhonglei = (By.XPATH,'//a[@title="徐洪雷（恒华）"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 王路勾选框
    wanglu_gouxuan = (By.XPATH,'//a[@title="王路"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 设置节点按钮
    setnode_button = (By.XPATH, '//button[text()="设置节点"]')
    # 规划咨询报告  勾选
    planreport = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 规划咨询报告  选择按钮
    planreport_choosebutton = (By.XPATH, '//a[@id="team-tree3_2_a"]//b')
    # 规划咨询  选择'海若梦'
    planreport_hairuomeng_choosebutton = (By.XPATH, '//span[@id="team-tree1_6_check"]')
    # 确定按钮
    plan_sure_button = (By.XPATH, '//button[text()="确定"]')
    # 规划面积文本值
    planarea_loc = (By.XPATH,'//span[contains(text(),"规划面积")]')
    # 10KV线路文本值
    kv_loc = (By.XPATH,'//span[contains(text(),"10kV线路")]')
    # 规划面积输入框
    planarea_input = (By.XPATH,'//span[contains(text(),"规划面积")]/following-sibling::input')
    # 10kv线路输入框
    kv_input = (By.XPATH,'//span[contains(text(),"10kV")]/following-sibling::input')
    # 设计校审 勾选
    shejijiaoshen = (By.XPATH,'//label[text()="设计校审"]/span')
    # 设计校审级别勾选框
    jiaoshenlevel = (By.XPATH,'//div[@id="children-span"]/div[@class="su_form_control su_select_box"]')
    # 1级
    level_1 = (By.XPATH,'//a[@title="1级"]')
    # 跳过会签阶段 勾选
    huiqianjieduan = (By.XPATH,'//label[text()="可跳过会签阶段"]/span')
    huiqian_new = (By.XPATH, '//span[text()="跳过会签阶段"]/following-sibling::label/span')
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
    # '项目台账'--'无匹配数据！'
    nulldatas = (By.XPATH,'//div[@class="nodatap"]')
    # '绩效管理'定位
    jixiaoguanli_loc = (By.XPATH,'//span[contains(text(),"绩效管理")]/parent::a')
    # 项目名称-测试_规划咨询名称
    guangfuname = (By.XPATH,'//tr[1]//span[contains(text(),"咨询工程")]/parent::td')
    # 成品质量系数
    zhiliang = (By.XPATH,'//b[text()="成品质量系数："]/following-sibling::span')
    zhiliang4 = (By.XPATH,'//div[@class="list list1 bd-e"]//tr[@class][1]//td[6]')
    zhiliangs = (By.XPATH,'//tr[@class]/td[8]')
    # 发起审批
    faqi_shenpi = (By.XPATH,'//span[text()="发起审批"]')
    # 提报比例输入框
    tibao_rate = (By.XPATH,'//b[text()="提报比例："]/following-sibling::input')
    # 提报比例确定按钮
    tibao_sure = (By.XPATH,'//div[@class="setting_parameter_box h-100"]/parent::div/following-sibling::div/span[text()="确定"]')
    # 提报比例链接
    tibaobili_link = (By.XPATH,'//tr[@class][1]//td[2]/span')
    # 回路系数
    huilu_xishu = (By.XPATH,'//span[contains(text(),"回路系数")]')
    # 最终系数
    zuizhong_xishu = (By.XPATH,'//span[contains(text(),"最终系数")]')
    # 项目总标准工日
    project_all_days = (By.XPATH,'//span[contains(text(),"项目总标准")]')
    # 标准工日
    biaozhun_days = (By.XPATH,'//b[text()="标准工日："]/following-sibling::span')
    # 提报工日
    tibao_days = (By.XPATH,'//b[text()="提报工日："]/following-sibling::span')
    # 提报比例
    tibaobili = (By.XPATH,'//b[contains(text(),"提报比例")]/following-sibling::span')

    # 面积系数
    mianji_xishu = (By.XPATH,'//span[contains(text(),"面积系数")]')
    # 最终系数
    zuizhong_xishu2 = (By.XPATH,'//span[contains(text(),"最终系数")]')
    # 项目总标准工日
    project_all_days2 = (By.XPATH,'//span[contains(text(),"项目总标准")]')
    # 标准工日
    biaozhun_days2 = (By.XPATH,'//b[text()="标准工日："]/following-sibling::span')
    # 提报比例
    tibaobili2 = (By.XPATH,'//b[contains(text(),"提报比例")]/following-sibling::span')

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
    # 规划咨询报告
    guihua = (By.XPATH,'//td[@title="规划咨询报告"]/span')
    # 发起五审
    faqiwushen = (By.XPATH,'//span[text()="发起五审"]')
    # 点击输入内容
    clickinput = (By.XPATH,'//input[@placeholder="点击输入内容"]')
    # 修改标识下拉框
    biaoshixiala = (By.XPATH,'//span[text()="修改标识："]/following-sibling::div//i')
    # 确认标识下拉框
    surebiaoshixiala = (By.XPATH,'//span[text()="确认标识："]/following-sibling::div//i')
    # 回复文本框
    huifutext = (By.XPATH,'//span[text()="回复："]/following-sibling::div/textarea')
    # 意见文本框
    yijiantext = (By.XPATH,'//span[text()="意见："]/following-sibling::div/textarea')
    # 第一个标识符
    firstmark = (By.XPATH,'//ul[@class="bg-f bd-d design-check-icon-list"]/li[1]')
    # 第一个标识符
    firstmarks = (By.XPATH,'//div[@class="pull-left por w-p80"]//li[1]')
    # 保存按钮
    save_button = (By.XPATH,'//span[text()="保存"]')
    # 发起按钮
    faqi = (By.XPATH,'//button[text()="发起"]')
    # 选择所属项目
    project_choose = (By.XPATH,'//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择规划咨询工程2
    choose_planproject = (By.XPATH,'//div[contains(text(),"规划咨询工程2")]/parent::td/parent::tr')
    choose_planproject6 = (By.XPATH,'//div[contains(text(),"规划咨询工程6")]/parent::td/parent::tr')
    # 确定按钮
    project_sure_button = (By.XPATH,'//button[@class="danger yes"]')
    # 选择卷册按钮
    choose_file_button = (By.XPATH,'//span[text()="选择卷册"]')
    # 规划咨询报告勾选
    planconsultgouxuan = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 同步校审文件勾选
    tongbujiaoshen_gouxuan = (By.XPATH,'//label[text()="同步校审文件"]/span')
    # 确定按钮
    surebutton = (By.XPATH,'//label[text()="同步校审文件"]/following-sibling::span[text()="确定"]')
    # 计划完成时间
    plan_finish_time = (By.XPATH,'//label[text()="计划完成时间："]/following-sibling::div//input')
    # 当月
    current_month = (By.XPATH,'//span[@class="mouse-cp currentmonth"]')
    # 下月按钮
    lastmonth = (By.XPATH,'//span[@class="pull-right"]/i[@class="fa fa-chevron-circle-right mouse-cp"]')
    # 时间确定按钮
    time_sure = (By.XPATH,'//span[text()="清空"]/following-sibling::span')
    # 校审设计说明输入框
    jishenshuoming = (By.XPATH,'//textarea[@placeholder="请输入说明"]')
    # 确认人选择按钮
    sureperson_choose = (By.XPATH,'//label[text()="确认人："]/following-sibling::div//span[text()="选择"]')
    # 海清选择
    haiqing = (By.XPATH,'//span[@id="managerTree_3_check"]')
    # 确定按钮
    person_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]/span')
    # 五审人选择按钮
    wushen_choosebutton = (By.XPATH,'//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    wushen_hairuomeng = (By.XPATH,'//span[@id="managerTree_6_check"]')
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
    ph_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    ph_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    ph_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    ph_wushenren_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--规划咨询工程2
    ph_file = (By.XPATH, '//tr[@class][1]//td[2]')
    # 五审
    ph_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 全部通过
    ph_all_pass = (By.XPATH, '//button[text()="全部通过"]')
    # 全部退回
    ph_all_tuihui = (By.XPATH, '//button[text()="全部退回"]')
    # 添加意见
    addadvoice = (By.XPATH,'//span[text()="+添加意见"]')
    # 名称图号输入框
    tuhao = (By.XPATH,'//input[@name="tuhao"]')
    # 意见输入框
    yijian = (By.XPATH,'//input[@name="yijian"]')
    # 意见确定按钮
    yijian_sure = (By.XPATH,'//div[@class="text-center ptb-5 por"]//button[text()="确定"]')
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

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH, '//span[text()="测试_规划咨询工程"]/ancestor::ul//span[text()="删除"]')
    delete2_loc = (By.XPATH, '//span[text()="测试_规划咨询工程2"]/ancestor::ul//span[text()="删除"]')
    delete3_loc = (By.XPATH, '//span[text()="测试_规划咨询工程3"]/ancestor::ul//span[text()="删除"]')
    delete4_loc = (By.XPATH, '//span[text()="测试_规划咨询工程4"]/ancestor::ul//span[text()="删除"]')
    delete5_loc = (By.XPATH, '//span[text()="测试_规划咨询工程5"]/ancestor::ul//span[text()="删除"]')
    delete6_loc = (By.XPATH, '//span[text()="测试_规划咨询工程6"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH, '//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH, '//div[text()="删除成功！"]')

    # 设计校审名称--规划咨询报告"]
    bfile = (By.XPATH, '//span[text()="规划咨询报告"]')
    # 发起确认按钮
    b_faqisure = (By.XPATH,'//span[text()="发起确认"]')
    # 发起按钮
    b_faqi = (By.XPATH,'//button[text()="发起"]')

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
    sfile = (By.XPATH, '//span[text()="规划咨询报告"]')
    # 确认按钮
    s_surebutton = (By.XPATH,'//div[@class="bg-f text-right por"]//span[text()="确认"]')
    # 全部通过按钮
    s_allpassbutton = (By.XPATH,'//button[text()="全部通过"]')
    # 确定按钮
    s_sure_button = (By.XPATH,'//button[text()="确定"]')




