# Thread

!!! info

	**OBS:** Ganska mycket överkurs. Det här möter man normalt först på högskola/universitet.
	

!!! info

	**OBS** Oftast gör man inte threading manuellt på det här viset i C#, men det är bra att förstå grundkonceptet. Istället används oftast [Tasks ](task.md)för asynkron programmering
	

Thread-klassen används när man manuellt vill skapa nya trådar. Som parameter anges en metod vars kod ska köras i den separata tråden. Observera att det är metodens namn – dess identifier – som anges, och att man inte skriver () efter namnet.

```csharp
using System.Threading; // Behövs för tillgång till Thread-klassen

Thread workerThread = new Thread(DoSomeHeavyLifting);

static void DoSomeHeavyLifting()
{
  // Kod som ska köras i den separata tråden
}
```

Man kan också använda metoder som tar emot en parameter. Parametern måste då vara av datatypen object, som sedan kan castas till sin egentliga datatyp.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);

static void DoSomeHeavyLifting(object n)
{
  string name = (string) n;
  
  // Kod som ska köras i den separata tråden
}
```

## Start

Startar körningen av tråden.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.Start();
```

När man startar körningen av en metod som tar emot parametrar, så anges parametervärdet som parameter i Start-metoden.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.Start("Saruman");

static void DoSomeHeavyLifting(object n)
{
  string name = (string) n;
  
  // Kod som ska köras i den separata tråden
}
```

## Join

Pausar körningen av den nuvarande tråden, tills den tråd som "joinas" är klar med sin körning.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.Start();

// Kod som ska köras samtidigt som tråden körs

workerThread.Join();
```

## Name

En [property ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)som är trådens namn. Användbart bl.a när man debuggar.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);

workerThread.Name = "Arbetaren";
```

## IsAlive

En [property ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)som berättar huruvida tråden är "levande"; alltså huruvida den just nu utför sitt arbete. Tråden börjar "leva" när den startas, och slutar leva när dess arbete är utfört – alltså när dess kod är färdigkörd.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);

while (workerThread.IsAlive)
{
  Console.WriteLine("Arbete pågår!");
  Thread.Sleep(500);
}
```

## IsBackground

En [property ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)för huruvida tråden är en bakgrunds-tråd eller ej.

Skillnaden mellan bakgrundstrådar och förgrundstrådar är att om huvudprogrammet når sitt slut innan en förgrundstråd är klar, så väntar huvudprogrammet på att tråden ska bli färdig innan körningen avslutas. Bakgrundstrådar avslutas automatiskt när huvudprogrammet når sitt slut.

Trådar är normalt sett _förgrundstrådar_.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.Start();

Console.WriteLine("Väntar på att tråden ska bli klar...");
```

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.IsBackground = true;
workerThread.Start();

Console.WriteLine("Väntar inte på att tråden ska bli klar...");
```

## CurrentThread

En statisk [property ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)som pekar på den nuvarande tråden.

```csharp
Thread workerThread = new Thread(DoSomeHeavyLifting);
workerThread.Name = "Arbetaren";

static void DoSomeHeavyLifting()
{
  Console.WriteLine(Thread.CurrentThread.Name); // Skriver ut "Arbetaren"
  Thread.CurrentThread.IsBackground = true;
  
  // Kod som ska köras i den separata tråden
}
```

## Sleep

En statisk metod som gör att den nuvarande tråden "somnar" (pausas) i så många millisekunder som anges som parametervärde.

```csharp
static void DoSomeHeavyLifting()
{
  Console.WriteLine("Väntar 1 sekund innan resten av trådens kod körs");
  Thread.Sleep(1000);  
  
  // Kod som ska köras i den separata tråden
}
```
