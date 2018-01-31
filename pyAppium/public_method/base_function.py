# coding=utf-8
import ConfigParser
import HTMLTestRunner
import sys

sys.path.append("..")
from config import constants


def getLocator(driver,type1, name):
    '''获取定位表达式方法'''
    cf = ConfigParser.ConfigParser()

    cf.read(constants.getPath("ini_path"))
    typename = cf.get(type1, name)
    location_value = typename.split(">")[1]
    location_type = typename.split(">")[0]

    if isinstance(location_value, unicode):
        location_value = location_value.encode('utf-8')
    else:
        location_value = location_value.decode('gbk').encode('utf-8')

    if location_type == "id":
        return driver.find_element_by_id(location_value)
    elif location_type == "xpath":
        return driver.find_element_by_xpath(location_value)
    elif location_type == "name":
        return driver.find_element_by_name(location_value)
    elif location_type == "classname":

        return driver.find_element_by_class_name(location_value)


def Report():
    '''自定义测试报告'''
    fp = file(constants.getPath("email_path"), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
    return runner


if __name__ == "__main__":
    Report()

