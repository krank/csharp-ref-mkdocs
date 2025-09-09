# Open, close, using

## File.Open()

Används för att skapa en koppling till en fil .

```csharp
FileStream file = File.Open(@"test.txt", FileMode.OpenOrCreate); 
```

Variabeln file blir ett "FileStream"-objekt, som man kan använda för att skriva till eller läsa från filen, i det här fallet test.txt.

FileModes:

* FileMode.Open – öppna en fil som garanterat finns. Kasta felmeddelande FileNotFoundException om den inte finns.
* FileMode.OpenOrCreate – öppna en fil; skapa den om den inte finns.

## Close()

Används för att "stänga" en koppling till en fil och informera operativsystemet om att den nu kan öppnas och användas av andra program igen.

```
file.Close();
```

Det är en mycket bra idé att alltid komma ihåg att stänga sina filer när man är klar med dem.

## Using()

Using gör att man slipper använda Close() – när kodblocket är slut så stängs filen automatiskt.

{% code lineNumbers="true" %}
```
using (FileStream file = File.Open(@"test.txt", FileMode.OpenOrCreate))
{
  /* Gör saker */
}
```
{% endcode %}
