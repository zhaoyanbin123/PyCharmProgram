#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2014/11/27
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print 'ģ�鵼�����,��ʹ��pip��װ,pytesseract�������¿⣺'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit

image = Image.open('D://img//2.jpg')
vcode = pytesseract.image_to_string(image)
print vcode