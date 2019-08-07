import json
from urllib.request import urlopen

with urlopen("http://www.floatrates.com/daily/gbp.json") as response:
    source = response.read()

data = json.loads(source)

currancies = []

for item in data:
    currancies.append(item)

for i in range(0,len(data)):
    spacing = " "
    length = 40 - len(data[currancies[i]]["name"])
    for space in range(0,length):
        spacing += " "
    print("Name: " + data[currancies[i]]["name"] + spacing + "Code: " + data[currancies[i]]["code"])

__v = input("")
