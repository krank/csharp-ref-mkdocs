# Linq-metoder

Linq-biblioteket bygger ut existerande [samlings-datatyper](../../klasser-och-objektorientering/generiska-klasser.md#samlingar) (som [List ](../../klasser-och-objektorientering/generiska-klasser.md#list)och även [arrayer](../../grundlaeggande/listor-och-arrayer.md#array)) med nya metoder.

Ofta tar metoderna emot [delegater ](../../grundlaeggande/delegates.md)som parametrar, och ofta används då istället [Lambda-uttryck](../../grundlaeggande/delegates.md#lambdas).

Flera av metoderna returnerar en generisk samling av den Linq-specifika datatypen _Enumerable_, som i sin tur kan omvandlas till en lista genom att man anropar ToList().

### Hämta flera

#### Where()

Tar emot ett kriterium i form av en delegat eller ett Lambda-uttryck, och returnerar en Enumerator som innehåller alla föremål som matchar kriteriet.

```csharp
List<GameObject> objects = new();
objects.Add(new Enemy());

List<GameObject> lowHealth = 
  objects.Where(g => g.hp < 10)
  .ToList();
```

#### OfType<>()

Returnerar en Enumerable som innehåller alla föremål som är av en specifik datatyp. Väldigt användbart ifall man använt [polymorfism ](../../klasser-och-objektorientering/polymorfism/)för att lagra instanser av subklasser i en [samling ](../../klasser-och-objektorientering/generiska-klasser.md#samlingar)där typvariabeln är basklassen.

```csharp
List<GameObject> objects = new();
objects.Add(new Enemy());

List<Enemy> enemies = objects.OfType<Enemy>().ToList();
```

### Hämta enstaka

#### First() / Last()

Returnerar det första/sista värdet i samlingen. Om samlingen är tom så skapas ett [runtime-fel](../../grundlaeggande/fel.md#runtime-fel-exceptions).

```csharp
List<int> myList = new List<int>() {4,3,2,1};

int i = myList.First(); // i blir 4
```

#### FirstOrDefault() / LastOrDefault()

Fungerar som First/Last, utom att metoden returnerar null, eller ett default-värde (t.ex. 0 för ints) ifall samlingen är tom.

```csharp
List<int> myList = new List<int>();
int i = myList.FirstOrDefault(); // i blir 0
```

### OrderBy()

Tar emot en delegate eller ett Lambda-uttryck som parameter, och använder den för att sortera samlingen. Delegaten tar emot ett föremål, och returnerar det värde som ska avgöra föremålens sortering.

OrderBy returnerar en Enumerable som innehåller samma föremål som originalsamlingen, sorterade i rätt ordning.

```csharp
List<Character> sortedCharacters = 
  characters.OrderBy(c => c.name)
  .ToList();
```

### Select

Tar emot en delegate eller ett Lambda-uttryck som parameter, och bygger en ny samling med det som returneras från delegaten/uttrycket för varje föremål i originalsamlingen.

Anges bara en parameter i delegaten/uttrycket så ska denna vara samma datatyp som originalsamlingens typparameter.

```csharp
List<int> intList = new() { 1, 2, 3, 4, 5 };

List<int> higherIntList = 
  intList.Select(x => x + 6)
  .ToList(); // 7,8,9,10,11
```

Skapa en lista med instanser av Character, där varje Characters konstruktor tar emot en string i form av ett namn (n):

```csharp
string[] names = {"Björn", "Mira", "Mohammad", "Kim"};

List<Character> characters = 
  names.Select(n => new Character(n))
  .ToList();
```

Skapa en lista med instanser av Character, där varje Characters konstruktor tar emot en string i form av ett namn (n) samt en siffra som är namnets index plus 1:

```csharp
string[] names = {"Björn", "Mira", "Mohammad", "Kim"};

List<Character> characters = 
  names.Select((n, i) => new Character(n, i+1))
  .ToList();
```

### Boolska

#### All()

Tar emot ett kriterium i form av en delegat eller ett Lambda-uttryck, och returnerar true ifall samtliga föremål i samlingen stämmer in på kriteriet.

```csharp
List<int> intList = new() { 1, 2, 3, 4, 5 };

bool allHigh = intList.All(n => n > 3); // false, för alla är inte > 3
```

#### Any()

Tar emot ett kriterium i form av en delegat eller ett Lambda-uttryck, och returnerar true ifall minst ett föremål i samlingen stämmer in på kriteriet.

```csharp
List<int> intList = new() { 1, 2, 3, 4, 5 };

bool hasHigh = intList.Any(n => n > 3); // true, för minst en är > 3
```

### Matematiska

Dessa fungerar bara för samlingar med tal – ints, doubles, floats och så vidare.

#### Max()

Returnerar det högsta värdet i samlingen.

```csharp
List<int> intList = new() { 2, 67, 23, 100, 1 };

int highest = intList.Max(); // 100
```

#### Min()

Returnerar det lägsta värdet i samlingen.

```csharp
List<int> intList = new() { 2, 67, 23, 100, 1 };

int lowest = intList.Min(); // 1
```

#### Average()

Returnerar medelvärdet av alla värden i samlingen, som en [double](../../grundlaeggande/datatyper/#double).

```csharp
List<int> intList = new() { 2, 67, 23, 100, 1 };

double avg = intList.Average(); // 38.6
```
