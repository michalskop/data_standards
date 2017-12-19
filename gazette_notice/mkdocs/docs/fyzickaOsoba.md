## Fyzická osoba

*Fyzická osoba - člověk*

**`fyzickaOsoba.jsonld`**

### adresa

Adresa

**@id**: `https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/misto.jsonld`

#### Příklad


###### JSON


```json
"Plzeňská 2, Plasy, 33101"
```
###### CSV


```csv
""

"Plzeňská 2, Plasy, 33101"
```
```json
{
    "ulice": "Plzeňská 2",
    "lokalita": "Plasy",
    "psc": "33101"
}
```
###### CSV


```csv
ulice,lokalita,psc

Plzeňská 2,Plasy,33101
```
### fyzickaOsoba

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/fyzickaOsoba.jsonld

### krestni_jmeno

Křestní jméno

**@id**: `schema:givenName`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"Tereza"
```
###### CSV


```csv
""

Tereza
```
### name

Jméno

**@id**: `schema:name`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"Tereze Nováková"
```
###### CSV


```csv
""

Tereze Nováková
```
### prijmeni

Příjmení

**@id**: `schema:familyName`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"Nováková"
```
###### CSV


```csv
""

Nováková
```
### Kompletní příklady


#### Příklad 1


###### JSON


```json
{
    "jmeno": "Tereza Nováková",
    "adresa": {
        "ulice": "Plzeňská 2",
        "lokalita": "Plasy",
        "psc": "33101"
    }
}
```


###### CSV


```csv
jmeno,adresa_ulice,adresa_lokalita,adresa_psc

Tereza Nováková,Plzeňská 2,Plasy,33101
```
#### Příklad 2


###### JSON


```json
{
    "krestni_jmeno": "Tereza",
    "prijmeni": "Nováková"
}
```


###### CSV


```csv
krestni_jmeno,prijmeni

Tereza,Nováková
```
