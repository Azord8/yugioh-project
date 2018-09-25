import json
import os

for root, dirs, files in os.walk("pretty sets/"):
    for file in files:
        data = open("final sets/" + file)
        dataset = json.load(data)
        for item in dataset:
            print(item)
            for key, value in item:
                print(value)
