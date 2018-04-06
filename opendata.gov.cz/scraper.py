# scraper for datasets and attributes from opendata.gov.cz

import csv
import json
from lxml import html
import requests

path = "/home/michal/project/data_standards/opendata.gov.cz/"

urls = ['https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-ministerstva', 'https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-centralni-organy', 'https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-kraje', 'https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-obce-s-rozsirenou-pusobnosti', 'https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-obce-ostatni']

# urls = ['https://opendata.gov.cz/vzor:vzorovy-publikacni-plan-ministerstva']

data = []
for url0 in urls:
    print(url0)
    r = requests.get(url0)
    root0 = html.fromstring(r.text)
    table = root0.xpath('//table')[0]
    trs = table.xpath('.//tr')
    i = 0
    for tr in trs:
        if i > 0:
            dataset = {
                'plan': url0,
                'dataset_name': tr.xpath('.//a')[0].text,
                'dataset_link': tr.xpath('.//a/@href')[0]
            }
            url = 'https://opendata.gov.cz' + dataset['dataset_link']
            print(url)
            r1 = requests.get(url)
            root = html.fromstring(r1.text)
            json_link = root.xpath('//a[@class="media mediafile mf_json"]/@href')[0]
            json_url = 'https://opendata.gov.cz' + json_link
            r2 = requests.get(json_url)
            try:
                json_schema = r2.json()
                # print(json_schema)
                for row in json_schema['fields']:
                    item = {**row, **dataset}
                    data.append(item)
                # print(json_schema)
            except Exception:
                print("error: " + json_url)
        i += 1
    # print(data)
with open(path + "attributes.csv", "w") as fout:
    header = ['name', 'title', 'type', 'description', 'plan', 'dataset_name', 'dataset_link']
    dw = csv.DictWriter(fout, header)
    dw.writeheader()
    for row in data:
        dw.writerow(row)
