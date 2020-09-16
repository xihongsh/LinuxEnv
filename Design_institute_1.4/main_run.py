# encoding: utf-8
import sys,os
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
import unittest
from Common.delete_log import DeleteLogFile as DF
from BeautifulReport import BeautifulReport
manman = DF(r"./Design_institute_1.4/Outputs/logs", r"./Design_institute_1.4/Outputs/screenshots")
manman.delete_file()
if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(r"./Design_institute_1.4/TestCases")
    BeautifulReport(suite_tests).report(filename='Design_institute报告', description='Design_institute报告', report_dir=r'./Design_institute_1.4/Outputs/reports')