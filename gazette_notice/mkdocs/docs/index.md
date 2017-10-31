# Oznámení na úředních deskách

**Draft 2017-10-30**

## Plný model
![plný model](./diagram_full.png)

Základ modelu je jedna zpráva na úřední desce: **[Oznámení na úřední desce](./gazette-notice-schema/)**

## Submodely
Praktická implementace může použít skoro libovolný submodel z plného modelu. Povinné jsou pouze `publisher`, `identifier` a `url` (kde `identifier` a `url` mohou být stejné, oboje `url`).

V případě, že implementace používá prvky z plného modelu, měly by se jmenovat tak, jak jsou popsány v modelu.

V implementaci je možné použít i další vlastní prvky, které nejsou popsány v plném modelu.

#### Anglické vs. české názvy
Je silně doporučeno používat anglické názvy proměnných. Specifikace v některých případech obsahuje i české alternativy z historických důvodů (např. `zverejneno_od` lze použít namísto `date_published`)

## Specifikace pomocí JSON schema
JSON schema modelu (v0.4):

  - [Interaktivní dokumentace schématu](https://michalskop.github.io/docson/#https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json_schema_cs/gazette-notice-schema.json)
  - [Popis na Github](https://github.com/michalskop/data_standards/tree/master/gazette_notice/json_schema_cs)

## Specifikace pomocí XSD
TBD **

## Serializace do CSV
Při použití formátu CSV se doporučuje použít [Tabular Data Resource](http://specs.frictionlessdata.io/table-schema/), popis takového souboru se doporučuje jako [Tabular Data Package](http://specs.frictionlessdata.io/table-schema/)

TBD **

## Příklady

TBD **

## Odkazy
  - [Přehled některých českých implementací](https://docs.google.com/spreadsheets/d/1x2ix9qv1DiXO26lLnvM9c7w83Wg_Wpeu8BP1OsTS1Q4/edit#gid=0)
  - [Open Corporates' Gazette Notice](https://github.com/openc/openc-schema/blob/master/schemas/gazette-notice-schema.json)
  - Diagram lze editovat na [Draw.io](https://www.draw.io) s použitím [zdrojového XML](https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/gazette_notice_diagram_full.xml)
  - [Mapování na existující standardy - Open Corporates](https://docs.google.com/spreadsheets/d/16hh30KrV9m6aTY5KWlG5mFqyi07cEMXlWYcWEe8GUKk/edit#gid=0)
  - [Existující standardy](http://www.popoloproject.com/appendices/survey.html)
  - [Přehled odkazů ke standardizaci](https://docs.google.com/document/d/1lejsvjTd86urF37X6H4S1OhP3zRpjuiOkz_kLQNCsTY/edit#)
