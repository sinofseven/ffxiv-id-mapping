import json
import os


def main():
    data = []
    target = "xivapi"
    for name in os.listdir(target):
        file = json.load(open(f'{target}/{name}'))
        data += file['Results']

    json.dump(data, open('all_xivapi.json', mode='w'), indent=2, ensure_ascii=False)
