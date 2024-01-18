import json
with open ("janv.json", "r", encoding="utf8") as maja:
    visi_dati=json.load(maja)

for i in visi_dati:
    name=i

    print(' otrā rinda:'f'{name} ')