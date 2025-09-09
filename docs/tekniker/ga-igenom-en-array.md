# Gå igenom en array (eller lista)

I en array används index från 0 till X, där X är 1 mindre än antalet saker i arrayen. Om det finns 3 saker så finns index 0, 1 och 2.

Detta kan utnyttjas för att effektivisera kod.

Istället för att skriva:

```csharp
string[] choices = {"Start", "Options", "Quit"};
Console.WriteLine(choices[0]);
Console.WriteLine(choices[1]);
Console.WriteLine(choices[2]);
```

Så kan man skapa en loop vars räknare först är 0, sedan 1, sedan 2:

```csharp
string[] choices = {"Start", "Options", "Quit"};
int i = 0;

while (i < choices.Length)
{
  Console.WriteLine(choices[i]);
  i++;
}
```

Detta gör att även om man skulle lägga till tio nya namn till arrayen så kommer alla de nya namnen att skrivas ut tillsammans med de gamla.

Detta kan även göras med listor och givetvis fungerar en [for-loop](../grundlaeggande/loopar.md#for-loop) lika bra (om inte bättre).

```csharp
string[] choices = {"Start", "Options", "Quit"};

for (int i = 0; i < choices.length; i++)
{
  Console.WriteLine(choices[i]);
}
```

[Foreach-loopar](../grundlaeggande/loopar.md#foreach-loop) är i princip skapade för exakt det här:

```csharp
string[] choices = {"Start", "Options", "Quit"};

foreach (string choice in choices)
{
  Console.WriteLine(choice);
}
```

Denna teknik används MYCKET, till exempel för att:

* Skriva ut alla saker i en array
* Undersöka varje grej i en array och se om den stämmer överens med något man letar efter
* Ändra på varje grej i en array (t.ex. fylla den med slumptal).
