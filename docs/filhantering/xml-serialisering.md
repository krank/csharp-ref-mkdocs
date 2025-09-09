# XML-serialisering

Serialisering handlar om att ta ett objekt – en instans – och göra om objektet till text som kan lagras i en fil eller till exempel skickas via internet. Se nedan för ett exempel på en klass och hur en serialiserad version av klassen skulle se ut.

=== "Spaceship.cs"

	```csharp
	public class Spaceship
	{
	 public int hp = 100;
	 public int maxHp = 100;
	 public int speed = 2;
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
	

### Förberedelser <a id="h.p_-KCOwdwp8MFv"></a>

Klassen vars instanser ska kunna serialiseras måste vara public.

```csharp
public class Spaceship
{
  // Lägg som vanligt in variabler, properties, metoder etc här
}
```

Det är också enbart publika variabler samt properties med publika getters och setters som serialiseras.

För att kunna serialisera till XML behövs följande bibliotek:

```csharp
using System.IO;
using System.Xml;
using System.Xml.Serialization;
```

### XmlSerializer <a id="h.p_eJ66SSYV9KYL"></a>

För att kunna serialisera instanser till XML behövs en XML-serialiserare, specialbyggd för att serialisera instanser av just den klassen.

```csharp
XmlSerializer shipSerializer = new XmlSerializer(typeof(Spaceship));
```

Tyvärr är XmlSerializern inte skriven som en generisk klass, så istället måste man använda typeof för att meddela vilken klass det är serialiseraren ska specialisera sig på.

### Serialize

När vi har en serialiserare så kan vi använda den för att serialisera en instans av en klass.

```csharp
Spaceship myShip = new Spaceship();

FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate);

shipSerializer.Serialize(file, myShip);

file.Close();
```

Resultatet av denna kod blir att XML-koden längre upp på den här sidan sparas ner i ship.xml.

Samma kod kan skrivas så här:

```csharp
Spaceship myShip = new Spaceship();

using (FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate))
{
  shipSerializer.Serialize(file, myShip);
}
```

### Deserialize

När det finns serialiserad data i en XML-fil så kan man också använda serialiseraren för att deserialisera datan, dvs skapa en ny instans av klassen och fylla den med datan från XML-filen.

```csharp
Spaceship myShip;

using (FileStream file = File.Open(@"ship.xml", FileMode.OpenOrCreate))
{
  myShip = (Spaceship) shipSerializer.Deserialize(file);
}
```

Eftersom serializern inte är skriven som en generisk klass så måste vi aktivt casta det Deserialize returnerar till den klass vi vill att det ska vara \(och vet att det borde vara\), i det här fallet Spaceship.

### XML-serialisering av samlingar \(arrayer, listor\) <a id="h.p_ehRsopTS-8jm"></a>

Det går utmärkt att serialisera även listor.

```csharp
List<Spaceship> fleet = new List<Spaceship>();

fleet.Add(new Spaceship());
fleet.Add(new Spaceship());
fleet.Add(new Spaceship());

XmlSerializer fleetSerializer = new XmlSerializer(typeof(List<Spaceship>));

FileStream file = File.Open(@"fleet.xml", FileMode.OpenOrCreate);

shipSerializer.Serialize(file, fleet);

file.Close();
```

Precis som med andra variabler och properties så kommer publika samlingar av instanser som lagrats i en instans också serialiseras.

=== "Fleet.cs"

	```csharp
	public class Fleet
	{
	  public List<Spaceship> ships = new List<Spaceship>();
	}
	```
	

=== "Fleet.xml"

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
	



