# Game states

Game states, eller state machines, är ett enkelt sätt att låta ditt spel, eller objekt i ditt spel, vara mer dynamiska.

Ett grundläggande exempel på game states:

```csharp
bool gameContinues = true;

int currentRoom = 0;

while (gameContinues == true)
{
  if (currentRoom == 0)
  {
    Console.WriteLine("You are in room #0. Go to which room?");
    string whatRoom = Console.ReadLine();
    if (whatRoom == "1")
    {
      currentRoom = 1;
    }
  }
  else if (currentRoom == 1)
  {
    // Kod för rum 1
  }
  else if (currentRoom == 2)
  {
    // Kod för rum 2
  }
}
```

Varje gång loopen körs, så kollar spelet vilket rum spelaren är i just den här "vändan", och kör den koden. I koden för varje rum lägger man in kod som kan ändra vilket rum som är "current". Så om man skriver "1" i det första rummet så kommer man, nästa gång loopen körs, att hamna i rum 1.

!!! info

	**TIPS:** Man kan använda en [enum ](../grundlaeggande/datatyper/enum.md)för sina rum istället för en int.
	

