from pathfinder import get_stops_near_location
from data_builder import search_for_routes, data_shrinker
import json
import csv

def single_mode():
  print("This program can tell you the public transit stops near a location in NY (and potentially more in the future)")
  print("Enter the coordinates below (If you're not sure of the coordinates try using this link: https://www.latlong.net/convert-address-to-lat-long.html)")
  user_lat = float(input("Enter the lattitude: "))
  user_lon = float(input("Enter the longitude: "))
  print("Enter how far you're willing to travel to a public transit stop (in meters). Keep in mind if you would theoretically be walking, riding a bike or car over, or getting dropped off")
  user_radius = float(input("Enter the distance: "))
  find_stops(user_lat,user_lon,user_radius)


def find_stops(user_lat,user_lon,user_radius):
  search_for_routes(user_lat,user_lon,user_radius)
  return get_stops_near_location(user_lat,user_lon,user_radius)
  

def route_runner(route_id,distance):
  coords_list = []
  found = False
  with open('routes.json','r') as openfile:
    json_file = json.load(openfile)
    for route in json_file['routes']:
      if route['route_short_name'] == route_id:
        found = True
        stops = route['route_stops']
        for stop in stops:
          stop_lat = stop['stop']['geometry']['coordinates'][1]
          stop_lon = stop['stop']['geometry']['coordinates'][0]
          coords_list.append([stop_lat,stop_lon])
  if not found:
    print("No Data Available")
  else:
    list_results = []
    counter = 1
    for coord in coords_list:
      print(f"{counter}/{len(coords_list)} completed")
      counter+=1
      search_result = find_stops(coord[0],coord[1],distance)

      write_data = {}
      write_data['latitude'] = coord[0]
      write_data['longitude'] = coord[1]
      write_data['radius_searched'] = distance
      write_data['number_of_stops'] = len(search_result)
    
      bus_stop_counter = 0
      metro_stop_counter = 0
      stop_name = ""
      for route in search_result.keys():
        stop = search_result[route]
        if stop['route']['route_type'] == 1:
          metro_stop_counter+=1
        if stop['route']['route_type'] == 3:
          bus_stop_counter+=1
        if route_id == stop['route']['route_short_name']:
          stop_name = stop['stop_name']
    
      write_data['number_of_bus_stops'] = bus_stop_counter
      write_data['number_of_metro_stops'] = metro_stop_counter
      write_data['google_maps_link'] = f"https://www.google.com/maps/search/?api=1&query={coord[0]},{coord[1]}"
      write_data['stop_name'] = stop_name
      list_results.append(write_data)
    print(list_results)
    write_file = route_id + ".csv"
    with open(write_file,'w') as openfile:
      fields = ['latitude','longitude','radius_searched','number_of_stops','number_of_bus_stops','number_of_metro_stops','google_maps_link','stop_name']
      csvwriter = csv.DictWriter(openfile, fieldnames = fields)    
      csvwriter.writeheader()
      csvwriter.writerows(list_results)

def list_runner(distance,read_file,write_file):
  with open(read_file,'r') as openfile:
    csvreader = csv.reader(openfile)
    rows = []
    for row in csvreader:
      rows.append(row)
  list_results = []
  counter = 1
  for row in rows:
    print(f"{counter}/{len(rows)} completed")
    counter+=1
    search_result = find_stops(row[0],row[1],distance)
    write_data = {}
    write_data['latitude'] = row[0]
    write_data['longitude'] = row[1]
    write_data['radius_searched'] = distance
    write_data['number_of_stops'] = len(search_result)
    
    bus_stop_counter = 0
    metro_stop_counter = 0
    for route in search_result.keys():
      stop = search_result[route]
      if stop['route']['route_type'] == 1:
        metro_stop_counter+=1
      if stop['route']['route_type'] == 3:
        bus_stop_counter+=1
    
    write_data['number_of_bus_stops'] = bus_stop_counter
    write_data['number_of_metro_stops'] = metro_stop_counter
    write_data['google_maps_link'] = f"https://www.google.com/maps/search/?api=1&query={row[0]},{row[1]}"
    list_results.append(write_data)
  with open(write_file,'w') as openfile:
    fields = ['latitude','longitude','radius_searched','number_of_stops','number_of_bus_stops','number_of_metro_stops','google_maps_link']
    csvwriter = csv.DictWriter(openfile, fieldnames = fields)    
    csvwriter.writeheader()
    csvwriter.writerows(list_results)
  

def route_mode():
  print("Enter how far you're willing to travel to a public transit stop (in meters). Keep in mind if you would theoretically be walking, riding a bike or car over, or getting dropped off")
  user_radius = float(input("Enter the distance: "))
  print("Enter The route you'd like to investigate")
  user_route = input("Enter the route ID: ")
  route_runner(user_route,user_radius)

def csv_read_mode():
  print("Enter how far you're willing to travel to a public transit stop (in meters). Keep in mind if you would theoretically be walking, riding a bike or car over, or getting dropped off")
  user_radius = float(input("Enter the distance: "))
  print("Enter the file name of the list of coordinates you'd like to investigate")
  user_file = input("Enter the file name you want to read from: ")
  print("Enter the name of the file you'd like to write the results to")
  user_name = input("Enter the file name you want to write to: ")
  list_runner(user_radius,user_file,user_name)
  
  
def main():
  print("Choose what mode to run the program in. \nEnter 1 to search for stops near a single location\nEnter 2 to search for stops near all locations in a CSV\nEnter 3 to search for stops near all stops along a route")
  mode = int(input("Enter the mode you want to use (1 is used by default)"))
  if mode == 2:
    csv_read_mode()
  elif mode == 3:
    route_mode()
  else:
    single_mode()

main()
