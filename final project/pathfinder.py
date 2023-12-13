from geopy import distance
import json

def distance_between_coordinates(lat1,lon1,lat2,lon2):
  coord1 = (lat1,lon1)
  coord2 = (lat2,lon2)
  return distance.distance(coord1,coord2).m

def create_stop_object(stop,distance,route_id,route_short_name,route_long_name,route_type):
  return_object = {
    "id":stop['stop']['id'],
    "stop_name":stop['stop']['stop_name'],
    "lat":stop['stop']['geometry']['coordinates'][1],
    "lon":stop['stop']['geometry']['coordinates'][0],
    "distance":distance,
    "route": {
      "route_id":route_id,
      "route_short_name":route_short_name,
      "route_long_name":route_long_name,
      "route_type":route_type
      }
  }
  return return_object

def print_return_stops(return_stops):
  print("\n###### The transit stops closest to your location are: ######\n")
  if len(return_stops.keys()) == 0:
    print("No transit stops found. Try increasing your search distance and running the program again.")
  for route in return_stops.keys():
    stop = return_stops[route]
    print(f"Stop: {stop['stop_name']}")
    print(f"Coordinates: {stop['lat']}, {stop['lon']}")
    print(f"{stop['distance']} meters away from you")
    print(f"Part of the {stop['route']['route_short_name']} {stop['route']['route_long_name']} route")
    print()
  print("############")
  

def get_stops_near_location(lat,lon,radius):
  return_stops = {}
  with open('routes.json','r') as openfile:
    json_file = json.load(openfile)
    for route in json_file['routes']:
      current_route = route['onestop_id']  
      stops = route['route_stops']
      for stop in stops:
        stop_lat = stop['stop']['geometry']['coordinates'][1]
        stop_lon = stop['stop']['geometry']['coordinates'][0]
        stop_distance = distance_between_coordinates(lat,lon,stop_lat,stop_lon)
        if (stop_distance < radius):
          if current_route not in return_stops.keys():
            
            target_stop = create_stop_object(stop,stop_distance,current_route,route['route_short_name'],route['route_long_name'],route['route_type'])
            return_stops[current_route] = target_stop
            
          elif return_stops[current_route]['distance'] > stop_distance:
            target_stop = create_stop_object(stop,stop_distance,current_route,route['route_short_name'],route['route_long_name'],route['route_type'])
            return_stops[current_route] = target_stop
  #maybe process with some function
  print_return_stops(return_stops)
  return return_stops



            
          
          
  
  
