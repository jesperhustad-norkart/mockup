import csv
from location import Location


"""
Reading and writing data files.
"""

def get_locations(path) -> list[Location]:
    locations = []
    
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=";")
        data = iter(reader)
        
        next(data) # skip headers
        
        for i in data: 
            locations.append(Location(
                uuid = i[33], 
                lat = float(i[17].replace(',','.')),
                lon = float(i[18].replace(',','.'))
            ))

    return locations

def mock_file():
    """returns (writer, file)"""
    f = open('output.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["id","Value","SeriesName.Value","Chimney.KomtekLocationReferenceId","Resolution.Value","Unit.Value","Timestamp"])
    return (writer, f)



import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv("locations.csv", delimiter=';', skiprows=0, low_memory=False)
    # get_locations("locations.csv")
    plt.scatter(x=df['longitude'], y=df['latitude'])
    plt.show()

if(__name__ == "__main__"): main()
