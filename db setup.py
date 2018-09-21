import json
import rethinkdb as r
import os

conn = r.connect()
conn.use("ygo")

for root, dirs, files in os.walk("final sets/"):
    for file in files:
        print(file)
        data = json.loads(open("final sets/" + file).read())
        r.table("cards").insert(data).run(conn)
