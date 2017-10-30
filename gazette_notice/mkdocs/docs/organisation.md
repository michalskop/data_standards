## Organizace <small>(Company)</small>

Organizace (právnická osoba)

**`organisation.json`**
#### identifiers

Alternativy: `identifiers`, `idenfitikatory`

Identifikátory, např. IČ

Typ: `array`

#### name

Alternativy: `name`, `jmeno`

Jméno organizace (právnické osoby)

Typ: `string`

#### registered_address

Alternativy: `registered_address`, `adresa`

Adresa organizace (právnické osoby)

Typ: `place.json`

### Příklad


```json
{
    "identifiers": [
        {
            "identifier": "00258245",
            "scheme": "IČ"
        }
    ],
    "name": "Město Plasy"
}
```


