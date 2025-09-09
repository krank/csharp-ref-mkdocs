# C# snabbreferens

Detta är en hemsida med förenklade förklaringar och exempel för C# och Visual Studio Code. Tanken är att den ska kunna användas som referensverk för gymnasieelever som läser kurserna **Programmering 1** och **Programmering 2**.

**Se även:**

* [Progdocs](https://app.gitbook.com/o/z5sgNMMcAnOUt1fqvUGW/s/t567cGmgFsbOXYO6QFYM/) – en portal med olika dokumentations-sajter som denna.
* [Unity](https://app.gitbook.com/o/z5sgNMMcAnOUt1fqvUGW/s/-MJTeBJlEweD3YcPwKkg/) – en sida med förenklade förklaringar och exempel för Unity och C#

## Vad behöver jag först?

* Installera [.NET SDK](mjukvara/dotnet-sdk.md) – version 8 eller senare: [https://dotnet.microsoft.com/en-us/download](https://dotnet.microsoft.com/en-us/download)
* Installera [Visual Studio Code](mjukvara/visual-studio-code/)
  * Och lämpliga [extensions](mjukvara/visual-studio-code/extensions.md).
* Installera [Git-scm](mjukvara/git-and-github/) och [ställ in namn och email](mjukvara/git-and-github/#foersta-gangen-efter-ny-git-installation).
* Kolla [lathunden ](lathund-skapa-projekt.md)för hur man skapar nya projekt.

Det enklaste sättet att installera .NET SDK, Visual Studio Code och Git-scm är via **winget**. Öppna ett terminalfönster/kommandotolken och kör:

```powershell
winget install Microsoft.VisualStudioCode
winget install git.git
winget install Microsoft.DotNet.SDK.9
```

Winget bör finnas och fungera i Windows 10 och 11; använder du en äldre version av windows kanske du får installera manuellt istället. Det kan också vara bra att köra **Windows Update** först, och installera alla tillgängliga uppdateringar (inklusive de man bara får om man klickar "Sök online…"

!!! info

	**TIPS:** winget kan användas för att installera [allt möjligt](https://winget.run/), och kan också hålla programmen uppdaterade.
	
	Om du skriver <mark style="color:orange;">`winget upgrade`</mark> så får du en lista med program som kan uppdateras, och du kan då antingen skriva <mark style="color:orange;">`winget upgrade <namnet på programmet>`</mark> för att uppdatera ett specifikt program eller <mark style="color:orange;">`winget upgrade --all`</mark> för att uppdatera alla.
	

## Hittat ett fel?

Hela den här sidan finns [speglad på GitHub](https://github.com/krank/csharp-ref) – där kan du skapa en buggrapport (issue) och beskriva problemet.

Eller så kan du forka repositoriet, göra ändringen och sedan göra en pull request!

## Progression

Den här sidan är byggd för kurserna Programmering 1 och 2, och detta är den tänkta uppdelningen.

Vissa saker som t.ex. [Raylib ](annat/raylib/)ligger utanför tabellen – det är inte ett obligatoriskt moment i någon kurs men är heller inte riktigt "överkurs".

| Programmering 1                                                 | Programmering 2                                                                                | Överkurs                                                               |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Datatyper](grundlaeggande/datatyper/)                          | [Klasser och instanser](klasser-och-objektorientering/klasser-och-instanser.md)                | [Delegates, events och lambdas](grundlaeggande/delegates.md)           |
| [Typkonvertering](grundlaeggande/typkonvertering.md)            | [Public, private och protected](klasser-och-objektorientering/public-private-och-protected.md) | [Reference vs value types](grundlaeggande/reference-vs-value-types.md) |
| [Operatorer](grundlaeggande/operatorer.md)                      | [Klassdiagram](klasser-och-objektorientering/klassdiagram.md)                                  | [Abstract](klasser-och-objektorientering/abstract.md)                  |
| [Konsolen](grundlaeggande/konsollen-console.md)                 | [Klassmetoder](klasser-och-objektorientering/klassmetoder.md)                                  | [Interface](klasser-och-objektorientering/interface.md)                |
| [If-satser](grundlaeggande/if-satser.md)                        | [Konstruktorer](klasser-och-objektorientering/kontruktorer.md)                                 | [Threading](annat/threading/)                                          |
| [Loopar](grundlaeggande/loopar.md)                              | [Arv](klasser-och-objektorientering/arv.md)                                                    |                                                                        |
| [Listor och arrayer](grundlaeggande/listor-och-arrayer.md)      | [Inkapsling och properties](klasser-och-objektorientering/inkapsling-och-properties.md)        |                                                                        |
| [Slump](grundlaeggande/slump.md)                                | [Static](klasser-och-objektorientering/static.md)                                              |                                                                        |
| [String-manipulering](grundlaeggande/string-manipulering.md)    | [Polymorfism](klasser-och-objektorientering/polymorfism/)                                      |                                                                        |
| [Egna metoder](grundlaeggande/egna-metoder.md)                  | [Generiska klasser](klasser-och-objektorientering/generiska-klasser.md)                        |                                                                        |
| [Använda bibliotek](grundlaeggande/anvaenda-bibliotek-using.md) | [Läsa och skriva](filhantering/laesa-och-skriva.md)                                            |                                                                        |
| [Namngivning](grundlaeggande/namngivning.md)                    | [Serialisering](filhantering/serialisering/)                                                   |                                                                        |
| [Begrepp](grundlaeggande/begrepp.md)                            | [Nätverk och internet](annat/naetverk-och-internet/)                                           |                                                                        |
| [Pseudokod och diagram](annat/pseudokod-och-diagram.md)         |                                                                                                |                                                                        |
