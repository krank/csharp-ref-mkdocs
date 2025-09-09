# Models/dataklasser

Models, eller modeller, är helt enkelt klasser som används av t.ex. en REST-server för att beskriva information. Ofta beskriver modellerna objekt som lagras i en databas av något slag, men det gås inte in på här.

## Modellklasser/dataklasser

Alla egenskaper som ska returneras av API:t måste vara publika [properties](../../../klasser-och-objektorientering/inkapsling-och-properties.md#properties).

=== "Pokemon.cs"

	```csharp
	public class Pokemon
	{
	  public string Name {get; set;}
	}
	```
	

## Returnera instanser som svar på requests

### JSON-serialiserade instanser

För att en \[HttpGet]-metod ska returnera en JSON-serialiserad version av en instans av en modellklass, behövs två saker: 

* När man deklarerar metoden säger man att den ska returnera ActionResult&lt;Something>, där Something är namnet på klassen vars instanser ska serialiseras.
* När man kör Ok, så lägger man in en instans av den klassen inom parenteserna.

=== "PokemonController.cs"

	```csharp
	namespace WebApplication1.Controllers
	{
	  [Route("api/[controller]")]
	  [ApiController]
	  public class PokemonController : ControllerBase
	  {
	    [HttpGet]
	    public ActionResult<Pokemon> Get()
	    {
	      Pokemon p = new Pokemon();
	      p.Name = "Pikachu";
	
	      return Ok(p);
	    }
	  }
	}
	```
	

Resultatet av ovanstående blir att följande JSON-kod skickas med i HTTP-response-bodyn:

```javascript
{
    "name": "Pikachu"
}
```

### JSON-serialiserade listor med instanser

Nedanstående kod skapar en lista med två pokemons, och returnerar den listan till klienter som anropar servern med ett GET-anrop.

```javascript
namespace WebApplication1.Controllers
{
  [Route("api/[controller]")]
  [ApiController]
  public class PokemonController : ControllerBase
  {
    private static List<Pokemon> pList = new List<Pokemon>()
    {
      new Pokemon() {Name = "Pikachu"},
      new Pokemon() {Name = "Bulbasaur"}
    };

    [HttpGet]
    public ActionResult<List<Pokemon>> Get()
    {
      return Ok(pList);
    }
  }
}
```

### Mer specifika frågor

Om en användare ska kunna stoppa in mer specifik information i sin request, och svaret anpassas efter denna information, så behövs något sätt att läsa av den informationen i Controllern.

När man skapar sin Get-metod så kan man lägga till en `[Route]`, och specificera något som ska bli en variabel mellan måsvingar. Så i nedanstående exempel står det `[Route("{num}")]`, vilket betyder att det är den metoden som ska användas om något anges i slutet av request-url:en – t.ex. att url:en är `/api/pokemon/23`.

Det som står inom {} kommer att tolkas som data, som stoppas in som parameter i metoden – observera att metoden också har en "num". Det nummer som anges i request-url:en kommer alltså at omvandlas till en int och stoppas in som motsvarande parameter.

Hade det stått `[Route("/find/{num}")]` istället, så hade routen matchat t.ex. `/api/pokemon/find/23`. 23 hade fortfarande omvandlats till int-parametern num.

```javascript
namespace WebApplication1.Controllers
{
  [Route("api/[controller]")]
  [ApiController]
  public class PokemonController : ControllerBase
  {
    private static List<Pokemon> pList = new List<Pokemon>()
    {
      new Pokemon() {Name = "Pikachu"},
      new Pokemon() {Name = "Bulbasaur"}
    };

    [HttpGet]
    public ActionResult<List<Pokemon>> Get()
    {
      return Ok(pList);
    }

    [HttpGet]
    [Route("{num}")]
    public ActionResult<Pokemon> Get(int num)
    {
      if (num > 0 && num < pList.Count)
      {
        return Ok(pList[num]);
      }
      else
      {
        return NotFound();
      }
    }
  }
}
```

