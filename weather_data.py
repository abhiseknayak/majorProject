import requests,json

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("bhilai")
print(location.address)
print((location.latitude, location.longitude))
address=(location.latitude, location.longitude)
import csv


api_key="#add your own key"

base_url="https://api.darksky.net/forecast/"
l=[]
for i in range(11,21):
    year="20"+str(i)
    print(year)
    for j in range(1,13):
        l1=[]
        if(j<10):
            month="0"+str(j)
        else:
            month=str(j)
        print(month)
        complete_url=base_url+api_key+"/"+str(address[0])+","+str(address[1])+","+year+"-"+month+"-02T11:00:00"+"?units=si"

        response = requests.get(complete_url)

        x = response.json()
        print(x)
        try:
            temp=x["currently"]["temperature"]
            hum=x["currently"]["humidity"]
            ws=x["currently"]["windSpeed"]
            ccover=x["currently"]["cloudCover"]
        except KeyError:
            temp=float(input("enter temperature"))
            hum=float(input("enter humidity"))
            ws=float(input("enter windspeed"))
            ccover=float(input("enter cloud cover"))
            
        l1.append(temp)
        l1.append(hum)
        l1.append(ws)
        l1.append(ccover)
        l.append(l1)
        print(str(temp)+" "+str(hum)+" "+str(ws)+" "+str(ccover))

print(len(l))

with open('weather_imp.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['temperature', 'humidity','windspeed','cloudcover'])
    for i in range(0,len(l)):
        tsv_writer.writerow([l[i][0],l[i][1],l[i][2],l[i][3]])
    





