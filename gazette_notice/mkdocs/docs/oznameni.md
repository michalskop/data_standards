## Oznámení na úřední desce

*Oznámení na úřední desce*

**`oznameni.jsonld`**

### agenda

Agenda, kategorie, správní činnost, pod které spadá oznámení

**@id**: `schema:category`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"dotace"
```
###### CSV


```csv
""

dotace
```
```json
"přenesená působnost"
```
###### CSV


```csv
""

přenesená působnost
```
### anotace

Krátké shrnutí

**@id**: `schema:description`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"Vyhlášení dotačního programu Podpora obnovy a rozvoje venkova Moravskoslezského kraje 2018"
```
###### CSV


```csv
""

Vyhlášení dotačního programu Podpora obnovy a rozvoje venkova Moravskoslezského kraje 2018
```
### autor

Původní autor oznámení, fyzická nebo právnická osoba.

**@id**: `schema:creator`

**@type**: `schema:Organization`, `schema:Person`

#### Příklad


###### JSON


```json
"https://or.justice.cz/ias/ui/rejstrik-$firma?ico=22841890"
```
###### CSV


```csv
""

https://or.justice.cz/ias/ui/rejstrik-$firma?ico=22841890
```
### dokument

Další dokument/y

**@id**: `schema:DigitalDocument`

**@type**: `xsd:anyURI`

#### Příklad


###### JSON


```json
"https://www.msk.cz/eudr/Ve%C5%99ejn%C3%A9%20vyhl%C3%A1%C5%A1ky/KUMS0B3KOOGY%230/KUMS0B3KOOGY%230%23KUMS0B3KOOGY/g5269707.pdf"
```
###### CSV


```csv
""

https://www.msk.cz/eudr/Ve%C5%99ejn%C3%A9%20vyhl%C3%A1%C5%A1ky/KUMS0B3KOOGY%230/KUMS0B3KOOGY%230%23KUMS0B3KOOGY/g5269707.pdf
```
```json
"https://www.msk.cz/assets/verejna_sprava/priloha-c--1---navrh-smlouvy-o-poskytnuti-dotace-z-rozpoctu-kraje_4.pdf"
```
###### CSV


```csv
""

https://www.msk.cz/assets/verejna_sprava/priloha-c--1---navrh-smlouvy-o-poskytnuti-dotace-z-rozpoctu-kraje_4.pdf
```
### gazetteNotice

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/oznameni.jsonld

### nazev

Název oznámení

**@id**: `schema:name`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"Rekonstrukce betonárny Šenov"
```
###### CSV


```csv
""

Rekonstrukce betonárny Šenov
```
### organizace

Majitel úřední desky

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
### revize

Označení revize/verze oznámení

**@id**: `schema:version`

#### Příklad


###### JSON


```json
1
```
###### CSV


```csv
""

1
```
```json
"2017-11-07"
```
###### CSV


```csv
""

2017-11-07
```
### schvaleno

Datum vydání/schválení oznámení

**@id**: `schema:dateCreated`

**@type**: `xsd:date`

#### Příklad


###### JSON


```json
"2017-11-07"
```
###### CSV


```csv
""

2017-11-07
```
### subjekt

Osoby, organizace a místa, kterých se oznámení týká

**@id**: `https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/subjekt.jsonld`

**@type**: `schema:Thing`

#### Příklad


###### JSON


```json
{
    "ico": "22841890"
}
```
###### CSV


```csv
ico

22841890
```
```json
{
    "jmeno": "Jan Novák"
}
```
###### CSV


```csv
jmeno

Jan Novák
```
### url

URL oznámení (s lidsky čitelnou zprávou)

**@id**: `schema:url`

**@type**: `xsd:anyURI`

#### Příklad


###### JSON


```json
"https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/"
```
###### CSV


```csv
""

https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/
```
### znacka

Značka, spisová značka, číslo jednací oznámení

**@id**: `schema:productID`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"123-456"
```
###### CSV


```csv
""

123-456
```
### zverejneno_do

Datum, příp. i čas, do kdy je oznámení zveřejněno na úřední desce

**@id**: `schema:expires`

**@type**: `xsd:date`

#### Příklad


###### JSON


```json
"2017-11-24"
```
###### CSV


```csv
""

2017-11-24
```
### zverejneno_od

Datum, příp. i čas, zveřejnění oznámení na úřední desce

**@id**: `schema:datePublished`

**@type**: `xsd:date`

#### Příklad


###### JSON


```json
"2017-11-04"
```
###### CSV


```csv
""

2017-11-04
```
### Kompletní příklady


#### Příklad 1


###### JSON


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


###### CSV


```csv
zverejneno_od,url,organizace_ico,zverejneno_do,nazev

2017-11-04,https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/,00258245,2017-11-24,Rekonstrukce betonárny Šenov
```
#### Příklad 2


###### JSON


```json
{
    "revize": 2,
    "url": "https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/",
    "autor": {
        "jmeno": "Tereza Nováková",
        "@type": "https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/fyzickaOsoba.jsonld",
        "adresa": {
            "ulice": "Plzeňská 1",
            "lokalita": "Plasy",
            "psc": "33101"
        }
    },
    "anotace": "Vyhlášení dotačního programu Podpora obnovy a rozvoje venkova Moravskoslezského kraje 2018",
    "schvaleno": "2017-11-07",
    "zverejneno_od": "2017-11-04T12:12:00+01:00",
    "organizace": {
        "adresa": {
            "ulice": "Plzeňská 2",
            "lokalita": "Plasy",
            "psc": "33101"
        },
        "nazev": "Město Plasy",
        "ico": "00258245"
    },
    "znacka": "123-456",
    "agenda": [
        "dotace",
        "přenesená působnost"
    ],
    "nazev": "Dotační program venkov 2018",
    "zverejneno_do": "2017-11-24",
    "dokument": [
        "https://www.msk.cz/eudr/Ve%C5%99ejn%C3%A9%20vyhl%C3%A1%C5%A1ky/KUMS0B3KOOGY%230/KUMS0B3KOOGY%230%23KUMS0B3KOOGY/g5269707.pdf",
        "https://www.msk.cz/assets/verejna_sprava/priloha-c--1---navrh-smlouvy-o-poskytnuti-dotace-z-rozpoctu-kraje_4.pdf"
    ],
    "subjekt": {
        "jmeno": "Moravskoslezský kraj",
        "@type": "organizace"
    }
}
```


###### CSV


```csv
revize,url,autor_jmeno,autor_@type,autor_adresa_ulice,autor_adresa_lokalita,autor_adresa_psc,anotace,schvaleno,zverejneno_od,organizace_adresa_ulice,organizace_adresa_lokalita,organizace_adresa_psc,organizace_nazev,organizace_ico,znacka,agenda_1,agenda_2,nazev,zverejneno_do,dokument_1,dokument_2,subjekt_jmeno,subjekt_@type

2,https://www.msk.cz/cz/verejna_sprava/dotacni-program-podpora-podnikani-v-moravskoslezskem-kraji-2017-92988/,Tereza Nováková,https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/fyzickaOsoba.jsonld,Plzeňská 1,Plasy,33101,Vyhlášení dotačního programu Podpora obnovy a rozvoje venkova Moravskoslezského kraje 2018,2017-11-07,2017-11-04T12:12:00+01:00,Plzeňská 2,Plasy,33101,Město Plasy,00258245,123-456,dotace,přenesená působnost,Dotační program venkov 2018,2017-11-24,https://www.msk.cz/eudr/Ve%C5%99ejn%C3%A9%20vyhl%C3%A1%C5%A1ky/KUMS0B3KOOGY%230/KUMS0B3KOOGY%230%23KUMS0B3KOOGY/g5269707.pdf,https://www.msk.cz/assets/verejna_sprava/priloha-c--1---navrh-smlouvy-o-poskytnuti-dotace-z-rozpoctu-kraje_4.pdf,Moravskoslezský kraj,organizace
```
