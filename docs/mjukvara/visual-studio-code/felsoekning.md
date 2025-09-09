# Felsökning

Visual Studio Code är ganska nytt och inte ett lika "färdigt paket" som Visual Studio. Därför kan det ibland bli krångel, lite beroende på vad man har på sin dator i övrigt, och hur den mår. Här nedan finns några saker man kan göra för att felsöka.

## Allmänna saker att testa

* Testa F1 (eller Fn+F1) för att få fram kommandopaletten, och kör "OmniSharp: Restart OmniSharp".
* Starta om Visual Studio Code.
*   Kolla om du har Visual Studio 2017 eller 2019 installerad. Om du har det, starta Visual Studio Installer och _uppdatera_ Visual Studio.

    * Eller avinstallera Visual Studio 2017/2019 helt.

    Kolla "Output" (View → Output) och se om VSCode håller på och installerar OmniSharp, .NET Core Debugger och Razor Language Server. Om den håller på med det, vänta tills den är klar.
* Dubbelkolla att [DotNet Core SDK](https://dotnet.microsoft.com/download) och [C#-tillägget i Visual Studio Core](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) är installerade
  * Du kan dubbelkolla att en tillräckligt ny version av DotNet Core SDK är installerat genom att öppna terminalen i Visual Studio Code och skriva "`dotnet --version`". Du bör få en siffra med en version, och du bör ha minst version 3.1.

## The nuclear option

Om ingenting fungerar så kan du testa en fullständig ominstallation.

* Avinstallera (alla versioner av) DotNet Core SDK
* Avinstallera (alla versioner av) Visual Studio
* Avinstallera Visual Studio Code
* Öppna Utforskaren (Windows + E)
  * Gå till din användarmapp
  * Visa → Dolda objekt
  * Ta bort mappen .vscode

Installera sedan DotNet Core SDK och Visual Studio Code igen, och de tillägg du vill ha.

## Min Debug är tom!

![](../../images/image-18.png) 

* Klicka på den lilla **klockan längst ner till höger** och se om du har en notification om att "Required assets to build and debug are missing". Om du har det, tryck "Yes".
  * Om du inte har det, testa att ta fram kommandopaletten (F1 eller View → Command Palette) och sök efter "**Generate Assets for Build and Debug**". Kör det kommandot.
  * Om du får ett felmeddelande när du gör det, sök efter "**OmniSharp: Restart OmniSharp**". Kör det kommandot.
* Sök efter "**Omnisharp: Select Project**" och välj SLN-filen.

## Jag får ingen kodkomplettering i Unity!

Ladda ner och installera [.NET Framework 4.7.1](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net471-developer-pack-offline-installer).
