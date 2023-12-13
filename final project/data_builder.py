import requests
import urllib.parse
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from pathlib import Path
import os
import copy
import json
import csv

#None of the below code ended up being necessary but may still be useful in the future
"""
def set_download_feed(feed_id):
  return_endpoint = transitland_feed_endpoint.replace("{FEED_ID}",feed_id)
  return return_endpoint

def download_feed(feed_id):
  new_endpoint = set_download_feed(feed_id)
  query_string = urllib.parse.urlencode(parameters)
  zip_url = transitland_base_url + new_endpoint + "?" + query_string

  with urlopen(zip_url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extract('stops.txt',path=os.path.join(dir_to_download_to,"test"))

dir_to_download_to = Path(__file__).parent
"""

transitland_key = "quD9G8eEMpNU9RmkrGb1G27crRc8DytB"
transitland_base_url = "https://transit.land/api/v2/rest"
transitland_feed_endpoint = "/feeds/{FEED_ID}/download_latest_feed_version"
transitland_route_endpoint = "/routes/{ROUTE_ID}"
transitland_geosearch_endpoint = "/routes"
#Note, can make route and geosearch one variable in the future


parameters = {
  'api_key':transitland_key,
}


#search proccess
# 1: Given starting location, get all the routes in a specified range using the geography-based search feature for routes
# 2: After getting all the routes nearby, make more API requests for each route that comes up and IS NOT already stored in our local database
# 3: Add each individual route response data (including stop information) to local database (will require modifying JSON file)
# 4: Go through local database now and find each stop within specified range given in step 1
# 4b: If there are multiple stops in range within same route, only get stop that is closest to the given location
# 5: Return data structure containing all stops meeting criteria in step 4 along with their corresponding route
# 6: Search through returned routes and see if the coordinates of any of the stops are within a specified range of ending location
# 7: For each route that meets this criteria, add to list of routes to be returned to user along with starting and ending stops as well
# 7b: Make sure to include distance from starting position to starting stop and from ending position to ending stop
# 8: If nothing found for Step 6, repeat steps 1-5 but using the ending location instead of the starting location
# 9: Search through returned routes in step 8 and see if the coordinates of any of the stops in each route are within a specified range (transfer distance) of any of the stops in any of the routes in step 5
# 10: For each route that meets this criteria, create a tuple (or something similar) combining that route with the route it connects with and add to a list of route-pairs to be returned to user
# 10b: Make sure to include what the transfer point is (If multiple transfer points in a route-pair pick the one with the smallest distance) and the distance between transfer points
# 11: Repeat recursively by going back to step 8 and creating a list of all routes that are within specified transfer distance of a stop in each of the returned routes (this means repeating steps 1-5 but using each stop as essentially a new starting point and having to request the API again)

temp_storage = []

def response_to_temp(response):
  data = response.json()
  data['routes'][0].pop('geometry')
  temp_storage.append(data['routes'][0])

# transfers data from temp_storage to routes.json
def temp_to_local_routes():
  with open('routes.json','r') as openfile:
    json_file = json.load(openfile)
    for route in temp_storage:
      json_file["routes"].append(route)
  with open('routes.json','w') as openfile:
    json.dump(json_file,openfile,indent=4)

# logs all attempted downloads as completed in download_log.json
def temp_to_local_logs():
  with open('download_log.json','r') as openfile:
    json_file = json.load(openfile)
    while len(json_file['attempted']) > 0:
      completed_route = json_file['attempted'].pop(0)
      json_file['completed'].append(completed_route)

  with open('download_log.json','w') as openfile:
    json.dump(json_file,openfile,indent=4)


def temp_to_local():
  temp_to_local_routes()
  temp_to_local_logs()
  temp_storage.clear()

  
  
  

def set_download_route(route_id):
  return_endpoint = transitland_route_endpoint.replace("{ROUTE_ID}",route_id)
  return return_endpoint

def download_route(route_id):
  print(f"Downloading Route Data for {route_id}")
  new_endpoint = set_download_route(route_id)
  query_string = urllib.parse.urlencode(parameters)
  route_url = transitland_base_url + new_endpoint + "?" + query_string
  response = requests.get(route_url)
  print(f"{route_id} Download Successful")
  return response

def download_list_of_routes(route_list):
  for route in route_list:
    route_data = download_route(route)
    response_to_temp(route_data)
  temp_to_local()


def search_for_routes(lat,lon,radius):
  search_parameters = {
    'api_key':transitland_key,
    'lat':lat,
    'lon':lon,
    'radius':radius,
    'limit':100
  }
  query_string = urllib.parse.urlencode(search_parameters)
  search_url = transitland_base_url + transitland_geosearch_endpoint + "?" + query_string
  response = requests.get(search_url)
  routes_to_download = check_download_logs(response)
  download_list_of_routes(routes_to_download)


def check_download_logs(response):
  search_data = response.json()

  temp_logs = []
  
  with open('download_log.json','r') as openfile:
    json_file = json.load(openfile)
    for route in search_data['routes']:
      #Checks to see if route has been downloaded before or attempted to be downloaded
      if route['onestop_id'] not in json_file['completed'] and route['onestop_id'] not in json_file['attempted']:
        #if not, add it to the attempted list for routes
        json_file['attempted'].append(route['onestop_id'])
        temp_logs.append(route['onestop_id'])

  with open('download_log.json','w') as openfile:
    json.dump(json_file,openfile,indent=4)
  #return temp_logs
  return json_file['attempted']

def save_results(file_name, return_stops):
  csv_name = file_name + ".csv"
  geojson_name = file_name + ".geojson"
  with open(csv_name,"w") as openfile:
    csvwriter = csv.writer(openfile)
    #csvwriter.writerow()

#function used to make routes.json much, much smaller by removing data we weren't using
def data_shrinker():
  with open('routes.json','r') as openfile:
    json_file = json.load(openfile)
    for route in json_file['routes']:
      route.pop('geometry')
  with open('routes.json','w') as openfile:
    json.dump(json_file,openfile,indent=4)
  
