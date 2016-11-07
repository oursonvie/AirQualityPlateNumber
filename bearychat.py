# -*- coding: utf-8 -*-
import urllib
import urllib2

url = 'https://hook.bearychat.com/=bw6fh/incoming/bfde58a43ba08fe1600a4e108082f224'

def bearySend(message):
    data = 'payload={"text":"%s"}' % message
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()
