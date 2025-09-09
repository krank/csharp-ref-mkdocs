# Ta bort saker ur listan man går igenom

## Problemet

Om man har en lista och använder for eller foreach för att gå igenom den, så blir det väldigt fel om man tar bort saker ur listan medan man loopar genom den.

```csharp
List<int> numbers = new List<int>() {1,2,3,4,5,6};

foreach (int n in numbers)
{
  if (n < 4)
  {
    numbers.Remove(n); // Ger runtime-felmeddelande
  }
}
```

## En traditionell lösning

Den här lösningen innebär att man helt enkelt lägger in alla saker som ska tas bort ur listan in i en ny, separat lista. Sedan går man igenom _den_ listan, men tar bort sakerna ur den _ursprungliga_ listan.

```csharp
List<int> numbers = new List<int>() {1,2,3,4,5,6};

List<int>numbersToRemove = new List<int>();

foreach (int n in numbers)
{
  if (n < 4)
  {
    numbersToRemove.Add(n);
  }
}

foreach(int n in numbersToRemove)
{
  numbers.Remove(n);
}

numbersToRemove.Clear();
```

## Lambda

RemoveAll()-metoden i List-klassen ger oss ett enklare sätt att lösa saken på ­med ett [Lambda-uttryck](../grundlaeggande/delegates.md#lambdas):

```csharp
List<int> numbers = new List<int>() {1,2,3,4,5,6};

numbers.RemoveAll(n => n < 4);
```
