# Konsolen (Console)

## Skriva ut och läsa in text

### Console.WriteLine()

Skriver ut något till konsolen, med en radbrytning i slutet.

```csharp
Console.WriteLine("Hello!");
```

### Console.Write()

Skriver ut något till konsolen, utan radbrytning efteråt.

```csharp
Console.Write("Hello");
Console.Write("World");
```

### Console.Clear()

Rensar skärmen.

```csharp
Console.Clear();
```

### Console.ReadLine()

Läser in en string från användaren och väntar på Enter-tryckning. Returnerar stringen så att den kan lagras i en variabel eller användas i koden.

```csharp
string answer = Console.ReadLine();
```

### Console.ReadKey()

Läser in ett knapptryck från användaren. Pausar körningen av programmet tills en knapptryckning sker.

```csharp
ConsoleKey key = Console.ReadKey();
```

### Console.KeyAvailable

Kollar om en knapptryckning skett sedan förra gången ReadLine eller ReadKey kördes. Praktisk för när man t.ex. inte vill att körningen av programmet ska pausas när man kör en ReadKey().

```csharp
if (Console.KeyAvailable)
{
  ConsoleKey key = Console.ReadKey();
}
```

### Console.OutputEncoding

Ändrar vilken teckenkodning som ska användas när saker skrivs ut till konsolen.

```csharp
Console.OutputEncoding = System.Text.Encoding.UTF8;
```

Med UTF-8 som teckenkodning kan man använda fler tecken – till exempel emojis som 🤖.

```csharp
Console.WriteLine("🤖");
```

## Färg

### Console.ForegroundColor

Variabel vars värde avgör färgen på texten i konsolfönstret.

```csharp
Console.ForegroundColor = ConsoleColor.Cyan;
```

!!! warning

	**OBSERVERA:** detta gäller enbart text som skrivs _efter_ det att färgen ändrats. Text som redan skrivits ut förändras inte.
	

### Console.BackgroundColor

Variabel vars värde avgör färgen på texten i konsolfönstret.

```csharp
Console.BackgroundColor = ConsoleColor.Magenta;
```

!!! warning

	**OBSERVERA:** detta gäller enbart text som skrivs efter det att färgen ändrats. Text som redan skrivits ut förändras inte. Man kan använda Console.Clear() för att fylla skärmen med den nya bakgrundsfärgen.
	

### Console.ResetColor

Återställer för- och bakgrundsfärg till konsolens vanliga.

```csharp
Console.ResetColor();
```

### ANSI-färger

ANSI är en gammal textstandard, med koder som fortfarande kan användas för att formatera text i konsolen. Man börjar varje kommando med `\x1b[`, följt av en siffra och sedan `m`. [En komplett lista finns här](https://gist.github.com/raghav4/48716264a0f426cf95e4342c21ada8e7).

I exemplet nedan används alltså `\x1b[34m` för att aktivera blå färg, och sedan används `\x1b[0m` för att återgå till normal färg.

```csharp
Console.WriteLine("\x1b[34mBlå\x1b[0m färg");
```

## Fönstret

### Console.Title

Ändrar konsolfönstrets namn.

```csharp
Console.Title = "Mitt fina fönster";
```

## Console.Beep()

Gör ett ljud!

```csharp
Console.Beep(294,1000) // 1 sekunds (1000 millisekunders) beep i D.
```

## Pekaren

### Console.SetCursorPosition()

Bestäm pekarens position i x- och y-led. Tar emot två int-värden.

```csharp
Console.SetCursorPosition(20, 10); // Plancera pekaren på column 20, rad 10
```

!!! warning

	**OBSERVERA:** y-axeln är **omvänd**! Med andra ord, den första raden är 0, den andra är 1, den tredje är 2… Och "origo" ligger uppe i vänstra hörnet.
	

### Console.GetCursorPosition()

Läs av pekarens position i x- och y-led. Returnerar en [tuple ](datatyper/tuples.md)där det första värdet är x, det andra y.

```csharp
(int x, int y) = Console.GetCursorPosition();
```

### Console.CursorLeft

Pekarens position i x-led, räknat från fönstrets vänstra kant (den första "kolumnen" är 0)

```csharp
Console.CursorLeft = 20; // Placera pekaren i kolumn 20
Console.CursorLeft -= 5; // Flytta pekaren fem steg åt vänster
```

### Console.CursorTop

Pekarens position i y-led, räknat från fönstrets överdel.

```csharp
Console.CursorTop = 10; // Placera pekaren på rad 10
Console.CursorTop-- // Flytta pekaren 1 rad uppåt
```

