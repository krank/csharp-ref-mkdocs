# JSON-serialisering

[JSON ](../filformat/json.md)är Javascript Object Notation, så för den som är van vid Javascript kanske det ser bekant ut.

[Här hittar du Microsofts officiella dokumentation.](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-how-to)

## Bibliotek

Lägg till detta using-statement:

```csharp
using System.Text.Json;
```

## Klassdesign

Klassen vars instanser ska kunna serialiseras/deserialiseras måste vara public.

{% code title="Pokemon.cs" lineNumbers="true" %}
```csharp
public class Pokemon
{
  public string name {get; set;}
  public int id {get; set;}
  public bool is_default {get; set;}
}
```
{% endcode %}

Vad som inkluderas i serialiseringen är:

* Publika [properties](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties) med publika get och set
* Variabler och properties som det står \[JsonInclude] framför

Om du ska deserialisera JSON-kod som du får från något annat ställe och inte designat själv, så behöver du vara noga med att **matcha namnet** på dina publika variabler/[properties ](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties)mot JSON-kodens. Serialiseringsprocessen är normalt känslig vad gäller stora och små bokstäver, men du kan ändra på detta (rekommenderas!).

=== "Pokemon.cs"

	```csharp
	public class Pokemon
	{
	  public string name {get; set;}
	  public int id {get; set;}
	  public bool is_default {get; set;}
	}
	```
	

=== "Ditto.json"

	```json
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
	

## JsonSerializer.Serialize<>()

Används för att serialisera ett objekt till en JSON-string.

{% code lineNumbers="true" %}
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
{% endcode %}

Denna string kan sedan lagras i en textfil eller t.ex. skickas som svar på ett [REST](../../annat/naetverk-och-internet/restful-client.md)-anrop.

### JsonSerializerOptions

Genom att skicka in ett JsonSerializerOptions-objekt kan man ge mer detaljerade instruktioner till serializern.

```csharp
JsonSerializerOptions options = new ()
{
  // Ger snygg, indenterad JSON-kod
  WriteIndented = true,
  // Omvandlar alla property-namn till snake_case
  PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower // döper om properties
};

string json = JsonSerializer.Serialize<Pokemon>(poke, options);
```

I JSON används oftast snake\_case, medan C# ju använder [camelCase eller PascalCase](../../grundlaeggande/namngivning.md#pascalcase-och-camelcase).

!!! warning

	**OBS:** SnakeCaseLower introducerades i dotnet 8!
	

## JsonSerializer.Deserialize<>()

Används för att deserialisera ett objekt från en JSON-string.

{% code lineNumbers="true" %}
```csharp
// jsonString innehåller json-data. Den kan t.ex. läsas in från en json-fil
// eller hämtas från en REST-server.
Pokemon ditto = JsonSerializer.Deserialize<Pokemon>(jsonString);
```
{% endcode %}

## Attribut

Mer om attribut [här](../../klasser-och-objektorientering/attribut.md).

!!! warning

	**OBS:** dessa kräver att du inkluderar `System.Text.Json.Serialization`.
	

### \[JsonInclude]

Används för att inkludera en variabel eller property i Json-serialiseringen

```csharp
using System.Text.Json.Serialization;

public class Pokemon
{
  [JsonInclude]
  public string Name;
  
  [JsonInclude]
  public bool IsDefault;
}
```

### \[JsonIgnore]

Används för att se till så att en variabel eller property på C#-sidan inte serialiseras till JSON.

{% code title="Pokemon.cs" lineNumbers="true" %}
```csharp
using System.Text.Json.Serialization;

public class Pokemon
{
  public string Name {get; set;}
  public bool IsDefault {get; set;}
  
  [JsonIgnore]
  public int CurrentHp {get; set;}
}
```
{% endcode %}

### \[JsonPropertyName()]

Med attributet `[JsonPropertyName()]` kan man bestämma att en C#-klass' property ska matchas mot ett JSON-värde med annat namn.

{% code title="Pokemon.cs" lineNumbers="true" %}
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
{% endcode %}

## Deserialisering av listor

Ibland beskriver JSON-kod listor av objekt eller värden. De kännetecknas av att ge omges av hakparenteser `[]`.

{% code lineNumbers="true" %}
```json
{
  "name": "ditto",
  "forms":
  [
    "Ditto",
    "Exempel"
  ]
}
```
{% endcode %}

För att deserialisera dessa, skapa helt enkelt publika [listor ](../../grundlaeggande/listor-och-arrayer.md#list)i klassen.

{% code title="Pokemon.cs" lineNumbers="true" %}
```csharp
class Pokemon
{
  [JsonPropertyName("name")]
  public string Name {get; set;}
  
  [JsonPropertyName("forms")]
  public List<string> Forms {get; set;}
}
```
{% endcode %}

## Deserialisering av objekt i flera led

Ibland beskriver JSON-kod objekt som innehåller andra objekt.

{% code lineNumbers="true" %}
```json
{
  "name": "ditto",
  "species":
  {
    "name": "ditto",
    "url": "https://pokeapi.co/api/v2/pokemon-species/132/"
  }
}
```
{% endcode %}

För att deserialisera dessa, skapa klasser som beskriver de inre objekten.

{% code title="PokemonSpecies.cs" lineNumbers="true" %}
```csharp
class PokemonSpecies
{
  [JsonPropertyName("name")]
  public string Name {get; set;}
  
  [JsonPropertyName("url")]
  public string Url {get; set;}
}
```
{% endcode %}

{% code title="Pokemon.cs" lineNumbers="true" %}
```csharp
class Pokemon
{
  [JsonPropertyName("name")]
  public string Name {get; set;}
  
  [JsonPropertyName("species")]
  public PokemonSpecies Species {get; set;}
}
```
{% endcode %}
