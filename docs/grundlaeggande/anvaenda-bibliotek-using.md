# Använda bibliotek (using)

C# har ett antal inbyggda kodbibliotek. Man kan lägga till ytterligare bibliotek i ett specifikt projekt genom NuGet-paket.

## Using

Skrivs högst upp i en cs-fil för att deklarera att innehållet i ett visst bibliotek ska användas.

{% code lineNumbers="true" %}
```csharp
using System;
using System.Net;
using System.Collections.Generic;
using System.Text.Json;
```
{% endcode %}

Man kan alltid använda sig av bibliotekens innehåll utan att skriva using, men då måste man skriva hela bibliotekets namn varje gång.

{% code lineNumbers="true" %}
```csharp
// Utan "using System":
System.Console.WriteLine("Hello");

// Med "using System":
Console.WriteLine("Hello");

// Utan "using System.Collections.Generic":
System.Collections.Generic.List<string> list = new System.Collections.Generic.List<string>();

// Med "using System.Collections.Generic":
List<string> list = new List<string>();
```
{% endcode %}

### Global using (.NET 6)

I .NET 6 introduceras globala using-statements. De måste skrivas ovanför alla vanliga using-statements.

```csharp
global using System.IO;
```

De gör att man bara behöver skriva varje using-statement en gång per projekt. Lämpligtvis samlar man dem då i samma fil.

### Implicit using (.NET 6)

I .NET 6 ingår som standard vissa globala using-statements utan att man behöver skriva dem. I konsollprogram ingår:

{% code lineNumbers="true" %}
```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
```
{% endcode %}

## NuGet Gallery

NuGet Gallery är ett Visual Studio Code-tillägg som gör att man kan söka efter och lägga till nya bibliotek till sitt projekt. De är packeterade som NuGet-paket, och Gallery hjälper till att hitta, laddaner och installera dem.

Man kommer åt tillägget genom att trycka F1 och söka efter det.

![](../images/image-10.png)

Därefter söker man efter det bibliotek man vill ha, till exempel Raylib eller Restsharp. Man markerar biblioteket man vill ha, sedan kan man trycka på "Install"-länken som står bredvid ens projekts csproj-fil i högerspalten.

![](../images/image-11.png)

## NuGet via terminalen

Om man känner till NuGet-paketets namn så kan man använda terminalkommandon istället. Man placerar sig då först i mappen där projektets csproj-fil ligger och sedan skriver man till exempel:

```powershell
dotnet add package Raylib-cs
```

Då kommer dotnet att upptäcka csproj-filen, lägga in en referens till biblioteket i den, och sedan se till att NuGet-paketet laddas ner och packas upp.
