# Datatyper \[…]

## int

Integer, heltal.

```csharp
int x = 3;
```

Man kan använda understreck för att göra heltalen mer lättlästa.

```csharp
int million = 1_000_000;
```

## string

En string är en text – en serie tecken efter varandra.

```csharp
string s = "Hello";
```

[Mer om strings finns här](../string-manipulering.md)

## float

Flyttal, decimaltal.

```csharp
float y = 3.4692f;

Console.WriteLine(y:N2); // Skriver ut talet med 2 decimaler
```

## double

Decimaltal som kan innehålla större tal – dubbelt så stora som floats.

```csharp
double x = 7.892;

Console.WriteLine(x:N2); // Skriver ut talet med 2 decimaler
```

## bool

Boolskt värde, är antingen true eller false.

```csharp
bool z = true;
```

## char

Ett tecken.

```csharp
char c = 'ä';
```

### Char.Is…

I klassen Char finns flera metoder för att undersöka char-tecken. Till exempel:

```csharp
Char.IsDigit(c) // true om c är en siffra
Char.IsLetter(c) // true om c är en bokstav
Char.IsLetterOrDigit(c) // true om c är en siffra eller en bokstav
Char.IsUpper(c) // true om c är en STOR BOKSTAV
Char.IsWhiteSpace(c) // true om c är ett mellanslag, en tabb eller en radbrytning
```

Observera att definitionen av "siffra" här inte bara inkluderar tecknen 0–9 utan också till exempel thailändska siffertecken.

## Andra heltal

Överkurs: det finns ett antal olika sätt att spara heltal, och de har olika min- och maxvärden.

* **int**, eller int32, är en 32-bitars integer. Den använder 32 ettor och nollor (bits/bitar) för att lagra ett heltal som kan vara positivt eller negativt. En av bitarna används för att avgöra ifall talet är positivt eller negativt.
* **long**, eller int64, är en 64-bitars integer.
* **short**, eller int16, är en 16-bitars integer.
* **uint**, **ulong** och **ushort** är versioner av int, long och short som inte kan bli negativa – men i gengäld kan mäta större positiva tal. Eftersom ingen bit används för att avgöra om talet är positivt/negativt.

Vilken som är lämplig vid vilket tillfälle beror på hur höga tal man behöver lagra samt hur viktigt det är att spara på minnesutrymmet.

```csharp
Console.WriteLine(int.MaxValue); //   2147483647
Console.WriteLine(int.MinValue); //  -2147483648
Console.WriteLine(uint.MaxValue); // 4294967295
Console.WriteLine(uint.MinValue); // 0

Console.WriteLine(long.MaxValue); //   9223372036854775807
Console.WriteLine(long.MinValue); //  -9223372036854775808
Console.WriteLine(ulong.MaxValue); // 18446744073709551615
Console.WriteLine(ulong.MinValue); // 0

Console.WriteLine(short.MaxValue); // 32767
Console.WriteLine(short.MinValue); // -32768
Console.WriteLine(ushort.MaxValue); // 65535
Console.WriteLine(ushort.MinValue); // 0
```

## Void

Void är egentligen inte en datatyp – det är mer ett ord som används när man specifikt inte förväntar sig någon data. Void används bara som returdatatyp för [metoder ](../egna-metoder.md)som inte ska returnera något.

## Null

Null är inte heller riktigt en datatyp, utan snarare "icke-data". En string-variabel som ges värdet null är inte ens en tom string – det är ett icke-värde.
