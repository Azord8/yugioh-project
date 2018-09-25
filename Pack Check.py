import json
import os

for root, dirs, files in os.walk("pretty sets/"):
    for file in files:
        data = open("final sets/" + file)
        dataset = json.load(data)
        print(file[:-7])
        for item in dataset:
            if item["pack"] != file[:-7]:
                print("error")
