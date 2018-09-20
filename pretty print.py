import json
import os
import pprint


for root, dirs, files in os.walk("/home/azord/PycharmProjects/ygo project/sets/"):
    for file in files:
        if "_pretty" in file:
            oldfile = open("/home/azord/PycharmProjects/ygo project/sets/" + file)
            newfile = open(file, "w")
            for line in oldfile:
                if '\'numbers\':' not in line:
                    newfile.write(line)





        # json_data = open("/home/azord/PycharmProjects/ygo project/sets/" + file).read()
        # data = json.loads(json_data)
        # f = open((file + "_pretty"), "w")
        # f.write(pprint.pformat(data, indent=1, width=100, depth=5, compact=False))





