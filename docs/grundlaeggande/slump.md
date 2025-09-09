# Slump (Random)

## Slumpgenerator

En slumpgenerator är ett objekt som används för att generera slumptal.

{% code lineNumbers="true" %}
```csharp
// Skapar en slumpgenerator och gör så att vi kan komma åt den 
// med hjälp av variabeln "generator".
Random generator = new Random();
```
{% endcode %}

I Dotnet 6 och senare finns också en färdig slumpgenerator i `Random.Shared`.

## Next – heltal (int)

Används för att slumpa heltal (int).

{% code lineNumbers="true" %}
```csharp
// Slumpar ett heltal mellan 0 och det största heltal int kan innehålla
int r = Random.Shared.Next();
```
{% endcode %}

Next kan anropas med en [parameter ](egna-metoder.md#parametrar)som anger "taket" för slumpen. Taket är exklusivt, dvs det tal som anges kommer aldrig att slumpas - bara lägre tal.

{% code lineNumbers="true" %}
```csharp
// Slumpar ett heltal som är 0, 1, 2 eller 3
int r = Random.Shared.Next(4);
```
{% endcode %}

Om man anger två parametrar så tolkas den första som ett golv, och den andra som ett tak. Golvet är inklusivt, dvs det tal som anges kan komma att slumpas fram.

{% code lineNumbers="true" %}
```csharp
// Slumpar ett heltal som är 2, 3 eller 4
int r = Random.Shared.Next(2,5);
```
{% endcode %}

## NextDouble  – decimaltal

Används för att slumpa decimaltal mellan 0 och 1. Man får värdet i form av en double, så den behöver dels multipliceras med ett tal för att bli något annat än 0–1, och dels konverteras till float.

```csharp
float percent = (float) Random.Shared.NextDouble() * 100f;
```
