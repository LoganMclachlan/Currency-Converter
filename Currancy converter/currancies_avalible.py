import json
from urllib.request import urlopen

# This program list the three letter symbols for each currency the program can use

with urlopen("http://www.floatrates.com/daily/gbp.json") as response:
    source = response.read()

data = json.loads(source)

print("gbp")
for item in data:
    print(item)

var = input("enter any character to exit")
