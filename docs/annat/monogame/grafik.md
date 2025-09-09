# Grafik\*

## GraphicsDevice

En abstraktion som ger tillgång till renderingssystemet.

### Clear()

Rensar skärmen/fönstret, använder färgen som anges som parameter.

```csharp
GraphicsDevice.Clear(Color.CornflowerBlue);
```

## Color

Datatyp som MonoGame använder för att hantera förg.

```csharp
Color hotPink = new(255, 105, 180);
Color semiTransparentWhite = new(255, 255, 255, 128);
```

Värdena som anges som parametrar är mängden rött, grönt och blått som färgen ska innehålla, på skalan 0–255. Anges ett fjärde värde så tolkas det som mängden "Alpha", alltså genomskinlighet där 0 är helt genomskinligt och 255 är helt ogenomskinligt.

## Texture2D

Ett Texture2D-objekt är en tvådimensionell bild. Oftast skapas de genom att man laddar in resources som man tidigare förberett i [mcgb-editor.md](mcgb-editor.md "mention").

```csharp
Texture2D hero = Content.Load<Texture2D>("heroSprite");
```

Man kan också skapa nya Texture2Ds. När de skapas är de då helt tomma.

```csharp
// Skapa en Texture2D som är 1x1 i storlek
Texture2D pixel = new Texture2D(GraphicsDevice, 1, 1);
```

### GetData&lt;Color>()

Avancerat – Fyller en array med färgdatan från texturen. Första parametern ska vara den array som fylls med datan; den måste ges samma storlek som det totala antalet pixlar i texturen.

```csharp
// Skapa en array av rätt storlek
Color[] pixels = new Color[hero.Height * hero.Width]

// Hämta datan in i arrayen
hero.GetData<Color>(pixels);
```

Arrayen är endimensionell – alla pixlar ligger efter varandra. Den är organiserad i rader, så först ligger alla pixlar på bildens första rad, sedan alla på bildens andra rad, sedan tredje raden, osv.

För att byta färg på en enskild pixel i arrayen används sedan vanlig indexering, och datatypen här är Color.

### SetData()

Avancerat – Motsvarigheten till GetData(). Används för att stoppa in en array med färgdata in i en Texture2D.

```csharp
hero.SetData<Color>(pixels);
```

## SpriteBatch

2D-grafik i Monogame ritas ut med SpriteBatches. När man skapar ett nytt Monogame-projekt får man automatiskt en SpriteBatch-variabel i Game1-klassen:

```csharp
private SpriteBatch _spriteBatch;
```

Och den initieras och kopplas till sysyemets renderingssystem (GraphicsDevice) i LoadContent:

```csharp
protected override void LoadContent()
{
  _spriteBatch = new SpriteBatch(GraphicsDevice);
}
```

Därefter kan den användas i Draw() för att rita ut Texture2D-objekt till MonoGame-fönstret.

```csharp
protected override void Draw(GameTime gameTime)
{
  GraphicsDevice.Clear(Color.CornflowerBlue);

  _spriteBatch.Begin();
  _spriteBatch.Draw(pixel, rectangle, Color.Red);
  _spriteBatch.End();
    
  // ...
  base.Draw(gameTime);
}
```

### Begin()

Aktiverar en SpriteBatch och gör den redo för att börja rita ut sprites till skärmen.

```csharp
_spriteBatch.Begin();
```

### End()

Avslutar en SpriteBatch' ritande för den här bildrutan.

```csharp
_spriteBatch.End();
```

### Draw()

Ritar ut en Texture2D till skärmen. Första parametern är alltid den textur som ska ritas ut och den sista är den färg som texturen ska färgas med. Använd `Color.White` om du bara vill använda texturens normala färger.

```csharp
Rectangle rect = new (10,20,64,64);
Vector2 pos = new(100,20);

// Rita ut 'hero' och passa in den i rektangeln 'rect'
_spriteBatch.Draw(hero, rect, Color.White);

// Rita ut 'monster' på positionen som anges av vektorn 'pos'
_spriteBatch.Draw(monster, pos, Color.White);
```

Vill man bara rita ut en del av en Texture2D så kan man ange en extra rektangel som beskriver vilken del som ska klippas ut och visas.

```csharp
Rectangle rect = new (10,20,64,64);
Rectangle localRect = new(0,0,16,16);

// Rita ut den del av 'spritesheet' som finns inom 'localRect' och 
// passa in den i rektangeln 'rect'
_spriteBatch.Draw(spriteSheet, rect, localRect, Color.White);
```

Det finns även andra varianter av Draw() som inte dokumenteras här.
