# Git & GitHub \[…]

Saker som behövs:

* [Visual Studio Code](https://code.visualstudio.com/)
  * `winget install Microsoft.VisualStudioCode`
  * [Gitignore-extension](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)
* [Git](https://git-scm.com/)
  * `winget install git.git`
  * Mac
    * Om Homebrew är installerat: `brew install git`
    * Ingår i Xcode command line tools: `xcode-select –-install`
      * OBS! Inte bara Git, kräver 1–2gb hårddiskutrymme
    * Finns som [standalone installer](https://sourceforge.net/projects/git-osx-installer/files/latest/download).
* Ett konto på [GitHub](https://github.com/).

Kan vara väldigt bra:

* [GitLens-extension](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (lägger till bl.a visuell historik direkt i vscode)

## Första gången efter ny Git-installation

* Gå till **Terminal** i menyn och välj **New terminal**.
* I terminalen som dyker upp längst ner, skriv:
  * `git config --global user.name "Förnamn Efternamn"` , fast med dina namn, och tryck enter.
  * `git config --global user.email "fornamn.efternamn@elev.ga.ntig.se"` , fast med den E-mailadress du registrerade dig med på GitHub, och tryck enter.

## Arbeta med Git (+GitHub) och Visual Studio Code

### Skapa ett projekt och göra det till ett repository + koppla till GitHub (en gång per projekt)

* Se till att ha [git](https://git-scm.com/) installerat, och VSCode-tillägget "gitignore".
* Skapa projektet [som vanligt](../../lathund-skapa-projekt.md).
* Source Control → Initialize Repository.
* Tryck F1 och sök "add gitignore". Välj **Visual Studio**.
* Tryck "Publish Branch"
  * Första gången: Följ instruktionerna för att knyta Visual Studio Code till github-kontot.
    * "The extension 'GitHub' wants to sign in using GitHub" --> Allow
    * Låt VSCode öppna länken i webbläsaren.
    * "Authorize Visual Studio Code to access GitHub".
    * "This site is trying to open Visual Studio Code" --> Open
    * "Allow an extension to open this URI?" --> Open
* Välj "Publish to GitHub **public** repository".
  * Första gången: Följ instruktionerna för att låta Visual Studio Code ladda upp filer.&#x20;
    * GitHub Sign in --> "Sign in with your browser"
    * Godkänn
    * Gå tillbaka till Visual Studio Code.

### Commits (då och då)

* Gör ändringar i projektet.
* Gå till Source Control.
* (Kryssa ur eventuella filer du inte vill ha med i committen.)
* Fyll i en kort Summary.
* Tryck Commit (Ctrl+Enter i Summary-rutan funkar också).

### Push (en gång per lektion)

När du gjort alla commits för denna gång och t.ex. ska stänga av datorn eller lämna lektionen.

* Gå till Source Control
* Tryck Sync Changes.

### Lämna in en Git-länk (en gång per projekt)

* Gå till projektsidan på github.com.
* Kopiera URL:en i adressfältet
* Kopiera länken och lämna in. Numera kan man lägga till länkar direkt i sitt svar i Classroom!

### Göra ett projekt publikt

Om man råkat göra ett projekt privat på GitHub.com…

* Gå till projektsidan på github.com.
* Gå till "Settings".
* Bland knapparna längst ner finns "Make Public".
* Skriv in repots namn för att bekräfta.

### Återgå till den senaste committen

* Gå till Source Control i Visual Studio Code.
* Högerklicka på filen eller filerna du vill återställa.
  * (Du kan markera flera filer genom att klicka på den första filen, hålla nere shift och klicka på den sista filen)
* Välj "Discard changes".

### Ångra den senaste committen

!!! info

	**OBSERVERA:** Kräver [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).
	

* Gå till Source Control i Visual Studio Code.
* Öppna "Commits" i listan under "Changes" för att se en lista med alla commits.
* Högerklicka på den senaste committen.
* Välj "Revert commit".
  * Välj alternativet med "--no-edit".

### Avancerat: gå tillbaka flera commits på en gång

!!! info

	**OBSERVERA:** Kräver [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).
	

* Gå till Source Control i Visual Studio Code.
* Öppna "Commits" i listan under "Changes" för att se en lista med alla commits.
* Högerklicka på den commit du vill gå tillbaka till.
  * Välj "Reset current branch to commit". Välj **Hard**.
* Expandera "changes to pull from Origin on GitHub".
* Högerklicka på den senaste/nyaste committen.
  * Välj "Reset current branch to commit". Välj **Soft**.
* Gör en ny commit. Denna commit kommer nu att innebära en radering av alla ändringar som fanns i alla commits mellan den senaste committen och den du återställde till.



