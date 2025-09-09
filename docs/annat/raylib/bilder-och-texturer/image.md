# Image

En Image är en bild som är sparad i datorns arbetsminne, och kan manipuleras på olika sätt.

För att man ska kunna rita ut den till fönstret behöver man sedan konvertera den till en [texture](image.md#texture). Det gör man genom [LoadTextureFromImage](image.md#loadtexturefromimage).

## Width och height

Varje image har en width och en height.

```csharp
Console.WriteLine($"Width: {filebasedImage.Width});
Console.WriteLine($"Height: {filebasedImage.Height});

Rectangle hitBox = new Rectangle(0, 0, filebasedImage.Width, filebasedimage.Height);
```

## Skapa eller ladda in

### LoadImage()

Läser in en bildfil från hårddisken och lagrar den i minnet som en Image.

**OBS!** bilden måste ligga i samma mapp som Program.cs-filen!

```csharp
Image filebasedImage = Raylib.LoadImage(@"hero.png");
```

### LoadImageFromTexture()

Läser in en bildfil från en textur och lagrar den i minnet som en Image.

```csharp
Image goombaImage = Raylib.LoadImageFromTexture(goombaTexture);
```

Detta är alltså motsatsen till [LoadTextureFromImage()](texture.md#loadtexturefromimage).

### LoadImageFromScreen()

Kopierar det som just nu syns i fönstret.

```csharp
Image screenshot = Raylib.LoadImageFromScree();
```

### GenImageColor()

Skapar en ny blank image i minnet, fylld av den angivna färgen.

```csharp
// Skapar en svart bild som är 200x200 pixlar.
Image blackImage = Raylib.GenImageColor(200, 200, Color.BLACK);

// Skapar en röd bild som är 200x200 pixlar.
Image redImage = Raylib.GenImageColor(200, 200, Color.RED);
```

## Redigera

De flesta metoder här använder nyckelordet [ref ](../../../grundlaeggande/reference-vs-value-types.md#out-och-ref)för att ange att den bild man stoppar in som parameter inte returneras i förändrad form, utan ändras på plats i minnet.

### ImageDrawPixel()

Ändrar färg på en pixel i en Image.

```csharp
// Ändrar pixeln som är 20 pixlar från vänsterkanten och 15 från 
// toppen av bilden till att bli blå
Raylib.ImageDrawPixel(ref targetImage, 20, 15, Color.BLUE);
```

### ImageDrawCircle()

Fungerar som [DrawCircle()](../geometriska-former.md#drawcircle).

```csharp
Raylib.ImageDrawCircle(ref targetImage, 150, 200, 40, Color.MAGENTA);
```

### ImageDrawRectangle()

Fungerar som [DrawRectangle()](../geometriska-former.md#drawrectangle).

```csharp
Raylib.ImageDrawRectangle(ref targetImage, 10, 10, 30, 40, Color.ORANGE);
```

### ImageDrawRectangleRec()

Fungerar som [DrawRectangleRec()](../geometriska-former.md#drawrectanglerec).

```csharp
Rectangle r1 = new Rectangle(10,5,30,15);
Raylib.ImageDrawRectangleRec(ref targetImage, r1, Color.PINK);
```

### ImageDrawText()

Fungerar som [DrawText()](../text.md#drawtext).

```csharp
Raylib.ImageDrawText(ref targetImage, "Hello World", 100, 50, 20, Color.ORANGE);
```

### ImageDrawTextEx()

Fungerar som [DrawTextEx()](../text.md#drawtextex).

```csharp
Raylib.DrawTextEx(ref targetImage, f1, "Hello", new Vector2(20, 15), 40,0,Color.BLACK);
```

### GetImageColor()

Läser av färgen på en specifik pixel.

```
// Hämtar färgen från x: 53, y: 17 i bilden redImage.
Color c = Raylib.GetImageColor(redImage, 53, 17);
```

### ImageFlipHorizontal()

Flippar en Image horisontellt (spegelvänder).

```csharp
Raylib.ImageFlipHorizontal(ref targetImage);
```

### ImageFlipVertical()

Flippar en Image vertikalt.

```csharp
Raylib.ImageFlipVertical(ref targetImage);
```

### ImageResize/ImageResizeNN()

Ändrar storlek på en bild. NN-versionen ger ett skarpt resultat vilket fungerar bra för pixelart som skalas med jämna multiplikationer.

```csharp
//Ändrar storleken på bilden "someImage" till 400x400 pixlar
Raylib.ImageResize(ref targetImage, 400, 400);

//Ändrar storleken på bilden "pixelartImage" till dubbla dess nuvarande storlek
RayLib.ImageResizeNN(ref pixelartImage, pixelartImage * 2, pixelartImage * 2);
```

## Spara till hårddisken

### ExportImage

Sparar en Image till hårddisken, som en png-bild.

```csharp
Raylib.ExportImage(sourceImage, "hello.png");
```

!!! info

	**OBS:** Filnamnet _måste_ sluta med ".png"!
	
