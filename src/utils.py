import math
from pydoc import resolve
from tokenize import Double
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
import csv
import geopy.distance
import random
import datetime 
from scipy import rand
from location import Location

from index import TIMESERIES_RESOULTION_DAYS

def perlin(x): return 0.3 * (-3.2 * np.sin(-1.3 * x) - 1.2 * np.sin(-1.7 * math.e * x) + 1.9 * np.sin(0.7 * math.pi * x))

def sig(x): return 0.1 + ( 1/(1 + np.exp(3 + (-x / 2))) ) / 1.3 + (perlin(x*2.5)/50)

def temp(x): return (np.sin( ( (x + 240) * 2 * math.pi) / 365) + 1) * 0.5

def temperature_multiplier(x): return np.abs((1 - temp(x)) + (perlin(x/6)/20))

def positive(x): return x if x > 0 else 0

def new_personality(): 0.6 + (random.random() * 0.4)

def when_person_moves(): return (( random.random() * 8 ) +1 ) * (365 / TIMESERIES_RESOULTION_DAYS)

def timeseries_delta(x): return datetime.timedelta(days=x*TIMESERIES_RESOULTION_DAYS)

def seed_random(seed): 
    random.seed(seed)
    return random.random()

def dist_from_center(coords) -> int: 
    """Calculate distance from Halden center."""
    halden_center = (59.125832, 11.389420)
    return geopy.distance.geodesic(halden_center, coords).km


# def distrRand(start, end):
#     return round(random.choice(np.random.normal(loc= end - ((end-start)/2), scale =(end-start)/2, size=1)), 2)


# visualize sigmoid function sig(x)
def main():
    x = np.linspace(0, 20, 365)
    y = sig(x)
    plt.plot(x, y)
    plt.show()


if(__name__ == "__main__"): main()
