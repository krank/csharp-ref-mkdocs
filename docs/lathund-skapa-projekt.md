# Lathund: Skapa projekt

* Starta Visual Studio Code
* **SKAPA PROJEKTET**
  * Stäng nuvarande projekt: File → Close folder
  * Explorer → Create .NET Project (C# Dev Kit)
  * Välj "Console App"
  * Skapa och välj en mapp att skapa projektet i.
  * Välj ett namn på projektet.
    * Namnet bör vara i formen PlatformGame (inga mellanslag, stor bokstav i början av varje ord)
  * Öppna csproj-filen och ta bort (eller kommentera bort) raden med `<Nullable>`.
* **GÖR SÅ PROJEKTET KAN KÖRAS**
  * Gå till "run and debug" (**Ctrl+Shift+D**, eller ikonen med play-knapp och insekt).
  * Tryck på "Run and Debug".
  * Välj "C#" och sedan projektets namn (bör vara enda i listan).
* **SKAPA GIT-REPOSITORY**
  * F1 → Add gitignore
    * Välj Visual Studio
  * Gå till Source Control
  * Initialize Repository
  * Skriv in ditt första commit-meddelande och stage:a alla filer du vill ha med (manuellt eller automatiskt)
  * Klicka på "Publish Branch".
  * Välj "Publish to GitHub **public** repository"
  * Om du behöver logga in eller göra något annat kommer VSCode att säga till. Följ instruktionerna.
