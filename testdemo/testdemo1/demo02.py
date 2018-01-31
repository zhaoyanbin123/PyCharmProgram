# coding=utf-8
a = int(raw_input(u"请输入第一个数："))
b = int(raw_input(u"请输入第2个数："))
c = int(raw_input(u"请输入第3个数："))
if a >= b:

    if c >= a:
        print u"从小到大的顺序是%d,%d,%d" % (b, a, c)
    else:
        if c >= b:
            print u"从小到大的顺序是%d,%d,%d" % (b, c, a)
        else:
            print u"从小到大的顺序是%d,%d,%d" % (c, b, a)
else:
    if c <= a:
        print u"从小到大的顺序是%d,%d,%d" % (c, a, b)
    else:

        if c <= b:
            print u"从小到大的顺序是%d,%d,%d" % (a, c, b)
        else:
            print u"从小到大的顺序是%d,%d,%d" % (a, b, c)
