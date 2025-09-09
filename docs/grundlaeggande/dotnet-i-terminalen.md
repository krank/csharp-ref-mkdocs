# Dotnet i terminalen

Visual Studio Code är i grunden bara ett program för att redigera text – allt annat sköts egentligen av andra, separata program. När man programmerar i C# så är ett av de programmen **dotnet**.

* Varje gång ett program till exempel körs så anropar Code först dotnet för att omvandla källkoden till körbara filer.
* Varje gång C# Dev Kit används för att skapa ett nytt projekt anropas dotnet med olika tillval för att skapa en solution och ett nytt tomt C#-projekt.

Man kan också köra dotnet själv, manuellt i terminalen / kommandotolken. Egentligen behövs inte Visual Studio Code – man kan skriva sin kod i Anteckningar eller nästan vilket textredigeringsprogram som helst.

### Dotnet --list-sdks

Skriver ut en lista på vilka dotnet-versioner som är installerade på datorn.

```powershell
PS C:\Users\krank> dotnet --list-sdks
5.0.408 [C:\Program Files\dotnet\sdk]
6.0.302 [C:\Program Files\dotnet\sdk]
PS C:\Users\krank>
```

### Dotnet new

Skapa ett konsollprojekt (ProjectName.csproj) och tillhörande filer i nuvarande mapp:

```
dotnet new console --name ProjectName
```

"Console" anger vilken av dotnets inbyggda C#-projektmallar som används.

Skapa en solution (MySolution.sln) i nuvarande mapp:

```
dotnet new sln --name MySolution
```

### Dotnet run

Kompilerar och kör projektet i den nuvarande mappen (eller solutionens primära projekt):

```
dotnet run
```

### Dotnet add package

Lägger till ett nuget-paket till projektet.

```
dotnet add package Raylib-cs
```

### Dotnet restore

Laddar ner saknade nuget-bibliotek (t.ex. [Raylib](../annat/raylib/)) som projektet använder. Väldigt användbart eftersom det betyder att de biblioteken inte måste skickas med till andra som ska jobba med projektet.

```
dotnet restore
```

### Dotnet sln add

Lägg till ett projekt (ProjectName.csproj) i den solution som finns i den nuvarande mappen:

```
dotnet sln add .\ProjectName\ProjectName.csproj
```

