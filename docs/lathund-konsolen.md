# Lathund: koda i konsolen

<details>

<summary>Problem med svenska tecken i konsolen?</summary>

Ibland kan det vara problem med svenska tecken i konsolen. Om det är problem skriv följande kod i början av programmet.

```csharp
Console.InputEncoding = System.Text.Encoding.Unicode;
Console.OutputEncoding = System.Text.Encoding.Unicode;
```

</details>

## Kommentarer

Genom att skriva // framför något så gör man så det inte tolkas som kod utan som en kommentar.

```csharp
// Det här är en kommentar.
// Console.WriteLine("Det här är också en kommentar; en kod som inte körs");
```

## Variabler

Variabler lagrar information – allt man vill kunna komma ihåg i programmet lagras i variabler.

Varje variabel har en [**datatyp**](grundlaeggande/datatyper/). När man skapar en variabel så anger man vilken sorts information som ska lagras i den.

```csharp
// int är datatypen, hp namnet på variabeln
int hp = 100;          // int = heltal
string name = "Micke"; // string = text
float money = 4.5f     // float = decimaltal
```

Man kan ändra på en variabels värde i efterhand. = funkar alltid, så länge variabeln är på vänster sida och det du vill ändra dess värde till är på höger.

```csharp
name = "Martin"; // Ändra name till 'Martin'
hp = hp + 10; // Öka hp med 10
hp += 5; // Öka hp med 5
hp++ // Öka hp med 1
hp-- // Minska hp med 1
```

## Läsa in data

### Läsa in text med [WriteLine](grundlaeggande/konsollen-console.md#console.writeline), [ReadLine](grundlaeggande/konsollen-console.md#console.readline)

Används för att skriva ut saker till användaren eller läsa in saker.

```csharp
Console.Write("Vad heter du? ");
string name = Console.ReadLine();
Console.WriteLine($"Hej {name}! Kul att du också är här :-)");  // Skriver ut 'Hej ...!  Kul att du också är här :-)
```

### Läsa in tal med [TryParse](grundlaeggande/typkonvertering.md#int.tryparse)

Tryparse gör att man kan göra om en string till en int.

```csharp
string pointsText = Console.ReadLine();
int points = 0;
bool success = int.TryParse(pointsText, out points);
```

## Villkorssatser

### [If-else](grundlaeggande/if-satser.md)

If gör att man kan ha kod som bara körs om ett villkor stämmer (är _true_).

```csharp
string name = Console.ReadLine();
if (name == "Micke")
{
  Console.WriteLine("Välkommen!");
}
```

I exemplet nedan används också else if och else för att skapa en kedja.

```csharp
string name = Console.ReadLine();

if (name == "Micke") // Först kollas name mot 'Micke'
{
  Console.WriteLine("Välkommen!");
}
else if (name == "Martin")  // Om det inte är 'Micke' kollas namn mot 'Martin'
{
  Console.WriteLine("Hej!");
}
else  // och om det varken är 'Micke' eller 'Martin' körs den här koden
{
  Console.WriteLine("Dig känner jag inte, hejdå!");
}
```

### [Villkor](grundlaggande/boolska-satser.md) och [jämförelser](grundlaeggande/operatorer.md#boolska)

Mellan parenteserna i if-satser och loopar skriver man någon form av jämförelse som blir sann eller falsk. Vanliga jämförelser kan vara:

* `==` "Är exakt lika med"
* `!=` "Är inte lika med"
* `>` "Är större än"
* `<` "Är mindre än"
* `<=` "Är större än eller lika med"
* `>=` "Är mindre än eller lika med

```csharp
int hp = 50;
if (hp < 10)
{
  Console.WriteLine("Skadad!");
}

if (hp > 100)
{
  Console.WriteLine("Overcharge!");
}
```

Man kombinerar ofta jämförelser med varandra, genom att använda && (och), || (eller).

```csharp
if (name == "Mikael" && pass == "password" && attempts < 4)
{
  Console.WriteLine("Välkommen!");
}
```

## [Slump](grundlaeggande/slump.md)

```csharp
// randomNumber blir ett tal som kan vara minst 0, max 99
int randomNumber = Random.Shared.Next(100);
// Talet kan vara minst 4, max 7
int otherNumber = Random.Shared.Next(4,7);
```

## Upprepa med loopar

### [While-loop](grundlaeggande/loopar.md#while-loop)

En loop när man inte vet hur många gånger koden skall köras.

```csharp
while (true) // Loop som körs för evigt
{
  string password = Console.ReadLine();
  if (password == "12345")
  {
    break; // Avbryter loopen
  }
}
```

En while-loop funkar exakt som en if-sats, utom att när koden som står under den är klar, så gör den jämförelsen igen – och om den fortfarande är _true_ så kör den en gång till.

```csharp
string name = Console.ReadLine();
while (name != "Micke")
{
  name = Console.ReadLine()
}
```

**Observera** att exemplet ovan kan användas för alla möjliga jämförelser – så fort du vill begränsa användarens input, göra så att hen inte får gå vidare förrän hen skrivit in något som är "rätt sorts input", så kan du använda en while.

### [For-loop](grundlaeggande/loopar.md#for-loop)

En sorts loop som är väldigt bra när man vill köra en loop ett specifikt antal gånger. For-loopar funkar egentligen som while-loopar, men inkluderar en _räknare_.

```csharp
// Räknaren heter i, börjar på 0 och ökar med 1 varje gång loopen körts.
for (int i = 0; i < 10; i++) 
{
  // Det som står här inne kommer köras 10 gånger
  // Första gången loopen körs, har i värde 0
  // Andra gången har i värde 1
  // Tredje gången har i värde 2...
}
```

## [List](grundlaeggande/listor-och-arrayer.md#list)

Med listor kan man ha flera värden i samma variabel.

```csharp
List<int> numbers = [2, 45, 13, 200];
List<string> names = ["Micke", "Martin"];
```

Man kan läsa av och ändra på vad som finns på platser i en lista genom _indexering_. Varje plats i listan är numrerad från 0 och uppåt.

```csharp
List<string> names = ["Micke", "Martin"];
Console.WriteLine(names[0]); // Skriver ut 'Micke'
Console.WriteLine(names[1]); // Skriver ut 'Martin'
names[0] = "Mohammad"; // Byter ut 'Micke' mot 'Mohammad'
Console.WriteLine(names[0]); // Skriver ut 'Mohammad'
```

Man kan också kolla hur lång en lista är med Count, lägga till saker med Add och ta bort med Remove eller RemoveAt.

```csharp
List<string> names = ["Micke", "Martin"];
Console.WriteLine(names.Count); // Skriver ut '2'

names.Add("Jenny"); // Lägg till Jenny, som får index 2
names.Remove("Martin"); // Ta bort Martin, så att Jenny får index 1
names.RemoveAt(0); // Ta bort namnet med index 0

if (names.Contains("Jenny")) // Kolla om Jenny finns i listan
{
  Console.WriteLine("Jenny är med!");
}
```

Med en [foreach-loop](grundlaeggande/loopar.md#foreach-loop) kan man gå igenom listan och läsa av varje sak i den i tur och ordning.

```csharp
foreach (string name in names) // Loopa igenom listan
{
  Console.WriteLine(name);
}
```

## [Metoder](grundlaeggande/egna-metoder.md#enkel-metod)

En metod är en bit återanvändbar kod, som kan anropas från andra delar av koden. Metoder som är statiska är helt separata från resten av koden – de kan inte komma åt variabler som inte är deras egna. Metoder är överlag lite som Las Vegas: Det som händer i metoden stannar i metoden. Om man inte specifikt säger något annat.

```csharp
static void CountDown()
{
  for (int i=10; i>0; i--)
  {
    Console.WriteLine(i + "...");
  }
}
```

### Parametrar

För att få _in_ data i en metod används parametrar. Det gör man generellt när man vill att en och samma metod ska kunna göra delvis olika saker beroende på vilken data den ges.

```csharp
static void CountDownFrom(int startValue)
{
  for (int i=startValue; i>0; i--)
  {
    Console.WriteLine(i + "...");
  }
}

CountDownFrom(100); // 100 stoppas in i parametervariabeln startValue
CountDownFrom(10);
```

### Returnering

Om man vill ta med sig något från inifrån en metod så använder man _return_.

```csharp
// 'string' betyder att vi lovar att metoden returnerar en string
//        ↓
static string GetName() 
{
  string name = "";
  while (name.Length == 0)
  {
    Console.WriteLine("Vad heter du?");
    name = Console.ReadLine();
  }
  
  return name; // 'return' avslutar metoden och skickar tillbaka innehållet i 'name'
}

string heroName = GetName();
string enemyName = GetName();
```

## Klasser

Varje klass läggs normalt i en egen fil.

{% code title="Enemy.cs" %}
```csharp
class Enemy
{
  public string Name;
}
```
{% endcode %}
