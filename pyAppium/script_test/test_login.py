# coding:utf-8
import unittest
from appium import webdriver
import time
import os, sys
import subprocess

sys.path.append("..")
from config import proper
from public_method import base_function,testlog


class Test(unittest.TestCase):
    def setUp(self):
        self.desired_caps = proper.getProper()
        testlog.log_fun().info("开启appium服务")
        subprocess.Popen("appium -a 127.0.0.1 -p 4723", shell=True)
        time.sleep(10)
        self.driver = ""

    def tearDown(self):
        self.driver.quit()

        # 结束appium服务--node.exe进程
        testlog.log_fun().info("结束appium服务")
        os.system('taskkill /f /fi "imagename eq node.exe"')

    def test_1(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        time.sleep(10)
        base_function.getLocator(self.driver, "info", "classification").click()

        # self.driver.find_element_by_xpath("//*[@class='android.widget.TextView'and @index='1' and @text='分类']").click()
        # self.driver.find_element_by_xpath("//*[@class='android.widget.EditText'and @index='1']").send_keys("15120037748")

        # self.driver.find_element_by_id("com.elianshang.yougong:id/password").send_keys("123456")
        # self.driver.find_element_by_id("com.elianshang.yougong:id/login").click()


if __name__ == "__main__":
    unittest.main()
