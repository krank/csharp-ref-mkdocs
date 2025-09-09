# Delegates, events och lambdas

!!! info

	**OBS:** Lite överkurs =)
	

Delegates är ett sätt att kunna göra så att variabler pekar mot metoder istället för mot värden eller objekt i minnet. De är lite överkurs, men ganska användbara.

{% code lineNumbers="true" %}
```csharp
// Skapar en delegate som passar in på metoder som 
// inte tar emot några parametrar eller returnerar något.
delegate void Task(); 

// En metod som passar in på delegaten
static void SayHello() {
  System.WriteLine("Hello!");
}

static void Main(string[] args)
{
  Task t = SayHello; // Lagra en referens till SayHello-metoden i "t"
  t(); // Att köra t som en metod är nu samma sak som att köra SayHello.
}
```
{% endcode %}

När man skapar en delegat så beskriver den en metodprofil. Man kan säga att varje delegat beskriver en **kategori** av metoder.

{% code lineNumbers="true" %}
```csharp
// Stämmer in på metoder som tar emot en int-parameter och inte returnerar något.
delegate void DelegateOne(int y);

// Stämmer in på metoder som returnerar en int utan att ta emot några parametrar.
delegate int DelegateTwo();

// Stämmer in på metoder som returnerar en float efter att ha tagit emot
// en string och en int.
delegate float DelegateThree(string x, int y);
```
{% endcode %}

När man skapat sin delegat används den alltså som om den vore en datatyp. När man lagrar metoderna i den så ser man till att inte använda () efter metodnamnet, för då körs ju metoden istället, innan tilldelningen.

```csharp
DelegateOne test = MethodOne;
```

## Action <a href="#h.p_qt3arehin8yt" id="h.p_qt3arehin8yt"></a>

En Action är en generisk delegat som passar in på metoder som inte returnerar ett värde. Om man vill matcha metoder som tar emot parametrar kan dessa anges mellan <>.

{% code lineNumbers="true" %}
```
static void Hello()
{
  Console.WriteLine("Hello");
}

static void HelloTo(string target)
{
  Console.WriteLine($"Hello {target}");
}

Action example1 = Hello;
Action<string> example2 = HelloTo

example1();
example2("Micke");
```
{% endcode %}

### Dictionary med Actions <a href="#h.p_qt3arehin8yt" id="h.p_qt3arehin8yt"></a>

Ett exempel på hur man kan använda delegater.

{% code lineNumbers="true" %}
```csharp
Dictionary<string, Action> actions = new Dictionary<string, Action>();

actions.Add("first", DoFirst);
actions.Add("second", DoSecond);
  
actions["first"](); // Kör DoFirst-metoden


static void DoFirst()
{
  /* .. */
}

static void DoSecond()
{
  /* .. */
}
```
{% endcode %}

## Func

Func är en generisk delegat som matchar metoder som returnerar något. En eller flera datatyper anges inom <>. Anges flera så är den sista alltid returtypen, resten är parametrar.

```csharp
static int Addition(int a, int b)
{
  return a + b;
}

static string MakeStrengthString(int str)
{
  return $"Strength: {str}";
}

Func<int, int, int> math = Addition;

Func<int, string> statDisplay = MakeStrengthString;

int y = math(3,4);

string strength = statDisplay(14);
```

## Anonyma metoder i delegatvariabler

Anonyma metoder saknar eget namn.

{% code lineNumbers="true" %}
```csharp
static void Main(string[] args)
{
  Action t = delegate()
    {
      System.WriteLine("Hello!");
    }
    
  t();
}
```
{% endcode %}

De är praktiska när man aldrig faktiskt kommer att anropa metoden med dess eget namn, utan bara vill kunna lägga in den i en variabel eller en lista.

{% code lineNumbers="true" %}
```csharp
Dictionary<string, Action> actions = new Dictionary<string, Action>();

actions.Add("greet", 
  delegate ()
  {
    Console.WriteLine("Hello");
  }
);

actions["greet"]();
```
{% endcode %}

## Multicasting: delegat-variabler med flera metoder

Om man vill att flera metoder ska köras när en delegat-variabel anropas så kan man kombinera delegater för att skapa s.k. [multicast-delegater](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/how-to-combine-delegates-multicast-delegates).

{% code lineNumbers="true" %}
```csharp
Action multiCaster = delegate() { Console.WriteLine("Hello"); };

multiCaster += delegate() { Console.WriteLine("World"); };

multiCaster(); // Skriver först ut Hello, sedan World
```
{% endcode %}

{% code lineNumbers="true" %}
```csharp
Action good = delegate() { Console.WriteLine("Good"); };

Action bye = delegate() { Console.WriteLine("Bye"); };

Action morning = delegate() { Console.WriteLine("Morning"); };

Action goodMorning = good + morning;
Action goodBye = good + bye;

goodMorning(); // Skriver ut "Good" och "Morning"
goodBye(); // Skriver ut "Good" och "Bye"
```
{% endcode %}

Att lägga till en metod till en multicast-delegat kallas **subscribing**, och att ta bort en metod från en multicast-delegat kallas **unsubscribing**.

## Events

Nackdelen med multicast-delegater är att den som har tillgång till dem inte bara kan lägga till nya metoder i dem, utan också aktivera dem och göra större ändringar – som att till exempel ändra dem till null.

Med en event kan den som har tillgång utifrån **bara** lägga till och ta bort metoder (subscribe/unsubscribe)

!!! info

	**Events kan bara existera i klasser**, och de kan bara anropas (invoke) inifrån den klassen
	

{% code title="Avatar.cs" lineNumbers="true" %}
```csharp
public class Avatar
{
  public event Action OnDeath; // OBS: nyckelordet "event"

  public Avatar()
  {
    OnDeath += DeathMessage; // Subscribe:a klassmetoden DeathMessage
  }

  public void Update()
  {
    OnDeath.Invoke(); // Aktivera (invoke) eventet
  }

  public void DeathMessage() { Console.WriteLine("YOU DIED"); }
}
```
{% endcode %}

{% code title="Program.cs" lineNumbers="true" %}
```csharp
Avatar p = new Avatar();

Action PauseGame = delegate() { Console.WriteLine("Game is paused"); };

// Subscribe:a den lokala metoden PauseGame till eventet OnDeath
p.OnDeath += PauseGame;

p.Update(); // Kör Update-metoden, som i sin tur invoke:ar eventet
```
{% endcode %}

## Lambdas

Lambda-uttryck är, enkelt uttryckt, ett sätt att skriva väldigt enkla anonyma metoder (anonyma delegater) vars returvärden är direkta resultat av deras parametrar. Ett lambda-uttryck består av en parentes där den anonyma metodens parametervärden anges, en => och slutligen en enkel uträkning som motsvarar det som ska returneras från metoden.

Uträkningen kan bytas ut mot ett kodblock som returnerar ett värde, om mer omfattande&#x20;

{% code lineNumbers="true" %}
```csharp
// Delegat som passar alla metoder som tar emot två int-parametrar och
// som returnerar en int som resultat
delegate int Calculation(int x, int y);

static void Main(string[] args)
{
  // Lambda-uttrycket => har två inputs på vänster sida, 
  // och uträkningen på höger sida resulterar i en int.
  // Därför passar lambda-uttrycket in på delegaten Calculation.
  Calculation c = (xInput, xOutput) => xInput * xOutput;

  int result = c(10, 5);
  
  // Detta gör samma sak som ovan, men med ett kodblock istället 
  // för en ren beräkning
  Calculation c2 = (xInput, xOutput) => {return xInput * xOutput};
}
```
{% endcode %}

Lambdas används väldigt ofta när man till exempel vill filtrera en lista på något sätt.

{% code lineNumbers="true" %}
```csharp
List<int> numbers = new List<int>() {2,3,4,5,6};

// FindAll returnerar en lista med alla föremål i listan som matchar ett visst
// kriterium. Kriteriet ska vara utformat som en metod, som tar emot ett
// föremål av rätt datatyp som parameter och returnerar en bool.
// lambda-uttrycket nedan tar emot en input på vänster sida (n) och uttrycket
// på höger sida är en boolsk jämförelse.
// Därför kommer lowNumbers att innehålla en lista med alla integers från
// numbers, som är < 4.
List<int> lowNumbers = numbers.FindAll(n => n < 4);
```
{% endcode %}

De kan också användas till events och till multicast-delegates. Ofta används detta när det bara är ganska lite kod som ska köras.

{% code lineNumbers="true" %}
```csharp
Avatar p = new Avatar();

p.OnDeath += () => Console.WriteLine("Game is paused");
```
{% endcode %}
