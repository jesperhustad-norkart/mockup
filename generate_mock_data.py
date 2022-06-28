
import json
import random
import uuid
import numpy as np
import csv


sensor_readings_per_house = 10




points = []
NorkartData = []
komtek_id = []
airMontData = []


file=open("komtekMatrikkel.csv", "r", encoding="utf-8")
reader = csv.reader(file, delimiter=";")

for line in reader:
    lat = line[17]
    lon = line[18]
    points.append([lat, lon])
            
            

# count of generated sensor data readings
data_size = len(points) * sensor_readings_per_house

# comomon furnace types found at: https://www.riksantikvaren.no/veileder/vedovner/
furnaces = ["kasseovn", "bjornovn", "sylinderovn", "etasjeovn"]
furnace_particle_pollution = [15.10, 18.00,	16.80, 1.28]

def getPoint(index, i):
    return points[index][i]

def distrRand(start, end):
    return round(random.choice(np.random.normal(loc= end - ((end-start)/2), scale =(end-start)/2, size=1)), 2)




for i in range(komtek_count):
    print("komtek progress: "+str(i)+"/"+str(komtek_count), end="\r")
    furnace_index = random.randint(0, len(furnaces)-1)
    NorkartData.append({
        "komtek_id" : str(uuid.uuid4()),
        "furnaceType" : furnaces[furnace_index],
        "particle_pollution" : furnace_particle_pollution[furnace_index],
        "daysSinceLastSweep" : random.randint(365, 365 * 4),
        "lat" : getPoint(i,"lat"),
        "lon" : getPoint(i, "lon")
    })


for building in NorkartData:
    komtek_id.append(building["komtek_id"])
   

for i in range(data_size):
    if(i%100==0):
        print("data progress: "+str(i)+"/"+str(data_size), end="\r")
    sootTime = distrRand(-20,8)
    sootTime = sootTime if sootTime > 0 else 0

    airMontData.append({
        "komtek_id" : komtek_id[random.randint(0, len(komtek_id)-1)],
        "furnaceId" : str(uuid.uuid4()),
        "AverageTemperature" : distrRand(15,50),
        "sootFormationTime" : round(sootTime,0),
        "furnaceLitTime" : distrRand(0, 40),
        "furnaceUsedCount" : distrRand(0, 8)
    })



with open("chimneySensorData.json", "w") as text_file: text_file.write(json.dumps(airMontData))
with open("komtek.json", "w") as text_file: text_file.write(json.dumps(NorkartData))