from db_configuration import db
import os
import json
import pandas as pd
from connection_status import Connection_Status
from helper import generate_url
from check_database import check_availability

images_records = db.images

print('Connection Status:\n',images_records)

# loading json file
# lodeJson = open('/home/lalitmahato/niche/unitId.json', "r")
lodeJson = open('unitId.json', "r")
uId_data = pd.read_json(lodeJson)

end = 3000
start = 0
status_count = db['status'].count_documents({})
print(status_count)
total_uid = len(uId_data)
print("Total University Count: ", total_uid)
scrap_data_count = status_count
number = status_count + start
unable_to_scrap = 0
while number < end:
# while number < 1:
    print(number)
    perc = scrap_data_count/(end-start) * 100
    print("Completed: {} %".format(perc))
    print("Data Scraped: ", scrap_data_count)
    print("Institution Name: ", uId_data["Institution Name"][number])
    url = generate_url('https://www.niche.com/colleges/', uId_data["Institution Name"][number], '-')
    print('URL: ', url)
    stat = Connection_Status(url, uId_data["Institution Name"][number], 0, uId_data["UnitID"][number])
    if stat == False:
        db['status'].insert_one({
            'uid': int(uId_data["UnitID"][number]),
            'institute_name': uId_data["Institution Name"][number],
            'institutation_type': '',
            'scrap_status': False
        })
        unable_to_scrap = unable_to_scrap + 1
    scrap_data_count = scrap_data_count + 1
    number = number + 1
