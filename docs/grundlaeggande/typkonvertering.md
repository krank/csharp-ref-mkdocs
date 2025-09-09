# Typkonvertering

## Implicit konvertering

En del datatyper kan lätt konverteras till andra utan att man behöver göra någon manuell konvertering. Det gäller framför allt när konverteringen inte innebär att man blir av med information eller precision.

{% code lineNumbers="true" %}
```csharp
int i = 9;
long l = i;
```
{% endcode %}

### Exempel:

* int → long
* int → string
* int → float
* float → double

## Casting

När konverteringen innebär att man blir av med precision, t.ex. går från en float till en int och blir av med decimaler, så använder man ibland **casting**. Det betyder att man helt enkelt skriver vilken datatyp man vill konvertera till inom parenteser innan värdet som ska konverteras.

{% code lineNumbers="true" %}
```csharp
float xPos = 3.4f;
int x = (int) xPos;
```
{% endcode %}

## As

As fyller en liknande funktion som casting, men fungerar bara på datatyper som är av referenstyp (t.ex. klasser) och datatyper som kan bli null (t.ex. string). Detta är mest användbart när man använt [polymorfi](../klasser-och-objektorientering/polymorfism/).

As går också lite snabbare än casting.

{% code lineNumbers="true" %}
```csharp
// Säger att instansen som enemy-variabeln pekar mot är en instans av Goomba,
//  och att Goomba-variabeln "g" också ska peka mot samma instans.
Goomba g = enemy as Goomba;
```
{% endcode %}

## Is

Is kan användas för att se vilken datatyp ett värde är. Detta är mest användbart när man använt [polymorfi](../klasser-och-objektorientering/polymorfism/).

{% code lineNumbers="true" %}
```csharp
// Om instansen som enemy-variabeln pekar mot är en instans av Goomba-klassen,
//  så kör koden inuti if-blocket.

if (enemy is Goomba)
{
  // ---
}
```
{% endcode %}

Is kan också göra en samtidig As-operation.

{% code lineNumbers="true" %}
```csharp
// Om instansen som enemy-variabeln pekar mot är en instans av Goomba-klassen
//  så skapa en ny variabel "g" som är an datatypen Goomba och pekar mot
//  samma instans.

if (enemy is Goomba g)
{
  g.SetColor("Brown");
}
```
{% endcode %}

## Konvertera till int

### int.Parse()

Många datatyper kan inte konverteras direkt till t.ex. en int. Metoden int.Parse tar emot nästan vad som helst – t.ex. en string – och försöker konvertera den till en int.

{% code lineNumbers="true" %}
```csharp
string tal = "42";
int i = int.Parse(tal);
```
{% endcode %}

!!! warning

	**OBS:** Parse kommer att orsaka ett runtime error ifall den string som anges inte kan konverteras till en int. Använd [try-catch](try-catch.md) för att fånga upp felet eller använd TryParse istället för Parse.
	

### int.TryParse()

För en enkel, säker konvertering kan man använda TryParse.

{% code lineNumbers="true" %}
```csharp
string tal = "42";
int resultat;
bool lyckad = int.TryParse(tal, out resultat);
```
{% endcode %}

TryParse returnerar true om konverteringen lyckades, false om den inte lyckades. Resultatet lagras i variabeln som anges som "out"-variabel i den andra parametern (i exemplet, variabeln "resultat"). Om konverteringen misslyckas så blir resultatet 0.

## Konvertera till float

### float.Parse()

Tar emot ett värde, och konverterar det till en float – om det går. Resultatet av konverteringen returneras.

{% code lineNumbers="true" %}
```csharp
string tal = "42.5"
float f = float.Parse(tal);
```
{% endcode %}

Om det inte går att konvertera värdet till en float, kommer Parse att ge ifrån sig ett runtime-felmeddelande.

### float.TryParse()

För en enkel, säker konvertering kan man använda TryParse.

{% code lineNumbers="true" %}
```csharp
string tal = "42.5";
float f;
bool lyckad = float.TryParse(tal, out f);
```
{% endcode %}

TryParse returnerar true om konverteringen lyckades, false om den inte lyckades. Resultatet lagras i variabeln som anges som "out"-variabel i den andra parametern (i exemplet, variabeln "resultat"). Om konverteringen misslyckas så blir resultatet 0.
