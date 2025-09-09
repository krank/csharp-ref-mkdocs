# Serialisering \[…]

[JSON-serialisering](json-serialisering.md) | [XML-serialisering](xml-serialisering.md)

Serialisering handlar om att ta ett objekt – en [instans ](../../klasser-och-objektorientering/klasser-och-instanser.md)– och göra om objektet till ren text (s.k. "plain text") som kan lagras i en fil eller till exempel skickas via internet.

För att den rena texten sen ska kunna avläsas (deserialiseras) tillbaka till ett objekt i andra änden så behöver man vara överens om ett format. JSON är idag ett av de absolut vanligaste, och XML är också förekommande.

Se nedan för ett exempel på en klass och hur en instans av klassen skulle se ut om man serialiserade den till JSON respektive XML.

=== "Spaceship.cs"

	```csharp
	public class Spaceship
	{
	 public int Hp {get; set;} = 100;
	 public int MaxHp {get; set;} = 100;
	 public int Speed {get; set;} = 2;
	}
	```
	

=== "Spaceship.json"

	```javascript
	{
	  "Hp": 100,
	  "MaxHp": 100,
	  "Speed": 2
	}
	```
	

=== "Spaceship.xml"

	```markup
	<?xml version="1.0"?>
	<Spaceship xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	           xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	 <hp>100</hp>
	 <maxHp>100</maxHp>
	 <speed>2</speed>
	</Spaceship>
	```
	

