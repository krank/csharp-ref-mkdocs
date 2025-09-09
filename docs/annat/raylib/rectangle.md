# Rectangle

Rectangle är en datatyp som beskriver rektanglar. De kan användas både för att rita ut rektanglar på skärmen och för att [kolla kollisioner](kollisioner.md).

```csharp
// Skapar två rektanglar
Rectangle r1 = new Rectangle(10,10,50,20);
Rectangle r1 = new Rectangle(5,5,50,20);

// Ritar ut en rektangel
Raylib.DrawRectangleRec(r1, Color.SKYBLUE);

// Kollar ifall två rektanglar överlappar varandra
bool isColliding = Raylib.CheckCollisionRecs(r1, r2);
```

Man kan ändra på en rektangels egenskaper i efterhand.

```csharp
r1.X += 3;
r1.Y = 90;
r1.Width = 50;
r1.Height = 30;
```

## Rectangle och List

Rectangles är inte [klasser](../../klasser-och-objektorientering/klasser-och-instanser.md) – de är Structs. Det betyder att om man lagrar rectangles i en lista, så kan man inte ändra rektanglarna direkt i listan.

```csharp
List<Rectangle> rects = new List<Rectangle>();

rects.Add(new Rectangle());
rects.Add(new Rectangle());
rects.Add(new Rectangle());
rects.Add(new Rectangle());

// SÅHÄR KAN MAN INTE GÖRA
rects[1].X = 5;

// GÖR SÅHÄR ISTÄLLET
Rectangle tmp = rects[1];
tmp.X = 5;
rects[1] = tmp;
```

