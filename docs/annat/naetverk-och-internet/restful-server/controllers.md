# Controllers

Controllers är klasser som kopplar ihop klientens HTTP-requests med serverns data, via lite egen logik.

Nedan – ett exempel på en controller som kopplar ihop GET-requests till url:en som slutar på /api/Something med metoden Get().

```csharp
using Microsoft.AspNetCore.Mvc;

[Route("api/[controller]")]
[ApiController]
public class SomethingController : ControllerBase
{
  [HttpGet]
  public ActionResult Get()
  {
    return Ok("Hej");
  }
}
```

## Attribut

Mer om attribut [här](../../../klasser-och-objektorientering/attribut.md).

### \[ApiController]

Dekorerar en klass. Meddelar API-serversystemet att denna klass är en API Controller och ska kunna ta emot requests.

=== "PokemonController.cs"

	```csharp
	[ApiController]
	public class PokemonController : ControllerBase
	{
	
	}
	```
	

### \[Route("thing")]

Dekorerar en klass eller en metod. Meddelar API-serversystemet att klassen eller metoden ska ta emot requests till en specifik "route". Exempel:

* https://localhost:5001/api/pokemon → routen är "api/pokemon"
* https://www.test.com/hello/world → routen är "hello/world"
* [https://192.168.1.100/number](https://www.google.com/url?q=https%3A%2F%2F192.168.1.100%2Fnumber\&sa=D\&sntz=1\&usg=AFQjCNHmakUtrDd1CIEFI8sA-zNgZhw2XA) → routen är "number"

=== "PokemonController.cs"

	```csharp
	[ApiController]
	[route("hello/world")]
	public class PokemonController : ControllerBase
	{
	
	}
	```
	

När man dekorerar metoder med en Route, så läggs denna till klassens route med snedstreck mellan. I exemplet nedan blir routen som leder till metoden alltså hello/world.

=== "PokemonController.cs"

	```csharp
	[ApiController]
	[route("hello")]
	public class PokemonController : ControllerBase
	{
	  [HttpGet]
	  [Route("world")]
	  public ActionResult Getter()
	  {
	    // Routen till denna metod blir hello/world.
	  }
	}
	```
	

### \[Route("\[controller]")]

När man dekorerar en klass, kan man skriva \[controller] inom hakparenteser inuti sin route. Det betyder att \[controller] i praktiken byts ut mot det som står innan Controller i klassens namn. Övrig text står kvar oförändrad.

=== "AngelController.cs"

	```csharp
	[ApiController]
	[route("creatures/[controller]")]
	public class AngelController : ControllerBase
	{
	  // Routen för denna klass blir creatures/angel.
	}
	```
	

### \[HttpGet]

Registrerar en metod som mottagare av GET-requests.

```csharp
[HttpGet]
public ActionResult Get()
{
  return Ok("Response");
}
```

Man kan också ange olika unika routes för olika Get-metoder. Det gör man genom att skriva in routen inom parenteser direkt i \[HttpGet].

```csharp
[ApiController]
[route("creatures/[controller]")]
public class AngelController : ControllerBase
{
  [HttpGet("all")]
  public ActionResult Get()
  {
    // Ifall användaren skickar en request till routen 
    // creatures/angel/all så kommer den här metoden köras. 
  
    return Ok("Response for your request");
  }

  [HttpGet("n/{num}")]
  public ActionResult Get(int num)
  {
    // Ifall användaren skickar en request till routen 
    // creatures/angel/n/7 så kommer parametern 
    // "num" i den här metoden att få värdet "7".
    return Ok("Response for your request for #" + num);
  }

  [HttpGet("name/{name}")]
  public ActionResult Get(string name)
  {
    // Ifall användaren skickar en request till routen 
    // creatures/angel/name/gabriel så kommer parametern 
    // "name" i den här metoden att få värdet "gabriel".
    
    return Ok("Response for your request for " + name);
  }
```

En \[HttpGet]-metod brukar normalt returnera via Ok(), NotFound(), NoContent() eller BadRequest().

### \[HttpPost]

Registrerar en metod som mottagare av POST-requests. API-servern gör också ett försök att deserialisera inkommande JSON-data (angiven i requestens body) till rätt sorts instans.

```csharp
[HttpPost]
public ActionResult AddPokemon(Pokemon newPokemon)
{
  // Parametern newPokemon innehåller här förhoppningsvis – 
  // om det gick att deserialisera bodyn – 
  // en ny Pokemon-instans.
}
```

Även HttpPosts kan ges route-information precis som HttpGet.

```csharp
[HttpPost("secret")]
public ActionResult AddPokemon(Pokemon newPokemon)
{
  // Den här metoden körs om användaren lägger till /secret i slutet av
  // sin URL.
}
```

En \[HttpPost]-metod brukar normalt returnera via Ok() eller BadRequest().

!!! warning

	**OBSERVERA:** För att servern ska kunna deserialisera inskickad JSON korrekt, måste Content-Type i requesten vara "application/json".
	

### \[HttpPut]

Registrerar en metod som mottagare av PUT-requests. API-servern gör också ett försök att deserialisera inkommande JSON-data (angiven i requestens body) till rätt sorts instans.

Skillnaden mellan POST och PUT är att när någon skickar en POST så förväntar de sig att det alltid ska skapas en ny sak i databasen, men vid PUT förväntar man sig att det bara skapas en ny sak ifall det inte finns en gammal, liknande, som kan uppdateras. Vad som bestämmer ifall det finns en gammal, liknande är du som programmerare. I en Pokemon-databas skulle man t.ex. kunna kolla om det redan finns en pokemon med samma unika ID-nummer.

```csharp
[HttpPut]
public ActionResult UpdatePokemon(Pokemon newPokemon)
{
  // Parametern newPokemon innehåller här förhoppningsvis – 
  // om det gick att deserialisera bodyn – 
  // en ny Pokemon-instans.
}
```

Även HttpPuts kan ges route-information precis som HttpGet.

```csharp
[HttpPut("n/{id}")]
public ActionResult UpdatePokemon(int id, Pokemon newPokemon)
{
  // Den här metoden körs om användaren lägger till /n/ och en siffra 
  // i slutet av sin URL, t.ex. /n/7.
  // Variabeln id får då värde 7.
  // Då kan man t.ex. byta ut den pokemonen som har id 7 mot den som
  // deserialiserats från http-bodyn.
}
```

En \[HttpPut]-metod brukar normalt returnera via Ok(), NotFound(), NoContent() eller BadRequest().

!!! warning

	**OBSERVERA:** För att servern ska kunna deserialisera inskickad JSON korrekt, måste Content-Type i requesten vara "application/json".
	

### \[HttpDelete]

Registrerar en metod som mottagare av DELETE-requests.

```csharp
[HttpDelete("n/{id}"]
public ActionResult DeletePokemon()
{
  // Den här metoden körs om användaren lägger till /n/ och en siffra 
  // i slutet av sin URL, t.ex. /n/7.
  // Variabeln id får då värde 7.
  // Då kan man t.ex. ta bort den pokemon som har id 7 från databasen.
}
```

En \[HttpDelete]-metod brukar normalt returnera via Ok(), NotFound() eller BadRequest().

## ActionResponse-metoder

ActionResponse är en klass som beskriver vanliga HTTP-responses. Genom att använda de här färdiga metoderna, som returnerar färdiga ActionResponse-instanser, kan man göra det enkelt för sig.

Det finns sådana metoder för många HTTP-statuskoder – de nedan är bara exempel.

### Ok()

Ger ett ActionResult med HTTP-koden "ok" (200). Parametervärdet skickas som body.

```csharp
[HttpGet]
public ActionResult Get()
{
  return Ok("Response");
}
```

### Created()

Ger ett ActionResult med HTTP-koden "created" (201). Parametervärdet skickas som body.

Created betyder att servern skapat en ny sak, baserat på den request som skickades.

```csharp
[HttpPost]
public ActionResult AddPokemon()
{
  return Created("Response");
}
```

### NotFound()

Ger ett ActionResult med HTTP-koden "not found" (404). Parametervärdet skickas som body.

Not found betyder att den sak som efterfrågades inte finns.

```csharp
[HttpGet]
public ActionResult Get()
{
  return NotFound("Response");
}
```

### NoContent()

Ger ett ActionResult med HTTP-koden "no content" (202). Parametervärdet skickas som body.

No content betyder att servern tog emot requesten men att det inte finns någon content att visa.

```csharp
[HttpGet]
public ActionResult Get()
{
  return NoContent("Response");
}
```

### BadRequest()

Ger ett ActionResult med HTTP-koden "bad request" (400). Parametervärdet skickas som body.

Bad request betyder att det var något fel på den request klienten skickade till servern, och att servern inte kunde göra något vettigt med den.

```csharp
[HttpGet]
public ActionResult Get()
{
  return BadRequest("Response");
}
```
