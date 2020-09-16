import os
# 框架项目顶层目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

logs_dir =  os.path.join(base_dir,"Outputs/logs")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")

companyname_dir = os.path.join(base_dir,"TestDatas")
