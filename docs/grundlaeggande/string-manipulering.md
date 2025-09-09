# Strings

En string är i C# alltid oföränderlig; man kan inte ändra direkt i en string. Men man kan använda olika metoder för att skapa **nya versioner** av existerande strings.

## Escape-sekvenser

Genom att skriva \ följt av ett annat tecken kan man få vissa specialeffekter. \n är till exempel **ny rad**.

```csharp
Console.WriteLine("Detta är en rad\nDetta är en annan rad");
```

Andra användbara sekvenser är:

* **`\\`** skriver ut ett faktiskt \\-tecken
* **`\"`** skriver ut ett citattecken
* **`\'`** skriver ut ett enkelt citattecken

## String interpolation

Genom att skriva $ framför citattecknet kan man lägga in variabler och även kod mitt i sina strings, mellan {}. Det viktiga är att det man skriver in antingen är en string, kan konverteras till en string eller blir en string när koden körs.

```csharp
string name = "Mikael";
Console.WriteLine($"Hello {name} how are you today?");
```

## Verbatim strings

Genom att skriva @ framför citattecknet stänger man av escape-sekvenser. Detta är väldigt praktiskt ifall man vill lägga in ASCII-art eller använda många '\\-tecken. Detta kan dock inte kombineras med string interpolation.

```csharp
Console.Writeline(@"\\\\\--- inga problem ---/////");
```

## Literal strings

Genom att använda **tre citattecken** i början och slutet av en string kan man kombinera verbatim string-tolkning med string interpolation.

Dessutom: om koden där stringen skapas är indenterad, ignoreras denna indentering när stringen skrivs ut. Mycket praktiskt för längre texter överlag!

```csharp
static void Hey()
{
  string name = "Luka";

  string s = $"""
    My name is {name}
      I live on the second floor 
  """;
  
  Console.WriteLine(s);
}
```

## String-metoder

### Replace()

Byter ut ett tecken eller en del-string.

{% code lineNumbers="true" %}
```csharp
string oldString = "Mikael är min programmeringslärare";

string newString = oldString.Replace("Mikael", "Micke");
```
{% endcode %}

### Substring()

Returnerar en del av stringen. Tar emot startposition och längd som parametrar. Anges bara en parameter så antas längden vara resten av stringen.

{% code lineNumbers="true" %}
```csharp
string oldstring = "Detta är en string";

string sub1 = oldString.Substring(2,5); // sub1 blir "tta ä"

string sub2 = oldString.Substring(2); // sub2 blir "tta är en string"
```
{% endcode %}

### Trim()

Returnerar en kopia av stringen där mellanslag och andra "tomma" tecken tagits bort från början och slutet.

```csharp
string clean = oldString.Trim();
```

Det finns också `TrimEnd` och `TrimStart` ifall man bara vill trimma slutet eller början av stringen.

### Insert()

Returnerar en kopia av stringen där en annan string stoppats in på en angiven plats. Tar emot en position och en string som parametrar.

{% code lineNumbers="true" %}
```csharp
string folk = "micke och kim och mimmi";

string nyFolk = folk.insert(5, " och herbert"); 
// nyFolk blir "micke och herbert och kim och mimmi"
```
{% endcode %}

### Contains()

Kollar om en string innehåller en annan string, t.ex. ifall "haj" finns i texten "en haj hoppar över en björn". Returnerar true om den finns, false om den inte gör det.

{% code lineNumbers="true" %}
```csharp
string answer = Console.ReadLine();
bool hasAShark = answer.Contains("haj");

if (hasAShark == true)
{
  Console.WriteLine("Du skrev något med ordet haj!");
}
```
{% endcode %}

### IndexOf()

Returnerar positionen för den första plats i stringen där en annan string finns. Tar emot något att söka efter som parameter.

{% code lineNumbers="true" %}
```csharp
string folk = "micke och kim och mimmi";
int kimPlats = folk.IndexOf("kim");
int mellanslagPlats = folk.IndexOf(" ");
```
{% endcode %}

Resultatet av ovanstående blir att variabeln kimPlats får värdet 10 och att mellanslagPlats får värdet 5. Positionssiffrorna börjar på 0.

### ToUpper()

Returnerar en kopia av stringen där alla gemener (små bokstäver) bytts ut mot versaler (stora bokstäver).

```csharp
string caps = oldString.ToUpper();
```

### ToLower()

Returnerar en kopia av stringen där alla versaler (stora bokstäver) bytts ut mot gemener (små bokstäver).

```csharp
string small = oldString.ToLower();
```

Denna används ofta för att till exempel förvandla strings man fått in från en användare så att det inte spelar någon roll ifall hen svarat t.ex. JA, Ja, jA eller ja.

### Sätta ihop och ta isär

#### String.Join()

Sätter ihop alla element i en array till en string. Tar emot två parametrar; en separator som placeras mellan elementen och en array med de element som ska sättas ihop.

{% code lineNumbers="true" %}
```csharp
string[] names = {"micke", "kim", "mimmi"};
string folk = String.Join(" och ", names);

// Variabeln "folk" får namnet "micke och kim och mimmi"
```
{% endcode %}

#### Split()

Returnerar en array som består av en uppdelad string. Tar emot en separator som parameter. Separatorn kan bara vara ett ensamt tecken, en **char**.

{% code lineNumbers="true" %}
```csharp
string folk = "micke och kim och mimmi";
string[] names = folk.Split(' ');

// Variabeln "names" får innehållet {"micke", "och", "kim", "och", "mimmi"}
```
{% endcode %}

## En string är en array

I grunden är en string helt enkelt en [array ](listor-och-arrayer.md#array)av [chars](datatyper/#char). Det betyder att man kan använda alla tekniker man normalt kan med arrayer – Length, indexering och ranges till exempel – även med strings

{% code lineNumbers="true" %}
```csharp
string name = "Mikael Bergström";

char firstChar = name[0]; // firstChar blir M

string firstPart = name[..6]; // firstPart blir "Mikael"
```
{% endcode %}
