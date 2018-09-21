import json
import os
from collections import OrderedDict


for root, dirs, files in os.walk("pretty sets/"):
    for file in files:
        oldfile = open("pretty sets/" + file)
        newfile = open("final sets/" + file, "w")
        numbers = False
        count = 0
        first = False
        for line in oldfile:
            if not numbers:
                if '"numbers": [' not in line:
                    newfile.write(line)
                else:
                    numbers = True
            else:
                if not first:
                    first = True

                else:
                    if "}" in line:
                        if count != 3:
                            count += 1
                            newfile.write(line)
                    elif count == 3:
                        count = 0
                        numbers = False
                        first = False
                    else:
                        newfile.write(line)


# for root, dirs, files in os.walk("sets/"):
#     for file in files:
#         json_data = open("sets/" + file).read()
#         data = json.loads(json_data)
#         f = open((file + "_pretty"), "w")
#         f.write(json.dumps(data, indent=4))

# for root, dirs, files in os.walk("sets/"):
#     for file in files:
#         with open('sets/' + file) as data_file:
#             data = json.load(data_file, object_pairs_hook=OrderedDict)
#             for key, value in data.items():
#                 if key == "data":
#                     for key2, value2 in value.items():
#                         if key2 == "cards":
#                             f = open("pretty sets/" + file + "_pretty", "w")
#                             f.write(json.dumps(value2, indent=4))



