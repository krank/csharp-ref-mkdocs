# Extensions

Extensions lägger till funktioner i Visual Studio Code. I grunden är ju Code en ganska simpel kod-editor utan stöd för specifika språk.

Klicka på den här ikonen i vänstermenyn för att se extensions:

![](../../images/image-17.png)

Där syns vilka som just nu är installerade, och man kan även söka efter nya extensions.

Om man har en länk till en extension – som de nedan – kan man helt enkelt klicka på länken, sedan "Install" och sedan låta webbäsaren öppna Visual Studio Code och installera extensionen.

!!! info

	**TIPS:** Man kan installera extensions via terminalen/kommandotolken också:
	
	`code --install-extension ms-dotnettools.csdevkit`
	
	`code --install-extension codezombiech.gitignore`
	
	`code --install-extension patcx.vscode-nuget-gallery`
	
	`code --install-extension eliostruyf.vscode-hide-comments`
	

## Användbara extensions

### Grunduppsättning för C\#

* [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) – Get Visual Studio Code stöd för C# & underlättar projekthantering.
  * **OBS:** Gå till "IntelliCode for C# Dev Kit" som automatiskt installeras, och stäng av (tryck Disable)! Den kan vara användbar, men inte medan man lär sig!
* [gitignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore) – Underlättar arbetet med git och Visual Studio Code. Om du söker efter den, se till att ta den av CodeZombie!
* [NuGet Gallery](https://marketplace.visualstudio.com/items?itemName=patcx.vscode-nuget-gallery) – Underlättar installationen av externa bibliotek och paket, t.ex. Raylib.
* [Hide Comments](https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-hide-comments) – Gömmer alla kommentarer. Används när du presenterar din kod.

### Bonus

* [Vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons) – ger tydligare ikoner för filer och mappar.
* [NoesisGUI XAML Tools](https://marketplace.visualstudio.com/items?itemName=NoesisTechnologies.noesisgui-tools) – hjälper till med kodkomplettering när man skriver [XAML](../../annat/windows-ui/xaml.md)-kod. Inte perfekt! Eftersom den egentligen är gjord för en väldigt specifik användning av XAML.
* [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) – gör att man kan testa API-anrop direkt i VScode, både mot lokala servrar som man bygger själv och servrar på det lokala nätverket eller internet.
* [Roslynator](https://marketplace.visualstudio.com/items?itemName=josefpihrt-vscode.roslynator) – Ger en hel del kodförslag och hjälp.
  * Vill du ha ännu mer pedantisk "hjälp"? Använd [NuGet Gallery](../../grundlaeggande/anvaenda-bibliotek-using.md#nuget-gallery) för att lägga till StyleCop.Analyzers till ditt projekt.
* [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) – Realtids-samarbete; flera personer kan skriva kod tillsammans samtidigt.
