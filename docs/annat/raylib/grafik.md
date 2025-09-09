# Grafik

## Mått och koordinatsystem

Observera att koordinatsystemet i Raylib har **origo i övre vänstra hörnet**, och att **Y-axeln är omvänd** så att positiva värden går nedåt.

Måtten är i **pixlar**.

## SetTargetFps()

Används normalt utanför spel-loopen, för att begränsa antalet bildrutor per sekund. Är ett av de sätt som finns att få t.ex. förflyttningar att ske lika snabbt på alla datorer.

```csharp
Raylib.SetTargetFps(60); // Begränsar till 60fps
```

## BeginDrawing(), EndDrawing()

Används för att påbörja, respektive avsluta, den delen av spelloopen som ritar ut saker till fönstret.

```csharp
while (!Raylib.WindowShouldClose())
{
  // Spelets logik
  
  Raylib.BeginDrawing();
  
  // Kod för att rita ut saker till fönstret
  
  Raylib.EndDrawing();
}
```

## ClearBackground()

Rensar fönstret. Görs normalt kort efter BeginDrawing.

```csharp
while (!Raylib.WindowShouldClose())
{
  Raylib.BeginDrawing();

  Raylib.ClearBackground(Color.WHITE);
  
  Raylib.EndDrawing();
}
```

## Färger

Det finns en hel del färdiga färger i Raylib, till exempel Color.MAGENTA eller Color.ORANGE.

Om man vill skapa en egen ny färg så kan man göra det:

```csharp
Color hotPink = new Color(255, 105, 180, 255);
```

Parametrarna är helt enkelt siffror från 0–255 för rött, grönt, blått och alpha (genomskinlighet). 0 alpha är helt genomskinlig, 255 är helt ogenomskinlig.
