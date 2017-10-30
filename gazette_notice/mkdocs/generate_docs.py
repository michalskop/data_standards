# generate docs
import glob
import json

lang = 'cs'

with open("texts_" + lang + ".json") as fin:
    t = json.load(fin)


def h(n, t):
    return n * '#' + " " + t + "\n\n"


def level(obj, hlevel):
    txt = ""
    try:
        if isinstance(obj["type"], list):
            for typ in obj['type']:
                txt += "`" + typ + "`\n\n"
    except Exception:
        nothing = None
    try:
        for k in sorted(obj['properties']):
            p = obj['properties'][k]
            txt += h(hlevel + 1, k)
            txt += t['alternatives'] + ': `' + k + '`'
            try:
                for a in p['alternatives']:
                    txt += ', `' + a + '`'
            except Exception:
                nothing = None
            txt += '\n\n'
            try:
                txt += p['description@' + lang] + "\n\n"
            except Exception:
                nothing = None
            txt += t['type'] + ": "
            try:
                txt += "`" + p['type'] + "`"
            except Exception:
                nothing = None
            try:
                txt += "`" + p['$ref'] + "`"
            except Exception:
                nothing = None
            txt += '\n\n'
    except Exception:
        nothing = None
    print("returing:" + txt + "***")
    return txt


files = {}
hlevel = 1
for filename in sorted(glob.glob("../json_meta_schema/*.json")):
    page = filename.split('/')[-1].split('.')[0]
    text = ''
    print(filename, page)
    with open(filename) as fin:
        j = json.load(fin)
        text += h(hlevel + 1, j['name@' + lang] + " <small>(" + j['name@en'] + ")</small>")
        text += j['description@' + lang] + "\n\n"
        text += "**`" + page + ".json" + "`**\n"
        files[j['name@' + lang] + " (" + j['name@en'] + ')'] = page + ".md"
        try:
            dontbreakit1 = True
            dontbreakit2 = True
            off = {}
            try:
                j['oneOf']
                htext = h(hlevel + 5, t['one_of'])
                off = j['oneOf']
            except Exception:
                dontbreakit1 = False
            try:
                j['anyOf']
                htext = h(hlevel + 5, t['any_of'])
                off = j['anyOf']
            except Exception:
                dontbreakit2 = False
            print(breakit1, breakit2, off)
            if dontbreakit1 or dontbreakit2:
                newtext = ""
                for subobj in off:
                    try:
                        text += h(hlevel + 2, subobj['name@' + lang] + " <small>(" + subobj['name@en'] + ")</small>")
                    except Exception:
                        nothing = None
                    try:
                        text += subobj['description@' + lang] + "\n\n"
                    except Exception:
                        nothing = None
                    newtext += level(subobj, hlevel + 2)
                    # print('calling level')
                if newtext == '':
                    abcdef
                else:
                    text += htext
                    text += newtext
            else:
                abcdef
        except Exception:
            text += level(j, hlevel + 2)
            print('calling level XXX')
    try:
        j['example']
        text += h(hlevel + 2, t['example']) + "\n"
        text += "```json\n" + json.dumps(j['example'], ensure_ascii=False, indent="    ") + "\n```\n"
        text += '\n\n'
    except Exception:
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
