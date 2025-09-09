# Tuples

_OBS: Detta fungerar bara i lite nyare C#. Om du arbetar i Visual Studio 2017 finns risk att Tuples inte fungerar om du inte krånglar lite (det går eventuellt att lägga till stöd för tuples genom att lägga till det NuGet-paket som heter ValueTuples)_

Tuples är ett sätt att lagra flera bitar information i samma variabel.

Datatypen för variabeln anges då som en parentes, och i den parentesen skriver man datatyperna som ska ingå, i ordning.

```csharp
(int, int) coordinate = (3, 4);

(string, int) property = ("strength", 10);
```

När man gör som i exemplen ovan så får varje egenskap ett automatiskt namn, utifrån modellen item#, där # är numret i ordningen för den datan.

Så för att få ut trean ur koordinaten skulle man skriva:

```csharp
Console.WriteLine(coordinate.item1);
```

Och för att få fram värdet 10 så skulle man skriva:

```csharp
Console.WriteLine(property.item2);
```

Observera alltså att namngivningen börjar på 1 och inte 0!

## Namnge en tuples egenskaper

Man kan ge egenskaperna namn, som man då bestämmer när man skapar datatypen.

```csharp
(int x, int y) coordinates = (3, 4);
Console.WriteLine(coordinates.x);
```

## Tuples i arrayer och listor

```csharp
(int x, int y)[] coordinateArray = new (int, int)[10];
List<(int x, int y)> coordinateList = new List<(int, int)>();
```

## Tuples som returtyp

```csharp
static (int x, int y) GetCoordinates()
{
  return (5, 6)
}
```

## Tuples som parameter

```csharp
static void ReceiveCoordinate((int x, int y) coord)
{
  Console.WriteLine(coord.x);
}
```
