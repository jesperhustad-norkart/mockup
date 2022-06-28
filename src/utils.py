import math
from pydoc import resolve
from tokenize import Double
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
import csv
import geopy.distance
import random

def perlin(x): return 0.3 * (-3.2 * np.sin(-1.3 * x) - 1.2 * np.sin(-1.7 * math.e * x) + 1.9 * np.sin(0.7 * math.pi * x))

def sig(x): return 0.2 + ( 1/(1 + np.exp(3 + (-x / 3))) ) / 1.3

def temp(x): return (np.sin( ( (x + 240) * 2 * math.pi) / 365) + 1) * 0.5

def temperature_multiplier(x): return temp(x) + (perlin(x/6)/20)

def positive(x): return x if x > 0 else 0

def dist_from_center(coords: tuple[int, int]) -> int: 
    """Calculate distance from Halden center."""
    halden_center = (59.125832, 11.389420)
    return geopy.distance.geodesic(halden_center, coords).km