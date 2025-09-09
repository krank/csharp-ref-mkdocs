# Konstruktorer

En konstruktor är en metod som anropas automatiskt när en instans skapas. Den skrivs in i klassen som en publik metod utan returtyp och med samma namn som klassen.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  private string _name = "";
  private int _strength = 0;

  public Fighter()
  {
    _strength = Random.Shared.Next(5,10);
  }
}
```
{% endcode %}

När man skapar en instans av klassen Fighter så ges instansen nu enligt koden ovan ett slumpat strength-värde.

## Parametrar och konstruktorer

Precis som andra metoder kan konstruktorer ta emot en eller flera parametrar. Det brukar till exempel användas som ett snabbt och enkelt sätt att skjuta in information som ska lagras i instansens variabler.

{% code title="Fighter.cs" lineNumbers="true" %}
```csharp
class Fighter
{
  private string _name = "";
  private int _strength = 0;

  public Fighter(string name)
  {
    _name = name;
    strength = Random.Shared.Next(5,10);
  }
}
```
{% endcode %}

{% code title="Program.cs" lineNumbers="true" %}
```csharp
Fighter heroFighter = new Fighter("Britta-Lena");
Fighter enemyFighter = new Fighter("Börje");
```
{% endcode %}

## Kontruktorer som anropar varandra (this)

Om man har flera konstruktorer så väljs vilken som körs genom samma principer som annan [metod-överlagring](../grundlaeggande/egna-metoder.md#oeverlagring). Vill man själv kalla på en annan konstruktor så kan man göra detta genom att skriva :this() efter konstruktorns parenteser. Mellan de nya parenteserna lägger man de värden som ska passeras till önskad konstruktor.

```csharp
public class Fighter
{
  private int _hp;

  public Fighter(): this(100)
  {
  }

  public Fighter(int hp)
  {
    _hp = hp;
  }
}
```

## Konstruktorer i arv

När en basklass och en subklass har varsin konstruktor så kommer _båda_ konstruktorerna att köras när en instans av subklassen skapas. Först körs basklassens konstruktor, därefter körs subklassens konstruktor.

{% code title="" lineNumbers="true" %}
```csharp
class Character
{
  protected int _hp;
  protected string _name = "";
  
  public Character()
  {
    _hp = 100;
  }
}
```
{% endcode %}

{% code title="Thief.cs" lineNumbers="true" %}
```csharp
class Thief: Character
{
  public Thief()
  {
    _name = "Thief";
    _hp = 20;
  }
}
```
{% endcode %}

I exemplet ovan kommer med andra ord en instans av Thief först 100 i hp när basklassens konstruktor körs, och sedan ändras hp till 20 och name till "Thief".

## Konstruktorer med parametrar i arv

Eftersom både basklassens och subklassens konstruktor körs, så betyder det att om basklassens konstruktor kräver ett parametervärde så måste det värdet stoppas in på något sätt även när det är subklassen som instansieras.

I exemplet nedan måste Character-klassens konstruktor få ett string-värde som parameter.

{% code title="Character.cs" lineNumbers="true" %}
```csharp
class Character
{
  public string _name;
  public int _hp = 100;

  public Character(string name)
  {
    _name = name;
  }
}
```
{% endcode %}

För att ange vilket värde som ska skickas till basklassens konstruktor så använder man base().

```csharp
class Dragon : Character
{
  public Dragon() : base("Dragon")
  {
    _hp = 200;
  }
}
```

Man kan också skicka vidare värden från subklassens konstruktor-parametrar till basklassens konstruktor.

{% code title="Hero.cs" lineNumbers="true" %}
```csharp
class Hero : Character
{
  public Hero(string name, int hp) : base(name)
  {
    _hp = hp;
  }
}
```
{% endcode %}

Här tar subklassens konstruktor emot två parametrar – name och hp – och skickar vidare värdet som lagras i parametern name till basklassens konstruktor.

## Primära konstruktorer (.net 8)

I dotnet 8 introduceras _primary constructors_ – de gör att man kan stoppa in parametervärden in i klassen utan att explicit skapa en konstruktor.

```csharp
public class Enemy (string name, int hp)
{
  private int _hp = hp;
  private string _name = name;
}
```

Om man då stoppar in andra, vanliga konstruktorer så måste man modifiera dem så att de matar "primärkonstruktorn" med rätt data.

```csharp
public class Enemy(string name, int hp)
{
  private int _hp = hp;
  private string _name = name;

  // Konstruktor som körs när man inte anger några parametervärden: new Enemy()
  public Enemy() : this("Goomba", 100)
  {
  }

  // Konstruktor som körs när man anger bara en string, som förs vidare in i
  //  primärkonstruktorn
  public Enemy(string name) : this(name, 50)
  {
  }
}
```
