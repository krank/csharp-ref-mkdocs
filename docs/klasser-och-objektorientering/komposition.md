# Komposition

När ett objekt skapas och får sin funktionalitet genom att instanser av flera olika klasser samlas, så kallas det **komposition**. Komposition är, liksom arv, ett sätt att återanvända kod.

!!! info

	**OBSERVERA:** Den relation som en komposition symboliserar är en "har-en-relation". En karaktär _har ett_ vapen, en karaktär _har en_ karaktärsklass. Medan "krigare" till exempel snarare _är en_ karaktärsklass.
	

Komposition skapas genom att man helt enkelt lägger in klassvariabler eller properties vars datatyp är en klass som beskriver något instanser av klassen _har_.

```csharp
public class CharClass
{
  public string name;
}

public class Warrior : CharClass // Arv
{
  public Warrior()
  {
    name = "Warrior";
  }
}

public class Weapon
{
  public string name;
  public int minDamage;
  public int maxDamage;
}
```

```csharp
public class Character
{
  public string name;
  public int hp;
  public Weapon mainWeapon = new Weapon(); // Komposition
  public CharClass charClass = new Warrior(); // Komposition
}
```
