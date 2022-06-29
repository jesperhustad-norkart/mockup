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