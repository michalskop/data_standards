# generate docs
import csv
import glob
import json
import io

lang = 'cs'


# https://stackoverflow.com/questions/9157314/how-do-i-write-data-into-csv-format-as-string-not-file
def csv2string(data):
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(data)
    return si.getvalue().strip('\r\n')


with open("texts_" + lang + ".json") as fin:
    t = json.load(fin)


def h(t, n):
    return n * '#' + " " + t + "\n\n"


def csvize(res, obj, prefix):
    # print(res, obj)
    if isinstance(obj, dict) or isinstance(obj, list):
        if isinstance(obj, dict):
            for k in obj:
                if prefix != '':
                    nprefix = prefix + "_" + k
                else:
                    nprefix = k
                lev = csvize(res, obj[k], nprefix)
                res['header'] = lev['header']
                res['value'] = lev['value']
        else:
            i = 1
            for o in obj:
                lev = csvize(res, o, prefix + "_" + str(i))
                res['header'] = lev['header']
                res['value'] = lev['value']
                i += 1
    else:
        res['header'].append(prefix)
        res['value'].append(obj)
    return res


exclude_keys = [
    "name@" + lang,
    "description@" + lang,
    "example@" + lang,
    "@language",
    "xsd",
    "schema"
]

files = {}
for filename in sorted(glob.glob("../json-ld-meta/*.jsonld")):
    page = filename.split('/')[-1].split('.')[0]
    text = ''
    # print(filename, page)
    with open(filename) as fin:
        js = json.load(fin)
        j = js['@context']
        text += h(j['name@' + lang], 2)
        text += "*" + j['description@' + lang] + "*\n\n"
        text += "**`" + page + ".jsonld" + "`**\n\n"
        files[j['name@' + lang]] = page + ".md"
        # print(page)

    # attributes
    for key in sorted(j):
        if key not in exclude_keys:
            text += h(key, 3)
            # print(key)
            # text += j[key]['description@' + lang] + "\n\n"
            if isinstance(j[key], dict):
                text += j[key]['description@' + lang] + "\n\n"
                for subkey in j[key]:
                    if subkey not in exclude_keys:
                        try:
                            text += "**" + subkey + "**: `" + j[key][subkey] + "`\n\n"
                        except Exception:   # list
                            text += "**" + subkey + "**: `" + "`, `".join(j[key][subkey]) + "`\n\n"

                if isinstance(j[key]['example@' + lang], list):
                    text += h(t['example'], 4) + "\n"
                    text += h("JSON", 6) + "\n"
                    for example in j[key]['example@' + lang]:
                        text += "```json\n" + json.dumps(example, ensure_ascii=False, indent="    ") + "\n```\n"
                        res = {
                            'header': [],
                            'value': []
                        }
                        csvized = csvize(res, example, '')
                        text += h("CSV", 6) + "\n"
                        text += "```csv\n" + csv2string(csvized['header']) + "\n"
                        text += "\n" + csv2string(csvized['value']) + "\n```\n"
                else:
                    text += h(t['example'], 4) + "\n"
                    text += h("JSON", 6) + "\n"
                    text += "```json\n" + json.dumps(j[key]['example@' + lang], ensure_ascii=False, indent="    ") + "\n```\n"
                    res = {
                        'header': [],
                        'value': []
                    }
                    csvized = csvize(res, j[key]['example@' + lang], '')
                    text += h("CSV", 6) + "\n"
                    text += "```csv\n" + csv2string(csvized['header']) + "\n"
                    text += "\n" + csv2string(csvized['value']) + "\n```\n"
            else:
                text += j[key] + "\n\n"

    # examples
    try:
        j['example@' + lang]
        k = 1
        text += h(t['complete_examples'], 3) + "\n"
        for example in j['example@' + lang]:
            text += h(t['example'] + " " + str(k), 4) + "\n"
            text += h("JSON", 6) + "\n"
            text += "```json\n" + json.dumps(example, ensure_ascii=False, indent="    ") + "\n```\n"
            text += '\n\n'
            k += 1
            res = {
                'header': [],
                'value': []
            }
            # print(example)
            csvized = csvize(res, example, '')
            text += h("CSV", 6) + "\n"
            text += "```csv\n" + csv2string(csvized['header']) + "\n"
            text += "\n" + csv2string(csvized['value']) + "\n```\n"
            # break
    except Exception as e:
        print(e)
        nothing = None

    with open("docs/" + page + ".md", "w") as fout:
        fout.write(text)
    # break

# YAML manually
yml = 'site_name: ' + t['site_name'] + "\n"
yml += 'pages:\n'
yml += '    - Obsah: index.md\n'
for k in sorted(files):
    yml += '    - ' + k + ': ' + files[k] + "\n"
yml += "theme: readthedocs"

# main = {
#     "site_name": t['site_name'],
#     "pages": files,
#     "theme": "readthedocs"
# }
with open("mkdocs.yml", "w") as fout:
    fout.write(yml)
    # fout.write(yaml.dump(main))
