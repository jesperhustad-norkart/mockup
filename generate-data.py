# MOCK DATA GENERATION

# id [int]
# Value
# SeriesName.Value
# Chimney.KomtekLocationReferenceId
# Resolution.Value
# Unit.Value
# Timestamp


# furnace_lit_frequency: random + distance_from_center
# time_of_year_multiplier: sin 365 + randomness
# oven_type: old, new_clean_burning


# burn function
# furnace_lit_frequency * time_of_year_multiplier 


# soot function
# burn_function * soot_danger_level * oven_type

# TYPES OF DATA:
# burn count
# burn minutes
# soot burn minutes


# 



import math
from pydoc import resolve
import numpy as np
import matplotlib.pyplot as plt
import csv
import geopy.distance
import random

def perlin(x): return 0.3 * (-3.2 * np.sin(-1.3 * x) - 1.2 * np.sin(-1.7 * math.e * x) + 1.9 * np.sin(0.7 * math.pi * x))

def sig(x): return 0.2 + ( 1/(1 + np.exp(3 + (-x / 3))) ) / 1.3

halden_center = (59.125832, 11.389420)
def dist_from_center(coords): return geopy.distance.geodesic(halden_center, coords).km

def temp(x): return (np.sin( ( (x + 240) * 2 * math.pi) / 365) + 1) * 0.5

def temperature_multiplier(x): return temp(x) + (perlin(x/6)/20)

def bell_curve(x, p, w):
    boundry = (p - (w/2),  p + (w/2))
    resolution = 20
    if(x <  boundry[0] or x > boundry[1]): return 0
    i = np.linspace(*boundry, w*resolution)
    std = np.std(i)
    men = np.mean(i)
    points = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (i - men)**2 / (2 * std**2))
    print(points.size)
    return points[int((x - boundry[0]) * resolution)]

def process_row(row):
    result = row
    result[0] = dist_from_center((row[17].replace(",","."),row[18].replace(",",".")))
    return row






with open('komtekMatrikkel.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=";")
    data = iter(list(reader))

next(data) # skip headers

locations = []

for i in data:
    locations.append({
        "id" : i[0],
        "lat" : i[17],
        "lon" : i[18]
    })


with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["id","Value","SeriesName.Value","Chimney.KomtekLocationReferenceId","Resolution.Value","Unit.Value","Timestamp"])
    for i in data:
        writer.writerow(process_row(i))



# id [int]
# Value
# SeriesName.Value
# Chimney.KomtekLocationReferenceId
# Resolution.Value
# Unit.Value
# Timestamp










# x = np.linspace(0, 10, 10*20)   
# y = [bell_curve(i, 1, 2) for i in x]
# plt.xlabel("day") 
# plt.ylabel("temp(x)")  
# plt.plot(x, y) 
# plt.show()



# 6 * sigma = WIDTH (3)


# plt.plot(x, y)
# plt.show()



