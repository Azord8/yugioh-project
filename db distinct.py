import rethinkdb as r
import json
import datetime

conn = r.connect()
conn.use("ygo")

# insert pack names into pack list
# data = r.table("packlist").insert(r.table("cards").pluck("pack").distinct()).run(conn)
# print(data)



packArray = [
    {"pack":'Dark Revelation Volume 1', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Ancient Prophecy', "release": datetime.date(2009,9,01), "shortname":"ANPR"}
    {"pack":'Ancient Sanctuary', "release": datetime.date(2004,6,01), "shortname":"AST"}
    {"pack":'Crimson Crisis', "release": datetime.date(2009,3,03), "shortname":"CRMS"}
    {"pack":'Crossroads of Chaos', "release": datetime.date(2008,11,18), "shortname":"CSOC"}
    {"pack":'Cyberdark Impact', "release": datetime.date(2006,11,15), "shortname":"CDIP"}
    {"pack":'Cybernetic Revolution', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Beginning 1', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Beginning 2', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Crisis', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Legends', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Revelation Volume 2', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Dark Revelation Volume 4', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Elemental Energy', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Enemy of Justice', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Exclusive Pack', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Flaming Eternity', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Force of the Breaker', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Gladiator\'s Assault', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Hidden Arsenal', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Invasion of Chaos', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Labyrinth of Nightmare', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Legacy of Darkness', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Light of Destruction', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Magic Ruler', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Magician\'s Force', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Metal Raiders', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Phantom Darkness', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Pharaoh\'s Servant', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Pharaonic Guardian', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Power of the Duelist', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Premium Pack (TCG)', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Premium Pack 2 (TCG)', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Raging Battle', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Retro Pack', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Retro Pack 2', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Rise of Destiny', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Shadow of Infinity', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Soul of the Duelist', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Stardust Overdrive', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Strike of Neos', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'Tactical Evolution', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'The Duelist Genesis', "release": datetime.date(2005,3,19), "shortname":"DR1"}
    {"pack":'The Lost Millennium', "release": datetime.date(2005,3,19), "shortname":"DR1"}
]
