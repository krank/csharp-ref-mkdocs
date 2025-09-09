# Dotnet SDK

För att du ska kunna skapa och kompilera C#-projekt behövs .NET SDK; ladda ner från [https://dotnet.microsoft.com/download](https://www.google.com/url?q=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload\&sa=D\&sntz=1\&usg=AFQjCNEZyeRMV73INiktjzYkeKEh8y7vUQ) eller använd winget:

```powershell
winget install Microsoft.DotNet.SDK.9
```

När du installerat; öppna terminalen / powershell och skriv:

```
dotnet --list-sdks
```

Nu bör du få en lista med de versioner av .NET SDK som är installerade.

## MacOS

Ta reda på ifall din Mac kör Intel eller Apple Silicon (M1/M2).

Gå till [https://dotnet.microsoft.com/download](https://www.google.com/url?q=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload\&sa=D\&sntz=1\&usg=AFQjCNEZyeRMV73INiktjzYkeKEh8y7vUQ) och välj rätt version att ladda ner.

Kör installationsprogrammet och skriv in lösenordet när det efterfrågas.

När du installerat: Se till så att Terminalen inte är öppen (stäng den isf). Öppna den. Skriv:

```
dotnet --list-sdks
```

Nu bör du få en lista med de versioner av .NET SDK som är installerade.

Om du har Homebrew installerat kan du istället installera dotnet med:

```
brew install --cask dotnet-sdk
```

### Saker att testa om det inte funkar

(Alla `dessa` innebär att man skriver kommandon i terminalen)

* Kör `/usr/local/share/dotnet/dotnet` – funkar det? Eller säger den att det inte finns något sådant kommando?
  * Om det inte funkar – då är dotnet inte installerat, och du bör kunna testa igen (förslagsvis via Homebrew).
  * Om det funkar – då är dotnet installerat, men systemet förstår inte var på hårddisken det ligger. Se nedan.
* Kolla om dotnet finns med i systemets lista med mappar som det letar i efter filer att köra: `echo $path`. Se ifall /usr/local/share/dotnet finns med i listan.
  * Om inte:   
    `cd /etc/paths.d` (går till mappen där infon ska läggas in)  
    `nano dotnet` (öppnar rätt fil i en texteditor)  
    lägg in `/usr/local/share/dotnet` i filen.  
    Ctrl+x för att avsluta, y för att spara.
* Om inte ovanstående funkar: Avinstallera alla dotnet-versioner och börja om
  * Med Brew är det lätt: `brew uninstall dotnet-sdk`
  * Annars – följ instruktionerna här: [https://github.com/dotnet/cli-lab/releases](https://github.com/dotnet/cli-lab/releases)
