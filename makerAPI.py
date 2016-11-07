import json
import urllib2

apiURL = 'https://maker.ifttt.com/trigger/weather_data/with/key/V_9xl1HgDOZDZaC_V20l5'

def triggerIFTTT(value_one, value_two, value_three):
    data = {
        'value1':value_one,
        'value2':value_two,
        'value3':value_three,
    }

    req = urllib2.Request(apiURL)
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(data))
    return response.read()
