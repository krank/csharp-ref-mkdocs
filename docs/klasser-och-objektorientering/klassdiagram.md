# Klassdiagram

Ett klassdiagram beskriver hur en klass är strukturerad, och ser likadant ut oavsett programmeringsspråk. Diagrammet här skulle t.ex. kunna omvandlas till kod i Java, C#, PHP eller vilket annat språk som helst som har objektorientering.

I ett klassdiagram beskrivs klassen i tre sektioner:

* Klassnamnet — i det här fallet "Character".
* Variabler — i det här fallet hp och name.
* Metoder — i det här fallet Hurt och Attack.

**Variablerna:** Skrivs med namn och datatyp, men aldrig värde. Oftast skriver man namnet först, sedan kolon, och slutligen datatypen.

**Metoderna:** Skrivs med namn, parametrar och returtyp, men aldrig funktion. Oftast skriver man namnet först, sedan parametrarna inom parentes (i samma form som man skrev variablerna), och slutligen vilken datatyp metoden returnerar.

**Synlighet:** Man anger synlighet för variabler och metoder genom att skriva +, - eller # innan namnet.

* \+ betyder "public"
* − betyder "private"
* \# betyder "protected"&#x20;

```mermaid
%%{init: {'theme': 'base', 'themeVariables': 
{ 'primaryBorderColor': 'black', 
'primaryColor': 'white'
}}}%%

classDiagram
  class Character{
        −_hp : int
        −_name : string 
        +  Hurt(amount : int) void
        + Attack() int
  }
```

## Arv i klassdiagram

För att visa [arv ](arv.md)i klassdiagram används pilar.

Pilarna pekar alltid FRÅN subklassen TILL basklassen. Man kan tänka sig att pilen betyder "är en sorts" eller "ärver från".

Subklassernas diagram ritas på samma sätt som basklassens. Man skriver in klassens variabler och metoder, inklusive metoder som använder [override](polymorfism/virtual-override.md). Däremot skriver man inte in variabler eller metoder som bara ärvs från basklassen.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': 
{ 'primaryBorderColor': 'black', 
'primaryColor': 'white'
}}}%%

classDiagram
  class Character{
        −_hp : int
        −_name : string 
        +Hurt(amount : int) void
        +Attack() int
  }
  class Hero{
        −_xp : int
        +GetLevel() int
  }
  Character <|-- Hero
```

## Komposition i klassdiagram

För att visa komposition i klassdiagram används en pil som avslutas i en romb.

Rombpilarna pekar alltid FRÅN del-klassen TILL huvud-klassen. Man kan tänka sig att pilen betyder "ingår i", så att den ena klassen "ingår i" den andra klassen.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': 
{ 'primaryBorderColor': 'black', 
'primaryColor': 'white'
}}}%%

classDiagram
  class Character{
        −_hp : int
        −_name : string 
        -_weapon : Weapon
        +Hurt(amount : int) void
        +Attack() int
  }
  class Weapon{
        −minDamage : int
        −maxDamage : int
        +Attack(target: Character) void
  }
  Character o-- Weapon
```

### Överkurs

Ibland görs skillnad mellan _komposition_ och _aggregering_. Skillnaden är då att man med komposition menar att de kopplade klasserna bara finns i huvudklassen och är integrerade delar av den – relationen är inte bara "ingår i" utan "är en del av". Aggregering är då namnet man ger den lösare typen av koppling.

```mermaid
%%{init: {'theme': 'base',
'themeVariables': 
{ 'primaryBorderColor': 'black', 
'primaryColor': 'white'
}}}%%

classDiagram
  class Character{
        −_hp : int
        −_name : string 
        +Hurt(amount : int) void
        +Attack() int
  }
  class Inventory{
        −_item: List<Item>
        +Add(item: Item)
        +Remove(item: Item)
  }
  class Weapon{
        −minDamage : int
        −maxDamage : int
        +Attack(target: Character) void
  }
  Character o-- Weapon
  Character *-- Inventory

```

## Vanliga frågor

* **Har man med variablers värde?** Nej, bara datatyp, namn och access modifier (public, private, protected)
* **Har man med metoders innehåll?** Nej, bara datatyp (returtyp), namn, parametrar (med namn och datatyp) och access modifier.
* **Hur gör man med listor?** Precis som vanligt, en int-listas datatyp skrivs som "List&lt;int>".
* **Hur gör man med properties?** Man kan lista dem som vanliga klassvariabler. NClass visar dem i metod-sektionen, kompletta med get och set. Det är också helt OK.

## NClass

NClass är ett enkelt program för att skapa klassdiagram. Det är gratis och [kan laddas ner här](https://github.com/gbaychev/NClass/releases).

!!! info

	**Observera:** Länken leder till en ny fork av den gamla versionen av NClass. Den nya verkar utvecklas aktivt och har t.ex. stöd för Ctrl+Z och nyare projekt i sin code generation (Visual Studio 2019… Fortfarande inte Dotnet 5/6 tyvärr)
	
