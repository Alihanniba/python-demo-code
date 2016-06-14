#_*_coding:utf8_*_
import json
import requests

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}

jscontent = requests.get('http://coral.qq.com/article/1227362953/comment?commentid=0&reqnum=20',\
                         headers = head).content
jsonMain = json.loads(jscontent)
jsDick = jsonMain['data']
commentid = jsDick['commentid']
print jsDick['last']
for each in commentid:
        print each['userinfo']['nick'] +'      ' + each['content']
        print '------------------------------------------------'

