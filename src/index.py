from linear_algebra import *
from utils import *
from file_process import get_locations, mock_file
from point import Point
import datetime 
from copy import deepcopy
from tqdm import tqdm
import random


def generate_points(id):
    point_count = 20
    p = Point.getDefault()
    p.komtekLocationReferenceId = id
    
    points = []
    now = datetime.datetime.today()
    
    for i in range(point_count):

        p.timestamp = now + datetime.timedelta(weeks=i)
        
        burn_count = deepcopy(p)
        burn_count.unit = "Count"
        burn_count.seriesName = "burn:start"
        burn_count.value = positive(random.randint(-10,3))

        burn_minutes = deepcopy(p)
        burn_minutes.unit = "Minute"
        burn_minutes.seriesName = "burn"
        burn_minutes.value = burn_count.value * random.randint(1,5) * 60

        soot_minutes = deepcopy(p)
        soot_minutes.unit = "Minute"
        soot_minutes.seriesName = "burn:soot"
        soot_minutes.value = burn_minutes.value * positive(random.random() - 0.7)

        points.extend((burn_count, burn_minutes, soot_minutes))

    return points

def main():
    writer, file = mock_file()
    location_csv = "../komtekMatrikkel.csv"

    for location in tqdm(get_locations(location_csv)):
        for point in generate_points(location):
            writer.writerow(point.toRow())

    file.close()


if(__name__ == "__main__"): main()
