# generate json schema from meta schema
import glob

lang = "cs"
notlang = "en"

for filename in sorted(glob.glob("../json_meta_schema/*.json")):
    page = filename.split('/')[-1]
    with open(filename) as fin:
        with open("../json_schema_" + lang + "/" + page, "w") as fout:
            for row in fin:
                if "@" + notlang not in row:
                    fout.write(row.replace("@" + lang, ""))
