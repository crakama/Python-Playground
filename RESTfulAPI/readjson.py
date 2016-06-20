import json
from pprint import pprint

f = open('pets.txt', 'r')
pets = json.loads(f.read())
f.close()

print(pets)
