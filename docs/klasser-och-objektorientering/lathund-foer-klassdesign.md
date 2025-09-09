# Lathund för klassdesign

## Klasser

* Vilka SAKER finns i programmet/spelet?
  * Spelarkaraktär, Fiender, Powerups, Andra objekt, Level/spelplan, Grafiska knappar
* Varje klass ska ha namn i **singular**, även om det finns flera i programmet/spelet.
  * Powerup, Player, Enemy, Football, BaseballBat
* Varje klass beskriver en **kategori** av saker.

### Underkategorier

* Är det liten skillnad mellan sakerna? Använd olika **instanser av samma klass**.
* Är det stor skillnad, framför allt i metoderna? Skapa nya klasser och använd **arv**.

### Variabler

* Vilka EGENSKAPER hos de olika sakerna är relevanta för spelet?
  * Position, Styrka, intelligens, Hit points
* En egenskap som bara är ett enkelt värde (int, strint, float etc) bör vara en **variabel**.
  * Exempel: namn, hit points
* En egenskap som är mer komplex, och i sig har en massa egenskaper/funktionalitet bör vara en referens till en **instans av en klass**.
  * Exempel: ett svärd, som har skadevärde, vikt etc
* Variabler kan leda till djupa hierarkier.
  * I en instans av klassen Game finns en instans av Scene, i instansen av Scene finns en instans av Player…

### Metoder

* Vilken kod hör samman med varje SAK?
  * Vilken kod använder enbart eller mestadels variabler som tillhör klassen?
* Vad ska varje SAK kunna göra?
* Metoder = verb, saker man kan göra med en instans eller som instansen kan göra.

### Public/private/protected

* Public, private och protected används för att skapa **gränssnittet ut mot världen**.
* Saker som ska kunna kommas åt utifrån – **public**.
  * Variabler – helst inte public alls. Använd [properties](inkapsling-och-properties.md) istället.
* Saker som bara ska kunna påverkas från metoder som tillhör den här klassen – **private**.
* Saker som ska kunna påverkas av metoder som tillhör den här klassen och klasser som ärver från den – **protected**.
