#coding=utf-8
import sys
import os


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import TestSuite
sys.path.append("..")
from public import BaseFunction,SendEmail
'''测试入口'''
if __name__ == "__main__":
    # 运行所有case
    BaseFunction.Report().run(TestSuite.createsuite())
    SendEmail.SendReport_Email()#发送邮件
    
