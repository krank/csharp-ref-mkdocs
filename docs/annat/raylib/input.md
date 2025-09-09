# Input

## Tangentbordet

### IsKeyDown()

Tar emot en tangent som parameter; returnerar true om den angivna tangenten är nedtryckt – false om den inte är det.

Under KeyboardKey finns variabler för i princip alla tangenter på tangentbordet.

```csharp
if (Raylib.IsKeyDown(KeyboardKey.KEY_LEFT))
{
  // Kodlogik
}
```

### IsKeyUp()

Fungerar som IsKeyDown fast… tvärtom

```csharp
if (Raylib.IsKeyUp(KeyboardKey.KEY_LEFT))
{
  // Kodlogik
}
```

### IsKeyPressed()

Returnerar true om knappen tryckts ned denna frame.

```csharp
if (Raylib.IsKeyPressed(KeyboardKey.KEY_SPACE))
{
  Jump();
}
```

### IsKeyReleased()

Returnerar true om knappen släppts upp denna frame.

```csharp
  if (Raylib.IsKeyReleased(KeyboardKey.KEY_LEFT_CTRL))
  {
    FireShot(shotPower);
    shotPower = 0;
  }
```

### SetExitKey()

I vanliga fall innebär ett tryck på ESC-knappen att hela spelet avslutas. SetExitKey kan användas för att byta vilken knapp som har den funktionen – eller ta bort den helt.

```csharp
Raylib.SetExitKey(KeyboardKey.KEY_Q); // Gör så Q avslutar spelet

Raylib.SetExitKey(0); // Gör så att det inte finns någon "avsluta spelet-knapp".
```

## Musen

### GetMouseX, GetMouseY

Hämtar musens nuvarande position i form av integervärden i x- respektive y-led.

```csharp
int mouseX = Raylib.GetMouseX();
int mouseY = Raylib.GetMouseY();
```

### GetMousePosition()

Hämtar musens nuvarande position i form av en tvådimensionell [vektor](../../grundlaeggande/vektorer-numerics.md).

```csharp
Vector2 mousePos = Raylib.GetMousePosition();
```

### IsMouseButtonDown()

Anropas med en musknapp som parameter; returnerar true om den musknappen just nu är nedtryckt.

```csharp
bool leftDown = Raylib.IsMouseButtonDown(MouseButton.MOUSE_LEFT_BUTTON);
bool rightDown = Raylib.IsMouseButtonDown(MouseButton.MOUSE_RIGHT_BUTTON);
```

### IsMouseButtonPressed()

Anropas med en musknapp som parameter; returnerar true om den musknappen tryckts ned någon gång sedan förra gången metoden anropades.

```csharp
bool leftWasPressed = Raylib.IsMouseButtonPressed(MouseButton.MOUSE_LEFT_BUTTON);
```
