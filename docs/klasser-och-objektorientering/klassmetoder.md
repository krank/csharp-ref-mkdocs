# Klassmetoder

Det går utmärkt att lägga in metoder i klasser. De anropas då genom att man skriver instansens namn följt av metodens namn, och lägger in parametrar och hanterar returneringar som vanligt.

Klassmetoders kod kan komma åt instansens variabler, properties och metoder. Det gäller även sådana den fått genom [arv](arv.md).

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  private string _name = "";
  public string GetName()
  {
    return _name;
  }
}
```
{% endcode %}

{% code title="Program.cs" lineNumbers="true" %}
```csharp
Fighter f1 = new Fighter();

string n = f1.GetName();
Console.WriteLine(n);
```
{% endcode %}

När en metod som ingår i en klass vill använda en variabel som ingår i samma klass så kan den göra detta genom att använda dess namn rakt av. Man behöver alltså inte skriva instansens namn.

Om man vill vara tydlig med att man använder en intern klassvariabel så kan man skriva **this.** framför.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  private string _name = "";
  
  public void WriteName()
  {
    Console.WriteLine(this._name);
  }
}
```
{% endcode %}
