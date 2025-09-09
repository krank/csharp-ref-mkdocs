# Struct

Structs är som klasser men skiljer sig på en viktig punkt: de är [value types snarare än reference types](../grundlaeggande/reference-vs-value-types.md).

```csharp
Hero h1 = new() { Name = "A1" };
Hero h2 = h1; // h2 blir en KOPIA av h1, inte en pekare till samma objekt
h2.Name = "A2";

Console.WriteLine(h1.Name); // Så när namnet på h2 byts, så påverkas inte h1.
Console.WriteLine(h2.Name);

struct Hero
{
  public string Name;
}
```

Den generella regeln [som rekommenderas](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/choosing-between-class-and-struct) i C# är:

* Klasser om du vill inkludera beteende eller ha innehåll som förändras (lätt att låta flera delar av programmet arbeta med samma objekt).
* Structs för små objekt, utan speciellt mycket beteende och med ganska oföränderlig data.

Arbetar man med structs finns risk att man använder mer minne – eftersom man gör kopior av structen varje gång den överförs någonstans.
