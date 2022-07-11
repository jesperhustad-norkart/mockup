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
TIMESERIES_RESOULTION_DAYS = 7

def generate_points(location : Location):
    global debug

    point_count = 170
    if(len(sys.argv) > 1): point_count = int(sys.argv[1])

    p = Point.getDefault()
    p.komtekLocationReferenceId = location.uuid
    dist_multiplier = 0.7 + sig(dist_from_center((location.lat, location.lon))) 

    #         Bad code added because year range doesn't take effect after a coupe years of running simulations
    person_moves_index = when_person_moves() - ((5 + (random.random()*3)) * (365 / TIMESERIES_RESOULTION_DAYS))
    
    # print(dist_muliplier, location.lat, location.lon)
    personality_multiplier = new_personality()


 

    points = []
    now = datetime.datetime.today()
    # print("\n\ntmp  day chan v dist")
    for i in range(point_count):

        if(i == person_moves_index): 
            person_moves_index = i + when_person_moves()
            personality_multiplier = new_personality()

        p.timestamp = now + timeseries_delta(i)

        day = p.timestamp.timetuple().tm_yday
        temp_multiplier = temperature_multiplier(day)

        burn_chance =  temp_multiplier * dist_multiplier * personality_multiplier

        burn_count = deepcopy(p)
        burn_count.unit = "Count"
        burn_count.seriesName = "burn:start"
        burn_count.value = int(burn_chance * 6 * ( random.random()+ 0.2) )


        if(debug): 
            print(f"{round(temp_multiplier,2):1.2f} {day:3.0f} {burn_chance:1.2f} {burn_count.value} {dist_multiplier:1.2f}")

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


# person moves every 5 to 10 years
# rand * 5   + 5


# personality stays identical forever
# multipler on burn amount



