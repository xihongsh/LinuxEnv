from selenium.webdriver.common.by import By
class ProcessPageLocator:
    """
    '自动化专用项目'项目元素定位
    """
    # '项目管理'定位
    projectmanager_loc = (By.XPATH,'//span[contains(text(),"项目管理")]/parent::a')
    # '项目台账'定位
    projectplatform_loc = (By.XPATH,'//span[contains(text(),"项目台账")]/parent::a')
    # 项目状态进度
    project_proc = (By.XPATH,'//span[text()=" 已延期 "]/following-sibling::span[1]')
    project_proc_new = (By.XPATH,'//span[contains(text(),"项目状态")]/span[2]')

    # 进度百分比 元素
    process_percent = (By.XPATH,'//span[@class="c-main"][1]/b')
    # 显示'进度占比' 元素
    show_process_percent = (By.XPATH,'//span[text()="显示“进度占比”"]')
    # 进度占比文字
    letter = (By.XPATH,'//span[text()="显示“进度占比”"]')
    # 显示'进度占比' 勾选框 元素
    show_process_box = (By.XPATH,'//span[@class="sufont-check"]')
    # 数据列表 进度占比 元素
    list_process_percent = (By.XPATH,'//tr[@class]//th[text()="进度占比%"]')
    list_process_percent_1 = (By.XPATH,'//tr[@class]//th[text()="进度占比%"][1]')
    list_process_percent_2 = (By.XPATH,'//tr[@class]//th[text()="进度占比%"][2]')
    list_process_percent_3 = (By.XPATH,'//tr[@class]//th[text()="进度占比%"][3]')
    list_process_percent_4 = (By.XPATH,'//tr[@class]//th[text()="进度占比%"][4]')

    # 水暖专业-忽略按钮
    plumbing_ignore = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//span[text()="忽略"]')
    # 水暖专业-操作
    plumbing_do = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//td[13]')
    # 水暖专业-回退按钮
    plumbing_fallback = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//span[text()="回退"]')
    # 水暖专业-完成按钮
    plumbing_finish = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//span[text()="完成"]')
    # 水暖专业-弹框提示语
    plumbing_box_info = (By.XPATH,'//div[@class="modal-container modal-content"]//p')
    # 水暖专业-弹框确定
    plumbing_sure = (By.XPATH,'//button[text()="确定"]')
    # 水暖专业-完成进度
    plumbing_finish_percent = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//td[11]')
    # 水暖专业-进度占比
    plumbing_process_percent = (By.XPATH,'//td[text()="通信"]/parent::tr/preceding::tr[1]//td[12]')

    # 通信专业-操作列
    communication_do = (By.XPATH,'//td[text()="航空测量"]/parent::tr/preceding::tr[1]//td[13]')
    # 通信专业-忽略按钮
    communication_ignore = (By.XPATH,'//td[text()="通信"]/parent::tr//span[text()="忽略"]')
    # 通信专业-恢复按钮
    communication_restore = (By.XPATH,'//td[text()="通信"]/parent::tr//span[text()="恢复"]')
    # 通信专业-完成按钮
    communication_finish = (By.XPATH,'//td[text()="通信"]/parent::tr//span[text()="完成"]')
    # 通信专业-完成进度
    communication_finish_percent = (By.XPATH,'//td[text()="通信"]/following-sibling::td[1]')
    # 通信专业-进度占比
    communication_process_percent = (By.XPATH,'//td[text()="通信"]/following-sibling::td[2]')

    # 航空测量-操作列
    aerial_survey_do = (By.XPATH,'//td[text()="资源"]/parent::tr/preceding::tr[1]//td[13]')
    # 航空测量-恢复按钮
    aerial_survey_restore = (By.XPATH,'//td[text()="航空测量"]/parent::tr//span[text()="恢复"]')
    # 航空测量-忽略按钮
    aerial_survey_ignore = (By.XPATH,'//td[text()="航空测量"]/parent::tr//span[text()="忽略"]')
    # 航空测量-完成按钮
    aerial_survey_finish = (By.XPATH,'//td[text()="航空测量"]/parent::tr//span[text()="完成"]')
    # 航空测量-完成进度
    aerial_survey_finish_percent = (By.XPATH,'//td[text()="航空测量"]/following-sibling::td[1]')
    # 航空测量-进度占比
    aerial_survey_process_percent = (By.XPATH,'//td[text()="航空测量"]/following-sibling::td[2]')

    # 新能源业务模块-完成进度
    energy_finsh_pro = (By.XPATH,'//td[text()="航空测量"]/parent::tr/preceding-sibling::tr//td[text()="设计校审"]/preceding::td[5]')
    # 新能源-收资-完成进度
    energy_money_finsh_pro = (By.XPATH,'//td[text()="航空测量"]/parent::tr/preceding::tr[4]//td[5]')
    # 收资-成果进度-完成进度
    money_result_finish_pro = (By.XPATH,'//td[text()="航空测量"]/parent::tr/preceding::tr[2]//td[8]')

    # 资源-操作列
    resources_do = (By.XPATH,'//td[text()="总图"]/parent::tr/preceding::tr[1]//td[13]')
    # 资源-回退按钮
    resources_fallback = (By.XPATH,'//td[text()="资源"]/parent::tr//span[text()="回退"]')
    # 资源-忽略按钮
    resources_ignore = (By.XPATH,'//td[text()="资源"]/parent::tr//span[text()="忽略"]')
    # 资源-完成按钮
    resources_finish = (By.XPATH,'//td[text()="资源"]/parent::tr//span[text()="完成"]')
    # 资源-完成进度
    resources_finish_percent = (By.XPATH,'//td[text()="资源"]/following-sibling::td[1]')
    # 资源-进度占比
    resources_process_percent = (By.XPATH,'//td[text()="资源"]/following-sibling::td[2]')

    # 总图-操作列
    general_layout_do = (By.XPATH,'//td[text()="资源"]/parent::tr/following-sibling::tr[1]//td[13]')
    # 总图-回退按钮
    general_layout_fallback = (By.XPATH,'//td[text()="总图"]/parent::tr//span[text()="回退"]')
    # 总图-忽略按钮
    general_layout_ignore = (By.XPATH,'//td[text()="总图"]/parent::tr//span[text()="忽略"]')
    # 总图-完成按钮
    general_layout_finish = (By.XPATH,'//td[text()="总图"]/parent::tr//span[text()="完成"]')
    # 总图-完成进度
    general_layout_finish_percent = (By.XPATH,'//td[text()="总图"]/following-sibling::td[1]')
    # 总图-进度占比
    general_layout_process_percent = (By.XPATH,'//td[text()="总图"]/following-sibling::td[2]')

    # 场区电气一次-操作列
    ground_do = (By.XPATH,'//td[text()="场区电气二次"]/parent::tr/preceding::tr[1]//td[13]')
    # 场区电气一次-恢复按钮
    ground_restore = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[1]//td/span[text()="恢复"]')
    # 场区电气一次-忽略按钮
    ground_ignore = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[1]//td/span[text()="忽略"]')
    # 场区电气一次-完成按钮
    ground_finish = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[1]//td/span[text()="完成"]')
    # 场区电气一次-完成进度
    ground_finish_percent = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[1]//td[11]')
    # 场区电气一次-进度占比
    ground_process_percent = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[1]//td[12]')

    # 场区电气二次-操作列
    ground_two_do = (By.XPATH,'//td[text()="资源"]/parent::tr/following-sibling::tr[3]//td[13]')
    # 场区电气二次-忽略按钮
    ground_two_ignore = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[2]//td/span[text()="忽略"]')
    # 场区电气二次-恢复按钮
    ground_two_restore = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[2]//td/span[text()="恢复"]')
    # 场区电气二次-完成按钮
    ground_two_finish = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[2]//td/span[text()="完成"]')
    # 场区电气二次-完成进度
    ground_two_finish_percent = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[2]//td[11]')
    # 场区电气二次-进度占比
    ground_two_process_percent = (By.XPATH,'//td[text()="总图"]/parent::tr/following-sibling::tr[2]//td[12]')
