# Public, private och protected

## Public

Variabler och metoder som är **publika** kan läsas av och ändras på **utifrån**.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  public string Name = "";
}
```
{% endcode %}

{% code title="Program.cs" lineNumbers="true" %}
```csharp
Fighter hero = new Fighter();
hero.Name = "Laban";
```
{% endcode %}

## Private

Variabler och metoder som inte är publika kan inte nås utifrån – men däremot kan de fortfarande nås **inifrån** metoder som ingår i samma klass. **Privata** variabler och metoder kan bara nås från metoder i **exakt** samma klass – så inte i någon subklass som ärver från den.

Om det **inte står något** framför en klassvariabel eller klassmetod är den **automatiskt private**.

För att man ska kunna få ut värdet hos en privat variabel behöver man gå via en publik metod som returnerar dess värde. Metoden tillhör ju klassen, så _den_ får komma åt den privata variabeln. Detta är en form av [inkapsling](inkapsling-och-properties.md).

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

## Protected

Fungerar som private, men metoden/variabeln kan kommas åt i klasser som _ärver_ från klassen där de deklareras.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  protected string _name = "";
  
  public string GetName()
  {
    return _name;
  }
}
```
{% endcode %}

{% code title="StrongFighter.cs" lineNumbers="true" %}
```csharp
class StrongFighter : Fighter
{
  public string GetName()
  {
    // kan använda name trots att variabeln tillhör basklassen
    return $"{_name} The Strong";
  }
}
```
{% endcode %}
