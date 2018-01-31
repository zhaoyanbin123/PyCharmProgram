#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import sys
import MySQLdb

reload(sys)
order_id = sys.argv[1]
#order_id="6290437923129008128"
url = "http://fh.market-tms.wmdev.lsh123.com"
xpath_type = "html/body/div[1]/div[2]/div/div/"
               
# 需要在数据库中将状态改成 可提交dc
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

#修改数据库状态

def UpdateSatus():

    db=MySQLdb.connect(host="192.168.60.59",port=5200,user="root",passwd="",db="lsh_oms",charset="utf8")

    cursor=db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    sql="update order_head set 'order_status'=20 where order_code={0};".format(order_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
            # 发生错误时回滚
            db.rollback()
            # 关闭数据库连接
    #db.close()

    #校验是否修改成功
    sql_1="select order_status from order_head where order_code={0};".format(order_id)
    cursor.execute(sql_1)
    
    data=cursor.fetchall()
    
    for i in data:
        status=i["order_status"]   
        print u"修改订单状态成功,状态为：{0}".format(status) if status==20 else u"修改失败,请检查"

        db.close()
    


#登录
def test(driver):
    
    driver.find_element_by_name("email").send_keys("shaobaodong@lsh123.com")
    driver.find_element_by_name("pwd").send_keys("111111qQ")
    driver.find_element_by_xpath(".//*[@id='login-box']/form/div[4]/button").click()
    time.sleep(2)

    driver.find_element_by_xpath(xpath_type + "div[2]/input").send_keys(order_id)
    time.sleep(2)
    driver.find_element_by_xpath(xpath_type + "div[4]/input[1]").click()
    time.sleep(2)

    swithc_to(driver,"div[4]/input[2]")

    swithc_to(driver,"div[4]/input[3]")

    # 发货
    swithc_to(driver,"div[6]/input")
    
    print u"发货完成"
    
    waybillno=driver.find_element_by_xpath(xpath_type+"div[6]/div[4]/input").get_attribute('value') 
    print u"运单号：{0}".format(waybillno)
    driver.quit()



def swithc_to(driver,t):
    driver.find_element_by_xpath(xpath_type + t).click()
    time.sleep(3)
    al = driver.switch_to_alert()
    al.accept()
    time.sleep(3)
    #a1.exit()




if __name__=="__main__":
    
    
    UpdateSatus()
    
    test(driver)
    
