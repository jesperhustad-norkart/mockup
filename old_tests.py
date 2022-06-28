from os import sep
from wsgiref.headers import Headers
import utm

import csv

# Bratner terrasse 44

# Lat	59.1447974
# Lon	11.4120554




# print(utm.to_latlon(6558669, 637977, 32, 'N'))
print(utm.to_latlon(637977, 6558669, 32, 'N'))


with open('matrikkelenAdresse.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=";")
    data = iter(list(reader))

rows = []

headers = next(data) # jump over headers
headers[17] = "latitude"
headers[18] = "longitude"
# print(headers)

index = 0
for i in data:
    index += 1
    print(str(index), end="\r")    
    result = i
    latlon = utm.to_latlon(float(i[18]), float(i[17]), 32, 'N')
    result[17] = str(round(latlon[0],7)).replace(".",",")
    result[18] = str(round(latlon[1],7)).replace(".",",")
    rows.append(result)

print(rows[1][17])

with open('komtekMatrikkel.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)
    for r in rows:
        writer.writerow(r)
    
