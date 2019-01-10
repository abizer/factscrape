#!/usr/bin/env python3

import sys
import os
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
import json
from pathlib import Path
from slugify import slugify

def coerce_open(path):
    g = path.open('rb').read()
    return g.decode('ascii', 'ignore')


def mangle(text):
    return text.strip().encode('ascii', 'ignore')


def extract_field_name(bsobj):
    """Extract field name from beautifulsoup object."""
    return mangle(bsobj.find(class_='fieldHeading').findChildren('th')[1].get_text())


def extract_country_list(bsobj):
    return bsobj.find_all(class_='country')


def extract_statistics(bsobj):
    """Extract country name and value of the statistic."""

    country = bsobj.get_text()
    statistic = bsobj.next_sibling.get_text()

    return mangle(country), mangle(statistic)


def parse_field_file(field_bs):

    field_data = {}

    field_name = extract_field_name(field_bs).decode('ascii')
    country_list = extract_country_list(field_bs)

    for country_bs in country_list:
        country, statistic = extract_statistics(country_bs)
        field_data[country.decode('ascii')] = statistic.decode('ascii')

    return field_name, field_data


def main():
    field_source = Path('fields')
    
    by_country = defaultdict(dict)
    by_field = {}

    for path in field_source.glob('print_*.html'):
        bs = BeautifulSoup(coerce_open(path), features='lxml')
        
        field_name, field_data = parse_field_file(bs)

        if field_name == '':
            print(path, "has an invalid or empty field name")

        by_field[field_name.lower()] = field_data

        for country, statistic in field_data.items():
            by_country[country][field_name.lower()] = statistic

            
    for field in by_field:
        with open('by-statistic/' + slugify(field) + '.json', 'w') as o:
            print('writing file for', field)
            o.write(json.dumps(by_field[field], indent=2))

    for country in by_country:
        with open('by-country/' + slugify(country) + '.json', 'w') as o:
            print('writing file for', country)
            o.write(json.dumps(by_country[country], indent=2))
        
        
if __name__ == '__main__':
    main()
