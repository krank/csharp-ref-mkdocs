# Geometriska former

## Rektanglar

### DrawRectangle()

```csharp
Raylib.DrawRectangle(10, 10, 30, 40, Color.ORANGE);
```

Parametrarna är, i tur och ordning: X- och Y-position för rektangelns övre vänstra hörn, rektangelns bredd och höjd, och dess färg.

### DrawRectangleLines(), DrawCircleLines()

Fungerar precis som DrawCircle respektive DrawRectangle, men använder färgen för att rita ut respektive forms kanter istället för att fylla dem.

```csharp
Raylib.DrawCircleLines(150, 200, 40, Color.MAGENTA);
```

### DrawRectangleRec()

Fungerar precis som DrawRectangle, men tar emot ett [Rectangle](rectangle.md)-objekt istället för koordinater och bredd/höjd.

```csharp
Rectangle r1 = new Rectangle(10,5,30,15);
Raylib.DrawRectangleRec(r1, Color.PINK);
```

## Cirklar och elipser

### DrawCircle()

```csharp
Raylib.DrawCircle(150, 200, 40, Color.MAGENTA);
```

Parametrarna är, i tur och ordning: X- och Y-position för cirkelns mitt, cirkelns radie, och cirkelns färg.

### DrawCircleV()

Ritar en cirkel men använder en [Vector2 ](../../grundlaeggande/vektorer-numerics.md#vector2)som mittpunkt.

```csharp
Vector2 midPoint = new Vector2(100, 100);
Raylib.DrawCircleV(midPoint, 40, Color.PINK);
```

### DrawCircleSector()

Ritar en del av en cirkel.

```csharp
Vector2 midPoint = new Vector2(100, 100);
Raylib.DrawCircleSector(midPoint, 50, 0, -45, 100, Color.PINK);
```

Parametrarna är alltså mittpunkten, radien, startgraden, slutgraden, antalet segment som ska ritas ut samt färgen. Graderna utgår från att noll är rakt nedåt, och räknar motsols(!). Med andra ord är 0 nedåt, 90 är rakt åt höger och −90 är rakt åt vänster.

### DrawEllipse()

Ritar ut en ellips. Parametrarna är mittpunktens x- och y-värde, den horisontella radien och den vertikala radien.

```csharp
Raylib.DrawEllipse(100, 250, 50, 200, Color.PINK);
```

## Andra former

### DrawTriangle()

Ritar ut en triangel. Parametrarna är triangelns tre hörn som [Vector2](../../grundlaeggande/vektorer-numerics.md#vector2) samt den färg triangeln ska ha.

```csharp
Vector2 top = new Vector2(150, 100);
Vector2 bottomLeft = new Vector2(100, 150);
Vector2 bottomRight = new Vector2(200, 150);

Raylib.DrawTriangle(top, bottomLeft, bottomRight, Color.GRAY);
```

!!! info

	**OBSERVERA:** Ange vektorerna i _motsols ordning_.
	

### DrawPoly()

Ritar en polygon. Parametrarna är mittpunkten, antalet sidor, radien, rotationen och färgen.

```csharp
Raylib.DrawPoly(centerPoint, 7, 64, 0, Color.GREEN);
```

## Linjer

### DrawLine()

Ritar en linje mellan två punkter. Parametrarna är startpunktens x- och y-värden och slutpunktens x- och y-värde, samt färgen.

```csharp
Raylib.DrawLine(10, 10, 10, 20, Color.PINK);
```

### DrawLineV()

Ritar en linje mellan två punkter. Parametrarna är en [vektor2 ](../../grundlaeggande/vektorer-numerics.md#vector2)för startpunkten, en vektor2 för slutpunkten, samt färgen.

```csharp
  Vector2 start = new Vector2(10,10);
  Vector2 end = new Vector2(10,20);

  Raylib.DrawLineV(start, end, Color.RED);
```

### DrawLineEx()

Precis som DrawLineV fast med en extra parameter: tjockleken.

```csharp
Raylib.DrawLineEx(start, end, 10, Color.GREEN);
```

### DrawLineBezierQuad()

Rita en böjd linje. Funkar som DrawLineEx, men med en extra parameter: en punkt som linjen böjer sig mot.

```csharp
  Vector2 start = new Vector2(10,10);
  Vector2 end = new Vector2(100,100);
  Vector2 control = new Vector2(200, 10);

  Raylib.DrawLineBezierQuad(start, end, control, 5, Color.GREEN);
```

