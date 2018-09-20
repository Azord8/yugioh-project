import json
import rethinkdb as r
import os

conn = r.connect()
conn.use("ygo")

json_data = open("/home/azord/PycharmProjects/ygo project/sets/Ancient Prophecy").read()
data = json.loads(json_data)
print(data)
r.table("cards").insert(data).run(conn)
