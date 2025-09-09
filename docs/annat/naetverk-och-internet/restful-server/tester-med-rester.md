# Tester med RESTer

Chrome-pluginet [RESTer](https://chrome.google.com/webstore/detail/rester/eejfoncpjfgmeleakejdcanedmefagga) låter oss göra REST-anrop till servrar utan att programmera en klient.

![](../../../images/image-6.png)

Det är ganska enkelt att använda

* Gå in i RESTer
* Välj din metod, t.ex. GET eller POST
* Skriv in din URL
* Klicka SEND
* Resultatet ser du under Response.

## Skicka JSON-data

Om man ska skicka in data till ett API den här vägen, behöver den skrivas in i RESTers Body-del. 

Antagligen behöver datan också formateras som JSON. Om man till exempel vill POST:a in en ny Pokemon in i exempel-API-servern vars modeller beskrivs under Models/dataklasser så skriver man såhär i Body:

```javascript
{
    "name": "Nyarlathotep"
}
```

Ofta kan man undersöka den output man får från GET för att se hur JSON-datan behöver vara formaterad.

!!! warning

	**OBSERVERA:** Om du skickar in JSON-data, kom ihåg att lägga till en header som säger att Content-Type är "application/json".
	
