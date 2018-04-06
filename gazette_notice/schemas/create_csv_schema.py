import csv
import copy
import json

path = "/home/michal/project/data_standards/gazette_notice/schemas/"

with open(path + "uredni-deska-20180406.json") as fin:
    schema = json.load(fin)


def prepare(obj, arr):
    out = []
    for k in obj["properties"]:
        marr = copy.deepcopy(arr)
        # print(k)
        if k == 'adresa':
            obj['properties'][k] = schema['definitions']['adresa']
        marr.append(k)
        # print(marr)
        try:
            # print('ww', obj['properties'][k]['items'])
            out = out + prepare(obj['properties'][k]['items'], marr)
            # print('**', out)
        except Exception:
            try:
                # print('pp', obj['properties'][k])
                out = out + prepare(obj['properties'][k], marr)
                # print('**', out)
            except Exception:
                # print(obj['properties'][k])
                try:
                    example = obj['properties'][k]['examples'][0]
                except Exception:
                    # print(obj['properties'][k])
                    example = obj['properties'][k]['items']['examples'][0]
                item = ['_'.join(marr), obj['properties'][k]['type'], obj['properties'][k]['description'], example]
                out.append(item)
                marr = arr
    # print('xxx', out)
    return out


prepared = prepare(schema['items'], [])

with open(path + "description.csv", "w") as fout:
    csvw = csv.writer(fout)
    for row in prepared:
        csvw.writerow(row)

csvschema = {'fields': []}
with open(path + "description_full.csv") as fin:
    dr = csv.DictReader(fin)
    for row in dr:
        csvschema['fields'].append({
            "name": row['nazev_atributu'],
            "title": row['nazev_atributu'],
            "type": row['datovy_typ'],
            "description": row['popis']
        })
with open(path + "csv-schema.json", "w") as fout:
    json.dump(csvschema, fout, ensure_ascii=False, indent=4)
