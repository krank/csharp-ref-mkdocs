# Linq-queries

Linq queries är databasfrågor som fungerar likadant oavsett om man kör dem mot en databas eller vilken [samling ](../../klasser-och-objektorientering/generiska-klasser.md#samlingar)som helst.

```csharp
List<Character> characters = new()
{
  new Character() {Name="Linda"},
  new Character() {Name="Micke"},
  new Character() {Name="Mira"},
  new Character() {Name="Pontus"},
  new Character() {Name="George"},
};

var shortNames =
            from c in characters
            where c.Name.Length < 6
            orderby c.Name
            select c;
            // Samlingen shortNames innehåller karaktärerna Micke, Mira och Linda,
            // sorterade i bokstavsordning efter namn.
```

Det finns en hel del man kan göra med Linq, men oftast klarar man sig med **from**, **in**, **where**, **orderby** och **select**.

## From…in

From och in anger tillsammans _varifrån_ datan ska hämtas, och vilken variabel varje rad tillfälligt ska lagras i. Först skrivs from, därefter namnet på en variabel (som inte behlver skapas innan eller ger datatyp), därefter in och slutligen datakällan.

```csharp
var shortNames = from c in characters
            select c;
```

## Where

Where anger ett villkor som fungerar som ett filter – bara de föremål i samlingen (eller rader i tabellen) som matchar kriteriet får vara med i resultatet.

```csharp
var user = from c in characters
           where c.Name == "Micke" && c.Password == "12345"
           select c;
```

## Orderby

Orderby avgör hur resultaten _sorteras_.

```csharp
var shortNames =
            from c in characters
            where c.Name.Length < 6
            orderby c.Age
            select c;
            // Samlingen shortNames innehåller karaktärerna Micke, Mira och Linda,
            // sorterade efter ålder.
```

## Select

Select avgör _vad som läggs in_ i resultatsamlingen.

```csharp
var shortNames =
            from c in characters
            where c.Name.Length < 6
            orderby c.Name
            select c.Name;
            // shortNames blir en string-samling med karaktärernas namn
```
