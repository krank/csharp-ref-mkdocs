# Text

## DrawText()

Ritar ut text.

```csharp
// Ritar ut texten "Hello World" på x-position 100 och y-position 50,
// med text i storlek 20 och med orange färg.
Raylib.DrawText("Hello World", 100, 50, 20, Color.ORANGE);
```

## LoadFont()

Laddar in en typsnittsfil (ttf eller otf-format)

```csharp
Font f1 = Raylib.LoadFont(@"Metrophobic.ttf");
```

## LoadFontEx()

Laddar in en typsnittsfil (ttf eller otf-format) med extra parametrar

```csharp
// Ladda in typsnittsfilen Lato-Regular.ttf, i storleken 36.
//  Vi anger null eftersom vi inte vill ange exakt vilka tecken som ska laddas in.
//  VI anger -1 eftersom vi inte vill ange ett maxantal tecken att ladda in.
Font f2 = Raylib.LoadFontEx(@"Lato-Regular.ttf", 36, null, -1);
```

## DrawTextEx()

Mer avancerad variant av DrawText, som använder Vector2 för positionering och tillåter att man anger typsnitt. Kräver att man lagt in `using System.Numerics;` högst upp.

```csharp
// Ritar ut texten "Hello" på x- position 20 och y-position 15,
// i storlek 40, utan något extra mellanrum mellan bokstäverna, med svart färg.
Raylib.DrawTextEx(f1, "Hello", new Vector2(20,15), 40,0,Color.BLACK);
```
