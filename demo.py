# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/heweather/weather/free?city=xian'

apikey = '451e1da33e5946c40d4303bb4e291ee4'

req = urllib2.Request(url)

req.add_header("apikey", apikey)

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
