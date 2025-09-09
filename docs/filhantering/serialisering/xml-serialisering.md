# XML-serialisering

## Bibliotek

Lägg till dessa using-statements:

{% code lineNumbers="true" %}
```csharp
using System.Xml.Serialization;
using System.IO;
```
{% endcode %}

## Klassdesign

Klassen vars instanser ska kunna serialiseras måste vara public.

{% code title="Spaceship.cs" lineNumbers="true" %}
```csharp
public class Spaceship
{
  // Lägg som vanligt in variabler, properties, metoder etc här
}
```
{% endcode %}

Det är också enbart publika variabler samt properties med publika getters och setters som serialiseras.

Om du ska deserialisera XML-kod som du får från något annat ställe och inte designat själv, så behöver du vara noga med att matcha namnet på dina publika variabler/[properties ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)mot XML-filens. Serialiseringsprocessen är dock inte känslig vad gäller stora och små bokstäver.

=== "Spaceship.cs"

	{% code lineNumbers="true" %}
	```csharp
	public class Spaceship
	{
	 public int Hp {get; set;} = 100;
	 public int MaxHp {get; set;} = 100;
	 public int Speed {get; set;} = 2;
	}
	```
	{% endcode %}
	

=== "Spaceship.xml"

	{% code lineNumbers="true" %}
	```markup
	<?xml version="1.0"?>
	<Spaceship xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	           xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	 <hp>100</hp>
	 <maxHp>100</maxHp>
	 <speed>2</speed>
	</Spaceship>
	```
	{% endcode %}
	

## XmlSerializer

För att kunna serialisera instanser till XML behövs en XML-serialiserare, specialbyggd för att serialisera instanser av just den klassen.

```csharp
XmlSerializer shipSerializer = new XmlSerializer(typeof(Spaceship));
```

Tyvärr är XmlSerializern inte skriven som en generisk klass, så istället måste man använda typeof för att meddela vilken klass det är serialiseraren ska specialisera sig på.

## Serialize()

När vi har en serialiserare så kan vi använda den för att serialisera en instans av en klass.

Beroende på om man vill ha ut XML-koden till en string eller till en fil behövs en StringWriter eller en FileStream.

=== "StringWriter"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip = new Spaceship();
	
	StringWriter textWriter = new StringWriter();
	
	shipSerializer.Serialize(textWriter, myShip);
	
	textWriter.Close();
	```
	{% endcode %}
	

=== "FileStream"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip = new Spaceship();
	
	FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate);
	
	shipSerializer.Serialize(file, myShip);
	
	file.Close();
	```
	{% endcode %}
	

Resultatet av denna kod blir att XML-koden längre upp på den här sidan sparas ner i ship.xml.

Samma kod kan skrivas så här, med hjälp av ett [using-statement](../open-close-using.md#using):

=== "StringWriter"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip = new Spaceship();
	
	using (StringWriter textWriter = new StringWriter())
	{
	  shipSerializer.Serialize(textWriter, myShip);
	}
	```
	{% endcode %}
	

=== "FileStream"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip = new Spaceship();
	
	using (FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate))
	{
	  shipSerializer.Serialize(file, myShip);
	}
	```
	{% endcode %}
	

## Deserialize()

Serialiseraren kan också användas för att omvandla XML-text till en instans av klassen.

Beroende på om XML-koden finns i en string eller till en fil behövs en StringReader eller en FileStream.

=== "StringReader"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip; // Variabeln resultatet lagras i
	
	// xmlText är en variabel som innehåller XML-data
	StringReader textReader = new StringReader(xmlText);
	
	myShip = (Spaceship) shipSerializer.Deserialize(textReader);
	
	textReader.Close();
	```
	{% endcode %}
	

=== "FileStream"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip; // Variabeln resultatet lagras i
	
	// ship.xml är en fil som innehåller XML-data
	FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate);
	
	myShip = (Spaceship) shipSerializer.Deserialize(textReader);
	
	file.Close();
	```
	{% endcode %}
	

Eftersom serializern inte är skriven som en generisk klass så måste vi aktivt casta det Deserialize returnerar till den klass vi vill att det ska vara (och vet att det borde vara), i det här fallet Spaceship.

Samma kod kan skrivas så här, med hjälp av ett [using-statement](../open-close-using.md#using):

=== "StringReader"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip;
	
	using (StringReader textReader = new StringReader(xmlText))
	{
	  myShip = (Spaceship) shipSerializer.Deserialize(textReader);
	}
	```
	{% endcode %}
	

=== "FileStream"

	{% code lineNumbers="true" %}
	```csharp
	Spaceship myShip;
	
	using (FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate))
	{
	  myShip = (Spaceship) shipSerializer.Deserialize(textReader);
	}
	```
	{% endcode %}
	

## XML-serialisering av samlingar (arrayer, listor)

Det går utmärkt att serialisera även listor.

{% code lineNumbers="true" %}
```csharp
List<Spaceship> fleet = new List<Spaceship>();

fleet.Add(new Spaceship());
fleet.Add(new Spaceship());
fleet.Add(new Spaceship());

XmlSerializer fleetSerializer = new XmlSerializer(typeof(List<Spaceship>));

using (FileStream file = File.Open(@"fleet.xml", FileMode.OpenOrCreate))
{
  shipSerializer.Serialize(file, fleet);
}
```
{% endcode %}

Precis som med andra variabler och properties så kommer publika samlingar av instanser som lagrats i en instans också serialiseras.

=== "Fleet.cs"

	{% code lineNumbers="true" %}
	```csharp
	public class Fleet
	{
	  public List<Spaceship> ships = new List<Spaceship>();
	}
	```
	{% endcode %}
	

=== "Fleet.xml"

	{% code lineNumbers="true" %}
	```markup
	<?xml version="1.0"?>
	<Fleet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	       xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	 <ships>
	   <Spaceship>
	     <hp>100</hp>
	     <maxHp>100</maxHp>
	     <speed>2</speed>
	   </Spaceship>
	   <Spaceship>
	     <hp>100</hp>
	     <maxHp>100</maxHp>
	     <speed>2</speed>
	   </Spaceship>
	 </ships>
	</Fleet>
	```
	{% endcode %}
	

