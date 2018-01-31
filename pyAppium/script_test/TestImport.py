#coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import TestSuite
sys.path.append("..")
from public_method import base_function,SendEmail,testlog
'''测试入口'''
if __name__ == "__main__":
    # 运行所有case
    testlog.log_fun().info("开始执行测试")
    base_function.Report().run(TestSuite.createsuite())
    testlog.log_fun().info("开始发送测试邮件")
    SendEmail.SendReport_Email()
