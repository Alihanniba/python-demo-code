#!usr/bin/python
#_*_coding:utf8_*_
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')      #python的str默认是ascii编码,和unicode编码冲突,你需要的是让编码用实际编码而不是 ascii,把 str 编码由 ascii 改为 utf8 (或 gb18030)

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
cinema_url = 'http://m.maizuo.com/mobile/getMovieList?city=10&index=0&count=100&type=1'

def ParseJson(response):
    comments = requests.get(response,headers=head).content
    JsonMain = json.loads(comments)
    filmList =  JsonMain['data']['filmList']
    for q in filmList:
        print q['filmName']+'                        '+q['shortIntro']+'                        '+q['grade']
ParseJson(cinema_url)






