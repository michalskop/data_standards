## Místo dle RÚIAN

*Identifikace místa dle RÚIAN*

**`ruian.jsonld`**

### gazette

https://raw.githubusercontent.com/michalskop/data_standards/master/gazette_notice/json-ld/ruian.jsonld

### kod

Identifikátor místa dle RÚIAN

**@id**: `schema:identifier`

**@type**: `xsd:integer`

#### Příklad


###### JSON


```json
"690775"
```
###### CSV


```csv
""

690775
```
### typ

Typ místa dle RÚIAN

**@id**: `schema:category`

**@type**: `xsd:string`

#### Příklad


###### JSON


```json
"budova"
```
###### CSV


```csv
""

budova
```
```json
"parcela"
```
###### CSV


```csv
""

parcela
```
### Kompletní příklady


#### Příklad 1


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
#### Příklad 2


###### JSON


```json
{
    "typ": "parcela",
    "kod": "1665545435"
}
```


###### CSV


```csv
typ,kod

parcela,1665545435
```
