# Inställningar

Under Settings (Kugghjulet och sen Settings, eller kortkommandot Ctrl+, ) finns en hel massa användbara inställningar.

![](../../images/image-19.png)

Man kan antingen bläddra själv, eller söka efter namnet på den inställning man vill ändra.

VS Code sparar alla inställningar i en JSON-fil, där varje inställning har ett unikt namn. Om man vill kan man redigera denna JSON-fil manuellt. För att få fram den, ta fram kommandopaletten (F1) och kör **Preferences: Open User Settings (JSON)**.

## Få bort "ghost text" för textförslag

En störande sak Code börjat göra är att visa förslag som grå text mitt i ens kod. Vill man inte att det  ska funka så, så kan man söka efter **editor.suggest.preview** och kryssa ur rutan.

## Kör/debugga i external terminal

I vanliga fall visas all output från koden i Visual Studio Codes egna interna terminalfönster. Det är inte idealiskt, så den här inställningen gör så att koden istället körs i ett separat terminalfönster.

Sök efter **csharp.debug.console** och ändra inställningen till "externalTerminal".

## Få bort "references"

Sök efter **csharp.referencesCodeLens.enabled**, och kryssa ur "Csharp › References Code Lens: Enabled".

## Visa mappar ordentligt

VS Code gillar att visa mappar "kompakt". Det betyder att den "sammanfattar" mappstrukturer i vissa fall, så att trädet under Explore blir konstigt.

> <img src="../../images/image (26).png" alt="" data-size="original">   
> _Med compact folders_

> <img src="../../images/image (27).png" alt="" data-size="original">   
> _Utan compact folders_

* För att stänga av det – sök efter **explorer.compactFolders** och kryssa ur "Explorer: Compact Folders".

## Sortera filer enligt svensk bokstavsordning

VS Code sorterar normalt sett å och ä som om de vore "a" och ö som om det vore "o".

Sök på **explorer.sortOrderLexicographicOptions** och välj "unicode" i dropdown-listan. DÅ sorteras istället å, ä och ö som de ska längst ner i listan.

## Automatiskt pusha commits

För att få VS Code att automatiskt göra en Git Push direkt efter varje Commit (se [Git](../git-and-github/) för mer info om commit och push):

Sök efter **git.postCommitCommand** och välj Push eller Sync istället för None.

## Settings.json

I .vscode-mappen kan det finnas en "settings.json", och om det inte finns en kan du skapa en. Där kan du samla inställningar du vill spara. Man kan alltså ha inställningar antingen per dator eller per projekt.

{% code title="settings.json" %}
```json
{
  "csharp.referencesCodeLens.enabled": false,
  "csharp.debug.console": "externalTerminal",
  "explorer.compactFolders": false,
  "explorer.sortOrderLexicographicOptions": "unicode",
  "git.postCommitCommand": "push"
}
```
{% endcode %}
