## Subjekt oznámení

*Osoby, organizace a místa, kterých se oznámení týká*

**`subjekt.jsonld`**

### fyzicka_osoba

Fyzická osoba, které se týká oznámení

**@id**: `https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/person.jsonld`

#### Příklad


###### JSON


```json
{
    "jmeno": "Tereza",
    "prijmeni": "Nováková"
}
```
###### CSV


```csv
jmeno,prijmeni

Tereza,Nováková
```
### organizace

Organizace, které se týká oznámení

**@id**: `https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/organizace.jsonld`

#### Příklad


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
### subjekt

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/subjekt.jsonld

### Kompletní příklady


#### Příklad 1


###### JSON


```json
{
    "@type": "organizace",
    "nazev": "Město Plasy",
    "ico": "00258245"
}
```


###### CSV


```csv
@type,nazev,ico

organizace,Město Plasy,00258245
```
#### Příklad 2


###### JSON


```json
{
    "@type": "fyzicka_osoba",
    "krestni_jmeno": "Tereza",
    "prijmeni": "Nováková"
}
```


###### CSV


```csv
@type,krestni_jmeno,prijmeni

fyzicka_osoba,Tereza,Nováková
```
#### Příklad 3


###### JSON


```json
{
    "jmeno": "Tereza Nováková",
    "@type": "fyzicka_osoba",
    "adresa": {
        "ulice": "Plzeňská 2",
        "lokalita": "Plasy",
        "psc": "33101"
    }
}
```


###### CSV


```csv
jmeno,@type,adresa_ulice,adresa_lokalita,adresa_psc

Tereza Nováková,fyzicka_osoba,Plzeňská 2,Plasy,33101
```
#### Příklad 4


###### JSON


```json
{
    "@type": "misto:ruian",
    "typ": "parcela",
    "kod": "1665545435"
}
```


###### CSV


```csv
@type,typ,kod

misto:ruian,parcela,1665545435
```
