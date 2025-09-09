# Kamera

## Camera2D

Kamera för 2D-spel

```csharp
Camera2D camera = new Camera2D(); // Skapa ny kamera
```

### zoom

Hur inzoomad kameran ska vara.

```csharp
  camera.Zoom = 1f; // Bestämma zoomvärdet till 1
```

!!! warning

	OBSERVERA: Om du inte bestämmer värdet för zoomen, så kommer kameran att bete sig underligt. Ge alltid kameran zoomvärde 1 (eller något annat) manuellt!
	

### target

Den punkt i världen som kameran ska roteras kring, och som även dess zoom fokuseras på – samt den punkt dess offset ska utgå från.

```csharp
camera.Target = new Vector2(400, 300);
```

### offset

Kamerans offset är en 2d-vektor som beskriver hur långt från sin target kamerans övre vänstra hörn befinner sig – alltså hur långt den ska flyttas från sin ursprungsposition, relativt allt annat.

```csharp
float screenWidth = Raylib.GetScreenWidth();
float screenHeight = Raylib.GetScreenHeight();

// Gör så att kamerans target hamnar i mitten av skärmen
camera.Offset = new Vector2(screenWidth / 2, screenHeight/2);
```

### rotation

Hur roterad kameran ska vara.

```csharp
camera.Rotation = 45; // Roterar kameran 45 grader
```



### BeginMode2D() / EndMode2D()

Används för att, **mellan Raylib.BeginDrawing() och Raylib.EndDrawing()**, avgränsa vilka delar som ska ritas relativt kameran. I de flesta spel betyder det "hela själva spelet". Utanför BeginMode / EndMode ritar man ut UI-element och sådant som inte ska påverkas av kamerans rotationer och förflyttningar.

BeginMode2D vill ha en kamera som första parameter.

```csharp
Raylib.BeginMode2D(camera);

Raylib.ClearBackground(Color.LIGHTGRAY);
Raylib.DrawRectangle(390,290,10,10,Color.RED);

Raylib.EndMode2D();
```
