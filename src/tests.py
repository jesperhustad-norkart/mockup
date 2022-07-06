import numpy as np
import matplotlib.pyplot as plt
import sys

from utils import *

def halden_locations_fallof():   
    halden_locations = [
        (59.121923, 11.386295),
        (59.115282, 11.395904),
        (59.111325, 11.399639),
        (59.094933, 11.413677),
        (59.082637, 11.425638),
        (59.049084, 11.453741),
        (59.012410, 11.479967),
        (58.941804, 11.504606)
    ]

    x = list(range(len(halden_locations)))
    y = []

    for loc in halden_locations:
        dist_muliplier = 0.2 + sig(dist_from_center(loc))
        y.append(dist_muliplier)

    plt.title("Selected distances should match sigmoid")
    plt.plot(x, y)
    plt.show()

def default(cases):
    print(f"{sys.argv[0]} not found, supported tests: {dict.keys(cases)}")

def main():
    cases =  {
        'dist': halden_locations_fallof(),
        'b': 2
    }

    if(sys.argv[0] in dict.keys(cases)): 
        cases.get(sys.argv[0])()
    else:
        default(cases)
   


if(__name__ == "__main__"): main()
