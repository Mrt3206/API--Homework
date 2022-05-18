""""API--Homework
https://api.nasa.gov adresindeki datalardan;
1- NeoWs (Near Earth Object Web Service) is a RESTful web service 
for near earth Asteroid information. With NeoWs a user can: search 
for Asteroids based on their closest approach date to Earth, lookup
a specific Asteroid with its NASA JPL small body id, as well asbrowse 
the overall data-set.1 temmuz 2016 ile 30 temmuz 2016 tarihleri arasinda 
dunyaya potansiyel tehlike olusturan astroid datasini alarak astorid.csv dosyasina kaydediniz."""

import requests
import datetime
import json
import csv

url='https://api.nasa.gov/neo/rest/v1/feed'
apiKey='coXhEEnYwg9CUcTzHgkgo2b7PDurWSfZKfMh4AJo'

d1=1
d2=8
fields=[]
data1=[]
#API connection
while(d1<30):
    start_date=datetime.date(2016,7,d1)
    end_date=datetime.date(2016,7,d2)
    print(start_date,end_date)
    r=requests.get(url, params={
    'start_date':start_date,
    'end_date':end_date,
    'api_key':apiKey
    })

    data=json.loads(r.text)
    
    print(r)
    print(data['element_count'])

    for j in range(8):
            for i in range(data['element_count']):
                try:
                    if data['near_earth_objects'][list(data['near_earth_objects'].keys())[j]][i]['is_potentially_hazardous_asteroid']==True:
                        data1.append(data['near_earth_objects'][list(data['near_earth_objects'].keys())[j]][i]) #put dict in list
                        if len(fields)==0:  #dict fields are defined for csv
                            fields=list(data['near_earth_objects'][list(data['near_earth_objects'].keys())[j]][i].keys())
                        # write csv
                        with open ('astreoids.csv','w') as f:
                            writer=csv.DictWriter(f,fieldnames=fields)
                            writer.writeheader()
                            writer.writerows(data1)
                except IndexError:        
                    break
    d1=d2+1
    d2=d2+8
    if d2>30:
        d2=30
    