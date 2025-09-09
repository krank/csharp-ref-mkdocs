# Loopar

## while-loop

Fungerar och ser ut som en [if-sats](if-satser.md) utom att körningen inte fortsätter när kodblocket körts, utan "hoppar upp" till kriteriet och testar det igen.

Precis som med if-satserna ska det som är mellan paranteserna vara kod som ger [boolskt](datatyper/#bool) resultat t.ex. en [jämförelse ](operatorer.md#boolska)eller en metod som [returnerar ](egna-metoder.md#returnering)ett boolskt värde.

While-loopar används när man **inte vet** hur många gånger loopen ska köras. Till exempel:

{% code lineNumbers="true" %}
```csharp
string name = "";

// Körs så många gånger som behövs för att 
// användaren ska förstå att hen ska skriva "Micke"
while (name != "Micke")
{
  Console.WriteLine("Skriv ditt namn:")
  name = Console.ReadLine();
}
```
{% endcode %}

## for-loop

Fungerar som en while-loop men har alltid en räknare – bra när man vill göra något ett visst antal gånger. Samlar deklaration av räknare, kriterie för att fortsätta loopa och förändring av räknarens värde på samma ställe.

{% code lineNumbers="true" %}
```csharp
// i är räknarvariabeln, vars värder börjar på 0
// i < 10 är villkoret; så länge det utvärderas som sant fortsätter loopen köras
// i++ körs i slutet av varje iteration, och betyder att i ökar med 1 varje gång

for (int i = 0; i < 10; i++)
{
  Console.WriteLine(i);
}
```
{% endcode %}

For-loopar används när man **vet** hur många gånger loopen ska köras – åtminstone när man når den. Så länge en räknare ska användas fungerar en for-loop bra.

## foreach-loop

Foreach-loopar är i princip likadana som for-loopar men är specialdesignade för att gå igenom listor och arrayer. En foreach-loop körs lika många gånger som det finns saker i en lista/array, och varje gång loopen körs så lagras en av sakerna i variabeln som anges.

Nackdelen jämfört med en for-loop är att man inte får ut vilket index (plats i listan/arrayen) respektive sak har. Behöver man skriva ut index eller använda det på något vis är därför for-loop ett bättre val.

{% code lineNumbers="true" %}
```csharp
string[] choices = {"Start", "Options", "Quit"};

foreach (string choice in choices)
{
  Console.WriteLine(choice);
}
```
{% endcode %}
