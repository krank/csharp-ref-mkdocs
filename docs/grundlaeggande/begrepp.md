# Begrepp

## Grundläggande

### Datatyp

En sorts information, till exempel heltal, decimaltal, text, datum, vektor.

### Variabel

En "behållare" som kan tilldelas ett innehåll i form av ett värde. Variabler har alltid en datatyp.

### Sekvens

Kod som körs uppifrån och ner.

### Selektion

En del av koden där körningen kan "hoppa ner" beroende på något villkor, t.ex. genom en if-sats.

### Iteration

En del av koden där körningen kan "hoppa upp" beroende på något villkor, t.ex. genom en while-loop

### Kodblock

Ett stycke kod som avgränsas från resten av programmet genom en { innan blocket och en } efter blocket.

### Metod

Ett namngivet kodblock, lite som ett separat program som kan köras av andra delar av koden.

### Returnering

Att föra ut data ur en metod så att datan kan användas i koden som anropade metoden.

### Parameter

Variabel-liknande, används för att föra in data i metoder. 

### Array

En datatyp som innehåller flera av något, t.ex. flera tal, eller flera texter.

### Scope

Det sammanhang som en variabel eller en metod existerar inom; generellt existerar de bara inom det kodblock där de skapats.

## Objektorientering

### Klass

En ritning för hur en kategori av objekt ska se ut – vilka variabler och metoder de ska innehålla. Exempel: Fiender ska ha hp och kunna förflytta sig.

### Instans

Ett objekt som skapats baserat på en klass. Exempel: en specifik fiende på skärmen.

### Arv

Att man kan låta klasser bygga på varandra. Exempel: en Goomba är en sorts Enemy. Goomba-klassen får alla variabler och metoder som Enemy-klassen har.

### Basklass

En klass som en eller flera andra klasser ärver från.

### Subklass / child class

En klass som ärver från en annan klass.

### Konstruktor

En metod som automatiskt anropas när det skapas en instans av klassen konstruktorn tillhör.

### Inkapsling

Att man "kapslar in" variabler som ingår i en klass, så att de inte kan ändras utifrån direkt – t.ex. att man har en hp-variabel som bara kan ändras genom att man anropas klassens Hurt-metod och bara kan läsas av genom att anropa en GetHP-metod. Detta gör att den som designar klassen kan förhindra att variabeln ges felaktiga värden.

### Polymorfism

Närhelst en instans av en basklass ska lagras, t.ex. i en variabel, så kan man istället ange en instans av en subklass till den basklassen. Exempel: en variabel som har datatypen Enemy kan användas för att lagra instanser av Enemy eller av Goomba, om Goomba är en subklass till Enemy.

## Filhantering

### Fil

En avgränsad bit information på hårddisken som fått ett namn och som ligger i en mapp.

Filnamnet slutar nästan alltid med en punkt och sedan några tecken till, detta är "filändelsen" som Windows och andra operativsystem använder för att bestämma vilket program som ska öppnas när man dubbelklickar på den.

### Mapp

En "behållare" i ett filsystem som kan innehålla filer eller andra mappar.

### Serialisering

Att omvandla ett objekt – ofta en instans av en klass – eller flera till ett strukturerat textformat, t.ex. XML eller JSON.

### Deserialisering

Att omvandla strukturerad text (t.ex. XML eller JSON) som beskriver ett eller flera objekt till en instans av en klass.

## Nätverk

### Klient

Ett program som kontaktar en server för att få tillgång till någon form av tjänst eller information. Används ibland också om datorer som har sådana program installerade.

> **Exempel:** Chrome.

### Server

Ett program som tillhandahåller någon form av tjänst åt klienter. Används ibland också om datorer som har sådana program installerade och som mest finns till för att just tillhandahålla tjänster (och inte t.ex. spelas på).

> **Exempel:** Apache web server

### IP-adress

Address som identifierar en dator på ett nätverk. Ännu är IPv4 vanligast; exempel på IP-adress enligt IPv4 är 192.168.0.1. Fyra siffror 0–255 med punkter mellan. IPv6 har större tal och skriv som fyra grupper av hexadecimala tal t.ex. 2001:db8::8a2e:370:7334.

Vi använder IP-adresser för att bestämma vilken dator vi ska försöka koppla upp oss mot.

### API

Application Programming Interface. Hur program pratar med varandra. Man kan t.ex. säga att PokeApi har ett RESTful API som låter användare hämta information om Pokemons

### REST

REpresentational State Transfer. Beskriver en standard för kommunikation mellan en klient och en server; i vårt fall för att beskriva hur man utför CRUD-operationer på en server med hjälp av HTTP-standarden. Ett API som följer REST-standarden kallas för ett RESTful API.

### CRUD

Create, Read, Update och Delete. De fyra saker man vanligtvis behöver kunna göra med innehållet i en databas eller annan lagring.
