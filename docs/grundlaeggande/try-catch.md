# Try-catch och Exception

## Try och catch

När man lägger in kod i ett try-block så förhindrar det att programmet avslutas när ett runtime-fel inträffar, t.ex. att man försöker konvertera något som inte kan konverteras eller komma åt ett index som inte finns i en array. Kort sagt _försöker_ C# köra koden. Istället avbryts körningen, och programmet hoppar istället ner till det catch-block som står under.

{% code lineNumbers="true" %}
```csharp
int[] nums = {4, 5, 7};

try
{
  Console.WriteLine(nums[8]); // Orsakar ett IndexOutOfRange-fel
}
catch
{
  Console.WriteLine("Nope!");
}
```
{% endcode %}

Ett Try-block måste alltid paras ihop med minst ett Catch-block.

## Att fånga specifika fel

När man får ett runtime-fel så talar C# alltid om vad det är för fel.

Om du vill skriva ett catch-block för att fånga ett specifikt fel så specificerar du feltypen inom parenteser.

{% code lineNumbers="true" %}
```csharp
int[] nums = { 4, 5, 7 };

try
{
  Console.WriteLine(nums[8]);
}
catch (System.IndexOutOfRangeException)
{
  Console.WriteLine("Fel index!");
}
```
{% endcode %}

Du kan skriva in flera olika catch-block om du vill:

{% code lineNumbers="true" %}
```csharp
int[] nums = { 4, 5, 7 };

try
{
  Console.WriteLine(nums[8]);
}
catch (System.IndexOutOfRangeException)
{
  Console.WriteLine("Fel index!");
}
catch
{
  Console.WriteLine("Något annat fel!");
}
```
{% endcode %}

## Throw

Om du vill kan du, i dina egna metoder, ge upphov till ett exception som sedan måste catch:as där metoden anropas. På så vis måste du inte hantera alla fel direkt, utan kan sköta allt sådant på ett ställe.

{% code lineNumbers="true" %}
```csharp
static int DoThing(int i)
{
  int[] nums = { 4, 5, 7 };
  
  if (i >= nums.Length || i < 0)
  {
    throw new IndexOutOfRangeException();
  }
  
  return nums[i];
}
```
{% endcode %}

### Kasta upp

Om du catch:ar ett fel du inte vill hantera direkt, så kan du helt enkelt använda **throw** för att tvinga den som anropade den nuvarande metoden att hantera felet.

{% code lineNumbers="true" %}
```csharp
static int DoThing(int i)
{
  int[] nums = { 4, 5, 7 };
  try
  {
    return nums[i];
  }
  catch
  {
    throw;
  }
}
```
{% endcode %}

### Exception-typer är klasser <a href="#h.p_-hpgx_vm4ynb" id="h.p_-hpgx_vm4ynb"></a>

`System.IndexOutOfRangeException` är en [klass](../klasser-och-objektorientering/klasser-och-instanser.md), liksom alla andra sorters exceptions. De har alla System.Exception som [basklass](../klasser-och-objektorientering/arv.md). Det gör att man kan fånga in alla exceptions genom att catch:a System.Exception och sedan undersöka felet man fått genom t.ex. `is`.

{% code lineNumbers="true" %}
```csharp
int[] nums = { 4, 5, 7 };
try
{
  Console.WriteLine(nums[8]);
}
catch (Exception e)
{
  if (e is System.IndexOutOfRangeException)
  {
    Console.WriteLine("Indexfel!");
  }
}
```
{% endcode %}
