# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import makerAPI
import moment
import schedule
import time

def getWeather():
    url = 'http://apis.baidu.com/heweather/weather/free?city=xian'

    apikey = '451e1da33e5946c40d4303bb4e291ee4'

    req = urllib2.Request(url)

    req.add_header("apikey", apikey)

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        return content
    else:
        return error

def limitedPlateNumber():
    number = int(moment.now().timezone("Asia/Shanghai").format("D"))
    if number > 5:
        return '%d, %d'%(number - 5, number)
    else:
        return '%d, %d'%(number, number + 5)

def main():
    rawData = getWeather()
    jsonData = json.loads(rawData)
    Data = jsonData['HeWeather data service 3.0'][0]

    #get detailed data
    airQuality = Data['aqi']['city']

    airAqi = airQuality['aqi']
    airGrader = airQuality['qlty']
    limitedNumber = limitedPlateNumber()

    makerAPI.triggerIFTTT(airAqi, airGrader, limitedNumber)

def job():
    main()
    timeNow = moment.now().timezone("Asia/Shanghai").format("YYYY-M-D h:m:s A")
    print('Air Quality Check at %s' % timeNow)

schedule.every().day.at("22:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
