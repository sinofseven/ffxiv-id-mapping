SHELL = /usr/bin/env bash -xeuo pipefail

format:
	poetry run isort src main.py
	poetry run black src main.py

00-configure-max-page-number:
	poetry run python main.py configure_max_page_number

_01-scrape-eorzea-database-ja:
	poetry run python main.py scrape_eorzea_database_ja

_02-scrape-eorzea-database-de:
	poetry run python main.py scrape_eorzea_database_de

_03-scrape-eorzea-database-fr:
	poetry run python main.py scrape_eorzea_database_fr

_04-scrape-eorzea-database-en:
	poetry run python main.py scrape_eorzea_database_en

01-scrape-eorzea-database-ja: 00-configure-max-page-number _01-scrape-eorzea-database-ja

02-scrape-eorzea-database-de: 00-configure-max-page-number _02-scrape-eorzea-database-de

03-scrape-eorzea-database-fr: 00-configure-max-page-number _03-scrape-eorzea-database-fr

04-scrape-eorzea-database-en: 00-configure-max-page-number _04-scrape-eorzea-database-en

05-scrape-xivapi:
	poetry run python main.py scrape_xivapi

06-merge-eorzea-database:
	poetry run python main.py merge_eorzea_database

07-merge-xivapi:
	poetry run python main.py merge_xivapi

08-craete-mapping:
	poetry run python main.py craete_mapping

all: \
	00-configure-max-page-number \
	_01-scrape-eorzea-database-ja \
	_02-scrape-eorzea-database-de \
	_03-scrape-eorzea-database-fr \
	_04-scrape-eorzea-database-en \
	05-scrape-xivapi \
	06-merge-eorzea-database \
	07-merge-xivapi \
	08-craete-mapping

.PHONY: \
	format \
	00-configure-max-page-number \
	01-scrape-eorzea-database-ja
