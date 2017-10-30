# generate docs
import glob
import json

lang = 'cs'

with open("texts_" + lang + ".json") as fin:
    t = json.load(fin)


def h(n, t):
    return n * '#' + " " + t + "\n\n"


files = {}
for filename in sorted(glob.glob("../json_meta_schema/*.json")):
    page = filename.split('/')[-1].split('.')[0]
    text = ''
    print(filename, page)
    with open(filename) as fin:
        j = json.load(fin)
        text += h(2, j['name@' + lang])
        text += j['description@' + lang] + "\n\n"
        files[j['name@' + lang]] = page + ".md"
        try:
            for k in sorted(j['properties']):
                p = j['properties'][k]
                text += h(3, k)
                text += t['alternatives'] + ': `' + k + '`'
                try:
                    for a in p['alternatives']:
                        text += ', `' + a + '`'
                except Exception:
                    nothing = None
                text += '\n\n'
                try:
                    text += p['description@' + lang] + "\n\n"
                except Exception:
                    nothing = None
                text += t['type'] + ": "
                try:
                    text += "`" + p['type'] + "`"
                except Exception:
                    nothing = None
                try:
                    text += "`" + p['$ref'] + "`"
                except Exception:
                    nothing = None
                text += '\n\n'
        except Exception:
            nothing = None


    with open("docs/" + page + ".md", "w") as fout:
        fout.write(text)

yml = 'site_name: ' + t['site_name'] + "\n"
yml += 'pages:\n'
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
