# String

En string är en text – en serie tecken efter varandra.

```csharp
string s = "Hello";
```

## $ – interpolated strings

Om man skriver $ framför en string, så kan man sedan stoppa in variabler och metodanrop och annat inuti måsvingar i stringen. Det som står innanför måsvingarna utvärderas och blir en del av stringen.

```csharp
int hp = 100;
string s = $"Du har {hp} hit points kvar";
```

Om man har ett decimaltal ([float](../../grundlaeggande/datatyper/#float) eller [double](../../grundlaeggande/datatyper/#double)) så kan man skriva : och sedan ett format med t.ex. antal decimaler.

```csharp
float c = 23;
float f = 32 + (c * 1.8f);
Console.WriteLine($"Fahrenheit: {f:00.00}");
```

## ToLower()

En metod som är inbyggd i alla strings, och ger en kopia av stringen där alla stora bokstäver bytts ut mot små.

```csharp
string name = "Micke";
string nameSmall = name.ToLower(); // värdet i nameSmall blir "micke".
```

Detta är praktiskt när man t.ex. vill göra jämförelser och det inte ska spela någon roll ifall användaren skriver med stor bokstav.

## Length

Length är en egenskap alla strings har. Det är en int som innehåller det antal tecken stringen har.

```csharp
Console.WriteLine($"Texten {s} har {s.Length} tecken");
```

## `\` – specialtecken

Om man skriver `\` i en string så kommer tecknet efter att tolkas som ett specialtecken. Det vanligaste är `\n`, som är en newline (ny rad).

```csharp
Console.WriteLine("Detta är första raden.\nDetta är andra raden.");
```

## `"""` – raw literal strings

Väldigt praktiskt för ASCII-art och andra strings som har flera rader.

Om man använder tre citattecken före och efter en string:

* Alla tecken inklusive `"` och `\` tolkas som vanliga tecken snarare än kommandon.
* Framför allt den avslutande `"""` måste vara på en egen ny rad
* Ingen rad i stringen får börja längre åt vänster än den avslutande `"""`.
* Indraget för sista """ anger var alla raderna anses "börja", så även om hela stringen har ett indrag på 8 mellanslag så kommer den skrivas ut med 2 mellanslags indrag om den avslutande """ är indragen 6 mellanslag.
* Man kan fortfarande använda `$` och `{}` för att infoga variabler.

```csharp
Console.WriteLine("""
          _  .   .   .
        .' '; '-' '-'|-.
      (     '------.'  )
        ;            \ /
        :     '   ' |/
        '._._       \    .;
        .-'   ;--.    '--' /
      /      \-'---.___.'
      |     / 7 \(>o<) /  
      |     | \ |  . \     
      |=====|   |  .  \ |-)
      |-'-'   ./_.-._.\|"
      '-.----'        |
        |       |     |
        |     | |   | |
        |_____|_|___|_|
        (-------',----'.
          '-'-----'-----'         
    """);
```

## @ – literal strings

Om man skriver @ framför en string, så kommer varje tecken i denna string sedan att tolkas väldigt bokstavligt. Framför allt används detta när man inte vill att \ ska tolkas, utan bara skrivas ut som just \\. Det är praktiskt när man ska göra sökvägar i Windows.

```
Console.WriteLine(@"Detta är första raden.\nDetta är också första rader.");
```

## All()

All() är en del av **Linq-biblioteket** så man måste först ha med `using System.Linq`. All har en [delegate ](../../grundlaeggande/delegates.md)som parameter, och förväntar sig då en metod (eller ett lambda-uttryck) som tar emot en `char` och returnerar `true` eller `false`. All stoppar sedan i var och ett av stringens tecken in i den angivna metoden. Om resultatet för alla blir `true` så returnerar All också `true`.

```csharp
using System.Linq;

string s1 = "12345";
string s2 = "123a45;

bool b1 = s1.All(char.IsDigit); // b1 = true
bool b2 = s2.All(char.IsDigit); // b2 = false
```
