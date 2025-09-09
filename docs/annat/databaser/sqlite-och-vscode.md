# SQLite och VSCode

Visual Studio Code har inget inbyggt stöd för SQLite, men det finns såklart bra extensions:

* [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) - gör att man kan öppna och utföra kommandon/queries mot en SQLite-databas

## Öppna en databas

Högerklicka på en sqlite-fil eller en db-fil och välj "Open database".

![](../../images/image-1.png)

Man kan också "öppna" tomma filer som SQLite-databaser – genom att sedan köra [CREATE TABLE](sqlite-kommandon.md#create-table) så görs den tomma filen till en databas.

När databasen är öppnad bör det dyka upp en "SQLite Explorer"-flik:

![](../../images/image-2.png)

Databasen i exemplet ovan innehåller en tabell som heter users, som i sin tur har kolumnerna id och name.

## Stäng en databas

Högerklicka på databasen i SQLite Explorer och välj "Close database".

## Köra ett kommando

Högerklicka på antingen databasen eller en av tabellerna i SQLite Explorer och välj "New query". För tabellen kan man välja mellan två färdigifyllda query-mallar: en för [INSERT INTO](sqlite-kommandon.md#insert-into) och en för [SELECT](sqlite-kommandon.md#select).

Det du får är en ny textfil som innehåller antingen ett tomt utrymme där du kan skriva en query, eller en ny textfil med förifyllda kommandon du kan redigera.

![](../../images/image-3.png)

För att köra queryn, tryck på F1 och kör "SQLite: Run Query". Om det du körde var en SELECT-query bör resultatet nu dyka upp i ett sidofönster.

## Skapa en databas

Skapa en tom fil, som du döper till något som slutar med .sqlite, t.ex. "database.sqlite".

Öppna filen som en databas, enligt ovan.

Högerklicka på databasen i SQLite, välj "New Query".

Lägg till en tabell genom att skriva in kommandot för CREATE TABLE.

Tryck F1 och välj "SQLite: Run Query".

## Titta på en tabell

Se till att databasen är öppnad.

Högerklicka på tabellen i SQLite Explorer, välj "Show Table".

