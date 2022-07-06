from linear_algebra import *
from location import Location
from utils import *
from files import get_locations, mock_file
from point import Point

import datetime 
from copy import deepcopy
from tqdm import tqdm
import random
import sys


debug = False


def generate_points(location : Location):
    global debug
    
    point_count = 170
    if(len(sys.argv) > 1): point_count = int(sys.argv[1])

    p = Point.getDefault()
    p.komtekLocationReferenceId = location.uuid
    dist_muliplier = 0.2 + sig(dist_from_center((location.lat, location.lon))) 

    # print(dist_muliplier, location.lat, location.lon)
 

    points = []
    now = datetime.datetime.today()
    # print("\n\ntmp  day chan v dist")
    for i in range(point_count):

        p.timestamp = now + datetime.timedelta(weeks=i)

        day = p.timestamp.timetuple().tm_yday
        temp_multiplier = temperature_multiplier(day)

        burn_chance =  temp_multiplier * ( dist_muliplier + 0.5)

        

        burn_count = deepcopy(p)
        burn_count.unit = "Count"
        burn_count.seriesName = "burn:start"
        burn_count.value = int(burn_chance * 6 * ( random.random()+ 0.2) )


        if(debug): 
            print(f"{round(temp_multiplier,2):1.2f} {day:3.0f} {burn_chance:1.2f} {burn_count.value} {dist_muliplier:1.2f}")

        # if(burn_count.value == 0): continue

        burn_minutes = deepcopy(p)
        burn_minutes.unit = "Minute"
        burn_minutes.seriesName = "burn"
        burn_minutes.value = int(burn_count.value * 60 * (0.2 + random.random() * 0.8) * 5)

        soot_minutes = deepcopy(p)
        soot_minutes.unit = "Minute"
        soot_minutes.seriesName = "burn:soot"
        soot_minutes.value = int(burn_minutes.value * positive(random.random() - 0.8))

        points.extend((burn_count, burn_minutes, soot_minutes))

    debug = False

    return points

def main():
    global debug
    writer, file = mock_file()
    location_csv = "locations.csv"

    for location in tqdm(get_locations(location_csv)):
        for point in generate_points(location):
            writer.writerow(point.toRow())
    file.close()


if(__name__ == "__main__"): main()
