import rethinkdb as r
import json
from datetime import datetime

conn = r.connect()
conn.use("ygo")

# insert pack names into pack list
# data = r.table("packlist").insert(r.table("cards").pluck("pack").distinct()).run(conn)
# print(data)


# packArray = [
#     {"pack": 'Dark Revelation Volume 1', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
#     {"pack": 'Ancient Prophecy', "release": datetime.date(2009, 9, 1), "shortname": "ANPR"},
#     {"pack": 'Ancient Sanctuary', "release": datetime.date(2004, 6, 1), "shortname": "AST"},
#     {"pack": 'Crimson Crisis', "release": datetime.date(2009, 3, 3), "shortname": "CRMS"},
#     {"pack": 'Crossroads of Chaos', "release": datetime.date(2008, 11, 18), "shortname": "CSOC"},
#     {"pack": 'Cyberdark Impact', "release": datetime.date(2006, 11, 15), "shortname": "CDIP"},
#     {"pack": 'Cybernetic Revolution', "release": datetime.date(2005, 8, 17), "shortname": "CRV"},
#     {"pack": 'Dark Beginning 1', "release": datetime.date(2004, 10, 12), "shortname": "DB1"},
#     {"pack": 'Dark Beginning 2', "release": datetime.date(2005, 7, 27), "shortname": "DB2"},
#     {"pack": 'Dark Crisis', "release": datetime.date(2003, 12, 1), "shortname": "DCR"},
#     {"pack": 'Dark Legends', "release": datetime.date(2008, 11, 21), "shortname": "DLG1"},
#     {"pack": 'Dark Revelation Volume 2', "release": datetime.date(2005, 20, 20), "shortname": "DR2"},
#     {"pack": 'Dark Revelation Volume 4', "release": datetime.date(2007, 11, 14), "shortname": "DR04"},
#     {"pack": 'Elemental Energy', "release": datetime.date(2005, 11, 16), "shortname": "EEN"},
#     {"pack": 'Enemy of Justice', "release": datetime.date(2006, 5, 17), "shortname": "EOJ"},
#     {"pack": 'Exclusive Pack', "release": datetime.date(2004, 8, 1), "shortname": "EP1"},
#     {"pack": 'Flaming Eternity', "release": datetime.date(2005, 3, 1), "shortname": "FET"},
#     {"pack": 'Force of the Breaker', "release": datetime.date(2007, 5, 16), "shortname": "FOTB"},
#     {"pack": 'Gladiator\'s Assault', "release": datetime.date(2007, 11, 14), "shortname": "GLAS"},
#     {"pack": 'Hidden Arsenal', "release": datetime.date(2009, 11, 10), "shortname": "HA01"},
#     {"pack": 'Invasion of Chaos', "release": datetime.date(2004, 3, 1), "shortname": "IOC"},
#     {"pack": 'Labyrinth of Nightmare', "release": datetime.date(2003, 3, 1), "shortname": "LON"},
#     {"pack": 'Legacy of Darkness', "release": datetime.date(2003, 6, 6), "shortname": "LOD"},
#     {"pack": 'Light of Destruction', "release": datetime.date(2008, 5, 13), "shortname": "LODT"},
#     {"pack": 'Magic Ruler', "release": datetime.date(2002, 9, 16), "shortname": "SRL"},
#     {"pack": 'Magician\'s Force', "release": datetime.date(2003, 10, 10), "shortname": "MFC"},
#     {"pack": 'Metal Raiders', "release": datetime.date(2002, 6, 26), "shortname": "MRD"},
#     {"pack": 'Phantom Darkness', "release": datetime.date(2008, 2, 13), "shortname": "PTDN"},
#     {"pack": 'Pharaoh\'s Servant', "release": datetime.date(2002, 10, 20), "shortname": "PSV"},
#     {"pack": 'Pharaonic Guardian', "release": datetime.date(2003, 7, 18), "shortname": "PGD"},
#     {"pack": 'Power of the Duelist', "release": datetime.date(2006, 8, 16), "shortname": "POTD"},
#     {"pack": 'Premium Pack (TCG)', "release": datetime.date(2007, 10, 8), "shortname": "PP01"},
#     {"pack": 'Premium Pack 2 (TCG) (TCG)', "release": datetime.date(2008, 7, 21), "shortname": "PP02"},
#     {"pack": 'Raging Battle', "release": datetime.date(2009, 5, 12), "shortname": "RGBT"},
#     {"pack": 'Retro Pack', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
#     {"pack": 'Retro Pack 2', "release": datetime.date(2005, 3, 19), "shortname": "DR1"},
#     {"pack": 'Rise of Destiny', "release": datetime.date(2004, 12, 1), "shortname": "RDS"},
#     {"pack": 'Shadow of Infinity', "release": datetime.date(2006, 2, 8), "shortname": "SOI"},
#     {"pack": 'Soul of the Duelist', "release": datetime.date(2004, 10, 1), "shortname": "SOD"},
#     {"pack": 'Stardust Overdrive', "release": datetime.date(2009, 11, 17), "shortname": "SOVR"},
#     {"pack": 'Strike of Neos', "release": datetime.date(2007, 2, 28), "shortname": "STON"},
#     {"pack": 'Tactical Evolution', "release": datetime.date(2007, 8, 15), "shortname": "TAEV"},
#     {"pack": 'The Duelist Genesis', "release": datetime.date(2008, 9, 2), "shortname": "TDGS"},
#     {"pack": 'The Lost Millennium', "release": datetime.date(2005, 6, 1), "shortname": "TLM"}
# ]

packnames = [
    {"pack": 'Absolute Powerforce', "release": datetime.strptime("02, 16, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Abyss Rising', "release": datetime.strptime("11, 9, 2012", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Ancient Prophecy', "release": datetime.strptime("09, 1, 2009", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Ancient Sanctuary', "release": datetime.strptime("06, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Battles of Legend: Light\'s Revenge', "release": datetime.strptime("07, 7, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Battles of Legend: Relentless Revenge', "release": datetime.strptime("06, 29, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Breakers of Shadow', "release": datetime.strptime("1, 15, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Circuit Break', "release": datetime.strptime("10, 20, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Clash of Rebellions', "release": datetime.strptime("08, 7, 2015", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Code of the Duelist', "release": datetime.strptime("08, 4, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Cosmo Blazer', "release": datetime.strptime("1, 25, 2013", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Crimson Crisis', "release": datetime.strptime("03, 3, 2009", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Crossed Souls', "release": datetime.strptime("05, 15, 2015", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Crossroads of Chaos', "release": datetime.strptime("11, 18, 2008", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Cyberdark Impact', "release": datetime.strptime("11, 15, 2006", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Cybernetic Horizon', "release": datetime.strptime("07, 27, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Cybernetic Revolution', "release": datetime.strptime("08, 17, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Beginning 1', "release": datetime.strptime("10, 12, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Beginning 2', "release": datetime.strptime("07, 27, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Crisis', "release": datetime.strptime("12, 1, 2003", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Legends', "release": datetime.strptime("11, 21, 2008", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Revelation Volume 1', "release": datetime.strptime("03, 19, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Revelation Volume 4', "release": datetime.strptime("11, 14, 2007", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dark Saviors', "release": datetime.strptime("05, 25, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Destiny Soldiers', "release": datetime.strptime("11, 18, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dimension of Chaos', "release": datetime.strptime("11, 6, 2015", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dragons of Legend', "release": datetime.strptime("04, 25, 2014", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Dragons of Legend 2', "release": datetime.strptime("1, 1, 2012", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Duelist Alliance', "release": datetime.strptime("08, 15, 2014", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Duelist Revolution', "release": datetime.strptime("08, 17, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Duelist Saga', "release": datetime.strptime("03, 31, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Elemental Energy', "release": datetime.strptime("11, 16, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Enemy of Justice', "release": datetime.strptime("05, 17, 2006", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Exclusive Pack', "release": datetime.strptime("08, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Extreme Force', "release": datetime.strptime("02, 2, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Extreme Victory', "release": datetime.strptime("05, 10, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Flames of Destruction', "release": datetime.strptime("05, 4, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Flaming Eternity', "release": datetime.strptime("03, 1, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Force of the Breaker', "release": datetime.strptime("05, 16, 2007", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Fusion Enforcers', "release": datetime.strptime("02, 24, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Galactic Overlord', "release": datetime.strptime("05, 8, 2012", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Generation Force', "release": datetime.strptime("08, 16, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Gladiator\'s Assault', "release": datetime.strptime("11, 14, 2007", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Arsenal', "release": datetime.strptime("11, 10, 2009", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Arsenal 2', "release": datetime.strptime("07, 20, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Arsenal 3', "release": datetime.strptime("12, 7, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Arsenal 4: Trishula\'s Triumph', "release": datetime.strptime("04, 19, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Arsenal 5: Steelswarm Invasion', "release": datetime.strptime("12, 6, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Hidden Summoners', "release": datetime.strptime("11, 16, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'High-Speed Riders', "release": datetime.strptime("10, 2, 2015", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Invasion of Chaos', "release": datetime.strptime("03, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Invasion: Vengeance', "release": datetime.strptime("11, 4, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Judgment of the Light', "release": datetime.strptime("08, 9, 2013", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Labyrinth of Nightmare', "release": datetime.strptime("03, 1, 2003", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Legacy of Darkness', "release": datetime.strptime("06, 6, 2003", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Legend of Blue Eyes White Dragon', "release": datetime.strptime("12, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Legendary Duelists', "release": datetime.strptime("09, 8, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Legendary Duelists: Ancient Millennium', "release": datetime.strptime("02, 23, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Legendary Duelists: White Dragon Abyss', "release": datetime.strptime("09, 28, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Light of Destruction', "release": datetime.strptime("05, 13, 2008", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Lord of the Tachyon Galaxy', "release": datetime.strptime("05, 17, 2013", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Magician\'s Force', "release": datetime.strptime("10, 10, 2003", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Maximum Crisis', "release": datetime.strptime("05, 5, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Metal Raiders', "release": datetime.strptime("06, 26, 2002", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Movie Pack', "release": datetime.strptime("08, 13, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Number Hunters', "release": datetime.strptime("07, 12, 2013", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Order of Chaos', "release": datetime.strptime("1, 24, 2012", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Pendulum Evolution', "release": datetime.strptime("06, 23, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Phantom Darkness', "release": datetime.strptime("02, 13, 2008", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Pharaoh\'s Servant', "release": datetime.strptime("10, 20, 2002", "%m, %d, %Y"), "shortname": "TAEV"},
    {"pack": 'Pharaonic Guardian', "release": datetime.strptime("07, 18, 2003", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Photon Shockwave', "release": datetime.strptime("11, 15, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Primal Origin', "release": datetime.strptime("05, 16, 2014", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Raging Battle', "release": datetime.strptime("05, 12, 2009", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Raging Tempest', "release": datetime.strptime("02, 10, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Return of the Duelist', "release": datetime.strptime("08, 28, 2012", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Rise of Destiny', "release": datetime.strptime("12, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Samurai Assault', "release": datetime.strptime("12, 6, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Secrets of Eternity', "release": datetime.strptime("1, 16, 2015", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Shadow of Infinity', "release": datetime.strptime("02, 18, 2006", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Shadow Specters', "release": datetime.strptime("11, 8, 2013", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Shadows in Valhalla', "release": datetime.strptime("08, 17, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Shining Victories', "release": datetime.strptime("05, 6, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Soul Fusion', "release": datetime.strptime("10, 19, 2018", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Soul of the Duelist', "release": datetime.strptime("10, 1, 2004", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Spell Ruler', "release": datetime.strptime("09, 16, 2002", "%m, %d, %Y"), "shortname": "TAEV"},
    {"pack": 'Spirit Warriors', "release": datetime.strptime("11, 17, 2017", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Stardust Overdrive', "release": datetime.strptime("11, 17, 2009", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Starstrike Blast', "release": datetime.strptime("11, 16, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Storm of Ragnarok', "release": datetime.strptime("02, 8, 2011", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Strike of Neos', "release": datetime.strptime("02, 28, 2007", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Tactical Evolution', "release": datetime.strptime("08, 15, 2007", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'The Dark Illusion', "release": datetime.strptime("08, 5, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'The Duelist Genesis', "release": datetime.strptime("09, 2, 2008", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'The Lost Millennium', "release": datetime.strptime("06, 1, 2005", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'The New Challengers', "release": datetime.strptime("11, 7, 2014", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'The Shining Darkness', "release": datetime.strptime("05, 11, 2010", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'War of the Giants: Round 2', "release": datetime.strptime("1, 17, 2014", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'Wing Raiders', "release": datetime.strptime("02, 12, 2016", '%m, %d, %Y'), "shortname": "TAEV"},
    {"pack": 'World Superstars', "release": datetime.strptime("04, 17, 2015", '%m, %d, %Y'), "shortname": "TAEV"}]

# for y in packnames:
#     if y["pack"] == 'World Superstars':
#         y["shortname"] = "blah"
#         print(y)

y = ""
file = open("packAbbrv")
for line in file:
    for x in range(0, len(packnames)):
        if packnames[x]["pack"] == line.strip():
            y = line.strip()
        elif y == packnames[x]["pack"]:
            packnames[x]["shortname"] = line.strip()
            print(packnames[x])


