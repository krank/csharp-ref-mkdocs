# Begränsa input

Om man vill att en användare ska få välja mellan två eller flera olika alternativ i en konsollapplikation, eller vill begränsa användarens input på något annat sätt så kan man använda en loop:

```csharp
string answer = ""; // Skapa en tom svarsvariabel

// Loopa så länge svar varken är a eller b
while (answer != "a" && answer != "b")
{
  Console.Write("Välj a eller b:");
  
  // Hämta in ett nytt värde för svar
  answer = Console.ReadLine();
  
  // Om svaret inte var a eller b, skriv ut ett felmeddelande
  if (answer != "a" && answer != "b")
  {
    Console.WriteLine("Du måste välja a eller b");
  }
}
```

Villkoret i loopen kan givetvis vara vad som helst - fundera ut vilka krav du vill ställa på användarens input och omvandla detta krav till en boolesk sats.

Om man bara vill göra sin jämförelse en gång så kan man använda en bool-variabel.

```csharp
string answer = "";

bool validAnswer = false;

while (!validAnswer)
{
  Console.Write("Välj a eller b:");
  
  answer = Console.ReadLine();
  
  validAnswer = answer == "a" || answer == "b";
  
  if (!validAnswer)
  {
    Console.WriteLine("Du måste välja a eller b");
  }
}
```

Vill man vara lite mer avancerad kan man använda en [lista ](../grundlaeggande/listor-och-arrayer.md#list)med giltiga svar:

```csharp
string answer = "";

List<string> validAnswers = new List<string>{"a", "b", "c"}
bool validAnswer = false;

while (!validAnswer)
{
  Console.Write($"Välj [{ String.Join(",", validAnswers) }]: ");
  
  answer = Console.ReadLine();
  
  // Blir true om svaret finns i arrayen
  validAnswer = validAnswers.Contains(answer);
  
  if (!validAnswer)
  {
    Console.WriteLine($"Du måste välja en av { String.Join(",", validAnswers) }!");
  }
}
```
