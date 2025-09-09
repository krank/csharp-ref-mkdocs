# Ljud

Raylib har stöd för en hel del ljudformat, bland annat mp3, ogg och wave.

### InitAudioDevice()

Gör att Raylibs ljudsystem initieras.

```csharp
Raylib.InitAudioDevice();
```

### SetMasterVolume()

Bestämmer volymen överlag på en skala mellan 0.0 och 1.0.

```csharp
Raylib.SetMasterVolume(0.3f);
```

## Ljudeffekter

### Sound

En datatyp för ljudeffekter.

### LoadSound()

Läser in en ljudfil och placerar dess innehåll i minnet, redo att läsas av och spelas upp.

```csharp
Sound exampleSound = Raylib.LoadSound("woop_woop.ogg");
```

### PlaySound()

Spelar upp ett ljud

```
Raylib.PlaySound(exampleSound);
```

### PauseSound()

Pausar uppspelningen av ett ljud.

```csharp
Raylib.PauseSound(exampleSound);
```

### ResumeSound()

Fortsätter uppspelningen av ett pausat ljud.

```csharp
Raylib.ResumeSound(exampleSound);
```

### StopSound()

Avbryter uppspelningen av ett ljud.

```csharp
Raylib.StopSound(exampleSound);
```

### IsSoundPlaying()

Returnerar en bool – true om ljudet just nu spelas, annars false.

```csharp
bool isPlaying = Raylib.IsSoundPlaying(exampleSound);
```

### SetSoundVolume()

Bestämmer volym för ett ljud. Volymen anges som en float mellan 0.0 och 1.0.

```csharp
Raylib.SetSoundVolume(exampleSound, 0.35f);
```

## Musik

### Music

En datatyp för musikströmmar.

### LoadMusicStream()

Skapar en musikström baserad på en ljudfil. Hela ljudfilen läses inte in i minnet samtidigt, utan bara en liten bit i taget.

```csharp
Music exampleMusic = Raylib.LoadMusicStream("file_example_OOG_1MG.ogg");
```

### PlayMusicStream()

Aktiverar uppspelningen av en musikström.

```csharp
Raylib.PlayMusicStream(exampleMusic);
```

### PauseMusicStream()

Pausar uppspelningen av en musikström.

```csharp
Raylib.PauseMusicStream(exampleMusic);
```

### ResumeMusicStream()

Fortsätter uppspelningen av en pausad musikström.

```csharp
Raylib.ResumeMusicStream(exampleMusic);
```

### StopMusicStream()

Avbryter uppspelningen av musikströmmen helt.

```csharp
Raylib.StopMusicStream(exampleMusic);
```

### UpdateMusicStream()

Behöver köras varje frame. Kollar ifall mer data behöver laddas in från ljudfilen som musikströmmen är kopplad till, och gör det i så fall.

```csharp
Raylib.UpdateMusicStream(exampleMusic);
```

### IsMusicPlaying()

Returnerar en bool – true om musikströmmen just nu spelas, annars false.

```csharp
bool isPlaying = Raylib.IsMusicPlaying(exampleMusic);
```

### SetMusicVolume()

Bestämmer volym för en musikström. Volymen anges som en float mellan 0.0 och 1.0.

```csharp
Raylib.SetMusicVolume(exampleMusic, 0.75f)
```
