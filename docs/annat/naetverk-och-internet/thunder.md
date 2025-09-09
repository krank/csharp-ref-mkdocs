# Thunder

VSCode-pluginet [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) låter oss göra REST-anrop till servrar utan att programmera en klient.

![](../../../images/image-4.png)

Den är ganska enkel att använda.

* Gå till Thunder client i VSCode.
* Välj din metod, t.ex. GET eller POST
* Skriv in din URL
* Klicka SEND
* Resultatet ser du under Response.

## Skicka JSON-data

Om man ska skicka in data till ett API den här vägen, behöver den skrivas in i requestens Body-del. 

Antagligen behöver datan också formateras som JSON. Om man till exempel vill POST:a in en ny Pokemon in i exempel-API-servern vars modeller beskrivs under Models/dataklasser så skriver man såhär i Body:

```javascript
{
    "name": "Nyarlathotep"
}
```

Ofta kan man undersöka den output man får från GET för att se hur JSON-datan behöver vara formaterad.

