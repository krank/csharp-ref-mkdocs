# RESTful client\*

## Snabbstart

Nedanstående exempelkod skapar ett klientobjekt och ett requestobjekt, skickar requesten genom klienten för att få ett response, och deserialiserar response-objektets text till en instans av Pokemon-klassen.

```csharp
using System.Text.Json;

HttpClient client = new HttpClient();
client.BaseAddress = new Uri("https://pokeapi.co/api/v2/");
HttpResponseMessage result = client.GetAsync("pokemon/ditto").Result;
Pokemon p = JsonSerializer.Deserialize<Pokemon>(result.Content.ReadAsStringAsync().Result);

// Alternativ till de två sista raderna:

Pokemon p = result.Content.ReadAsAsync<Pokemon>().Result;
```

## HttpClient

En klass som sköter kommunikationen med API-servern.

```csharp
HttpClient client = new HttpClient();
client.BaseAddress = new Uri("https://pokeapi.co/api/v2/");
```

Skapar ett klientobjekt som kommer att skicka requests till PokeAPI.

BaseAddress behöver egentligen inte ändras, men det är praktiskt ifall man ska göra många anrop till url:er som börjar på samma sätt.

### GetAsync, PostAsync, PutAsync, DelAsync

Dessa metoder används för att skicka en request till en RESTful API-server och leverera resultatet.

Välj rätt metod:

<table><thead><tr><th width="160.33333333333331">Metod</th><th width="139">HTTP-metod</th><th width="245.66666666666669">Aktivitet</th></tr></thead><tbody><tr><td>PostAsync</td><td>POST</td><td>Skapa en ny resurs</td></tr><tr><td>GetAsync</td><td>GET</td><td>Hämta data om en resurs</td></tr><tr><td>PutAsync</td><td>PUT</td><td>Ändra en resurs</td></tr><tr><td>DelAsync</td><td>DELETE</td><td>Ta bort en resurs</td></tr></tbody></table>

Metoderna tar alla emot en url-sträng och returnerar en [Task](../threading/task.md). Denna Task ger sedan ifrån sig, som Result, ett [HttpResponseMessage](restful-client.md#httpresponsemessage).

```csharp
HttpResponseMessage response = client.GetAsync("pokemon/snorlax").Result;
```

Post och Put vill också ha en _body_ – alltså det som ska skickas in.

```csharp
using System.Net.Http.Json;

// ---

// Serialisera snorlax till JSON och skicka som body
JsonContent jsonBody = JsonContent.Create<Pokemon>(snorlax);
HttpResponseMessage response = client.PostAsync("pokemon/snorlax", jsonBody).Result;
```



Många metoder här är [asynkrona metod](../threading/task.md). Med andra ord går det att använda await istället för .Result om man är i en asynkron metod.

```csharp
async string GetPokemon(string pokemonName)
{
  Task<HttpResponseMessage> task = client.GetAsync($"pokemon/{pokemonName}");
  
  // gör något annat medan klienten hämtar resultatet
  
  await task;
  return task.Result;
}
```

## HttpResponseMessage

Ett HttpResponseMessage-objekt innehåller det svar servern skickat tillbaka.

### StatusCode

I response-objektet ingår en StatusCode. Dess datatyp är en [Enum](../../grundlaeggande/datatyper/enum.md) som heter HttpStatusCode och finns i biblioteket System.Net. Dess möjliga värden är alla existerande, definierade statuskoder från HTTP-standarden. Till exempel Ok och NotFound.

```csharp
  if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
  {
    Console.WriteLine("Not found!");
  }
```

För att slippa skriva System.Net hela tiden kan du använda ett using-statement högst upp i filen:

```csharp
using System.Net;
```

### Content

Content är det "innehåll" servern svarat med.

```csharp
// Hämtar content som string-data
string jsonText = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(jsonText);
```

Ofta är Content JSON eller XML-format, och då kan informationen deserialiseras till ett objekt antingen via [JSON-deserialisering](../../filhantering/serialisering/json-serialisering.md#jsonserializer.deserialize-less-than-greater-than) eller [XML-deserialisering](../../filhantering/serialisering/xml-serialisering.md#deserialize).

Om det är JSON så finns ett enklare sätt – inkludera `System.Net.Http.Json` och använd `ReadFromJsonAsync` istället för `ReadAsStringAsync`.

```csharp
using System.Net.Http.Json;

HttpClient client = new();
client.BaseAddress = new("https://pokeapi.co/api/v2/");
HttpResponseMessage response = client.GetAsync("pokemon/snorlax").Result;
Pokemon p = response.Content.ReadFromJsonAsync<Pokemon>().Result;
```

## Kommunicera med en lokal server

Om du vill anropa en lokal server (localhost) men får ett felmeddelande om ett SSL-fel, så kan du kör denna kod i terminalen för att det ska fungera:

```powershell
dotnet dev-certs https --trust
```

## Öppna databas-API:er

* [Pokemon API](https://pokeapi.co/)
* [Digimon API](https://digimon-api.herokuapp.com/)
* [Star Wars API](https://swapi.py4e.com/)
* [Star Trek API](http://stapi.co/)
* Steam-API
  * [Skaffa en API-nyckel](https://steamcommunity.com/dev/apikey)
  * [Dokumentation](https://partner.steamgames.com/doc/webapi)
* [Marvel API](https://developer.marvel.com/) (kräver en del egna efterforskningar och krångel – hög svårighetsgrad!)
