# RESTful server (Minimal API)

Nedan är instruktioner för att skapa en enkel API-server som svarar på GET-anrop.

[Här finns Microsofts officiella snabbreferens.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis)

## Skapa projektet

Skapa projektets solution som vanligt, men välj **ASP.NET Core Empty** som projekttyp istället för **Console application**.

## Ett minimalt projekt

Nedanstående är ett absolut minimalt, enkelt projekt som helt enkelt skickar "Hello World!" till den som skickar en get-request till programmet:

{% code lineNumbers="true" %}
```csharp
// Skapa en webbapplikation-instans
WebApplication app = WebApplication.Create(args);

// Använd HTTPS när det går
app.UseHttpsRedirection();

// När en GET-request kommer för "/" så svarar servern med det som 
//  returneras från GimmeHello
app.MapGet("/", GimmeHello);

// Kör webbapplikationen
app.Run();

// Metoden som ska köras när någon gör en GET-request
static string GimmeHello()
{
  return "Hello World!";
}
```
{% endcode %}

## WebApplication

WebApplication-objektet är det som sköter kommunikationen över webben och som ser till att anropa rätt metod när rätt HTTP-request skickas till programmet.

### MapGet(), MapPost(), MapPut() och MapDelete()

Dessa metoder kopplar en [HTTP-metod](../rest-och-crud.md) (GET, POST, PUT eller DELETE) och en [REST-resurs](../url-er-och-rest.md#rest-resurs) till en specifik C#-metod. Detta kallas "mapping".

```csharp
app.MapGet("/pokemon/", GimmePokemon);
```

Om någon sedan gör en request till serverns adress, och requesten har metoden GET och inkluderar /pokemon/ (t.ex. **https://localhost:7174/pokemon**, så kommer det response som skickas tillbaka vara det som returneras från GimmePokemon-metoden.

MapGet kopplar till GET-requests, MapPost till POST-requests, MapPut till PUT-requests och MapDelete till DELETE-requests.

C#-metoden kan vara en statisk metod, en instansmetod eller ett [Lambda-uttryck](../../../grundlaeggande/delegates.md#lambdas).

```csharp
app.MapGet("/hello/", () => "Say hello!");
```

### Parametrar

C#-metoden kan förses med parametervärden via URL:en.

```csharp
app.MapGet("/double/{num}/", Double);

static string Double(int num)
{
  return (num * 2).ToString();
}
```

När man i exemplet ovan besöker t.ex. **https://localhost:7174/double/7** så blir det 14 som skickas tillbaka som HTTP-response.

Detta används ofta för att välja vilken data som ska skickas – en parameter kan till exempel vara ett unikt ID eller namnet på ett objekt (en användare eller ett dokument). Då skriver man en metod som letar igenom en lista eller en databas efter rätt ID, och returnerar den datan. Ofta skickas då datan som ett objekt.

### Returnera Objekt som JSON

Om metoden som mappas returnerar ett objekt, så kommer det objektet [serialiseras ](../../../filhantering/serialisering/json-serialisering.md#jsonserializer.serialize-less-than-greater-than)till [JSON ](../../../filhantering/filformat/json.md)innan det skickas tillbaka som ett [HTTP-response](../rest-och-crud.md#http).

{% code title="Hero.cs" %}
```csharp
public class Hero
{
  public string Name { get; set; }
  public int Hitpoints { get; set; }
}
```
{% endcode %}

<pre class="language-csharp"><code class="lang-csharp"><strong>app.MapGet("/hero/superman/", GetSuperman);
</strong>
static Hero GetSuperman()
{
  Hero h = new Hero();
  h.Name = "Superman";
  h.Hitpoints = 100;
  return h;
}
</code></pre>

Resultatet om man skickar en GET-request till **/hero/superman**:

```json
{
  "name": "Superman",
  "hitpoints": 100
}
```

### Skicka in nya objekt via POST/PUT och JSON

För att kunna hantera att nya objekt skickas till serverprogrammet, mappa POST eller PUT till en metod som har en parameter av den datatyp [JSON](../../../filhantering/filformat/json.md)-koden ska [deserialiseras ](../../../filhantering/serialisering/json-serialisering.md#jsonserializer.deserialize-less-than-greater-than)till.

```csharp
app.MapPost("/hero/new/", AddNewHero);

static void AddNewHero(Hero h)
{
  heroList.Add(h);
  Console.WriteLine($"Added hero {} to the list"
}
```

När en användare då skickar in JSON-kod som [body ](../rest-och-crud.md#header-och-body)i sin HTTP-request till servern, så deserialiseras koden automatiskt till en instans av klassen och resultatet hamnar i parametern när metoden anropas.

### Results

För att skicka någon annan statuskod än OK, gör så att C#-metoderna returnerar Results.

```csharp
static IResult GetBatman()
{
  Hero h = new Hero();
  h.Name = "Batman";
  h.Hitpoints = 30;
  return Results.Ok(h);
}
```

Det finns en hel del olika HTTP-statuskoder, till exempel:

* **Results.Ok** – allt gick bra.
* **Results.NotFound** – det du frågade efter fanns inte.
* **Results.BadRequest** – den request du skickade kunde inte tolkas, eller innehöll fel.

## Komma åt servern från andra datorer

Normalt sett kan servern inte kommas åt från andra datorer än den den körs på; den kallas "localhost". För att också kunna komma åt den från andra datorer på samma nätverk, lägg till en URL med wildcard (\*):

```csharp
app.Urls.Add("http://localhost:3000");
app.Urls.Add("http://*:3000");
```

Ovanstående gör att man kan komma åt servern både genom url:en localhost:3000 (på den lokala datorn) och genom att skriva datorns ip-nummer följt av 3000 (på den lokala datorn eller på någonnannan dator på samma nätverk).

## WebApplicationBuilder

Ifall man vill göra något lite mer avancerat med sin WebApplication, så använder man en WebApplicationBuilder för att konstruera den. Buildern fungerar då som en "fabrik" – man skapar den, gör inställningar, och säger sedan åt den att skapa en WebApplication.

```csharp
WebApplicationBuilder builder = WebApplication.CreateBuilder();

// Lägg till funktionalitet för Swagger/OpenAPI
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Bygg själva applikationen
WebApplication app = builder.Build();
```

## Använda HTTPS

Om du får problem med att komma åt din server, via webbläsare eller via klienter skrivna i C#, så kan det här behövas.

Börja med att generera och lägga till ett certifikat för lokal utveckling och debuggning. Kör i terminalen:

```powershell
dotnet dev-certs https
dotnet dev-certs https --trust
```

Lägg sedan till URL:er för https:

```
app.Urls.Add("https://localhost:3000");
app.Urls.Add("https://*:3000");
```

Nu bör HTTPS fungera – åtminstone på din egna dator.
