# scraper all agendas from https://rpp-ais.egon.gov.cz/gen/agendy-detail/

import copy
import csv
import openpyxl


def create_link_zpl(item):
    t = "https://www.zakonyprolidi.cz/cs/" + str(item['bill_year']) + "-" + str(item['bill_number'])
    if item['bill_section'] is not None:
        t += '#p' + item['bill_section']
    if item['bill_subsection'] is not None:
        t += '-' + item['bill_subsection']
    if item['bill_paragraph'] is not None:
        t += '-' + item['bill_paragraph']
    return t


items = []
current_files = []
files_object = {}
with open("files.csv") as fin:
    dr = csv.DictReader(fin)
    for row in dr:
        try:
            files_object[row['code']]
        except Exception:
            files_object[row['code']] = []
        files_object[row['code']].append(row)

for k in files_object:
    files_object[k].sort(key=lambda Item: Item['date'], reverse=True)

for code in sorted(files_object):
    # code = 'A1281'
    print(code)
    row = files_object[code][0]
    wb = openpyxl.load_workbook('xlsx/' + row['file'])
    sheet = wb['ÚDAJE']
    # if code not in ['A1281', 'A1046', 'A1133', 'A117', ''A1183', 'A124', 'A1361', 'A4080', 'A951']:
    try:
        if sheet[4][2].value is not None:
            for i in range(9, 100):
                if sheet[i][1].value == 'Kód údaje':
                    if sheet[i + 1][1].value is None:
                        i += 2
                    else:
                        i += 1
                    break

            # head = {
            #     "bject_code": sheet[4][0].value,
            #     "bject_name": sheet[4][2].value,
            #     "bject_description": sheet[4][4].value,
            #     "bject_bill_number": int(sheet[7][2].value),
            #     'bject_bill_year': int(sheet[7][3].value),
            #     'bject_bill_name': sheet[7][4].value,
            #     'bject_bill_section': sheet[7][5].value,
            #     'bject_bill_subsection': sheet[7][6].value,
            #     'bject_bill_paragraph': sheet[7][7].value
            # }
            head = {}
            nextt = True
            # i = 10
            while nextt:
                # print(i)
                item = head
                item['code'] = sheet[i][1].value
                item['name'] = sheet[i][2].value
                item['description'] = sheet[i][4].value
                item['type'] = sheet[i][6].value
                another = True
                while another:
                    item['bill_number'] = int(sheet[i + 3][2].value)
                    item['bill_year'] = int(sheet[i + 3][3].value)
                    item['bill_name'] = sheet[i + 3][4].value
                    item['bill_section'] = sheet[i + 3][5].value
                    item['bill_subsection'] = sheet[i + 3][6].value
                    item['bill_paragraph'] = sheet[i + 3][7].value
                    item['direct_link'] = create_link_zpl(item)
                    items.append(copy.deepcopy(item))
                    try:
                        int(sheet[i + 3 + 1][2].value)
                        i += 1
                    except Exception:
                        another = False
                if sheet[i + 4][1].value is None:
                    nextt = False
                else:
                    i += 4
            # break
    except Exception:
        print("error:", code)
        break

with open("terms_current.csv", "w") as fout:
    # header = ["bject_code", "bject_name", "bject_description", "bject_bill_name", "bject_bill_number", "bject_bill_year", "bject_bill_section", "bject_bill_subsection", "bject_bill_paragraph", "code", "name", "description", "type", "bill_name", "bill_number", "bill_year", "bill_section", "bill_subsection", "bill_paragraph"]
    header = ["code", "name", "description", "type", "bill_name", "bill_number", "bill_year", "bill_section", "bill_subsection", "bill_paragraph", "link"]
    dw = csv.DictWriter(fout, header)
    dw.writeheader()
    for item in items:
        dw.writerow(item)
