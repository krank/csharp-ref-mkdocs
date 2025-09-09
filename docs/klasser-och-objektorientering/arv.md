# Arv

När man bygger en klass som bygger på en annan klass så kallas det **arv**. Arvet innebär att subklassen får samma variabler och metoder som basklassen. Arv är alltså ett sätt att _återanvända kod_.

!!! info

	**OBSERVERA:** Arv symboliserar en "är-en-relation", det vill säga subklassen ska kunna sägas vara en underkategori till basklassen. En Hero _är en_ sorts Character. En Goomba _är en_ sorts Enemy. Ett svärd _är en_ sorts vapen.
	

Man skapar ett arv genom att skriva ett kolon (:) efter klassnamnet, följt av namnet på basklassen. Så om man vill att klassen Hero ska ärva från klassen Character så skriver man `class Hero: Character` när man skapar klassen.

{% code title="Character.cs" lineNumbers="true" %}
```csharp
class Character
{
  public string name;
  public int hp = 100;
  public int x = 0;
  public int y = 0;

  public void Hurt(int amount)
  {
    hp -= amount;
  }
}
```
{% endcode %}

{% code title="Hero.cs" lineNumbers="true" %}
```csharp
class Hero: Character
{
  int _xp = 0;
  int _level = 1;
  
  public AddExperience(int amount)
  {
    _xp += amount;
    _level = 1 + _xp / 10;
  }
}
```
{% endcode %}

{% code title="Program.cs" lineNumbers="true" %}
```csharp
Hero myHero = new Hero();

myHero.name = "Britt-Marie";

myHero.Hurt(3);
myHero.AddExperience(12);
```
{% endcode %}

Hero bygger på Character, så alla instanser av Hero-klassen har egna name, hp, x och y-variabler. Dessutom har de egna kopior av Hurt-metoden, som då påverkar Hero-instansens egen hp.

Dessutom tillför Hero-klassen ett par egna variabler och en egen metod.
