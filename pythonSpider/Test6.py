#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib

#从文件中获取Cookie并访问

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()

#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)

#创建请求的request

req = urllib2.Request("http://www.baidu.com")

#利用urllib2的build_opener方法创建一个opener

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()


