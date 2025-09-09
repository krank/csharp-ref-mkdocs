# Databaser

När det gäller att lagra stora mängder data så används nästan alltid någon form av specialiserad mjukvara för detta. Ett vanligt exempel är MySQL, som körs som ett helt eget databas-serverprogram som olika programmeringsspråk sedan kan kontakta. Ett mer lättanvänt exempel är SQLite, där databaserna är relativt enkla textfiler som kan läsas av genom enkla anrop till ett SQLite-bibliotek. Ingen servermjukvara behöver köras på datorn.

SQL står för Structured Query Language, och alla SQL-språk brukar använda liknande språk. SQLite stöder färre SQL-kommandon än MySQL, men man kan ändå göra det mesta. Se [SQLite-kommandon](sqlite-kommandon.md) för dokumentation

Det finns extensions för Visual Studio Code som gör att man kan [jobba med SQLite-databaser](sqlite-och-vscode.md) utan att skriva C#-kod. Det är praktiskt för att skapa tabeller och förbereda databaser.

Slutligen finns [C#-bibliotek man kan installera via NuGet Gallery](c-och-sqlite.md) för att köra SQL-kommandon mot en specifik SQLite-databas.

## Databas

En traditionell relationell databas består av ett antal tabeller. Varje tabell beskriver en kategori av saker. Det som gör databasen relationell är kopplingarna mellan tabellerna. Om man t.ex. har en tabell med användare, och en tabell med artiklar som användarna skrivit, så lagrar man inte användarnamnet etc för respektive användare i artikel-tabellen. Istället lagrar man användarens unika ID.

### Tabeller

En tabell innehåller data om en kategori av "saker" – man kan till exempel ha en tabell för användare, eller en tabell för highscores. En tabell består av ett antal kolumner och rader.

### Kolumner

Varje kolumn i en tabell beskriver någon egenskap hos de saker som tabellen beskriver. T.ex. kan en kolumn innehålla förnamn, efternamn, användarnamn, lösenord, etc. Varje kolumn ska helst bara innehålla EN kategori av värden, så att varje cell i tabellen i sin tur bara innehåller ETT värde.

### Rader

Varje rad i en tabell beskriver en "sak", till exempel en användare, en artikel, ett highscore eller ett datorspel. Rader kan också kallas **entries**.

### Primärnycklar

För att kunna identifiera en specifik entry i en tabell, behöver man vara säker på att det finns något unikt med varje rad. Den delen som är unik brukar kallas "primärnyckel". I teorin kan vilken kolumn eller kombination av kolumner som helst vara primärnyckel, men i de allra flesta fall ges bara varje entry ett unikt nummer, ett ID, som deklareras som primärnyckel.

### Relation

Ifall man har en tabell vars information behöver refereras i en annan tabell, så säger man att de två tabellerna har en _relation_. Den enklaste formen av relation är en-till-många. Till exempel: En användare kan tillhöra en grupp, men en grupp kan innehålla många användare. Då kan man ha en tabell för grupper och en för användare, och så har man en kolumn i användar-tabellen som beskriver vilken grupp den användaren tillhör – där lagras grupptabellens primärnyckel.

### Normalisering

Normalisering kallas det när man följer ett antal regler designade att göra databasen så lätt att använda som möjligt. Till exempel försöker man att se till så att ingen data finns lagrad på flera ställen.

## CRUD

CRUD – Create, Read, Update och Delete – är de fyra operationer man brukar behöva göra med information som lagras i en databas.

### Create

Lägga till nya saker i en tabell, t.ex. nya användare.

### Read

Läsa av informationen om en sak i en tabell, t.ex. läsa av en användares användarnamn och lösenord för att kolla av mot inloggningsuppgifter.

### Update

Ändra en sak i en tabell, t.ex. byta en användares mailadress.

### Delete

Ta bort en sak ur en tabell, t.ex. ta bort en artikel.
