import os
import json


def main():
    data = {}
    base_dir_name = 'eorzea_database'
    target_langs = ["de", "en", "fr", "ja"]

    ls = os.listdir('.')
    for lang in target_langs:
        if f'{base_dir_name}_{lang}' not in ls:
            raise Exception(f'No Exists {base_dir_name}_{lang}')

    for lang in target_langs:
        target_dir = f"{base_dir_name}_{lang}"
        for name in os.listdir(target_dir):
            file = json.load(open(f'{target_dir}/{name}'))
            for k, v in file.items():
                node = data.get(k, {'ID': k})
                node[f'Name_{lang}'] = v
                data[k] = node

    json.dump(list(data.values()), open('all_eorzea_database.json', mode='w'), indent=2, ensure_ascii=False)
