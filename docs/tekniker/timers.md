# Timers

Om man vill att något ska utföras till exempel var tionde gång en loop körs, kan man använda sig av en "timer".

```csharp
int timerMaxValue = 10;
int timerCurrentValue = 10;

while (true)
{
  timerCurrentValue--;
  if (timerCurrentValue <= 0)
  {
    Console.WriteLine("Tenth!");
    timerCurrentValue = timerMaxValue;
  }
}
```

Varje gång loopen ovan körs, så minskar timerns värde med 1.

Om timerns värde blivit lika med eller under 0, så skriver programmet ut "Tenth!" och återställer timern till dess maxvärde.

Det här kan såklart byggas vidare på – i Unity eller Raylib kan man låta räknarvärdet vara en float, och dra av mängden tid sedan föregående frame (i Unity drar man då av `Time.DeltaTime`, i Raylib drar man av `Raylib.GetFrameTime()`.

```csharp
float timerMaxValue = 1;
float timerCurrentValue = timerMaxValue;

while (!Raylib.WindowShouldClose())
{
  timerCurrentValue -= Raylib.GetFrameTime();
  if (timerCurrentValue < 0 && Raylib.IsKeyDown(KeyboardKey.KEY_SPACE))
  {
    // Gör någonting, t.ex. skjut ett skott (varje sekund)
    
    timerCurrentValue = timerMaxValue;
  }
  
  Raylib.BeginDrawing();
  Raylib.EndDrawing();

}
```
