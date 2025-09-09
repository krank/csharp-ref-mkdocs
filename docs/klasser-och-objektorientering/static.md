# Static

Statiska variabler och metoder tillhör klassen istället för instanserna. Alla instanser delar alltså på en och samma variabel/metod.

## Statiska variabler

När man läser eller ändrar på en statisk variabel utifrån skriver man klassens namn, sedan en punkt och därefter variabelns namn. Inuti klassmetoder kan man alltid bara använda variabeln som vilken som helst.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  // En statisk slumpgenerator som alla fighters delar på
  static Random _generator = new Random();
  
  private int _strength;
  
  // En konstruktor där slumpgeneratorn används
  public Fighter()
  {
    _strength = _generator.Next(10,20);
  }
}
```
{% endcode %}

## Statiska metoder

När man anropar en statisk metod skriver man klassens namn, sedan en punkt och därefter metodens namn. Inuti icke-statiska klassmetoder kan man anropa statiska metoder som om de vore vanliga metoder.

!!! info

	En viktig detalj är att **inuti en statisk metod** kan man **bara** anropa de metoder i samma klass som **också är statiska**. Detta eftersom metoden tillhör just klassen och inte instanserna. Detta gäller också variabler - i en statisk metod kan man bara använda statiska klassvariabler.
	

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  public static string GetRandomFighterName()
  {
    /* ... */
  }
}
```
{% endcode %}
