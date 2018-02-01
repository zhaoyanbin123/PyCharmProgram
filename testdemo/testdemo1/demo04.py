#coding=utf-8
import  random
result=["石头","剪刀","布"]
game_rule=[["石头","剪刀"],["剪刀","布"],["布","石头"]]
while True:
    result1= raw_input("请输入你的选择：")
    computer=random.choice(result)
    if result1 not in result:
        print u"请重新输入"
        continue
    if [computer,result1] in game_rule:
        print "电脑win"
        break
    else:
        print "you win"
        break

