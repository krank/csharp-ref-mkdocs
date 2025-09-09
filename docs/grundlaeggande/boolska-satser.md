# Boolska satser

En boolsk sats är en formel som resulterar i antingen ett sant eller ett falskt värde – ett [bool](../grundlaeggande/datatyper/#bool)-värde.

```csharp
int i = Random.Shared.Next(10);

// Den boolska satsen blir true om i är högre än 2 och samtidigt lägre än 8.
// Resultatet av den boolska satsen sparas i result
bool result = i > 2 && i < 8;
```

Man kan inkludera allt möjligt – jämförelser med [boolska ](../grundlaeggande/operatorer.md#boolska)och [logiska ](../grundlaeggande/operatorer.md#logiska)operatorer, bool-variabler, metoder som returnerar boolska värden.

```csharp
bool jumpThisFrame = IsGrounded() && hasReleasedJumpButton && jumpCharge > 0;
```

Boolska satser används ofta i if-satser, while-loopar och liknande för att _göra flera jämförelser samtidigt_.

```csharp
int r = Random.Shared.Next(10);

while (r < 2 || r > 8)
{
  Console.WriteLine($"Sorry, fick en {r} så jag är fast i loopen en stund till");
}
```

Det är en teknik som ofta används som del av när man vill [begränsa input](../tekniker/begraensa-input.md) för användaren
