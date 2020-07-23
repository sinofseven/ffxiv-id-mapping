import json


def main():
    eorzea_database = json.load(open('all_eorzea_database.json'))
    xivapi = json.load(open("all_xivapi.json"))
    mapping = {}
    illegal = []

    for item in xivapi:
        parsed = [
            x
            for x in eorzea_database
            if x["Name_de"] == item["Name_de"] \
               or x["Name_en"] == item["Name_en"] \
               or x["Name_fr"] == item["Name_fr"] \
               or x["Name_ja"] == item["Name_ja"]
        ]

        if len(parsed) == 1:
            mapping[str(item["ID"])] = parsed[0]["ID"]
        else:
            illegal.append(item)

    json.dump(mapping, open("raw_mapping.json", mode="w"), indent=2, ensure_ascii=False)
    json.dump(illegal, open("raw_illegal.json", mode="w"), indent=2, ensure_ascii=False)
    print(json.dumps({
        "mapping": len(mapping),
        "illegal": len(illegal)
    }, indent=2, ensure_ascii=False))
