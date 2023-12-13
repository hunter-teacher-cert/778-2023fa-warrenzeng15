import requests
import urllib.parse

"""
transitland_key = "quD9G8eEMpNU9RmkrGb1G27crRc8DytB"
transitland_base_url = "https://transit.land/api/v2/rest"
transitland_endpoint = "/routes/r-dr5r-a"

parameters = {
  'api_key':transitland_key,
  #'adm1_name':"New York",
  #'onestop_id':"r-dr5r-a",
  #'limit':1
}
query_string = urllib.parse.urlencode(parameters)
print(query_string)
final_url = transitland_base_url + transitland_endpoint + "?" + query_string
"""
###Testing Lat/Lon/Radius ###

transitland_key = "quD9G8eEMpNU9RmkrGb1G27crRc8DytB"
transitland_base_url = "https://transit.land/api/v2/rest"
#transitland_endpoint = "/routes" commented out to test stops
transitland_endpoint = "/stops"

parameters = {
  'api_key':transitland_key,
  #'adm1_name':"New York",
  #'onestop_id':"r-dr5r-a",
  #'limit':1,
  'lat':40.672980,
  'lon':-73.704950,
  'radius':1000
}
query_string = urllib.parse.urlencode(parameters)
#print(query_string)
final_url = transitland_base_url + transitland_endpoint + "?" + query_string

### Ending Test ###

## Below For Routes ##
"""
response = requests.get(final_url)
data = response.json()
print("\n Data Responses \n")
for routes in data['routes']:
  print("OneStop Id:" + routes['onestop_id'])
  print("Short Name:" + routes['route_short_name'])
  print("Long Name:" + routes['route_long_name'])
  print()
#print(data['operators'])
#for thing in data['operators']:
#  print(thing)
#  print("\n")

#print(data)


#Now attempting same thing for movies near me
parameters['lat'] = 40.657660
parameters['lon'] = -73.672020

query_string = urllib.parse.urlencode(parameters)
#print(query_string)
final_url = transitland_base_url + transitland_endpoint + "?" + query_string


response = requests.get(final_url)
data = response.json()
print("\n Data Responses \n")
for routes in data['routes']:
  print("OneStop Id:" + routes['onestop_id'])
  print("Short Name:" + routes['route_short_name'])
  print("Long Name:" + routes['route_long_name'])
  print()
"""
##End of Route Testing Code ##

##Below for Stops ##
response = requests.get(final_url)
data = response.json()
print("\n Data Responses \n")
for stops in data['stops']:
  print("Source Feed:" + stops['feed_version']['feed']['onestop_id'])
  print("OneStop Id:" + stops['onestop_id'])
  print("Stop Name:" + stops['stop_name'])
  print()
#print(data['operators'])
#for thing in data['operators']:
#  print(thing)
#  print("\n")

#print(data)


#Now attempting same thing for movies near me
parameters['lat'] = 40.657660
parameters['lon'] = -73.672020
parameters['limit'] = 100


query_string = urllib.parse.urlencode(parameters)
#print(query_string)
final_url = transitland_base_url + transitland_endpoint + "?" + query_string


response = requests.get(final_url)
data = response.json()
print("\n Data Responses \n")
for stops in data['stops']:
  print("Source Feed:" + stops['feed_version']['feed']['onestop_id'])
  print("OneStop Id:" + stops['onestop_id'])
  print("Stop Name:" + stops['stop_name'])
  print()



##End of Stop Testing Code
