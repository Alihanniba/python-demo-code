#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import requests
from bs4 import BeautifulSoup

#爬出京东手机版块所有手机价格信息

def ParseJD(page):
    url = 'http://list.jd.com/list.html?cat=9987%2C653%2C655&page='+str(page)
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")
    items = soup.select('li.gl-item')
    # print len(items)
    for item in items:
        sku = item.find('div')['data-sku']
        print sku,
        price_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(sku)
        price = requests.get(price_url).json()[0]['p']
        print price,
        nameinfo = item.find('div', class_="p-name").find('a')
        name = nameinfo['title']
        item_url = 'http:' + nameinfo['href']
        print name, item_url,
        commit = item.find('div', class_="p-commit").find('a')
        if commit:
            print commit.get_text()
    if len(items) > 0:
        ParseJD(page+1)
    else:
        pass
ParseJD(1)