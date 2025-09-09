# Klasser och instanser

Klasser är ett sätt att klumpa ihop variabler och metoder som hör till samma "sak" i ett spel eller ett program. De gör det lättare att felsöka och lättare att hålla god struktur.

Man kan betrakta en **klass** som en ritning för något - "såhär ska fiender i spelet se ut - de ska ha de här egenskaperna".

Sedan skapar man **instanser** av klassen - de konkreta, faktiska fienderna. Alla goombas i Super Mario Bros och alla paladiner i World of Warcraft bygger på samma ritning. De har samma egenskaper och utseende i grunden, även om de skiljer sig åt i vilka värden en del av egenskaperna har. De befinner sig till exempel på olika positioner, även om de alla _har_ en position.

## Skapa klasser

Generellt bör varje klass läggas i sin egen fil. Med C# Dev Kit finns ett snabbt och enkelt sätt:

* Gå till **Explorer** och öppna **Solution Explorer**.
* **Högerklicka på projektet** klassen/filen ska läggas till i.
* Välj **"Add new File"**.
* Välj **"Class"**.
* Skriv in namnet på klassen – glöm inte [namngivning ](../grundlaeggande/namngivning.md)med **PascalCase**!
* Skriv in skriv in **using** och namnet på klassens **namespace** högst upp i Program.cs

{% code title="Goomba.cs" lineNumbers="true" %}
```csharp
namespace PlumberPlatformer

class Goomba
{
  // Klassvariabler
  public int X = 0;
  public int Y = 0;
  public bool IsDead = false;
}
```
{% endcode %}

{% code title="Program.cs" %}
```csharp
using PlumberPlatformer;

```
{% endcode %}

## Skapa instanser

Kodordet `new` skapar **nya instanser** i minnet ([heapen](../grundlaeggande/reference-vs-value-types.md#minnet-stacken-och-heapen)).

Därefter behöver en [referens ](../grundlaeggande/reference-vs-value-types.md)till instansen lagras någonstans, till exempel i en variabel.

{% code lineNumbers="true" %}
```csharp
Goomba g1 = new Goomba();
Goomba g2 = new Goomba();
```
{% endcode %}

Därefter kan man ändra på de individuella instansernas variabler separat:

{% code lineNumbers="true" %}
```csharp
g1.X = 60;
g1.Y = 20;
g2.X = 80;
g2.Y = 25;
```
{% endcode %}

Man kan också tilldela värden till variablerna direkt när instansen skapas:

```csharp
Goomba g3 = new Goomba() {x = 10, y = 6};
```

### New()

Om man (som ovan) skapar en instans av exakt samma klass som variabeln så kan koden förenklas. Det gäller med andra ord nästan jämt – undantaget är vid [polymorfism](polymorfism/#polymorfism-klasser-och-arv).

{% code lineNumbers="true" %}
```csharp
Goomba g4 = new();
Goomba g5 = new() {X = 100};
```
{% endcode %}



