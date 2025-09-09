# Projektstruktur

Ett C#-projekt består av ett antal textfiler. Några av dem innehåller själva C#-koden; andra innehåller information om hur den koden ska köras, vilken version av C# som ska användas och så vidare.

Oftast brukar C#-projektet också ingå i en _solution_ – ett slags samling av ett eller flera projekt. När ett nytt projekt skapas genom C# Toolbox-tillägget så skapas både en solution, ett projekt i denna solution, och en första C#-fil i projektet.

## Mappstruktur

![](../images/image-12.png)

Mappen som skapas av C# Dev Kit har följande struktur:

* .vscode
* Mapp med projektet
  * obj
  * bin
  * csproj-fil
  * cs-filer
* sln-fil

**.vscode** är en mapp som Vidual Studio Code skapar för att hålla reda på sina egna inställningar – till exempel när filer för körning och debuggning skapas, eller när man sedan ändrar i de filerna (internalConsole --> externalTerminal).

**Mapp med projektet** – en mapp som får projektets namn och innehåller alla filer som hör till själva C#-projektet.

**obj-mappen** innehåller "mellanfiler" – filer som dotnet/C# skapar som ett mellanled mellan källkoden och de färdiga körbara filerna. Den kan tas bort, men kommer då att återskapas nästa gång projektet körs eller debuggas.

**bin-mappen** innehåller de körbara filer som dotnet/C# skapar utifrån källkoden. Det är filerna i den här mappen som är själva "programmet", och som man kan distribuera till andra människor och datorer.

**csproj-filen** innehåller information om C#-projektet.

**cs-filerna** innehåller själva C#-källkoden.

**sln-filen** är den fil som innehåller information om den _solution_ som skapats.

## C#-projekt (csproj)

{% code lineNumbers="true" %}
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```
{% endcode %}

En csproj-fil är en XML-fil med information om C#-projektet. Några viktiga delar är:

* **TargetFramework** – vilken version av dotnet / C# som ska användas. I exemplet är det dotnet 6.
* **ImplicitUsings** – huruvida man vill använda [implicita usings](anvaenda-bibliotek-using.md#implicit-using-.net-6).
* **Nullable** – Dotnet 6 introducerar "nullable reference types", något som mestadels märks i att man får varningar vid vanliga strings… Enklaste lösningen att hantera detta är att helt enkelt stänga av Nullable genom att kommentera bort raden eller ändra "enable" till "disable".

## Dotnet-solutions (sln)

{% code lineNumbers="true" %}
```
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 16
VisualStudioVersion = 16.0.30114.105
MinimumVisualStudioVersion = 10.0.40219.1
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "DemoProject", "DemoProject\DemoProject.csproj", "{FE320B4D-B077-4D3C-BBF4-306ADAA15842}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{FE320B4D-B077-4D3C-BBF4-306ADAA15842}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{FE320B4D-B077-4D3C-BBF4-306ADAA15842}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{FE320B4D-B077-4D3C-BBF4-306ADAA15842}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{FE320B4D-B077-4D3C-BBF4-306ADAA15842}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
EndGlobal
```
{% endcode %}

SLN-filen innehåller en hel del information, där det viktigaste för oss är vilka projekt som ingår. I exemplet ingår ett enda projekt – "DemoProject".
