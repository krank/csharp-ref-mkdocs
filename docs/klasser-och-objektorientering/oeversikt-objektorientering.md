# Översikt objektorientering

## Objekt

Ett objekt är en samling variabler, metoder och algoritmer som "hör ihop" och motsvarar en "sak" i programmet.

_Exempel på objekt: Ett svärd, en fiende, en bok, en bana, ett päron, en kund._

## Klass

En klass är en ritning, eller en mall, för en kategori av objekt. En klass är inte i sig ett objekt, utan bara en instruktion för hur ett objekt ska se ut och fungera.

_Exempel på klasser: Svärd, fiende, bok, bana, päron, kund._

En klass fungerar också som en datatyp, så varje gång kod förväntar sig en datatyp (t.ex. string eller int) kan man istället skriva dit en klass.

[Mer om klasser.](klasser-och-instanser.md#skapa-klasser-i-visual-studio-code)

## Instans

En instans är ett _objekt_ man skapat utifrån en _klass_.

[Mer om instanser.](klasser-och-instanser.md#skapa-klasser-i-visual-studio-code)

## Klassvariabler och klassmetoder

En klassvariabel är en variabel som ingår i en klass, och en [klassmetod ](klassmetoder.md)är en metod som ingår i en klass.

Alla instanser av en klass får tillgång till alla klassens metoder och egen kopia av alla klassens variabler.

_Exempel:_

{% code title="" lineNumbers="true" %}
```csharp
class Pear
{
  public int Cost = 100; // <-- klassvariabel
  public bool Eaten = false; // <-- klassvariabel
  
  public void Eat() // <- klassmetod
  {
    eaten = true;
  }
}
```
{% endcode %}

## Arv

En klass kan [ärva ](arv.md)från en annan klass. Det betyder att subklassen får basklassens alla metoder och variabler, men den kan också lägga till egna.

Man brukar också beskriva det som att subklassen är en mer specialiserad version av basklassen – ett exempel på basklass kan vara `Weapon` och en subklass till Weapon kan då vara `Sword`. Sedan kan Sword agera basklass till `LongSword` och `ShortSword`. Relationen mellan subklass och basklass är att \[subklassen] är en sorts \[basklassen], så att ShortWord är en sorts Weapon till exempel.

Alla svärd är då vapen, och har alla metoder etc som ingår i vapen – fast de kan ha egna tillägg, och de kan också delvis fungera annorlunda (se [Polymorfism](polymorfism/)).

## Komposition

Man kan också lägga in instanser av en klass i instanser av en annan klass. Detta kallas [komposition](komposition.md).

Man brukar också beskriva det som att klassernas relation blir en _har-en-relation_. En hjälte _har ett_ vapen (klassen Hero har en Weapon-variabel som innehåller instanser av den klassen eller dess subklasser).

## Inkapsling

[Inkapsling ](inkapsling-och-properties.md)är principen att varje objekt – varje klass – ska sköta sin egen logik. Det innebär att man samlar all kod som hör ihop med ett objekt inuti metoder i objektets klass.

Det innebär också att man har så få variabler, properties och metoder som är publika. Man vill visa upp ett så litet "gränssnitt" mot resten av världen som möjligt.

Framför allt bör man, om man jobbar med inkapsling, inte ha några publika variabler. Istället används properties och metoder för att ändra på variablernas värde.

Anledningen till att man gör detta är dels för att skapa en tydlig struktur, dels minska risken att man gör fel när man skriver kod. Om det inte går att ändra på de privata variablerna direkt så kan man heller inte råka t.ex. ge dem ett felaktigt värde.

## Interaktion mellan objekt

När två objekt interagerar direkt med varandra, till exempel när data från ett objekt förs över till ett annat, eller när ett objekt stoppas in som parametervärde in i ett annat objekts metod.

{% code lineNumbers="true" %}
```csharp
Fighter hero = new Fighter();
Fighter opponent = new Fighter();

hero.Attack(opponent);
opponent.Attack(hero);
```
{% endcode %}

## Polymorfism

[Polymorfism ](polymorfism/#polymorfism-klasser-och-arv)i objektorientering är när en instans av en subklass lagras i en variabel eller t.ex. en lista vars datatyp är subklassens basklass. Så om man har subklassen Goomba som ärver från Monster, och lagrar en Goomba-instans i en Monster-variabel eller lägger in den i en Monster-lista så använder man polymorfism.

## Generiska klasser

[Generiska klasser](generiska-klasser.md) är klasser där datatypen för en eller flera variabler eller metoder inte bestämts, utan avgörs när man skapar en instans av klassen. Ett exempel på färdig generisk klass är List.
