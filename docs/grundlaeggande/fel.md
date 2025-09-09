# Fel

## Syntaxfel

Ett syntaxfel är ett fel i själva grammatiken i koden; ett ganska lättfångat fel där man helt enkelt skrivit något ogiltigt. Syntaxfel signaleras i Visual Studio Code genom att strykas under med röda vågiga streck, s.k, "sqiggley lines". Man kan också få fram en lista med alla syntaxfel genom att gå till Problems-panelen (View → Problems).

## Runtime-fel (exceptions)

Ett runtime-fel är ett fel som uppstår när programmet körs. Koden som orsakar felet är syntaxmässigt korrekt, men den operation som koden beskriver går inte att utföra. Det kan till exempel vara att man försöker komma åt en position i en array som inte finns.

```csharp
int[] numbers = {3, 4, 12, 66};
Console.WriteLine(numbers[8]); // Det finns ingen åttonde int i arrayen
```

När ett runtime-fel uppstår så skapas ett Exception. Detta kan fångas upp av en [try-catch](try-catch.md).

## Logiska fel

Logiska fel är de svåraste att hitta – de hittas inte av Visual Studio (inga röda sqiggley lines), de orsakar inga felmeddelanden. De är helt enkelt resultatet av ett feltänk hos programmeraren – som leder till oönskat beteende.

```csharp
// Eftersom || används istället för && så räcker det med att ha rätt
//  användarnamn ELLER rätt lösenord.

if (username == "micke || password == "12345")
{
  loggedIn = true;
}
```
