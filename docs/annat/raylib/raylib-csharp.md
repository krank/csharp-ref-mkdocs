# Raylib-CSharp\*

Raylib är från början ett bibliotek till C++, och Raylib-cs är inte det enda sättet att koppla Raylib till C#. **Raylib-CSharp** är ett annat paket, som funkar delvis annorlunda.

## Separata bibliotek

Raylib-CSharp är mer uppdelat än Raylib-cs. Varje kategori av funktioner har sitt eget bibliotek, som man måste inkludera via [using](../../grundlaeggande/anvaenda-bibliotek-using.md).

```csharp
using System.Numerics;
using Raylib_CSharp.Colors;
using Raylib_CSharp.Rendering;
using Raylib_CSharp.Windowing;

Window.Init(800, 600, "Hello");

Vector2 position = new (400, 300);

while (!Window.ShouldClose())
{
  Graphics.BeginDrawing();
  Graphics.ClearBackground(Color.Green);

  Graphics.DrawCircleV(position, 40, Color.Black);

  Graphics.EndDrawing();
}
```

## Funktioner



<table><thead><tr><th width="331">Raylib-cs</th><th width="258">Raylib-CSharp</th><th>Bibliotek</th></tr></thead><tbody><tr><td>Raylib.InitWindow</td><td>Window.Init</td><td>Windowing</td></tr><tr><td>Raylib.SetTargetFPS</td><td>Time.SetTargetFPS</td><td>Raylib_CSharp</td></tr><tr><td>Raylib.WindowShouldClose</td><td>Window.ShouldClose</td><td>Windowing</td></tr><tr><td>Raylib.BeginDrawing</td><td>Graphics.BeginDrawing</td><td>Rendering</td></tr><tr><td>Raylib.EndDrawing</td><td>Graphics.EndDrawing</td><td>Rendering</td></tr><tr><td>Raylib.ClearBackground</td><td>Graphics.ClearBackground</td><td>Rendering</td></tr><tr><td>Raylib.DrawRectangle</td><td>Graphics.DrawRectangle</td><td>Rendering</td></tr><tr><td>Raylib.DrawCircle</td><td>Graphics.DrawCircle</td><td>Rendering</td></tr><tr><td>Raylib.DrawLine</td><td>Graphics.DrawLine</td><td>Rendering</td></tr><tr><td></td><td></td><td></td></tr></tbody></table>

Varianter av funktionerna – DrawRectangleRec, DrawRectangleLines osv finns såklart också.

## Datatyper

<table><thead><tr><th width="592">Struct</th><th>Bibliotek</th></tr></thead><tbody><tr><td>Rectangle</td><td>Transformations</td></tr><tr><td>Color</td><td>Colors</td></tr><tr><td>Texture</td><td>Textures</td></tr><tr><td>Image</td><td>Images</td></tr></tbody></table>

