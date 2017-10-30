## Identifikátor <small>(Identifier)</small>

Identifikátor, např. IČ, číslo dle RÚIAN. Identifikátor by měl být řádně definován, např. vydán veřejnou institucí.

**`identifier.json`**
#### identifier

Alternativy: `identifier`

Unikátní identifikátor vydaný - měl by být unikátní v rámci systému (např. IĆ, RÚIAN/budovy, apod.)

Typ: `string`

#### scheme

Alternativy: `scheme`

Schéma, v kterém je daný identifikátor. Např. 'IĆ', 'RÚIAN/budovy', apod.

Typ: `string`

### Příklad


```json
{
    "identifier": "00258245",
    "scheme": "IČ"
}
```


