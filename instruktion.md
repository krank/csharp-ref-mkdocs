# Komma igång lokalt


## Instruktion:
- Krävs (typ):
  - Python 3.x
  - VS Code
  - Git
- Forka och klona ner repot
- Öppna mappen i VS Code
  - Acceptera förslag på extensions
- F1 -> Python: Create Environment
- Öppna ny terminal (Ctrl+ö)
  - Förhoppningsvis "Python virtual environment was successfully activated"
- `pip install -r requirements.txt`

## Använda
- Live preview:
  - Öppna ny terminal (Ctrl+ö)
  - `mkdocs serve`
  - Ctrl+klicka på länken (http://127.0.0.1:8000/)
- Lägga in bild/screenshot
  - Kopiera bilden
  - Klistra in med Ctrl+Alt+v
    - Acceptera defaultnamn eller välj eget
    - Nu bör bilden hamna i assets-mappen, och en bild-tagg hamnar i texten
- Klistra in kod: Ctrl+Alt+c (funkar inte jättebra)
- Snippets
  - lncode: kodblock med radnummer & titel
  - admon: inforutor
  - cadmon: kollapsade inforutor
  - tab: tabbat innehåll