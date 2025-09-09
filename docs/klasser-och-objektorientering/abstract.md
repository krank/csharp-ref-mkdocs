# Abstract

## Abstrakta klasser

En abstrakt klass kan aldrig instansieras, utan kan bara användas som basklass för arv.

{% code title="Character.cs" lineNumbers="true" %}
```csharp
abstract class Character
{
  public string Name;
  public int Hp = 100;

  public void Hurt(int amount)
  {
    Hp -= amount;
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
  public void AddExperience(int amount)
  {
    _xp += amount;
    _level = 1 + _xp / 10;
  }
}
```
{% endcode %}

## Abstrakta metoder

Den huvudsakliga anledningen till att göra en basklass abstrakt är för att man vill kunna använda sig av abstrakta metoder. En abstrakt metod saknar kod, och måste overridas i alla subklasser. Det är med andra ord ett sätt att tvinga de som skapar subklasser att bygga egna versioner av den metoden.

Abstrakta metoder fungerar bäst i de fall där det inte finns någon lämplig "standardversion" av metoden som kan ingå i basklassen

{% code title="Character.cs" lineNumbers="true" %}
```csharp
abstract class Character
{
  public string Name;
  public int Hp = 100;
  public int Strength = 5;
  public int Level = 1;
  public int Xp = 0;
  public string[] Attacks = {"Kick", "Punch"}

  public abstract void LevelUp();
}
```
{% endcode %}

{% code title="Warrior.cs" lineNumbers="true" %}
```csharp
class Warrior : Character
{
  public override void LevelUp()
  {
    Level = Xp / 10;
    if (Level == 3)
    {
      Attacks = new string[] { "Kick", "Punch", "Bite" };
    }
  }
}
```
{% endcode %}

I exemplet ovan är det alltså tänkt att metoden LevelUp ska anropas för att ge karaktärer ny level, ifall de fått tillräckligt med xp. I och med att olika karaktärer ska ha olika progression baserat på vilken klass de tillhör (t.ex. Warrior) så kan man låta LevelUp-metoden vara abstrakt och ha en egen implementation för varje subklass.
