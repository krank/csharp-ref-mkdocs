# Raylib setup

Skapa ett nytt konsollprojekt som vanligt.

* Ta fram **NuGet-fliken** i Visual Studio Codes nedre panel (bredvid Terminal). Du behöver [ha tillägget NuGet Gallery installerat](https://marketplace.visualstudio.com/items?itemName=patcx.vscode-nuget-gallery).
  * Om du inte ser den fliken, tryck F1 och sök efter "nuget", välj "Focus on NuGet view".
* I galleriet, sök efter Raylib. Välj senaste versionen av "Raylib\_cs".
* Kryssa i ditt projekt, klicka Install.
* Om du vill använda bilder eller andra filer i ditt spel, se till att [konfigurera din csproj för att hantera resursfiler](../../filhantering/resursfiler.md#loesning-3-kopiera-filerna-automatiskt-till-malmappen).

### Inkludera Raylib <a href="#h.p_juwpvkt-mpln" id="h.p_juwpvkt-mpln"></a>

!!! warning

	**OBSERVERA:** För att du ska kunna använda Raylib så måste du skriva in följande bland dina using-rader högst upp i programfilen:
	
	```csharp
	using Raylib_cs;
	```
	
