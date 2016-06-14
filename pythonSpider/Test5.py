#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib

#保存cookie到文件

#设置保存cookie的文件,同级目录下得cookie.txt
filename = 'cookie.txt'

#声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
cookie = cookielib.MozillaCookieJar(filename)

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib2.build_opener(handler)

#创建一个请求,原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")

#保存cookie到文件
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
# ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入，
# 在这里，我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中
cookie.save(ignore_discard=True,ignore_expires=True)


