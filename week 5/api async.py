# api_async.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: n/a

import json
import requests
import pandas as pd
import numpy as np
from sodapy import Socrata

# Use the NASA API database
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data.items())

# print the DataFrame
print(df)
print("")
print("Address of the NASA Photo of the day:", df.at[7,1])

print("")


# data.ny.gov fire departments

client = Socrata("data.ny.gov", None)
print("")

target_city = input("Please enter a city: ")
target_city = target_city.upper()       #all the cities are uppercase

results = client.get("qfsu-zcpv", city= target_city, select="phone_number,lat,long")

#print(results)

phone_number = results[0]['phone_number']
lat = results[0]['lat']
long = results[0]['long']

print("The phone number of the fire department in", target_city, "is: ")
print(phone_number)

print("The google maps link for the fire department in", target_city, "is: ")

maps_url = "https://www.google.com/maps/place/" + lat + "+" +long

print(maps_url)
print("")



# park usage api


target_county = input("Please enter a county: ")
results = client.get("8f3n-xj78", county = target_county, year = '2022', select = 'facility, Attendance')

#print(results)

new_list = []

for park in results:
    new_list.append(park['facility'])
    
counter = 0 
for park in new_list:
    print(counter, park)
    counter += 1 

print("")
target_park = input("Please enter a number corresponding to a park: ")
target_park = int(target_park)

attendance = results[target_park]['Attendance']

print("Attendance number in 2022 for that park was: ", attendance)

