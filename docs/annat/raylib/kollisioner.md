# Kollisioner

## CheckCollisionRecs()

Tar emot två [Rectangles ](rectangle.md)som parametrar och returnerar true om de överlappar, false om de inte gör det.

```csharp
Rectangle playerRect = new Rectangle(5,5,10,10);
Rectangle enemyRect = new Rectangle(10,10,10,10);

bool areOverlapping = Raylib.CheckCollisionRecs(playerRect, enemyRect); // true
```

## GetCollisionRec()

Tar emot två [Rectangles](rectangle.md) som parametrar och returnerar en Rectangle som motsvarar överlappet mellan dem.

```csharp
Rectangle playerRect = new Rectangle(50,50,100,100);
Rectangle enemyRect = new Rectangle(100,100,100,100);
Rectangle overlap = Raylib.GetCollisionRec(playerRect, enemyRect);

Raylib.DrawRectangleRec(playerRect, Color.RED);
Raylib.DrawRectangleRec(enemyRect, Color.BLUE);
Raylib.DrawRectangleRec(overlap, Color.ORANGE);
```

![](../../images/image-7.png) 

## CheckCollisionCircles()

Tar emot två [vektorer ](../../grundlaeggande/vektorer-numerics.md)som beskriver två cirklars mittpunkter, och två floats som beskriver cirklarnas radie, och returnerar true om de överlappar, false om de inte gör det.

```csharp
Vector2 playerPos = new Vector2(10,10);
Vector2 enemyPos = new Vector2(20,20);

// true
bool areOverlapping = Raylib.CheckCollisionCircles(playerPos, 10, enemyPos, 15);
```

## CheckCollisionCircleRec()

Tar emot en positions[vektor](../../grundlaeggande/vektorer-numerics.md) och en radie för en cirkel, och en [Rectangle](rectangle.md). Returnerar true om rektangeln och cirkeln överlappar varandra, false om de inte gör det.

```csharp
Rectangle playerRect = new Rectangle(5,5,10,10);
Vector2 enemyPos = new Vector2(20,20);

// true
bool areOverlapping = Raylib.CheckCollisionCircleRec(enemyPos, 15, playerRect);
```

## CheckCollisionPointRec()

Tar emot en punkt i form av en positions[vektor](../../grundlaeggande/vektorer-numerics.md) samt en [Rectangle](rectangle.md). Returnerar true om punkten befinner sig inuti rektangeln, false om den inte gör det.

```csharp
Rectangle enemyRect = new Rectangle(10,10,10,10);

mousePos = Raylib.GetMousePosition();

bool areOverlapping = Raylib.CheckCollisionPointRec(mousePos, enemyRect))
```
