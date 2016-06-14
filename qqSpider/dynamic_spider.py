#!/usr/bin/python
#_*_ coding:utf8 _*_
import requests
import re
import json

head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
start_url = 'http://v.qq.com/cover/n/nvblqd32r7lr8x6.html?vid=x0018h9wuat'
commet_url = 'http://sns.video.qq.com/fcgi-bin/video_comment_id?otype=json&low_login=1&op=3&vid='
last_url = 'http://coral.qq.com/article/jjjj/comment?commentid=6077082562022945024&reqnum=20'

#解析第一个url
jscontent = requests.get(start_url,headers = head).content
#匹配vid
vid = re.findall('vid:"(.*?)"',jscontent,re.S)
#生成第二个url
middle_url = str(commet_url) + vid[0]
#解析第二个url
twocontent = requests.get(middle_url,headers = head).content
#匹配comment_id
comment_id = re.findall('"comment_id":"(.*?)","result"',twocontent,re.S)
#替换字符串,生成最终请求url
request_url = last_url.replace('jjjj',comment_id[0])

def parseJson(response):

    #请求最终url,解析json字符串
    comments = requests.get(response,headers = head).content
    jsonMain = json.loads(comments)

    data = jsonMain['data']
    last = data['last']
    print 'last:' +'                      ' + last
    commentid = data['commentid']
    for each in commentid:
        print each['userinfo']['nick'] + '                   ' + each['content']
        print '----------------------------------------------------------------------'

    #匹配commentid,并以last替换
    commentid = re.findall('[1-9][0-9]{4,}',response,re.S)
    new_url = response.replace(commentid[1],last)
    if new_url == response:
        print "没有评论了"
    else:
        parseJson(new_url)
    # print commentid[1]

parseJson(request_url)


