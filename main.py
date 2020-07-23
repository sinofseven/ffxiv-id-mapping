import sys

from src.n00_configure_max_page_number import main as configure_max_page_number
from src.n01_scrape_eorzea_database_ja import main as scrape_eorzea_database_ja
from src.n02_scrape_eorzea_database_de import main as scrape_eorzea_database_de
from src.n03_scrape_eorzea_database_fr import main as scrape_eorzea_database_fr
from src.n04_scrape_eorzea_database_en import main as scrape_eorzea_database_en
from src.n05_scrape_xivapi import main as scrape_xivapi
from src.n06_merge_eorzea_database import main as merge_eorzea_database
from src.n07_merge_xivapi import main as merge_xivapi
from src.n08_create_mapping import main as craete_mapping

funcs = {
    "configure_max_page_number": configure_max_page_number,
    "scrape_eorzea_database_ja": scrape_eorzea_database_ja,
    "scrape_eorzea_database_de": scrape_eorzea_database_de,
    "scrape_eorzea_database_fr": scrape_eorzea_database_fr,
    "scrape_eorzea_database_en": scrape_eorzea_database_en,
    "scrape_xivapi": scrape_xivapi,
    "merge_eorzea_database": merge_eorzea_database,
    "merge_xivapi": merge_xivapi,
    "craete_mapping": craete_mapping
}

if __name__ == "__main__":
    funcs[sys.argv[1]]()
