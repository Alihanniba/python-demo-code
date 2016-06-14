#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '花一'

#导入re模块
import re

#匹配如下内容:单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P.*)','hello world')

print "m.string:",m.string
print "m.re:",m.re
print "m.pos:",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup
print "m.group():",m.group()
print "m.group(1,2):",m.group(1,2)
print "m.groups():",m.groups()
print "m.groupdict():",m.groupdict()
print "m.start(2):",m.start(2)
print "m.end(2):",m.end(2)
print "m.span(2):",m.end(2)
print r"m.expand(r'\g \g\g'):",m.expand(r'\2 \1\3')