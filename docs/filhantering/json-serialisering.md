# JSON-serialisering

Serialisering handlar om att ta ett objekt – en instans – och göra om objektet till ren text som kan lagras i en fil eller till exempel skickas via internet. Se nedan för ett exempel på en klass och hur en serialiserad version av klassen skulle se ut.

=== "Spaceship.cs"

	```csharp
	public class Spaceship
	{
	 public int Hp {get; set;} = 100;
	 public int MaxHp {get; set;} = 100;
	 public int Speed {get; set;} = 2;
	}
	```
	

=== "Spaceship.json"

	```javascript
	{
	  "Hp": 100,
	  "MaxHp": 100,
	  "Speed": 2
	}
	```
	

JSON är Javascript Object Notation, så för den som är van vid Javascript kanske det ser bekant ut.

[Här hittar du Microsofts officiella dokumentation.](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-how-to)

## Bibliotek för enkel deserialisering

Lägg till detta using-statement:

```csharp
using System.Text.Json;
```

## Deserialisering av JSON

### Förberedelser

Utgå från den JSON-kod du ska deserialisera.

```javascript
{
  "form_name": "",
  "form_names": [],
  "form_order": 1,
  "id": 132,
  "is_battle_only": false,
  "is_default": true,
  "is_mega": false,
  "name": "ditto",
  "names": [],
  "order": 198, 
  // (...)
}
```

Skapa en publik klass som har publika [properties ](../klasser-och-objektorientering/inkapsling-och-properties.md#properties)som motsvarar de egenskaper du är intresserad av.

=== "Pokemon.cs"

	```csharp
	class Pokemon
	{
	  public string name {get; set;}
	  public int id {get; set;}
	  public bool is_default {get; set;}
	}
	```
	

### JsonSerializer.Deserialize

Används för att deserialisera ett objekt från en JSON-string.

```csharp
Pokemon ditto = JsonSerializer.Deserialize<Pokemon>(jsonString);
```

### Stora och små bokstäver

Properties ska döpas med stor bokstav i C\#, men i json döps egenskaper nästan alltid med liten bokstav. Deserialize är känsligt för skillnader mellan stora och små bokstäver. Det går att stänga av den känsligheten:

```csharp
var options = new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true
};

// Nu kan property-namnen i Pokemon.cs döpas med stor bokstav
Pokemon ditto = JsonSerializer.Deserialize<Pokemon>(jsonString, options);
```

### Manuell matchning av properties

Med \[JsonPropertyName\(\)\] kan man bestämma att en C\#-klass' property ska matchas mot ett JSON-värde med annat namn.

!!! info

	**OBS:** detta kräver att du inkluderar `System.Text.Json.Serialization`.
	

=== "Pokemon.cs"

	```csharp
	using System.Text.Json.Serialization;
	
	class Pokemon
	{
	  public string Name {get; set;}
	  public int Id {get; set;}
	  
	  [JsonPropertyName("is_default")]
	  public bool IsDefault {get; set;}
	}
	```
	

### Deserialisering av objekt i flera led

Ibland beskriver JSON-kod objekt som innehåller andra objekt.

```javascript
{
  "name": "ditto",
  "species":
  {
    "name": "ditto",
    "url": "https://pokeapi.co/api/v2/pokemon-species/132/"
  }
}
```

För att deserialisera dessa, skapa klasser som beskriver de inre objekten.

=== "PokemonSpecies.cs"

	```csharp
	class PokemonSpecies
	{
	  public string Name {get; set;}
	  public string Url {get; set;}
	}
	```
	

=== "Pokemon.cs"

	```csharp
	class Pokemon
	{
	  public string Name {get; set;}
	  public PokemonSpecies Species {get; set;}
	}
	```
	

### Deserialisering av listor

Ibland beskriver JSON-kod listor av objekt eller värden. De kännetecknas av att ge omges av hakparenteser `[]`.

```javascript
{
  "name": "ditto",
  "forms":
  [
    0: "Ditto"
    1: "Exempel"
  ]
}
```

För att deserialisera dessa, skapa helt enkelt publika [listor ](../grundlaeggande/listor-och-arrayer.md#list)i klassen.

=== "Pokemon.cs"

	```csharp
	class Pokemon
	{
	  public string Name {get; set;}
	  public List<string> Forms {get; set;}
	}
	```
	

## Serialisering till JSON

### JsonSerializer.Serialize

Används för att serialisera ett objekt till en JSON-string.

```csharp
  Pokemon poke = new Pokemon()
  {
    Name = "Ditto",
    Id = 132,
    IsDefault = true,
    Species = new PokemonSpecies() {
      Name = "ditto",
      Url = "https://pokeapi.co/api/v2/pokemon-species/132/"
    }
  };

  string json = JsonSerializer.Serialize<Pokemon>(poke);
```

Denna string kan sedan lagras i en textfil eller t.ex. skickas som svar på ett [REST](../grafik/naetverk-och-internet-.../restful-server/)-anrop.

!!! info

	OBS: Det finns inget sätt att automatiskt förvandla namnen på properties till snake\_case, vilket ju ofta används i JSON. Vill du serialisera med snake\_case så får du med andra ord använda JsonPropertyName-attributet.
	

### Användbara SerializationOptions

```csharp
JsonSerializerOptions options = new JsonSerializerOptions() {
  // serialiserar properties med camelCase
  PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
  
  // Gör JSON-koden snygg och läsbar
  WriteIndented = true 
};

string json = JsonSerializer.Serialize<Pokemon>(poke, options);
```

## Användbara attribut

### \[JsonIgnore\]

Används för att se till så att en variabel eller property på C\#-sidan inte serialiseras till JSON.

=== "C\#"

	```csharp
	public class Pokemon
	{
	  public string Name {get; set;}
	  public bool IsDefault {get; set;}
	  
	  [JsonIgnore]
	  public int CurrentHp {get; set;}
	}
	```
	

