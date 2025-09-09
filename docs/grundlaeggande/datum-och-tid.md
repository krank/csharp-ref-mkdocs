---
description: (Under uppbyggnad)
---

# Datum och tid

## DateTime

Datatyp – mer exakt en [klass ](../klasser-och-objektorientering/klasser-och-instanser.md)– som lagrar tidpunkter.

{% code lineNumbers="true" %}
```csharp
// Datumet 10:e december 1815
DateTime lovelaceBirthday = new DateTime(1815, 12, 10);

// Tidpunkten 14:32:00 på datumet 1969-07-16
DateTime apolloEleven = new DateTime(1969, 8, 16, 14, 32, 0);
```
{% endcode %}

### Egenskaper

Man kan få ut information ur DateTime-objekt genom att läsa av dess egenskaper. (Alla dessa är i själva verket [properties](../klasser-och-objektorientering/inkapsling-och-properties.md#properties).)

{% code lineNumbers="true" %}
```csharp
lovelaceBirthday.DayOfWeek; // vilken dag i veckan det är
lovelaceBirthday.Year;
lovelaceBirthday.Month;
lovelaceBirthday.Day; // Dag i månaden
apolloEleven.Hour; // 14
apolloEleven.Minute; // 32
apolloEleven.Second; // 0
apolloEleven.Millisecond; // 0
```
{% endcode %}

### Metoder

Man kan justera ett DateTime-objekts innehåll genom att anropa dess metoder.

{% code lineNumbers="true" %}
```csharp
// Flytta fram klockan
apolloEleven.AddYears(1);
apolloEleven.AddMonths(2);
apolloEleven.AddDays(14);
apolloEleven.AddHours(2);
apolloEleven.AddMinutes(30);
apolloEleven.AddSeconds(10);
apolloEleven.AddMilliseconds(300);
```
{% endcode %}

Alla dessa kan också användas för att flytta klockan bakåt – då stoppar man helt enkelt in negativa tal.

## DateTime.Now

Tidpunkten _just nu_. (Är egentligen en [static ](../klasser-och-objektorientering/static.md#statiska-variabler)[property](../klasser-och-objektorientering/inkapsling-och-properties.md#properties))

{% code lineNumbers="true" %}
```csharp
// Spara en kopia av tidpunkten "just nu" i variabeln startTime
DateTime startTime = DateTime.Now;
```
{% endcode %}

## TimeSpan

Datatyp som beskriver ett tidsspann, till exempel "tiden mellan 26:e mars 1926 och 27:e februari 2015".

Om man subtraherar en DateTime från en annan DateTime så blir resultatet en TimeSpan.

{% code lineNumbers="true" %}
```csharp
DateTime leonardBirth = new DateTime(1926, 3, 26);
DateTime leonardDeath = new DateTime(2015, 2, 27);

TimeSpan life = leonardDeath - leonardBirth;
```
{% endcode %}

### Tidsenheter i en TimeSpan

{% code lineNumbers="true" %}
```csharp
// Dagar
Console.WriteLine(life.Days); // en int: 32480 hela dagar i spannet
Console.WriteLine(life.TotalDays); // en double, som inkluderar delar av dagar

// Timmar
Console.WriteLine(life.Hours); // Timme-komponenten för spannet. Går mellan -23 och 23.
Console.WriteLine(life.TotalHours); // En double: 779520 hela timmar i spannet

// Minuter
Console.WriteLine(life.Minutes); // Minut-komponenten för spannet. Går mellan -59 och 59.
Console.WriteLine(life.TotalMinutes); // En double: 46771200 minuter i spannet

// Sekunder
Console.WriteLine(life.Seconds); // Timme-komponenten för spannet. Går mellan -59 och 59.
Console.WriteLine(life.TotalSeconds); // En double: 2806272000 sekunder i spannet

// Millisekunder
Console.WriteLine(life.Milliseconds); // Timme-komponenten för spannet. Går mellan -59 och 59.
Console.WriteLine(life.TotalMilliseconds); // En double: 2806272000000 millisekunder i spannet
```
{% endcode %}

## Att mäta tid

Ett vanligt användningsområde för DateTime och TimeSpan är att mäta hur lång tid något tar.

{% code lineNumbers="true" %}
```csharp
DateTime start = DateTime.Now

// Någon tung och jobbig kod körs här

DateTime end = DateTime.Now

TimeSpan span = end - start;

Console.WriteLine("Det tog:");
Console.WriteLine($"{span.Hours} timmar");
Console.WriteLine($"{span.Minutes} minuter");
Console.WriteLine($"{span.Seconds} sekunder");
Console.WriteLine($"{span.Milliseconds} millisekunder");
```
{% endcode %}

