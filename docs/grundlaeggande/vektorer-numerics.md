# Vektorer (Numerics)

Numerics är ett bibliotek som innehåller mer avancerade numeriska typer, som komplement till de vanliga, t.ex. int.

```csharp
using System.Numerics;
```

De används ofta i spel, till exempel sådana man skapar med [Raylib](../annat/raylib/). Däremot har Unity sina egna Vector-klasser.

## Vector2

En Vector2 är en tvådimensionell vektor som består av två komposanter, en i x-led och en i y-led. Komposanterna har datatypen float.

{% code lineNumbers="true" %}
```csharp
// Skapa en vektor med X-värde 20 och Y-värde 30.5
Vector2 position = new Vector2(20f, 30.5f);
```
{% endcode %}

Man kan använda räknesätt med vektorer.

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 20);
Vector2 movement = new Vector2(0.1f, 0.1f);

// Adderar movement-vektorn till position-vektorn
position += movement;
```
{% endcode %}

Man kan till och med kombinera vektorer med vanliga siffror och räknesätt.

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 20);

// Skapar en vektor med X-värde 1 och Y-värde 0; 
// multiplicerar sedan både X och Y med 0.5.
Vector2 movement = new Vector2(1f, 0f) * 0.5f;

position += movement;
```
{% endcode %}

### X och Y

X och Y är float-egenskaper hos varje vektor.

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 30);

Console.WriteLine(position.X); // 20
Console.WriteLine(position.Y); // 30
```
{% endcode %}

### Length()

En metod inbyggd i varje vektor. Ger vektorns storlek (magnitud) som en [float](datatyper/#float).

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 20);
float l = position.Length(); // 28.284271
```
{% endcode %}

### Vector2.Distance()

Ger avståndet mellan två vektorer som en float.

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 20);
Vector2 enemyPosition = new Vector2(30, 30);

float d = Vector2.Distance(position, enemyPosition); // 14.142136
```
{% endcode %}

### Vector2.Normalize()

Ger en normaliserad version av en vektor.

{% code lineNumbers="true" %}
```csharp
Vector2 position = new Vector2(20, 10);

// Ger en vektor med storlek 1, X 0.8944272 och Y 0.4472136
Vector2 n = Vector2.Normalize(position);
```
{% endcode %}
