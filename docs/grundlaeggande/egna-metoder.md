# Metoder

## Enkel metod

En metod är ett namngivet kodblock, som kan anropas från andra delar av koden genom att man skriver dess namn. Det gör att koden kan återanvändas och man slipper skriva samma kod flera gånger.

{% code lineNumbers="true" %}
```csharp
static void MetodensNamn()
{
  Console.WriteLine("Hej!");
}
```
{% endcode %}

För att anropa metoden skriver man sedan:

```csharp
MetodensNamn();
```

"static"-delen behövs _enbart_ om metoden ska kunna anropas från en annan metod som också är static, till exempel Main.

För mer information om vad "static" egentligen betyder – [läs här](../klasser-och-objektorientering/static.md).

## Parametrar

Genom parametrar kan man föra in information i metoden när den anropas.

{% code lineNumbers="true" %}
```csharp
static void PrettyPrint(string text)
{
  Console.WriteLine($"--~~== {text} ==~~--");
}
```
{% endcode %}

För att deklarera värdet av parametern vars namn är text anropas metoden ovan såhär:

```csharp
PrettyPrint("Horsies!");
```

Resultatet blir att följande skrivs ut till konsolen:

```
--~~== Horsies! ==~~--
```

## Returnering

För att få ut information ur en metod så att informationen kan användas i resten av programmet används returnering. Det innebär att man istället för void skriver vilken datatyp informationen man vill få ut från metoden ska ha, och sedan någonstans i metoden skriver return följt av en information som har denna datatyp.

{% code lineNumbers="true" %}
```csharp
static float OneThird()
{
  float result = 1f / 3f;
  return result;
} 
```
{% endcode %}

När man sedan anropar metoden så fångar man upp den returnerade informationen i en variabel.

```csharp
float f = OneThird();
```

Ofta kombinerar man parametrar och returneringar för att bygga metoder som bearbetar den information man stoppar in på något sätt.

{% code lineNumbers="true" %}
```csharp
static int Multiply(int a, int b)
{
  int result = a * b;
  return result;
}
```
{% endcode %}

Och ovanstående metod anropas såhär:

```csharp
int area = Multiply(3, 4);
```

Resultatet blir att 3 multipliceras med 4 inuti metoden, och resultatet (12) returneras och lagras i variabeln `area`.

## Överlagring

Att överlagra metoder innebär att man döper flera metoder till samma namn, men låter dem ha olika parametrar.

Effekten blir att när man anropar metodnamnet så används de parametervärden man anger för att avgöra vilken av de olika metoderna som ska köras.

{% code lineNumbers="true" %}
```csharp
static void Shout()
{
  Console.WriteLine("AAAAAAAAH!");
}
```
{% endcode %}

{% code lineNumbers="true" %}
```csharp
static void Shout(string exclamation)
{
  Console.WriteLine(exclamation.ToUpper());
}
```
{% endcode %}

De två Shout-metoderna ovan har samma namn, men den ena tar emot en parameter. Om man nu anropar så här:

```csharp
Shout();
```

Så kommer den övre versionen att köras. Inget parametervärde angavs, och det finns en version av Shout som inte behöver några parametrar, alltså körs den.

Om man däremot anropar så här:

```csharp
Shout("abracadabra!");
```

Så kommer den nedre versionen att köras. Ett string-värde angavs som parametervärde, och det finns en version av Shout som behöver ett string-värde, alltså körs den.

## Generiska metoder

Generiska metoder är metoder där datatypen för någon eller några av variablerna eller parametrarna inte bestäms när metoden deklareras, utan när den anropas.

I exemplet nedan används 1 typ-parameter, "T". Efter att den skrivits mellan <> efter metodens namn så kan T användas i koden som om den vore en datatyp.

{% code lineNumbers="true" %}
```csharp
static void PrintInRed<T>(T content)
{
  ConsoleColor defaultColor = Console.ForegroundColor;
  Console.ForegroundColor = ConsoleColor.Red;
  Console.WriteLine(content);
  Console.ForegroundColor = defaultColor;
}
```
{% endcode %}

När metoden sedan anropas så anges vilken datatyp T ska vara vid just det anropet genom att datatypen skrivs mellan <> efter metodens namn.

{% code lineNumbers="true" %}
```csharp
PrintInRed<int>(8);
PrintInRed<string>("Hello, World!");
```
{% endcode %}

Detta liknar hur [generiska klasser](../klasser-och-objektorientering/generiska-klasser.md) fungerar.
