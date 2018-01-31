# coding=utf-8
def getProper():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.elianshang.yougong'
    # self.desired_caps['noReset'] = True #不加这句启动会报错，目前没有找到原因，但是加上这行代码启动APP时如果之前已登录，就不会再次登录了，没法测试登录情况
    desired_caps['appActivity'] = 'com.elianshang.yougong.ui.activity.WelcomeActivity'

    return desired_caps
