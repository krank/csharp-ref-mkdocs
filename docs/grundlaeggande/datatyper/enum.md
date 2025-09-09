# Enum

Enums är ett snabbt, enkelt sätt att skapa egna "datatyper".

Man skriver dem **utanför de vanliga metoderna**.

När man skapar en enum, så bestämmer man vilka värden som ska vara giltiga – ungefär som att de enda giltiga värdena för en boolean är true och false.

```csharp
Enum Room {
  entrance,
  corridor,
  dungeon
}
```

I exemplet är de enda giltiga värdena för en variabel med Rooms-datatypen entrance, corridor och dungeon.

Senare, i metoderna, kan de användas som datatyper.

Man skapar alltså variabler där man anger datatypen som enum-namnet:

```
Room currentRoom = Room.entrance;
```

Man kan också använda dem i till exempel if-satser:

```csharp
if (currentRoom == Room.corridor)
{
  // kod
}
```

Vill man skapa mer komplexa egna datatyper så är det [klasser](https://sites.google.com/view/csharp-referens/klasser-och-objektorientering?authuser=0) som gäller.
