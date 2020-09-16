from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import logger_fun
import calendar as cal
# import win32gui
# import win32con
import time
import datetime
from Common.dir_config import screenshot_dir
# 任何一个步骤都会做到  捕获异常、日志输出、失败截图
class BasePage:
    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图
    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_elevisible(self,loc,timeout=120,frequency=0.5,doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        start_time = time.time()
        try:

            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger_fun.logging.exception("等待{}元素可见超时".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            end_time = time.time()
            duration = end_time - start_time
            logger_fun.logging.info("等待{}元素可见,耗时{}".format(loc, duration))

    # 查找元素
    def is_element_exsits(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger_fun.logging.exception("等待 {} 元素存在，失败！".format(loc))
            self.do_save_screenshot(doc)
            return False
        else:
            logger_fun.logging.info("查找{}的元素{}成功。".format(doc, loc))
            return True

    # 查找元素
    def get_element(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger_fun.logging.exception("等待 {} 元素存在，失败！".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("查找{}的元素{}成功。".format(doc, loc))
            return ele


    # 输入框输入文本
    def input_text(self, loc, value, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(value)
        except:
            logger_fun.logging.exception("向{}元素输入{}失败".format(loc, value))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("向{}元素输入{}成功".format(loc, value))

    # 输入框输入文本
    def clear_text(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.clear()
        except:
            logger_fun.logging.exception("清除{}内容失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("清除{}内容成功".format(loc))

    # 点击
    def click(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.click()
        except:
            logger_fun.logging.exception("向{}元素点击失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("向{}元素点击成功".format(loc))

    # 点击
    def click_by_js(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        time.sleep(0.5)
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            self.driver.execute_script("$(arguments[0]).click()", ele)
        except:
            logger_fun.logging.exception("向{}元素点击失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("向{}元素点击成功".format(loc))

    # 获取元素文本值
    def get_element_text(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            text = ele.text
        except:
            logger_fun.logging.exception("获取{}元素文本值失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("获取{}元素文本值成功".format(loc))
            return text

    def get_element_attribute(self, loc, attr, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param attr:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            value = ele.get_attribute(attr)
        except:
            logger_fun.logging.exception("获取{}元素属性值失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("获取{}元素属性值成功".format(loc))
            return value

    # 查找多个元素
    def get_elements(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            ele = self.driver.find_elements(*loc)
        except:
            logger_fun.logging.exception("等待 {} 元素存在，失败！".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("查找{}的元素{}成功。".format(doc, loc))
            return ele


    # 获取列表数据长度
    def get_list_length(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_elements(loc, doc)
        try:
            value = len(ele)
        except:
            logger_fun.logging.exception("获取{}元素属性值失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("获取{}元素属性值成功".format(loc))
            return value

    def do_save_screenshot(self,doc=""):
        """
        :param doc:
        :return:
        """
        cur_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')
        file = screenshot_dir+"/{}_{}.png".format(doc,cur_time)
        try:
            self.driver.save_screenshot(file)
        except:
            logger_fun.logging.exception("网页截图操作失败")
        else:
            logger_fun.logging.info("网页截图成功，存储路径为{}".format(file))

    def upload_file(self,filepath,doc=""):
        try:
            # 一级窗口"#32770","打开"
            dialog = win32gui.FindWindow("#32770", "打开")
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
            # 编辑按钮
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            # 打开按钮
            button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 四级
            # 往编辑当中，输入文件路径 。
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        except:
            logger_fun.logging.exception("上传文件{}失败".format(filepath))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("上传文件{}成功".format(filepath))

    def switch_window(self,doc=""):
        try:
            # 获取所有的window列表
            windows = self.driver.window_handles
            #切换到最新窗口
            self.driver.switch_to.window(windows[-1])
        except:
            logger_fun.logging.exception("切换窗口失败")
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("切换窗口成功")

    # 获取多个元素的文本值（新增方法）
    def get_elements_text_value(self, loc, doc=""):
        """
        :param loc:
        :param doc:
        :return:
        """
        try:
            check_results = []
            eles = self.driver.find_elements(*loc)
            for ele in eles:
                check_results.append(ele.text)
        except:
            logger_fun.logging.exception("获取 {} 元素文本值存在，失败！".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("获取{}的元素{}文本值成功。".format(doc, loc))
            return check_results

    # 获取当前日期
    def get_date(self):
        return time.strftime("%Y-%m-%d",time.localtime(time.time()))

    # 获取元素默认值
    def get_default_value(self, loc, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        self.wait_elevisible(loc, timeout, frequency, doc)
        ele = self.get_element(loc, doc)
        try:
            default_value = ele.get_attribute('value')
        except:
            logger_fun.logging.exception("获取{}元素文本值失败".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("获取{}元素文本值成功".format(loc))
            return default_value

    # 输入框输入文本形式上传文件
    def input_text_uploadfile(self, loc, value, timeout=60, frequency=0.5, doc=""):
        """
        :param loc:
        :param value:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        # 元素可见# 找它
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(value)
        except:
            logger_fun.logging.exception("向{}元素输入{}失败".format(loc, value))
            self.do_save_screenshot(doc)
            raise
        else:
            logger_fun.logging.info("向{}元素输入{}成功".format(loc, value))

    # 获取当月的第一天和最后一天
    def get_first_and_last_day(self):
        i = datetime.datetime.now()
        FORMAT = "%d-%d-%d\t%d-%d-%d"
        d = cal.monthrange(i.year, i.month)
        list = str(FORMAT % (i.year, i.month, 1, i.year, i.month, d[1])).split("\t")
        list = "-".join(list).split("-")
        for count in range(len(list)):
            if len(list[count]) == 1:
                list[count] = "0" + str(list[count])
                print(list[count])
        list = "-".join(list)
        return list

    # 距离今天N天的未来某一天
    def future_oneday(self,countdays):
        today = time.time()
        future_five = today + countdays * 86400
        future_one_date = time.strftime('%Y-%m-%d', time.localtime(future_five))
        return future_one_date











