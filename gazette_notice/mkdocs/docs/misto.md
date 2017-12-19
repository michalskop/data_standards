## Místo

*Definované místo*

**`misto.jsonld`**

### adresa

Adresa (jako text)

**@id**: `schema:Text`

**@type**: `xsd:string`

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
### misto

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/adresa.jsonld

### postovni_adresa

Poštovní adresa

**@id**: `schema:PostalAddress`

#### Příklad


###### JSON


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
### ruian

Klasifikace dle RÚIAN

**@id**: `https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/ruian.jsonld`

#### Příklad


###### JSON


```json
{
    "typ": "budova",
    "kod": "690775"
}
```
###### CSV


```csv
typ,kod

budova,690775
```
### Kompletní příklady


#### Příklad 1


###### JSON


```json
{
    "ulice": "Plzeňská 2",
    "@type": "postovni_adresa",
    "psc": "33101",
    "lokalita": "Plasy"
}
```


###### CSV


```csv
ulice,@type,psc,lokalita

Plzeňská 2,postovni_adresa,33101,Plasy
```
#### Příklad 2


###### JSON


```json
{
    "@type": "adresa",
    "adresa": "Plzeňská 2, Plasy, 33101"
}
```


###### CSV


```csv
@type,adresa

adresa,"Plzeňská 2, Plasy, 33101"
```
#### Příklad 3


###### JSON


```json
{
    "@type": "ruian",
    "typ": "budova",
    "kod": "690775"
}
```


###### CSV


```csv
@type,typ,kod

ruian,budova,690775
```
