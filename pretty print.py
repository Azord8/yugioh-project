import json
import os
import pprint


# for root, dirs, files in os.walk("/home/azord/PycharmProjects/ygo project/sets/"):
#     for file in files:
#         oldfile = open("/home/azord/PycharmProjects/ygo project/sets/" + file)
#         newfile = open(file + "2", "w")
#         cards = False
#         for line in oldfile:
#             if not cards:
#                 if '"cards":' not in line:
#                     newfile.write(line)
#                 else:
#                     newfile.write("[")
#                     cards = True



# for root, dirs, files in os.walk("sets/"):
#     for file in files:
#         json_data = open("sets/" + file).read()
#         data = json.loads(json_data)
#         f = open((file + "_pretty"), "w")
#         f.write(json.dumps(data, indent=4))

with open('pretty sets/Crossroads of Chaos_pretty') as data_file:
    setlist = json.load(data_file)

for element,data in setlist:
    print(data)

