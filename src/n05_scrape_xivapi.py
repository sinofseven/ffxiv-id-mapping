from .utils import get_web_document
from urllib.parse import quote
import json
from subprocess import run
from time import sleep


def main():
    max_page = 1
    page = 1
    directory = 'xivapi'
    run(f'rm -rf {directory}; mkdir {directory}', shell=True)
    while page <= max_page:
        if page != 1:
            sleep(1)
        print(f'=== {page:05}/{max_page:05} ===')
        data = get_xivapi_data(page)
        if page == 1:
            max_page = data['Pagination']['PageTotal']
        json.dump(data, open(f'{directory}/{page:05}.json', mode='w'), indent=2, ensure_ascii=False)
        page += 1


def get_xivapi_data(page: int) -> dict:
    option = {
        'indexes': 'item',
        'limit': 250,
        'columns': 'ID,Name_de,Name_en,Name_fr,Name_ja,ItemSearchCategory.Name,ItemSearchCategory.ID',
        'filters': 'ItemSearchCategory.ID>=1',
        'page': page
    }
    query = '&'.join([
        f'{k}={quote(str(v))}'
        for k, v in option.items()
    ])
    url = f'https://xivapi.com/search?{query}'
    body = get_web_document(url)
    return json.loads(body)
