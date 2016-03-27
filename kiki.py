# -*- coding: utf-8 -*-
import random
import sys
str = u'こん'
string = u''
strlist = list(str)
f = open('File.txt')
kongo = f.read()
f.close()
while True:
    for i in range (4):
        x = random.randint(0,len(strlist)-1)
        string += strlist[x]
    
    print string
    kiki = u'こんこん'
    if string == kiki:
        print '金剛力士像\n'
        print kongo
        break
    string = ''
