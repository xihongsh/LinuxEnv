from selenium.webdriver.common.by import By
class IndexRoutePageLocator:
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
    # '项目台账'列表数量
    project_list = (By.XPATH,'//div[@class="pjlist-box mt-10"]')
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
    线路工程元素定位
    """
    # 线路工程
    routeproject_loc = (By.XPATH,'//a[@title="线路工程"]/parent::li')
    # 工程类型选项
    projecttypechoice_loc = (By.XPATH,'//label[contains(text(),"工程类型")]/following-sibling::div')
    # 建设性质选择框
    consult_choose_box = (By.XPATH,'//label[text()="建设性质："]/following-sibling::div')
    # 建设性质选项
    consult_xingzhi = (By.XPATH,'//label[text()="建设性质："]/parent::li//ul')
    # 工程类型-架空勾选框
    jiakong = (By.XPATH,'//label[text()="架空"]/span')
    # 设计阶段-下拉框
    design_box = (By.XPATH,'//label[text()="设计阶段："]/following-sibling::div')
    # 设计阶段-施工图选项
    shigongtu = (By.XPATH,'//a[@title="施工图"]/parent::li')
    kexingxing_yanjiu = (By.XPATH,'//a[@title="可行性研究"]/parent::li')
    # 电压等级选择框
    dianya_choose_box = (By.XPATH,'//label[text()="电压等级："]/following-sibling::div')
    # 电压等级-35kv选项
    kv35 = (By.XPATH,'//a[@title="35kV"]/parent::li')
    kv110 = (By.XPATH,'//a[@title="110kV"]/parent::li')
    # 建设性质-新版绩效建设性质
    xinban = (By.XPATH,'//a[@title="新版绩效建设性质"]/parent::li')
    yitihua = (By.XPATH,'//a[@title="可研勘测设计一体化项目"]/parent::li')
    # 选择成员
    choose_member = (By.XPATH,'//button[text()="选择成员"]')
    # 设总
    shezong = (By.XPATH,'//li[text()="设总"]')
    # 项目经理
    xinagmujingli = (By.XPATH,'//li[text()="项目经理"]')
    # 线路电器设计人
    xianlu_shejiren = (By.XPATH,'//li[text()="线路电气-设计人"]')
    # 添加成员
    add_member = (By.XPATH,'//span[text()="添加成员"]/parent::li')
    # 员工姓名/手机号输入框
    name_input = (By.XPATH, '//input[@id="searchId"]')
    # 张无忌 勾选框
    zhangwuji_gouxuan = (By.XPATH, '//a[@title="张无忌"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 确定按钮
    sure_button = (By.XPATH, '//button[text()="确定"]')
    # 海清 勾选框
    haiqing_chooose = (By.XPATH, '//a[@title="海清"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 郑凯 勾选框
    zhengkai_chooose = (By.XPATH, '//a[@title="郑凯"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 龙美心
    longmeixin_choose = (By.XPATH,'//a[@title="龙美心"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 王祖蓝勾选框
    wangzulan = (By.XPATH,'//a[@title="王祖蓝"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 孙红雷勾选框
    sunhonglei = (By.XPATH,'//a[@title="孙红雷"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 总工
    zonggong = (By.XPATH,'//li[text()="总工"]')
    # 海若梦 勾选
    hairuomeng_choose = (By.XPATH,'//a[@title="海若梦"]/parent::li/span[@class="button chk checkbox_false_full"]')
    hairuomeng_choose2 = (By.XPATH,'//a[@title="海若梦"]/parent::li/span[@class="button chk radio_false_full"]')
    # 海清勾选
    haiqing = (By.XPATH,'//a[@title="海清"]/parent::li/span[@class="button chk radio_false_full"]')
    # 徐鸿磊勾选
    xuhonglei = (By.XPATH,'//a[@title="徐洪雷（恒华）"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 设置节点按钮
    setnode_button = (By.XPATH, '//button[text()="设置节点"]')
    # 01-设计输入资料  勾选
    input01_file = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 01-设计输入资料 选择按钮
    design_input = (By.XPATH,'//a[@id="team-tree3_2_a"]//b')
    # 04前期阶段批复意见
    pifu04 = (By.XPATH,'//a[@title="04-前期阶段批复意见"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 04前期阶段批复意见择按钮
    pifuchoose = (By.XPATH,'//a[@title="04-前期阶段批复意见"]/parent::li/a//b')
    # 03线路电气
    dianqi03 = (By.XPATH,'//a[@title="03-线路电气"]/parent::li/span[@class="button chk checkbox_true_full"]')
    # 03线路电气选择按钮
    dianqi03choose = (By.XPATH,'//a[@title="03-线路电气"]/parent::li/a//b')
    # 01-设计输入资料  选择王祖蓝
    design_choice = (By.XPATH,'//span[@id="team-tree1_10_check"]')
    design_choice2 = (By.XPATH,'//span[@id="team-tree1_4_check"]')

    # 确定按钮
    water_sure_button = (By.XPATH, '//button[text()="确定"]')
    # 设计费输入框
    design_cost = (By.XPATH,'//span[text()="设计费："]/parent::li//input')
    # 设计校审 勾选
    shejijiaoshen = (By.XPATH,'//label[text()="设计校审"]/span')
    # 设计校审级别勾选框
    jiaoshenlevel = (By.XPATH, '//div[@id="children-span"]/div[@class="su_form_control su_select_box"]')
    # 1级
    level_1 = (By.XPATH, '//a[@title="1级"]')
    # 无
    null = (By.XPATH, '//a[@title="无"]')
    # 跳过会签阶段 勾选
    huiqianjieduan = (By.XPATH, '//label[text()="可跳过会签阶段"]/span')
    # 可低于标准级别 勾选
    diyubiaozhun = (By.XPATH, '//label[text()="可低于标准级别"]/span')
    # 跳过会签阶段 勾选
    huiqianjieduan = (By.XPATH,'//label[text()="可跳过会签阶段"]/span')
    biaozhunjibie = (By.XPATH,'//label[text()="可低于标准级别"]/span')
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
    # 绩效统计
    jixiaotongji_loc = (By.XPATH, '//span[text()="绩效统计"]')
    # 绩效统计勾选框
    jixiaotongji_gouxuan = (By.XPATH,'//tr[@class]//span[@class="sufont-check"]')
    # 提交时间
    submittime = (By.XPATH,'//span[text()="至"]/preceding-sibling::div[@class="pull-left su_datepicker"]//input')
    # 至时间
    zhitime = (By.XPATH,'//span[text()="至"]/following-sibling::div//input')
    # 绩效勾选确定
    jixiao_sure = (By.XPATH,'//div[@id="popup_list_id"]/following-sibling::div//span[text()="确定"]')
    # 总计
    zongji = (By.XPATH,'//span[text()="总计："]/parent::span')
    # 工程绩效
    gongcheng_jixiao = (By.XPATH,'//span[text()="工程绩效："]/parent::span')
    # 项目名称-测试_线路
    xianlu = (By.XPATH, '//tr[1]//span[contains(text(),"线路工程")]/parent::td')
    # 发起审批
    faqi_shenpi = (By.XPATH, '//span[text()="发起审批"]')
    # 预支勾选框
    yuzhi_gouxuan = (By.XPATH,'//label[text()="预支"]/span')
    # 提报比例输入框
    tibao_rate = (By.XPATH, '//b[text()="提报比例："]/following-sibling::input')
    # 提报比例确定按钮
    tibao_sure = (By.XPATH, '//div[@class="box medium_box box1 por"][2]//span[text()="确定"]')
    # 提报比例链接
    tibaobili_link = (By.XPATH, '//tr[@class][1]//td[2]/span')
    # 编辑按钮
    edit_button = (By.XPATH,'//span[text()="编辑"]')
    # 我知道了
    i_know = (By.XPATH,'//span[text()="我知道了"]')
    # 调整系数按钮
    edit_xishu_button = (By.XPATH,'//div//span[text()="恢复初始"]/following-sibling::span[text()="系数调整"]')
    # 保存数据按钮
    save_data_button = (By.XPATH,'//div//span[text()="恢复初始"]/following-sibling::span[text()="保存数据"]')
    # 退出编辑按钮
    cancle_edit_button = (By.XPATH,'//div//span[text()="恢复初始"]/following-sibling::span[text()="退出编辑"]')
    # 系数调整输入框
    xishu_input = (By.XPATH,'//div[@style="width: 600px;"]//input')
    # 确定按钮
    sure_button_xishu = (By.XPATH,'//div[@style="width: 600px;"]//span[text()="确定"]')
    # 提示语
    prom_info = (By.XPATH,'//div[@class="prompt-txt"]')
    # 取消按钮
    cancle_button_xishu = (By.XPATH,'//div[@style="width: 600px;"]//span[text()="取消"]')
    # 项目经理输入框
    man_input = (By.XPATH,'//table[@class="text-left table table-hover su-grid"]//tr[2]/td[8]/input')
    # 刷新按钮
    refresh = (By.XPATH,'//b[text()="成品质量系数："]/following-sibling::img[@src]')
    # 同步更新
    tongbugengxin = (By.XPATH,'//label[text()="同步更新提报工日"]/span')
    # 刷新确定
    refresh_sure = (By.XPATH,'//span[text()="刷新成品质量系数"]/parent::h1/following-sibling::div/span[text()="确定"]')
    # 提报比例
    tibaobili = (By.XPATH, '//b[text()="提报比例："]/parent::span/span')
    # 专业占比
    zhuanye_zhanbi = (By.XPATH, '//b[text()="专业占比"]/parent::span')
    # 成品质量系数
    chengpinzhiliang = (By.XPATH,'//b[text()="成品质量系数："]/parent::span')
    # 标准工日
    biaozhun_days = (By.XPATH, '//b[text()="标准工日："]/parent::span/span')
    # 提报工日
    tibao_days = (By.XPATH, '//b[text()="提报工日："]/parent::span/span')
    # 提交审批按钮
    tijiao_shenpi = (By.XPATH,'//span[text()="提交审批"]')
    # 韩正勾选框
    hanzheng = (By.XPATH,'//span[@id="selectRolePersonTree_22_check"]')
    hanzheng1 = (By.XPATH,'//a[@title="韩正"]/preceding-sibling::span[@class="button chk radio_false_full"]')
    # 确定按钮
    sure = (By.XPATH,'//div[@class="frameView-item txt-c"]//span[text()="确定"]')
    # 成功
    success = (By.XPATH,'//div[@class="prompt-txt"]')
    # 审批留痕
    shenpi_liuhen = (By.XPATH,'//span[text()="审批留痕"]')

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
    # 选择水利设计工程
    choose_waterproject = (By.XPATH,'//div[contains(text(),"水利设计工程")]/parent::td/parent::tr')
    # 确定按钮
    project_sure_button = (By.XPATH,'//button[@class="danger yes"]')
    # 选择卷册
    choose_file_button = (By.XPATH,'//span[text()="选择卷册"]')
    # 01设计输入资料
    input_file = (By.XPATH,'//span[@id="team-tree3_2_check"]')
    # 前期阶段批复意见
    pifuyijian = (By.XPATH,'//a[@title="04-前期阶段批复意见"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 同步校审文件勾选
    tongbujiaoshen_gouxuan = (By.XPATH,'//label[text()="同步校审文件"]/span')
    # 确定按钮
    surebutton = (By.XPATH,'//label[text()="同步校审文件"]/following-sibling::span[text()="确定"]')
    # 计划完成时间
    plan_finish_time = (By.XPATH,'//label[text()="计划完成时间："]/following-sibling::div//input')
    # 当月
    current_month = (By.XPATH, '//span[@class="mouse-cp currentmonth"]')
    # 下月按钮
    lastmonth = (By.XPATH, '//span[@class="pull-right"]/i[@class="fa fa-chevron-circle-right mouse-cp"]')
    # 时间确定按钮
    time_sure = (By.XPATH,'//span[text()="清空"]/following-sibling::span')
    # 校审设计说明输入框
    jishenshuoming = (By.XPATH,'//textarea[@placeholder="请输入说明"]')
    # 确认人选择按钮
    sureperson_choose = (By.XPATH,'//label[text()="确认人："]/following-sibling::div//span[text()="选择"]')
    # 海清选择
    haiqing_choose = (By.XPATH,'//span[@id="managerTree_3_check"]')
    haiqing_choose_new = (By.XPATH,'//span[text()="海清"]/../../span[2]')

    # 龙美心
    longmeixin = (By.XPATH,'//a[@title="龙美心"]/parent::li/span[@class="button chk checkbox_false_full"]')
    # 确定按钮
    person_sure_button = (By.XPATH,'//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    huiqian = (By.XPATH,'//label[text()="跳过会签阶段"]/span')
    huiqian_new = (By.XPATH,'//span[text()="跳过会签阶段"]/following-sibling::label//span')
    # 五审人选择按钮
    wushen_choosebutton = (By.XPATH,'//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    wushenhairuomeng_choose = (By.XPATH,'//a[@title="海若梦"]/parent::li/span[@class="button chk checkbox_false_full"]')
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
    w_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    w_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    w_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    w_wushenren_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 确认人状态
    w_sure = (By.XPATH,'//tr[@class][1]//td[15]')
    # 设计校审名称--01-设计输入资料
    w_file = (By.XPATH, '//tr[@class][1]//td[2]')
    # 五审
    w_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 确认
    w_sure_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="确认"]')
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
    # 已处理确认状态
    w_dealed_sure_state = (By.XPATH, '//tr[@class][1]//td[15]')

    # 设计校审名称--规划咨询报告"]
    bfile = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 设计校审名称--04-前期阶段批复意见"
    bfile2 = (By.XPATH, '//span[text()="04-前期阶段批复意见"]')
    # 发起确认按钮
    b_faqisure = (By.XPATH,'//span[text()="发起确认"]')
    # 发起按钮
    b_faqi = (By.XPATH,'//button[text()="发起"]')

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
    w_faqi_sure_state = (By.XPATH,'//tr[@class][1]//td[13]')
    w_faqi_sure_state2 = (By.XPATH,'//tr[@class][1]//td[8]')

    """
    审批人'韩正'元素定位
    """
    # 我监管的
    jianguan = (By.XPATH,'//span[text()="我监管的"]')
    # 项目名称'测试线路工程'
    route_project = (By.XPATH,'//tr[@class][1]/td[2]')
    # 提报比例链接
    tibaobili_link_shen = (By.XPATH, '//tr[@class][1]//td[2]/span')
    # 通过 按钮
    pass_button = (By.XPATH,'//span[text()="通过"]')
    # 确定按钮
    pass_sure = (By.XPATH,'//span[contains(text(),"通过后")]/parent::div/following-sibling::div/span[text()="确定"]')
    # 成功
    """我监管的"""
    j_pass_success = (By.XPATH,'//div[@class="prompt-txt"]')
    # 审批时间
    j_pass_time = (By.XPATH,'//tr[@class][1]/td[13]')
    # 所属项目名称
    j_projectname = (By.XPATH,'//tr[@class][1]/td[2]')
    # 参审卷册/所属比例
    j_rate = (By.XPATH,'//tr[@class][1]/td[3]')
    # 审批状态
    j_approve_state = (By.XPATH,'//tr[@class][1]/td[11]')

    """我审批的"""
    # 我审批的
    my_approve = (By.XPATH,'//span[text()="我审批的"]')
    # 线路工程
    routeproject = (By.XPATH,'//span[contains(text(),"测试_线路工程")]')
    # 审批状态
    approvestate = (By.XPATH,'//span[contains(text(),"测试_线路工程")]/parent::td/parent::tr/Td[10]')
    # 审批序号
    approve_no = (By.XPATH,'//span[contains(text(),"测试_线路工程")]/parent::td/parent::tr/Td[1]')
    # 列表所有数据
    s_all_datas = (By.XPATH,'//tr[@class]')
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
    r_mywork_loc = (By.XPATH, '//span[contains(text(),"我的工作")]/parent::a')
    # 校审
    r_jiaoshen_loc = (By.XPATH, '//span[text()="校审"]/parent::a')
    # 空数据
    r_liucheng_null = (By.XPATH, '//p[contains(text(),"无匹配")]')
    # 所属项目名称
    r_suoshuxiangmu = (By.XPATH, '//tr[@class]//td[3]')
    # 我发起的流程列表
    r_faqiliucheng_list = (By.XPATH, '//tr[@class]')
    # 发起流程
    r_faqiliucheng = (By.XPATH, '//span[contains(text(),"发起流程")]')
    # 选择所属项目
    r_project_choose = (By.XPATH, '//label[contains(text(),"所属项目")]/following-sibling::div//span[text()="选择"]')
    # 选择线路工程
    r_choose_routeproject = (By.XPATH, '//div[contains(text(),"测试_线路工程")]/parent::td/parent::tr')
    # 确定按钮
    r_project_sure_button = (By.XPATH, '//button[@class="danger yes"]')
    # 选择卷册按钮
    r_choose_file_button = (By.XPATH, '//span[text()="选择卷册"]')
    # 01设计输入资料勾选
    r_designfilegouxuan = (By.XPATH, '//span[@id="team-tree3_2_check"]')
    # 同步校审文件勾选
    r_tongbujiaoshen_gouxuan = (By.XPATH, '//label[text()="同步校审文件"]/span')
    # 确定按钮
    r_surebutton = (By.XPATH, '//label[text()="同步校审文件"]/following-sibling::span[text()="确定"]')
    # 计划完成时间
    r_plan_finish_time = (By.XPATH, '//label[text()="计划完成时间："]/following-sibling::div//input')
    # 时间确定按钮
    r_time_sure = (By.XPATH, '//span[text()="清空"]/following-sibling::span')
    # 校审设计说明输入框
    r_jishenshuoming = (By.XPATH, '//textarea[@placeholder="请输入说明"]')
    # 确认人选择按钮
    r_sureperson_choose = (By.XPATH, '//label[text()="确认人："]/following-sibling::div//span[text()="选择"]')
    # 海若梦选择
    r_hairuomeng = (By.XPATH, '//span[@id="managerTree_7_check"]')
    # 海清选择
    r_haiqing = (By.XPATH, '//span[@id="managerTree_3_check"]')
    # 确定按钮
    r_person_sure_button = (By.XPATH, '//center/span[text()="确定"]')
    # 跳过会签阶段勾选框
    r_huiqian = (By.XPATH, '//label[text()="跳过会签阶段"]/span')
    # 五审人选择按钮
    r_wushen_choosebutton = (By.XPATH, '//label[text()="五审人："]/following-sibling::div//span[text()="选择"]')
    # 五审选择海若梦
    r_wushen_hairuomeng = (By.XPATH, '//span[@id="managerTree_9_check"]')
    # 五审确定按钮
    r_wushen_sure_button = (By.XPATH, '//center/span[text()="确定"]')
    # 设计校审文件添加按钮
    r_jiaoshenfile_add = (By.XPATH, '//label[text()="设计校审文件："]/following-sibling::div//span[text()="+添加"]')
    # 上传文件按钮
    r_upload_file = (By.XPATH, '//button[text()="上传文件"]')
    # 确定按钮
    r_file_sure_button = (By.XPATH, '//button[text()="确定"]')
    # 发起流程
    r_faqi_liucheng = (By.XPATH, '//button[text()="发起流程"]')
    # 五审人的五审状态
    r_wushenren_approvestate = (By.XPATH, '//tr[@class]//td[12]')
    # 退出按钮
    r_logout = (By.XPATH, '//span[text()="退出"]/parent::a')

    """确认人龙美心"""
    # 校审名称
    s_jiaoshenmingcheng = (By.XPATH, '//tr[@class][1]//td[2]')
    # 所属项目
    s_suoshuxiangmu = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审状态
    s_wushen_state = (By.XPATH, '//tr[@class][1]//td[12]')
    # 六审状态
    s_liushen_state = (By.XPATH, '//tr[@class][1]//td[13]')
    # 七审状态
    s_qishen_state = (By.XPATH, '//tr[@class][1]//td[14]')
    # 确认人
    s_sure_state = (By.XPATH, '//tr[@class][1]//td[15]')
    s_sure_state1 = (By.XPATH, '//tr[@class][1]//td[13]')
    # 设计校审名称--01-设计输入资料"]
    sfile = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 设计校审名称--04前期阶段批复意见"
    sfile2 = (By.XPATH, '//span[text()="04-前期阶段批复意见"]')
    # 确认按钮
    s_surebutton = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="确认"]')
    # 全部通过按钮
    s_allpassbutton = (By.XPATH, '//button[text()="全部通过"]')
    # 确定按钮
    s_sure_button = (By.XPATH, '//button[text()="确定"]')

    """
    五审人登陆元素定位
    """
    # 待处理按钮
    r_needdeal_button = (By.XPATH, '//button[text()="待处理"]')
    # 待处理数量
    r_needdeal_num = (By.XPATH, '//tr[@class]')
    # 待处理所属项目名称
    r_needdeal_projectname = (By.XPATH, '//tr[@class][1]//td[3]')
    # 五审人的五审状态
    r_wushen_approvestate = (By.XPATH, '//tr[@class][1]//td[12]')
    # 设计校审名称--01-设计输入资料"]
    r_file = (By.XPATH, '//span[text()="01-设计输入资料"]')
    # 五审
    r_wushen_button = (By.XPATH, '//div[@class="bg-f text-right por"]//span[text()="五审"]')
    # 全部通过
    r_all_pass = (By.XPATH, '//button[text()="全部通过"]')
    # 五审审批通过确定
    r_wushen_sure = (By.XPATH, '//button[text()="确定"]')
    # 待处理空数据
    r_nulldatas = (By.XPATH, '//p[contains(text(),"无匹配数据")]')
    # 已处理
    r_dealed_button = (By.XPATH, '//button[text()="已处理"]')
    # 已处理校审名称
    r_dealed_jiaoshen_name = (By.XPATH, '//tr[@class][1]//td[2]')
    # 已处理了所属项目
    r_dealed_suoshu_project = (By.XPATH, '//tr[@class][1]//td[3]')
    # 已处理五审状态
    r_dealed_wushen_state = (By.XPATH, '//tr[@class][1]//td[12]')
    # 共XX行
    r_all_datas = (By.XPATH, '//a[contains(text(),"共")]')

    """
    删除元素定位
    """
    # 删除元素
    delete1_loc = (By.XPATH, '//span[text()="测试_线路工程"]/ancestor::ul//span[text()="删除"]')
    delete1_loc2 = (By.XPATH, '//span[text()="测试_线路工程2"]/ancestor::ul//span[text()="删除"]')
    delete1_loc3 = (By.XPATH, '//span[text()="测试_线路工程3"]/ancestor::ul//span[text()="删除"]')
    # 删除确定
    delete_sure_loc = (By.XPATH, '//button[text()="确定"]')
    # 删除成功
    delete_success = (By.XPATH, '//div[text()="删除成功！"]')






