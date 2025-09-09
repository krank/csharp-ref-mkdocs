# Task

!!! info

	**OBS:** Ganska mycket överkurs. Det här möter man normalt först på högskola/universitet.
	

**Den korta versionen:** Om man använder ett bibliotek som tillhandahåller asynkrona metoder som returnerar Task<>, så kan man göra metoden man själv skriver, där metoden anropas, _asynkron_ och då får man använda _await_.

Det gör att man inte måste vänta på att den asynkrona metoden avslutas innan man går vidare – man kan göra det väntandet när man vill.

```csharp
static async Task GetMeThing() // Asynkrona metoder returnerar alltid en Task
{
  // Anropa en metod som hämtar en string från internet.
  // Men vänta inte på att den ska bli klar - gå direkt vidare.
  Task<string> task = SomeLibrary.FetchThingFromInternetAsync();
  
  // Gör något annat arbete medan vi väntar
  
  // Vänta tills metoden är klar
  await task;
  Console.WriteLine(task.Result);
  // Man behöver inte skriva return här; metoden returnerar ändå en Task
}
```

## Task<>

Den [generiska ](../../klasser-och-objektorientering/generiska-klasser.md)Task-klassen abstraherar och förenklar användningen av threading i C#.&#x20;

Genom att kapsla in en metod i en **Task** så körs metoden parallellt med övrig kod i programmet.

Oftast får man dock Tasks från metoder man inte själv skrivit, t.ex. från bibliotek man lagt till.

### Task.Run()

Används för att köra en vanlig (icke-async) metod som en Task. Praktiskt framför allt för CPU-intensiva aktiviteter, som massiva och tidsintensiva beräkningar.

Task.Run tar emot en [Action ](../../grundlaeggande/delegates.md#h.p\_qt3arehin8yt)som parameter, och kör den som en Task. Run() returnerar en referens till task:en som körs. Som vanligt kan man ange antingen en existerande metod eller en [anonym metod](../../grundlaeggande/delegates.md#anonyma-metoder-i-delegatvariabler) som sin Action.

```csharp
static void RegularWork()
{
  // Någonting intensivt
}

// Använd RegularWork som en Action
Task t1 = Task.Run(RegularWork);
```

```csharp
static int WorkWithReturn()
{
  // Någonting intensivt
  return 23;
}

// Använd HelloWorld som en Action<int>
Task<int> t2 = Task.Run(HelloWorld);
```

Taskens typ-parameter ska vara densamma som returtypen för metoden som kapslas in.

Vill man köra Task.Run med en metod som tar emot parametrar så kan man nyttja en anonym metod:

```csharp
static string WorkWithParameter(int t)
{
  // Någonting intensivt
  return "ready";
}

Task<string> t3 = Task.Run( () => WorkWithParameter(42) );
```

### Wait()

Pausar körningen av koden tills den inkapslade metoden körts färdigt.

```csharp
Console.WriteLine("Waiting...");
t1.Wait();
Console.WriteLine("Finished!");
```

### Result

Innehåller det som returnerats från den inkapslade metoden, när den körts färdigt. Om Result läses av innan metoden körts färdigt så pausar koden precis som med Wait().

```csharp
Console.WriteLine("Waiting...");
int result = taskMaster.Result;
Console.WriteLine($"Finished with a result of {result}!");
```

## Await

Väntar på att en Task ska avslutas. Tasken kan skapas/köras på samma rad eller, vilket är vanligare och smartare, på en rad längre upp.

```csharp
// Skapa Task:en och kör igång den; spara en referens i variabeln task
Task<string> task = SomeLibrary.FetchThingFromInternetAsync();
  
// Gör något annat arbete medan vi väntar
  
string result = await task; // Vänta tills metoden är klar

// Det ofta sämre sättet: Kör igång task:en direkt, och väntar 
// på samma radtills den är klar.
string result2 = await SomeLibrary.FetchThingFromInternetAsync();
```

## Async

De flesta async-metoder får man från något existerande bibliotek, till exempel [RestSharp](../naetverk-och-internet/restful-client.md#restsharp). Standard är att döpa dem till något som slutar på Async.

En asynkron metod:

* Deklareras med async
* Döps till något som slutar med Async
* Har alltid en Task som returtyp
* När man faktiskt skriver return, så är det inte en Task, utan den datatyp som Task:en har mellan <>. Så en async-metod med Task&lt;int> som returtyp bör ha t.ex. en `return 34;`.

Oftast skriver man asynkrona metoder när man har nytta av await – vilket man normalt sett bara har ifall man vill köra igång flera Tasks och köra dem parallellt, för att sedan await:a deras avslut.

```csharp
static async Task<int> GetLengthAsync() // Task<int> som returtyp
{
  // Kör igång 2 Tasks
  Task<string> t1 = SomeLibrary.FetchThingFromInternetAsync(); 
  Task<string> t2 = SomeLibrary.FetchThingFromInternetAsync(); 
  
  // Väntar tills båda är färdiga
  string s = await t1;
  string s2 = await t2;
  
  // Returnerar en int
  return s.Length + s2.Length;
}
```
