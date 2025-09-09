# 2D-spelbräden

Tvådimensionella arrayer kan fungera väldigt bra för att lagra alla sorters rutnät, till exempel tvådimensionella spelbräden.

## Skapa brädet

```csharp
// Skapar inte en lista, utan ett "rutnät" där varje position 
// inte har ett utan två index. 
// Så board[4, 5] är en annan position än board[4, 6].
int[,] board = new int[20, 10];
```

## Nästlade loopar

En nästlad loop är en loop som ligger i en annan loop. De används ofta när man vill göra något med tvådimensionella arrayer – till exempel fylla dem med information.

```csharp
for (int y = 0; y < board.GetLength(1); y++)
{
  for (int x = 0; x < board.GetLength(0); x++)
  {
    // Den inre loopen här körs en gång per unik position i 
    // den tvådimensionella arrayen, och variablerna x och y 
    // har index-värdena för den aktuella positionen.

    board[x, y] = 4; // Ändrar alla positioners värde till 4.


    // Ändrar alla positioner som är "längst till höger" i rutnätet till 2.
    if (x == 0)
    {
      board[x, y] = 2; 
    }
  }
}
```

Samma teknik används också ofta för att rita ut rutnätet till skärmen:

```csharp
for (int y = 0; y < board.GetLength(1); y++)
{
  for (int x = 0; x < board.GetLength(0); x++)
  {
    Console.Write(board[x, y]); // Ritar ut den nuvarande rutan
  }
  Console.WriteLine(); // Lägger till en radbrytning i slutet på varje utritad rad.
}
```

