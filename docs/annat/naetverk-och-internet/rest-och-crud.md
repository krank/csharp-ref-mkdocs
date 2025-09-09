# CRUD, HTTP och REST

Se [Databaser ](../databaser/)och framför allt [CRUD](../databaser/#crud).

## HTTP

HyperText Transfer Protocol. En standard för att föra över information via nätverk. Är grunden till internet.

HTTP bygger på request-response-modellen:

1. Klienten skickar ett request-meddelande till servern. I det specifieras vad det är man vill göra och vilken resurs man vill göra det med. Till exempel: hämta en specifik html-fil eller läsa av en specifik pryl ur en databas.
2. Servern svarar med ett response-meddelande. I det specifieras vad resultatet blev när servern försökte utföra det klienten bad om.

### Header och body

Varje HTTP-meddelande består av en header och en body. Bodyn kan vara tom, och det är den ofta när man t.ex. försöker hämta en hemsida som inte finns eller när man inte försökte hämta något alls.

Headern innehåller allmän data och information om meddelandet. Här finns till exempel info om vilken version av HTTP som används, serverns/klientens mjukvara, när meddelandet skickades etc.

Request-meddelanden innehåller alltid en "metod" – motsvarar ungefär verb. Metoden avgör vilken sorts operation det är man försöker göra – POST, PUT, GET etc.

Response-meddelanden innehåller alltid en respons-kod som talar om ifall requesten lyckades eller om något gick fel. Det kan t.ex. vara kod 200 ("ok") eller 404 ("not found").

### POST

Används för att skicka in en ny resurs till en server.

### GET

Används för att hämta en resurs från en server.

### PUT

Används för att ersätta en resurs som redan finns på en server med en ny resurs.

### DELETE

Används för att ta bort en resurs från en server.

## REST

REST är en förkortning av Representational State Transfer. Förenklat kan man säga att REST innebär att man utför [CRUD-operationer](../databaser/#crud) med hjälp av HTTP-kommandon på ett standardiserat sätt.

| CRUD   | HTTP   |
| ------ | ------ |
| Create | POST   |
| Read   | GET    |
| Update | PUT    |
| Delete | DELETE |

Så för att till exempel läsa/hämta information om en specifik artikel så kan man i ett REST-API skicka en HTTP-request med GET som metod till https://www.somenews.net/api/articles/45 och då får man ett HTTP-response som innehåller artikel nummer 45s data.

Och för att lägga in en ny artikel skulle man då kunna skicka en HTTP-request med POST som metod till http://www.somenews.net/api/articles. Då skulle man också inkludera den nya artikelns data i requesten. Som svar skulle man då kunna få ett HTTP-response med statuskoden Ok, och då vet man att artikeln lagts till.

Exakt hur requests ska se ut beror på vad den som bygger servern bestämmer. Det finns inget automatiskt i att det är just /api/articles som gäller, det skulle lika gärna kunnat vara /cyberzone/fluff/gauntlet eller vad som helst.
