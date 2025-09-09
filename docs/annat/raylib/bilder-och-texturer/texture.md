# Texture

En Texture är en bild som är sparad i grafikkortets minne, och är redo att ritas ut på skärmen. Man kan skapa en Texture utifrån en [Image ](image.md)eller läsa in en bildfil från hårddisken direkt.

## Width och height

Varje texture har en width och en height.

```csharp
Console.WriteLine($"Width: {goombaTexture.Width});
Console.WriteLine($"Height: {goombaTexture.Height});

Rectangle hitBox = new Rectangle(0, 0, goombaTexture.Width, goombaTexture.Height);
```

## Läsa in

### LoadTexture()

Läser in en bildfil och skapar en texture direkt från den.

```csharp
Texture2D goombaTexture = Raylib.LoadTexture(@"goomba.png");
```

### LoadTextureFromImage()

Skapar en ny texture baserat på en [Image](texture.md#image).

```csharp
Texture2D heroTexture = Raylib.LoadTextureFromImage(originalImage);
```

Detta är alltså motsatsen till [LoadImageFromTexture()](image.md#loadimagefromtexture).

## Rita ut till skärmen

### DrawTexture()

Ritar ut en texture till fönstret.

```csharp
// Ritar texturen heroTexture till fönstret, på x-position 40 och 
// y-position 300, utan infärgning (WHITE färgar inte)
Raylib.DrawTexture(heroTexture, 40, 300, Color.WHITE)
```

### DrawTextureEx()

Ritar ut en texture till fönstret, med andra parametrar: En [Vector2 ](../../../grundlaeggande/vektorer-numerics.md#vector2)för att ange x och y-positionen den ska ritas ut på, och floats som anger rotation och skalning av texturen.

Rotationen anges i grader och skalningen i decimalform.

```csharp
// Ritar texturen heroTexture till fönstret, på x-position 40 och 
// y-position 300, utan infärgning (WHITE färgar inte)
// Använd skalning 0.5 och rotation 0.
Vector2 position = new Vector2(40, 300);
Raylib.DrawTexture(heroTexture, position, 0, 0.5f, Color.WHITE)
```

!!! info

	**OBSERVERA:** För att kunna använda [Vector2 ](../../../grundlaeggande/vektorer-numerics.md)så måste du lägga in detta bland dina using-statements:
	
	```csharp
	using System.Numerics;
	```
	

### DrawTextureRec()

Ritar ut en del av en texture till fönstret. Fungerar som DrawTextureEx men utan rotationen och skalan, och med en rektangel som säger vilken del av texturen man vill klippa ut.

```csharp
Rectangle source = new Rectangle(0, 0, 100, 100);
Vector2 position = new Vector(40, 300);

Raylib.DrawTextureRec(heroTexture, source, position, Color.WHITE);
```

Det här kan man bland annat använda sig av när man har en bild som är ett s.k. sprite sheet, där alla bildrutor i en karaktärs animation finns med. Man behöver då inte klippa upp animationen i en massa olika bildfiler utan kan istället använda DrawTexturePro för att kopiera en del av bilden till raylibfönstret i taget.

Man kan också ange en source-rektangel med negativ bredd eller höjd för att få en urklippt bild som är flippad längs x- eller y-axeln.

```csharp
Rectangle source = new Rectangle(0, 0, -100, 100);
Vector2 position = new Vector(40, 300);

Raylib.DrawTextureRec(heroTexture, source, position, Color.WHITE);
```

### DrawTexturePro()

En ännu mer avancerad version av DrawTexture. Här anges två rektanglar – en för källan, alltså vilken del av texturen som ska kopieras. Och så en för destinationen, alltså var någonstans på fönstret kopian ska placeras och hur stor den ska göras.

Dessutom anges en Vector2 för "origin", som är den position som ritandet och roterandet utgår från. Vill man rotera och skala en textur kring dess mittpunkt anger man alltså en Vector2 vars x- och y-värden är halva destination-rektangelns bredd och höjd.

```csharp
Texture2D spriteSheet = Raylib.LoadTexture("herosheet.png");

// Det som ska kopieras från texturen är en ruta i storlek 64x64 pixlar från 
//  dess övre vänstra hörn (0,0)
Rectangle heroSpriteSource = new Rectangle(0,0,64,64);

// Hjältespriten ska ritas ut på position 200, 200 och förstoras upp till 256x256.
Rectangle heroSpriteDest = new Rectangle(200, 200, 256, 256);

// En Vector2 med halva destinationens bredd och höjd som x- och y-värde.
// Den räknas från destinationens övre vänstra hörn, så hamnar alltså i mitten av den.
Vector2 heroOrigin = new Vector2(
  heroSpriteDest.width / 2,
  heroSpriteDest.height / 2
);

float rotation = 0;

// ---

Raylib.DrawTexturePro(
  texture, 
  heroSpriteSource,
  heroSpriteDest,
  heroOrigin,
  rotation,
  Color.WHITE );
```

Bilden nedan visar principen:

![](../../../images/image-8.png)

### SetTextureFilter()

I vanliga fall när man ritar ut en texture i en annan storlek än den är från början så skalas den med interpolering – den hittar på mjuka övergångar mellan originalpixlarna. Det fungerar bra för foton och liknande, men sämre för pixelart.

```csharp
// Bestäm att texturen heroTexture ska skalas med "point"-filter, som ger skarp
// pixelart - ingen interpolering.
Raylib.SetTextureFilter(heroTexture, TextureFilter.TEXTURE_FILTER_POINT);
```
