# Filer och mappar

Alla dessa kräver att du först inkluderar System.IO i filen där du vill använda dem.

```csharp
using System.IO;
```

## Filer

### File.Delete()

Tar bort den fil som anges som parameter.

```csharp
File.Delete(@"localfile.txt");
```

### File.Exists()

File.Exists är en metod som returnerar true om filen som anges som parameter existerar, false om den inte gör det.

```csharp
if (File.Exists(@"localfile.txt"))
{
  Console.WriteLine("The file exists!");
}
```

## Mappar

### Directory.CreateDirectory()

Skapa en mapp.

```csharp
Directory.Create(@"Savegames");
```

### Directory.Delete()

Ta bort en mapp.

```csharp
Directory.Delete(@"Savegames");
```

### Directory.Exists()

Kolla om en mapp existerar.

{% code lineNumbers="true" %}
```csharp
if (Directory.Exists(@"Savegames")
{
  /* Stuff */
}
```
{% endcode %}

### Directory.GetFiles()

Hämta en array som innehåller alla filer som finns i en mapp.

{% code lineNumbers="true" %}
```csharp
foreach (string filename in Directory.GetFiles(@"Savegames")
{
  Console.WriteLine(filename);
}
```
{% endcode %}
