# download all agendas from https://rpp-ais.egon.gov.cz/gen/agendy-detail/

import csv
from lxml import html
import requests

files = []
url = "https://rpp-ais.egon.gov.cz/gen/agendy-detail/"
r = requests.get(url, verify=False)
r.encoding = 'utf-8'
root = html.fromstring(r.text)
trs = root.xpath('//tr')
trs.pop(0)
for tr in trs:
    tds = tr.xpath('td')
    ds = tds[2].text.split('.')
    item = {
        "code": tds[0].xpath('a')[0].text,
        "file": tds[0].xpath('a/@href')[0],
        "name": tds[1].xpath('a')[0].text,
        "date": '-'.join([ds[2], ds[1], ds[0]])
    }
    files.append(item)

with open("files.csv", "w") as fout:
    header = ["code", "name", "date", "file"]
    dw = csv.DictWriter(fout, header)
    dw.writeheader()
    for row in files:
        dw.writerow(row)

for row in files:
    url = "https://rpp-ais.egon.gov.cz/gen/agendy-detail/" + row['file']
    r = requests.get(url, verify=False)
    with open("xlsx/" + row['file'], "wb") as fout:
        fout.write(r.content)
        print(row['code'])
