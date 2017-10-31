# Oznámení na úředních deskách

**Draft 2017-10-30**

## Plný model
![plný model](./diagram_full.png)
Základ modelu je jedna zpráva na úřední desce `gazette-notice-schema`.

## Submodely
Praktická implementace může použít skoro libovolný submodel z plného modelu. Povinné jsou pouze `publisher`, `identifier` a `url` (kde `identifier` a `url` mohou být stejné, oboje `url`).

Ovšem v případě, že implementace používá prvky z plného modelu, měly by se jmenovat tak, jak jsou popsány v modelu.

V implementaci je možné použít i další vlastní prvky, které nejsou popsány v plném modelu.

#### Anglické vs. české názvy
Je silně doporučeno používat anglické názvy proměnných. Specifikace v některých případech obsahuje i české alternativy z historických důvodů (např. `zverejneno_od` namísto `date_published`)

## Specifikace pomocí JSON schema
JSON schema modelu:

## Specifikace pomocí XSD
TBD **

## Serializace do CSV
Při použití formátu CSV se doporučuje použít [Tabular Data Resource](http://specs.frictionlessdata.io/table-schema/), popis takového souboru se doporučuje jako [Tabular Data Package](http://specs.frictionlessdata.io/table-schema/)

TBD **
