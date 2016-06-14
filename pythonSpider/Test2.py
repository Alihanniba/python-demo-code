#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}

#POST方式

# values = {"username":"llzazy@163.com","password":"xxx"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()


# values = {}
# values['username'] = 'llzazy@163.com'
# values['password'] = 'xxx'
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data,10)
# response = urllib2.urlopen(request)
# print response.read()



#GET方式
values = {}
values['username'] = 'llzazy@163.com'
values['password'] = 'xxx'
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
# print(geturl)


#urllib2使用代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":"http://some-proxy.com:8080"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


