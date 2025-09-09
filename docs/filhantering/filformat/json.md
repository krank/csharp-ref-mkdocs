# JSON

JSON är Javascript Object Notation, så för den som är van vid Javascript kanske det ser bekant ut.

## Datatyper

Det finns fem datatyper i JSON:

* **string** – "test"
* **number** – 42
* **bool** – true
* **array** – \[]
* **object** – {}

## Objekt och egenskaper

Objekt kan innehålla **egenskaper**. Varje egenskap har ett **namn** och ett **värde**. Värdet är en av de fem datatyperna. Egenskapsnamnen är **strings**. Man separerar egenskaperna från varandra med **kommatecken**, och separerar egenskapsnamn från egenskapsvärde med **kolon**.

```json
{
  "name": "Albert",
  "age": 3000
}
```

En egenskap kan ha ett objekt som värde:

```json
{
  "name": "Albert",
  "age": 3000,
  "weapon": {
    "name": "Sword",
    "damage": 300
  }
}
```

## Arrayer

En array kan innehålla flera värden. Värdena är oftast av samma datatyp, men måste inte vara det.

```
["Sword", "Shield", "Socks"]
```

```
[66, 32, "black hole", true]
```

I Javascript kommer man sedan åt varje position i arrayen genom att hänvisa till dess position, som anges som ett heltal. Den första saken i listan får nummer 0.

Skillnaden mellan en array och ett objekt är med andra ord att arrayer är [indexerade ](../../grundlaeggande/listor-och-arrayer.md#indexering)med _heltal_ – så varje sak i listan identifieras med ett nummer – medan objects är indexerade med _strings_.

## Nästling

I JSON är det vanligt att lägga objekt i andra objekt, och objekt i listor, och listor i objekt.

Exempel på objekt i en array:

```json
[
  {
    "name": "Axe",
    "damage": 20
  },
  {
    "name": "Bazooka",
    "damage": 9001
  }
]
```
