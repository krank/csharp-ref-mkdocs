# Länkade listor och andra strukturer

## Länkade listor

Fördelar med en länkad lista jämfört med arrayer:

* Som en List behöver man inte definiera storleken från början.
* Det går ganska snabbt att lägga in något nytt i mitten, eller ta bort det.
* Förstår man länkade listor så blir det väldigt lätt att sedan skapa andra strukturer såsom träd eller nätverk.

Nackdelar:

* Mycket jobbiga att sortera.
* Jobbigt att läsa av en specifik position.

### Hur det funkar

En länkad lista består av **noder**. Varje nod innehåller (minst) ett **värde** samt en **pekare** till nästa nod. Det finns ingen samling av alla noder någonstans; allt som finns är pekaren från en nod till en annan.

 

![](../images/image-20.png)

=== "Node.cs"

	```csharp
	class Node
	{
	  public int value = 0; // Kan såklart göras generisk för mer flexibilitet.
	  public Node nextNode;
	}
	```
	

**Program.cs**

=== "Program.cs"

	```csharp
	static void Main(string[] args)
	{
	  Node firstNode = new Node();
	  firstNode.value = 3;
	  Node currentNode = firstNode;
	
	  // Lägg till 10 noder till den länkade listan
	  for (int i = 0; i < 10; i++)
	  {
	    firstNode.nextNode = new Node();
	    currentNode = firstNode.nextNode;
	    currentNode.value = 10 - i;
	  }
	
	  // Stoppa in en nod mellan den första och den andra
	  Node newNode = new Node();
	  newNode.value = 9;
	  newNode.nextNode = firstNode.nextNode;
	  firstNode.nextNode = newNode;
	}
	```
	

## Tvåvägs länkade listor, träd och nätverk

Flera pekare kan peka på samma objekt. Det gör att man kan skapa mer komplexa strukturer.

### Tvåvägs

![](../images/image-21.png)

=== "Node.cs"

	```csharp
	class Node
	{
	  public int value = 0;
	  public Node nextNode;
	  public Node prevNode;
	}
	```
	

### Träd

![](../images/image-22.png)

=== "Node.cs"

	```csharp
	class Node
	{
	  public int value = 0;
	  public List<Node> children = new List<Node>();
	}
	```
	

### Nätverk

![](../images/image-23.png)

=== "Node.cs"

	```csharp
	class Node
	{
	  public int value = 0;
	  public List<Node> connections = new List<Node>();
	}
	```
	
