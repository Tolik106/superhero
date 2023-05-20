from pprint import pprint
import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
spisok = response.json()
#pprint(spisok)
Thanos = next(x for x in spisok if x["name"] == "Thanos")
Hulk = next(x for x in spisok if x["name"] == "Hulk")
Captain_America = next(x for x in spisok if x["name"] == "Captain America")

powerstats_Hulk = Hulk['powerstats']
Hulk_int = powerstats_Hulk['intelligence']

powerstats_Thanos = Thanos['powerstats']
Thanos_int = powerstats_Thanos['intelligence']

powerstats_Captain_America = Captain_America['powerstats']
Captain_America_int = powerstats_Captain_America['intelligence']

if Hulk_int <= Thanos_int >= Captain_America_int:
    print(f' Самый умный супергерой - Thanos, его интеллект = {Thanos_int}')
elif Thanos_int <= Hulk_int >= Captain_America_int:
    print(f' Самый умный супергерой - Hulk, его интеллект = {Hulk_int}')
elif Hulk_int <= Captain_America_int >= Thanos_int:
    print(f' Самый умный супергерой - Captain_America, его интеллект = {Captain_America_int}')

#for name in spisok:

   # print(name)









