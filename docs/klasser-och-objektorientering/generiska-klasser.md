# Generiska klasser

En generisk klass är en klass där någon datatyp inte är fördefinierad, utan deklareras i koden. En lista där värdena som lagras är `int` har till exempel datatypen List&lt;int> och en lista med strings är en List&lt;string>.

Det som skrivs mellan <> i en generisk klass kallas för en **typ-parameter**.

## Samlingar

C# innehåller ett antal färdiga generiska klasser i form av "samlingar" – helt enkelt objekt som _samlar_ flera objekt eller värden av andra datatyper. Till exempel kan en samling innehålla integers, strings eller instanser av en klass.

Några exempel på generiska samlingar är [List](generiska-klasser.md#list), [Queue](generiska-klasser.md#queue), [PriorityQueue](generiska-klasser.md#priorityqueue), [Stack](generiska-klasser.md#stack), [HashSet ](generiska-klasser.md#hashset)och [Dictionary](generiska-klasser.md#dictionary).

!!! info

	**OBS:** För att dessa ska fungera om du kör äldre versioner av dotnet (t.ex. dotnet 5), så behöver du skriva in följande högst upp i din kod:
	
	```csharp
	using System.Collections.Generic;
	```
	

### Gemensamt för samlingar

Nedanstående finns i de flesta samlingar – några saknas i Dictionary, som är lite av ett specialfall.

Många samlings-datatyper kan också få ytterligare funktionalitet via [Linq-metoder](../annat/linq/linq-metoder.md).

#### Count

En [property ](inkapsling-och-properties.md#properties)som används istället för Length för att räkna antalet saker i samlingen.

```csharp
List<int> myList = [1, 2, 3, 4, 5];

Console.WriteLine(myList.Count);
```

#### ToList() / ToArray()

Returnerar en lista eller en array som innehåller samma saker som samlingen.

```csharp
Queue<int> myQueue = new Queue<int>();
myQueue.Enqueue(4);

List<int> myList = myQueue.ToList();
```

#### Contains()

Tar emot ett värde. Om värdet finns i samlingen returnerar metoden true, annars false.

```csharp
List<int> myList = [4, 5, 6, 7];

if (myList.Contains(6))
{
  Console.WriteLine("Yes!");
}
```

#### Clear()

Rensar bort alla saker som finns i samlingen.

```csharp
List<int> myList = [4, 5, 6, 7];

myList.Clear();

Console.WriteLine(myList.Count); // skriver ut 0
```

### List

Fungerar som arrayer, utom att man inte bestämmer storlek från början utan kan använda bl.a Add och Insert och RemoveAt-metoder för att lägga till, stoppa in och ta bort grejer ur listan när som helst.

{% code lineNumbers="true" %}
```csharp
List<string> myList = [];

myList.Add("hej");

Console.WriteLine(myList[0])

List.RemoveAt(0);
```
{% endcode %}

När man skapar en lista kan man också direkt lägga in värden genom att ange en array efter parenteserna.

```csharp
List<int> myList = [1, 2, 3, 4, 5];
```

#### Add()

Lägger till något i listan.

```
myList.Add("hej");
```

#### Remove()

Tar bort något från listan. När man tar bort något ur listan&#x20;

```
myList.Remove("hej");
```

#### RemoveAt()

Tar bort något från en specifik indexposition i listan.

```
myList.RemoveAt(0);
```

#### RemoveAll()

Tar emot en [delegate ](../grundlaeggande/delegates.md)som beskriver ett kriterie. Delegaten tar emot ett objekt eller ett värde av samma datatyp som listan lagrar, och returnerar en bool ifall instansen uppfyller kriteriet. Normalt används ett [lambda-uttryck](../grundlaeggande/delegates.md#lambdas) istället för en metod för att uppfylla delegaten.

RemoveAll() tar bort alla element som matchar kriteriet, och returnerar ett int-värde som beskriver hur många som togs bort.

```csharp
List<int> intList = [1, 2, 3, 4, 5];

int i = intList.RemoveAll(x => x > 3); // i blir 2, och 4 och 5 tas bort ur listan.
```

#### Find()

Tar emot en [delegate ](../grundlaeggande/delegates.md)som beskriver ett kriterie. Delegaten tar emot ett objekt eller ett värde av samma datatyp som listan lagrar, och returnerar en bool ifall instansen uppfyller kriteriet. Normalt används ett [lambda-uttryck](../grundlaeggande/delegates.md#lambdas) istället för en metod för att uppfylla delegaten.

Find() returnerar det första föremål (värde eller objekt) i listan som matchar kriteriet. Om inget hittas, returneras null eller defaultvärdet för datatypen (t.ex. 0 för integers).

```csharp
List<int> intList = [1, 2, 3, 4, 5];

int i = intList.Find(x => x > 3); // i blir 4
```

#### FindLast()

Fungerar som Find, men kollar igenom listan bakifrån  och returnerar därmed det _sista_ föremål som matchar kriteriet.

```csharp
List<int> intList = [1, 2, 3, 4, 5];

int i = intList.FindLast (x => x < 3); // i blir 2
```

#### FindAll()

Fungerar som Find, men returnerar en lista med _alla_ matchande föremål i listan.

```csharp
List<int> intList = [1, 2, 3, 4, 5];

List<int> lowNumbers = intList.FindAll (x => x < 4); // lowNumbers blir 1,2,3
```

#### FindIndex()

Fungerar som Find, men returnerar _index_ för första matchande föremål.

```csharp
List<int> intList = [11, 12, 13, 14, 15];

int i = intList.FindIndex (x => x > 12); // i blir 2
```

#### FindLastIndex()

Fungerar som FindIndex(), men kollar igenom listan bakifrån och returnerar därmed _index_ för det _sista_ föremål som matchar kriteriet.

```csharp
List<int> intList = [11, 12, 13, 14, 15];

int i = intList.FindLastIndex (x => x < 13); // i blir 1
```

### Queue

Fungerar som en lista, utom att man bara kan lägga till saker längst bak i kön, och ta bort dem längst fram. Detta kallas FIFO, eller First In, First Out.

{% code lineNumbers="true" %}
```csharp
Queue<int> myQueue = new Queue<int>();

myQueue.Enqueue(5);
myQueue.Enqueue(42);
myQueue.Enqueue(665);

// Peek returnerar en kopia av värdet som ligger 
// längst fram i kön – 5 i det här fallet
Console.WriteLine(myQueue.Peek());

// Dequeue tar bort värdet som ligger längst fram ur kön 
// och returnerar det. Så nu är kön = 42, 665.
int n = myQueue.Dequeue();
```
{% endcode %}

#### Enqueue()

Lägger till ett objekt i kön.

```csharp
myQueue.Enqueue(5);
```

#### Dequeue()

Tar bort och returnerar nästa objekt i kön.

```csharp
int n = myQueue.Dequeue();
```

#### Peek()

Returnerar, men tar inte bort, nästa objekt i kön.

```csharp
Console.WriteLine(myQueue.Peek();
```

### PriorityQueue

Fungerar som en Queue, plus att varje sak som läggs in i kön ges en _prioritet_. När man sedan kör Dequeue eller Peek så är det objektet med högst prioritet (lägst prioritets-värde) som returneras. När man skapar en PriorityQueue så anger man två datatyper – en för de saker som ska sparas i kön, en som ska användas för att avgöra prioritet. Oftast är den senare bara en int eller annan numerisk datatyp.

Om flera saker har samma prioritet så returneras de i ordning motsvarande en vanlig queue.

```csharp
PriorityQueue<string, int> queue = new PriorityQueue<string, int>();

queue.Enqueue("Micke", 2);
queue.Enqueue("Martin", 1);
queue.Enqueue("Lena", 3);

Console.WriteLine(queue.Peek()); // Skriver ut "Martin"
```

### Stack

Fungerar som en "hög" – man kan bara lägga till saker högst upp i högen och även bara plocka bort saker från högst upp i högen. Detta kallas FILO, eller First In, Last Out.

{% code lineNumbers="true" %}
```csharp
Stack<int> myStack = new Stack<int>();

myStack.Push(5);
myStack.Push(42);
myStack.Push(665);

// Precis som för queue, peekar "nästa värde". Det som ligger högst upp – 665.
Console.WriteLine(myStack.Peek());

// Tar bort det som ligger högst upp i högen och returnerar det.
// Så nu är bara 5 och 42 kvar i högen.
int n = myStack.Pop();
```
{% endcode %}

### HashSet

Saknar indexering, men kan bara innehålla unika objekt – man riskerar inte att råka lägga till samma sak flera gånger.

{% code lineNumbers="true" %}
```csharp
HashSet<int> mySet = new HashSet<int>();

mySet.Add(5);
mySet.Add(42);
mySet.Add(5);

// skriver ut true, eftersom 5 ingår i setet.
Console.WriteLine(mySet.Contains(5));

// Skriver ut 2, för det finns bara 2 unika objekt i setet
//  – den andra femman lades aldrig till.
Console.WriteLine(mySet.Count());
```
{% endcode %}

### Dictionary

Fungerar som en lista, utom att man kan använda andra datatyper än ints som index. I Dictionaries använder man ofta ordet "key" istället för "index".

{% code lineNumbers="true" %}
```csharp
Dictionary<string, int> myStats = new Dictionary<string, int>();

myStats.Add("Strength", 20);
myStats.Add("Intelligence", 12);

Console.WriteLine(myStats["Strength"]);
```
{% endcode %}

#### Keys

Man kan få fram en samling av alla keys i ett dictionary genom att läsa av egenskapen Keys som är inbyggd i alla Dictionaries.

{% code lineNumbers="true" %}
```csharp
foreach (string key in myStats.Keys)
{
  Console.WriteLine($"{key}: {myStats[key]}");
}
```
{% endcode %}

## Skapa egna generiska klasser

Generiska klasser är oftast "container-klasser", alltså klasser vars uppgift det är att lagra ett annat värde.

{% code title="Node.cs" lineNumbers="true" %}
```csharp
class Node<T>
{
  public T Value;
  public Node NextNode;
}
```
{% endcode %}

Ovanstående kod är en enkel nod i en s.k. länkad lista. I en länkad lista känner varje nod bara till "nästa nod".&#x20;

Nu bestäms vilken datatyp variabeln value ska ha genom att den anges mellan <> när instansen skapas:

{% code lineNumbers="true" %}
```csharp
Node<string> firstTextNode = new Node<string>(); // value blir en string
firstTextNode.Value = "Bananas";

Node<int> firstNumberNode = new Node<int>(); // value blir en int
firstNumberNode.Value = 23;
```
{% endcode %}
