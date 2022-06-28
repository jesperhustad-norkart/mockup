import csv



"""
Reading and writing data files.
"""

def get_locations(path):
    locations = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=";")
        data = iter(list(reader))
        next(data) # skip headers

    for i in data: 
        locations.append(i[33])

    return locations

def mock_file():
    """returns (writer, file)"""
    f = open('output.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["id","Value","SeriesName.Value","Chimney.KomtekLocationReferenceId","Resolution.Value","Unit.Value","Timestamp"])
    return (writer, f)