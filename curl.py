import urllib2
import sys
import json
url ="http://www.sojson.com/open/api/weather/json.shtml?city=上海"
req = urllib2.Request(url)
#req.add_header('IAF',abc.token_authiaas)
try:
    resp = urllib2.urlopen(req)
except urllib2.HTTPError,error:
    print "Cannot remove serice ", error
    sys.exit(1)
response = resp.read()
#print response
s= json.loads(response)
#print s['data']
print s['data']['forecast'][0]['type']
print s['data']['forecast'][0]['fengxiang']
#print s['data']['forecast'][0]['fengji']

#print s['data']['yesterday']['type']

#print s['data']['yesterday']['type']


