## Organizace

*Organizace, např. majitel úřední desky*

**`organizace.jsonld`**

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
### ico

IČO organizace, např. majitele úřední desky

**@id**: `schema:identifier`

**@type**: `xsd:string`

**law**: `https://www.zakonyprolidi.cz/cs/2009-111#p26-2-d`

#### Příklad


###### JSON


```json
"00258245"
```
###### CSV


```csv
""

00258245
```
### nazev

Organizace, např. majitel úřední desky

**@id**: `schema:legalName`

**@type**: `xsd:string`

**law**: `https://www.zakonyprolidi.cz/cs/2009-111#p26-2-a`

#### Příklad


###### JSON


```json
"Město Plasy"
```
###### CSV


```csv
""

Město Plasy
```
### organizace

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/organizace.jsonld

### Kompletní příklady


#### Příklad 1


###### JSON


```json
{
    "nazev": "Město Plasy",
    "ico": "00258245"
}
```


###### CSV


```csv
nazev,ico

Město Plasy,00258245
```
#### Příklad 2


###### JSON


```json
{
    "ico": "00258245"
}
```


###### CSV


```csv
ico

00258245
```
#### Příklad 3


###### JSON


```json
{
    "adresa": {
        "ulice": "Plzeňská 2",
        "lokalita": "Plasy",
        "psc": "33101"
    },
    "nazev": "Město Plasy",
    "ico": "00258245"
}
```


###### CSV


```csv
adresa_ulice,adresa_lokalita,adresa_psc,nazev,ico

Plzeňská 2,Plasy,33101,Město Plasy,00258245
```
