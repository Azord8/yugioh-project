import rethinkdb as r
import json
import datetime

conn = r.connect()
conn.use("ygo")

# insert pack names into pack list
# data = r.table("packlist").insert(r.table("cards").pluck("pack").distinct()).run(conn)
# print(data)


packArray = [
    {"pack": 'Dark Revelation Volume 1', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
    {"pack": 'Ancient Prophecy', "release": datetime.date(2009, 9, 1), "shortname": "ANPR"},
    {"pack": 'Ancient Sanctuary', "release": datetime.date(2004, 6, 1), "shortname": "AST"},
    {"pack": 'Crimson Crisis', "release": datetime.date(2009, 3, 3), "shortname": "CRMS"},
    {"pack": 'Crossroads of Chaos', "release": datetime.date(2008, 11, 18), "shortname": "CSOC"},
    {"pack": 'Cyberdark Impact', "release": datetime.date(2006, 11, 15), "shortname": "CDIP"},
    {"pack": 'Cybernetic Revolution', "release": datetime.date(2005, 8, 17), "shortname": "CRV"},
    {"pack": 'Dark Beginning 1', "release": datetime.date(2004, 10, 12), "shortname": "DB1"},
    {"pack": 'Dark Beginning 2', "release": datetime.date(2005, 7, 27), "shortname": "DB2"},
    {"pack": 'Dark Crisis', "release": datetime.date(2003, 12, 1), "shortname": "DCR"},
    {"pack": 'Dark Legends', "release": datetime.date(2008, 11, 21), "shortname": "DLG1"},
    {"pack": 'Dark Revelation Volume 2', "release": datetime.date(2005, 20, 20), "shortname": "DR2"},
    {"pack": 'Dark Revelation Volume 4', "release": datetime.date(2007, 11, 14), "shortname": "DR04"},
    {"pack": 'Elemental Energy', "release": datetime.date(2005, 11, 16), "shortname": "EEN"},
    {"pack": 'Enemy of Justice', "release": datetime.date(2006, 5, 17), "shortname": "EOJ"},
    {"pack": 'Exclusive Pack', "release": datetime.date(2004, 8, 1), "shortname": "EP1"},
    {"pack": 'Flaming Eternity', "release": datetime.date(2005, 3, 1), "shortname": "FET"},
    {"pack": 'Force of the Breaker', "release": datetime.date(2007, 5, 16), "shortname": "FOTB"},
    {"pack": 'Gladiator\'s Assault', "release": datetime.date(2007, 11, 14), "shortname": "GLAS"},
    {"pack": 'Hidden Arsenal', "release": datetime.date(2009, 11, 10), "shortname": "HA01"},
    {"pack": 'Invasion of Chaos', "release": datetime.date(2004, 3, 1), "shortname": "IOC"},
    {"pack": 'Labyrinth of Nightmare', "release": datetime.date(2003, 3, 1), "shortname": "LON"},
    {"pack": 'Legacy of Darkness', "release": datetime.date(2003, 6, 6), "shortname": "LOD"},
    {"pack": 'Light of Destruction', "release": datetime.date(2008, 5, 13), "shortname": "LODT"},
    {"pack": 'Magic Ruler', "release": datetime.date(2002, 9, 16), "shortname": "SRL"},
    {"pack": 'Magician\'s Force', "release": datetime.date(2003, 10, 10), "shortname": "MFC"},
    {"pack": 'Metal Raiders', "release": datetime.date(2002, 6, 26), "shortname": "MRD"},
    {"pack": 'Phantom Darkness', "release": datetime.date(2008, 2, 13), "shortname": "PTDN"},
    {"pack": 'Pharaoh\'s Servant', "release": datetime.date(2002, 10, 20), "shortname": "PSV"},
    {"pack": 'Pharaonic Guardian', "release": datetime.date(2003, 7, 18), "shortname": "PGD"},
    {"pack": 'Power of the Duelist', "release": datetime.date(2006, 8, 16), "shortname": "POTD"},
    {"pack": 'Premium Pack (TCG)', "release": datetime.date(2007, 10, 8), "shortname": "PP01"},
    {"pack": 'Premium Pack 2 (TCG)', "release": datetime.date(2008, 7, 21), "shortname": "PP02"},
    {"pack": 'Raging Battle', "release": datetime.date(2009, 5, 12), "shortname": "RGBT"},
    {"pack": 'Retro Pack', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
    {"pack": 'Retro Pack 2', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
    {"pack": 'Rise of Destiny', "release": datetime.date(2004, 12, 1), "shortname": "RDS"},
    {"pack": 'Shadow of Infinity', "release": datetime.date(2006, 2, 8), "shortname": "SOI"},
    {"pack": 'Soul of the Duelist', "release": datetime.date(2004, 10, 1), "shortname": "SOD"},
    {"pack": 'Stardust Overdrive', "release": datetime.date(2009, 11, 17), "shortname": "SOVR"},
    {"pack": 'Strike of Neos', "release": datetime.date(2007, 2, 28), "shortname": "STON"},
    {"pack": 'Tactical Evolution', "release": datetime.date(2007, 8, 15), "shortname": "TAEV"},
    {"pack": 'The Duelist Genesis', "release": datetime.date(2008, 9, 2), "shortname": "TDGS"},
    {"pack": 'The Lost Millennium', "release": datetime.date(2005, 6, 1), "shortname": "TLM"}
]
