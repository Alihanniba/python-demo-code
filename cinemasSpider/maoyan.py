#!/usr/bin/python
#_*_ coding:utf8 _*_
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')      #python的str默认是ascii编码,和unicode编码冲突,你需要的是让编码用实际编码而不是 ascii,把 str 编码由 ascii 改为 utf8 (或 gb18030)

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
cinema_url = 'http://m.maoyan.com/cinemas.json'

def ParseJson(response):
    comment = requests.get(response,headers=head).content
    jsonMain = json.loads(comment)

    data = jsonMain['data']
    for w in data:
        for q in data[w]:
            print str(q['id'])+'             int类型不能直接与str类型合并,需将int类型转化为str类型              '+q['nm']+'                  '+q['addr']
            print '---------------------------------------------------------------------------------------------------------------'
ParseJson(cinema_url)







