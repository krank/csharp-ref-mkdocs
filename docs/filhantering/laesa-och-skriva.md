# Läsa och skriva

## Att läsa data från en fil

Börja med att lägga till System.IO högst upp bland de bibliotek som inkluderas.

```csharp
using System.IO;
```

### ReadAllText()

Läser in all information från angiven fil till en string

```csharp
string contents = File.ReadAllText(@"localfile.txt");
```

Exempelkoden läser in all data från filen localfile.txt och lagrar datan i string-variabeln contents.

### ReadAllLines()

Läser in all information från angiven fil till en string-array — en rad från filen per position i arrayen.

```csharp
string[] contents = File.ReadAllLines(@"localfile.txt");
```

Exempelkoden läser in all data från filen localfile.txt och lagrar datan i string-array-variabeln contents.

Om localfile.txt t.ex. innehåller:

{% code title="localfile.txt" %}
```
Banana
Apple
Monkey
```
{% endcode %}

så kommer contents-arrayen att ha tre strings i sig: Banana, Apple och Monkey.

## Att skriva data till en fil

Börja med att lägga till System.IO högst upp bland de bibliotek som inkluderas.

```csharp
using System.IO;
```

### WriteAllText()

Skriver en string till en textfil.

```csharp
File.WriteAllText(@"localfile.txt", "Banana");
```

Exempelkoden skriver texten "Banana" till textfilen localtext.txt.

### WriteAllLines()

Skriver en string-array till en textfil - med en av arrayens strings per rad.

{% code lineNumbers="true" %}
```csharp
string[] contents = {"Apple", "Banana", "Monkey"};

File.WriteAllLines(@"localfile.txt", contents);
```
{% endcode %}

Exempelkoden skriver innehållet från string-arrayen contents till filen localfile.txt. Resultatet blir att localfile.txt innehåller följande:

{% code title="localfile.txt" %}
```
Apple
Banana
Monkey
```
{% endcode %}
