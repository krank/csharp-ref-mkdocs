# Virtual, override

När man vill kunna låta en subklass ha en egen version av en metod som finns i basklassen så använder man virtual och override.

Virtual används för att markera metoder i basklassen som får "skrivas över" av subklasserna.

{% code title="Character.cs" lineNumbers="true" %}
```csharp
class Character
{
  protected int _hp = 100;
  protected int _damage = 5;
  
  public int Attack()
  {
    return Random.Shared.Next(_damage);
  }

  public virtual void Hurt(int amount)
  {
    _hp -= amount;
  }
}
```
{% endcode %}

Override används för att ge en subklass en egen version av en metod från basklassen som markerats som virtuell.

{% code title="Berbarian.cs" lineNumbers="true" %}
```csharp
class Barbarian: Character
{
  public override void Hurt(int amount)
  {
    _hp -= amount / 2;
  }
}
```
{% endcode %}

För att Override ska fungera så måste det finnas en metod i basklassen som ser likadan ut (samma namn, samma returtyp, samma antal parametrar med samma datatyper) och som är virtual.

Syftet med detta är att göra så att man inte måste skapa nya metoder åt subklasserna när de ska fungera annorlunda än basklassen. Det här är en av byggstenarna för [polymorfism](https://sites.google.com/view/csharp-referens/klasser-och-objektorientering/polymorfism?authuser=0).

### Base <a href="#h.p_gkwodfcvlsmn" id="h.p_gkwodfcvlsmn"></a>

Base låter en subklass få tillgång till basklassens version av en metod.

{% code title="Character.cs" lineNumbers="true" %}
```csharp
class Character
{
  protected int _hp = 100;
  protected int _damage = 5;

  public virtual int Attack()
  {
    return Random.Shared.Next(_damage);
  }

  public virtual void Hurt(int amount)
  {
    _hp -= amount;
  }
}
```
{% endcode %}

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  public override int Attack()
  {
    return base.Attack() * 2;
  }
}
```
{% endcode %}

När en Fighter-instans' Attack-metod anropas i koden ovan, så anropas först basklassens Attack-metod, som returnerar 5. Den femman multipliceras med 2 och resultatet returneras. Med andra ord:

{% code lineNumbers="true" %}
```csharp
Fighter f = new Fighter();
int damage = f.Attack();
```
{% endcode %}

I exemplet ovan blir damage lika med 10.
