from linear_algebra import *
from location import Location
from utils import *
from files import get_locations, mock_file
from point import Point

import datetime 
from copy import deepcopy
from tqdm import tqdm
import random


first = True


def generate_points(location : Location):
    global first
    point_count = 55
    p = Point.getDefault()
    p.komtekLocationReferenceId = location.uuid
    dist_muliplier = 0.2 + sig(dist_from_center((location.lat, location.lon))) + (random.random()/10)

    points = []
    now = datetime.datetime.today()
    
    for i in range(point_count):

        p.timestamp = now + datetime.timedelta(weeks=i)

        day = p.timestamp.timetuple().tm_yday
        temp_multiplier = temperature_multiplier(day)

        

        burn_chance = random.random() * 2  * temp_multiplier * dist_muliplier

        if(first): print(f"{round(temp_multiplier,2):1.2f} {day:3.0f} {burn_chance:1.2f} {dist_muliplier:1.2f}")

        burn_count = deepcopy(p)
        burn_count.unit = "Count"
        burn_count.seriesName = "burn:start"
        burn_count.value = int(burn_chance * 7)

        if(burn_count.value == 0): continue

        burn_minutes = deepcopy(p)
        burn_minutes.unit = "Minute"
        burn_minutes.seriesName = "burn"
        burn_minutes.value = int(burn_count.value * 60 * (0.1 + (random.random() * 5)))

        soot_minutes = deepcopy(p)
        soot_minutes.unit = "Minute"
        soot_minutes.seriesName = "burn:soot"
        soot_minutes.value = int(burn_minutes.value * positive(random.random() - 0.8))

        points.extend((burn_count, burn_minutes, soot_minutes))

    first = False

    return points

def main():
    writer, file = mock_file()
    location_csv = "locations.csv"

    for location in tqdm(get_locations(location_csv)):
        for point in generate_points(location):
            writer.writerow(point.toRow())
        break

    file.close()


if(__name__ == "__main__"): main()
