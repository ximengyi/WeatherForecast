import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/df4174420f8d568d/forecast/conditions/q/CN/Xintiandi.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
