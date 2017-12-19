# Oznámení na úředních deskách

**Draft 2017-12-19**

## Plný model
![plný model](./diagram_full.png)

Základ modelu je jedna zpráva na úřední desce: **[Oznámení na úřední desce](./oznameni/)**

## Submodely
Praktická implementace může použít skoro libovolný submodel z plného modelu. Povinné jsou pouze `organizace`(úřední deska) a `url`.

V případě, že implementace používá prvky z plného modelu, měly by se jmenovat tak, jak jsou popsány v modelu.

V implementaci je možné použít i další vlastní prvky, které nejsou popsány v plném modelu.

## Specifikace pomocí JSON-LD
  - [Oznámení na úřadní desce](https://github.com/michalskop/data_standards/blob/master/gazette_notice/json-ld/oznameni.jsonld)


## Specifikace pomocí XSD
TBD **

## Serializace do CSV
Při použití formátu CSV se doporučuje použít [CSV on the web](https://www.w3.org/TR/2016/NOTE-tabular-data-primer-20160225/)


## Příklady
Pozn.: více příkladů přímo u jednotlivých prvků.

**JSON**
```json
{
    "zverejneno_od": "2017-11-04",
    "url": "https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/",
    "organizace": {
        "ico": "00258245"
    },
    "zverejneno_do": "2017-11-24",
    "nazev": "Rekonstrukce betonárny Šenov"
}
```
**CSV**
```csv
zverejneno_od,url,organizace_ico,zverejneno_do,nazev
2017-11-04,https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/,00258245,2017-11-24,Rekonstrukce betonárny Šenov
```
## Odkazy
  - [Přehled některých českých implementací](https://docs.google.com/spreadsheets/d/1x2ix9qv1DiXO26lLnvM9c7w83Wg_Wpeu8BP1OsTS1Q4/edit#gid=0)
  - [Open Corporates' Gazette Notice](https://github.com/openc/openc-schema/blob/master/schemas/gazette-notice-schema.json)
  - Diagram lze editovat na [Draw.io](https://www.draw.io) s použitím [zdrojového XML](https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/gazette_notice_diagram_full.xml)
  - [Mapování na existující standardy - Open Corporates](https://docs.google.com/spreadsheets/d/16hh30KrV9m6aTY5KWlG5mFqyi07cEMXlWYcWEe8GUKk/edit#gid=0)
  - [Existující standardy](http://www.popoloproject.com/appendices/survey.html)
  - [Přehled odkazů ke standardizaci](https://docs.google.com/document/d/1lejsvjTd86urF37X6H4S1OhP3zRpjuiOkz_kLQNCsTY/edit#)
