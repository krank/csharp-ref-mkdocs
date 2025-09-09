# WPF

WPF står för Windows Presentation Foundation och är ett sätt att skapa fönster-appar, alltså sådana med vanliga Windows-knappar, textrutor och så vidare.

(BILD)

WPF-projekt använder [XAML](xaml.md) för att beskriva gränssnittet och vanlig C# för att få till logiken bakom; vad som ska hända när man klickar på knappar etc.

## Skapa ett WPF-projekt

Eftersom WPF-projekt numera inte finns med i listan över projekt man får fram när man använder "New .NET Project" så får man skapa projektet manuellt istället:

Skapa en **ny mapp** för projektet och öppna den mappen i Visual Studio Code.

Gå till terminalen och skriv:

```powershell
dotnet new wpf --name ProjectName
```

Detta bör innebära att ett fungerande WPF-projekt skapas i mappen, och en SLN-fil genereras av C# Dev Kit.





