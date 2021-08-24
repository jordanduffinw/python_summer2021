# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/
# look at this: https://googlemaps.github.io/google-maps-services-python/docs/

import importlib
import os
import googlemaps

os.chdir(r'C:\Users\jorda\OneDrive\Keys')
imported_items = importlib.import_module('start_google_jdw')
gmaps = imported_items.client


whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

from pprint import pprint

### Q1
# Grabs location of White House
location = gmaps.distance_matrix(whitehouse, embassies)
pprint(location["rows"][0]["elements"][0]["distance"]["text"])
pprint(location["rows"][0]["elements"][1]["distance"])
pprint(location["rows"][0]["elements"][2]["distance"])


emb_dict = {}
distances = []

for i in range(3):
    emb = location["destination_addresses"][i]
    d = float(location["rows"][0]["elements"][i]["distance"]["text"].split()[0])
    emb_dict[emb] = d

#print(emb_dict)
#print(location["destination_addresses"][0])

# find minimum:
#print(min(emb_dict.values()))
min_emb = min(emb_dict)

for k, v in emb_dict.items():
    if v == min(emb_dict.values()):
        print("The closest embassy to the White House is {} with a distance of {} meters.".format(k, v*1000))
        
### Q2
cafe_result = gmaps.places_nearby(embassies[1], rank_by = "distance", type = "cafe", keyword = "breakfast")
cafe = cafe_result["results"][0]["name"]

### Q3
bar_result = gmaps.places_nearby(embassies[1], rank_by = "distance", type = "bar")
bars = {}
print(len(bar_result))

for i in range(len(bar_result)):
    name = bar_result["results"][i]["name"]
    rating = bar_result["results"][i]["rating"]
    bars[name] = rating
    
print(max(bars))