#final project datasets
import pandas as pd
import operator
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token='geA6qNwvpHVBEDAVXq33qNDOb')
print("")


bikes_in_buildings = client.get("scjj-6yaf", select = 'noofbicyclerequested, ownerzipcode', limit = 50000) #not sure if all of these are necessary

#find the areas with the most requests
#print(bikes_in_buildings)

zip_codes = {}

for entry in bikes_in_buildings:
    if entry['ownerzipcode'] not in zip_codes:      #traverse through entire list of entries and add zip codes to dictionary while counting the entries for each zip code
        zip_codes[entry['ownerzipcode']] = int(entry['noofbicyclerequested'])
    else:
        zip_codes[entry['ownerzipcode']] += int(entry['noofbicyclerequested'])

# print(zip_codes) #this is a dictionary with the zip codes and the number of requests for each one
sorted_zip_codes = dict( sorted(zip_codes.items(), key=operator.itemgetter(1), reverse=True)) #sorts by descending values. found the solution online: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php


print('Dictionary in descending order by value : ', sorted_zip_codes)

print()
print("line break")
print()

bus_service_delivered = client.get("2e6s-9gpm", select = 'borough, route_id, service_delivered',  limit = 50000) 

bad_service = []

for entry in bus_service_delivered:

    if float(entry['service_delivered']) < 0.60 and entry['route_id'] not in bad_service: #if the service delivered is less than 60% and the route id is not already in the list of bad service, add it to the list
        bad_service.append(entry['route_id'])

bad_service = [entry for entry in bad_service if not entry.startswith('S')]  #remove all the routes related to Staten island because they are outliers (sorry SI)
print(bad_service)


