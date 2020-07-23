import json
import urllib.request
from subprocess import run
from time import sleep
from typing import List, Tuple

from bs4 import BeautifulSoup as bs
from bs4.element import Tag


def get_web_document(url: str) -> str:
    headers = {
        'User-Agent': 'insomnia/2020.3.3'
    }
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req).read().decode()


def parse_id_from_path(path: str) -> str:
    index = -2 if path[-1] == "/" else -1
    return path.split("/")[index]


def parse_id_name_from_tag(tag: Tag) -> Tuple[str, str]:
    href = tag["href"]
    db_id = parse_id_from_path(href)
    return db_id, tag.string


def parse_item_data_from_html(html: str) -> dict:
    soup = bs(html, "html.parser")
    result = {}
    for tag in soup.select("a.db-table__txt--detail_link"):
        db_id, name = parse_id_name_from_tag(tag)
        result[db_id] = name
    return result


def save_max_page_number(max_page_number: int):
    json.dump(
        {"max_page_number": max_page_number},
        open(".max_page_number.json", mode="w"),
        indent=2,
        ensure_ascii=False,
    )


def load_max_page_number() -> int:
    return json.load(open(".max_page_number.json"))["max_page_number"]


def scrape_eorzea_database(is_de: bool, is_fr: bool, is_jp: bool, is_na: bool):
    if sorted([is_de, is_fr, is_jp, is_na]) != [False, False, False, True]:
        raise ValueError("Country Code must be single.")
    if is_de:
        country = "de"
        lang = "de"
    elif is_fr:
        country = "fr"
        lang = "fr"
    elif is_jp:
        country = "jp"
        lang = "ja"
    elif is_na:
        country = "na"
        lang = "en"
    else:
        raise Exception()

    directory = f"eorzea_database_{lang}"
    max_page_number = load_max_page_number()
    run(f"rm -rf {directory}; mkdir {directory}", shell=True)

    for i in range(1, max_page_number + 1):
        print(f"=== {i:05}/{max_page_number:05} ===")
        url = f"https://{country}.finalfantasyxiv.com/lodestone/playguide/db/item/?page={i}"
        html = get_web_document(url)
        data = parse_item_data_from_html(html)
        json.dump(
            data,
            open(f"{directory}/{i:05}.json", mode="w"),
            indent=2,
            ensure_ascii=False,
        )
        sleep(1.6)
