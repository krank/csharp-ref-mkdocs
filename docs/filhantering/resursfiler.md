# Resursfiler

Ofta jobbar vi med filer som ska finnas i samma mapp som vårt program, eller i en filsökväg relativt programmet. Till exempel:

* Json-filer som ska sparas till eller läsas in
* Bildfiler som Raylib ska läsa in och rita till skärmen
* Textfiler som innehåller spelets berättelse

Dessa letar programmet alltid efter i den nuvarande mappen (**current folder**). Vad som räknas som current folder varierar.

* Använder man en utförlig launch.json (via t.ex. [Generate assets…](../lathund-skapa-projekt.md)) så är current folder **mappen csproj-filen ligger i**.
* Använder man den ganska tomma default-launch-json-filen som C# Dev Kit numera skapar, så är current folder mappen som den kompilerade exe/dll-filen ligger i.

## Lösning 1: Kopiera filerna automatiskt till målmappen

Det här är **det rekommenderade sättet** att lösa problemet på.

Öppna projektets csproj-fil. Den bör se ut ungefär såhär:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <!-- <Nullable>enable</Nullable> -->
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Raylib-cs" Version="4.5.0.4" />
  </ItemGroup>
</Project>
```

Lägg till en ny ItemGroup, till exempel direkt under den PropertyGroup som redan finns. I den nya ItemGroup:en lägger du in nya Content-element för de filer du vill ha med.&#x20;

```xml
  <ItemGroup>
    <Content Include="character.png" CopyToOutputDirectory="Always"/>
    <Content Include="tree.png" CopyToOutputDirectory="Always"/>
  </ItemGroup>
```

### Många filer av samma typ

För att kopiera alla filer av en viss typ kan du använda \*-tecken.

```xml
  <ItemGroup>
    <Content Include="*.png" CopyToOutputDirectory="Always"/>
  </ItemGroup>
```

### En hel mapp

Skapa en mapp där du lägger alla bilder, textfiler och annat du vill ha med. Döp den till t.ex. Assets.

Gör så att mappen, inklusive alla undermappar och filer, kopieras:

```xml
  <ItemGroup>
    <Content Include="Assets\**\*.*" CopyToOutputDirectory="Always"/>
  </ItemGroup>
```

## Lösning 2: Generate assets

* Lägg bilder etc direkt i samma mapp som csproj-filen.
* Använd **F1 → .NET: Generate Assets for Build and Debug** för att generera en launch.json.

## Lösning 3: Lägg filerna manuellt till målmappen

* Lägg alla nödvändiga filer direkt till mappen där exe/dll:en ligger. Kör du dotnet 7 blir det i **bin\Debug\net7.0**.
* Kom ihåg att inte ta bort mappen utan att vara säker på att du har kopior av filerna!
* Kom ihåg att kopiera in samma filer i din exe-fils mapp när du [kompilerar för publicering](../kompilering-och-publicering.md)!
