# C# och SQLite

Börja med att lägga till NuGet-paketet **Microsoft.Data.Sqlite**. Antingen genom att använda NuGet Gallery eller genom att köra i konsolen:

```powershell
dotnet add package Microsoft.Data.Sqlite
```

## SqliteConnection

En SqliteConnection är ett objekt som är kopplat till en SQLite-databasfil.

```csharp
SqliteConnection connection = new SqliteConnection("Data Source=users.sqlite")
connection.Open();
```

Det är ofta en bra idé att använda ett [using-kodblock](../../filhantering/open-close-using.md#using) för att säkerställa att programmet inte håller kvar kopplingen längre än nödvändigt. Då stängs kopplingen ner säkert i samband med att using.kodblocket avslutas.

```csharp
using (SqliteConnection connection = new SqliteConnection("Data Source=users.sqlite"))
{
  connection.Open();
  // Kod som använder kopplings-objektet
}
```

### CreateCommand()

Skapar ett nytt SqliteCommand-objekt. Se nedan.

```csharp
SqliteCommand command = connection.CreateCommand();
```

## SqliteCommand

Ett SqliteCommand är ett objekt som motsvarar ett [SQLite-kommando](sqlite-kommandon.md). Det har ett textinnehåll i form av själva kommandot, och kan köras på flera olika sätt. Ett SQLiteCommand är alltid kopplat till en SqliteConnection; kommandot skickas alltid till den SQLite-databasen.

### commandText

commandText är kommandotexten som ska köras mot databasen.

```csharp
command.CommandText =
  @"
    SELECT name
    FROM users
  ";
```

### ExecuteNonQuery()

Kör kommandot. Perfekt för t.ex kommandon som lägger in ny information i en tabell. Returnerar en integer som beskriver hur många rader som ändrats, tagits bort eller lagts till.

```csharp
SqliteCommand newUserCommand = connection.CreateCommand();
command.CommandText =
  @"
    INSERT INTO users (name,password,email)
    VALUES('Mikael Bergström','12345','fake@bullshit.com');
  ";

int rowsAffected = command.ExecuteNonQuery();
```

### ExecuteScalar()

Kör kommandot, och returnerar resultatet – men bara första cellen (första kolumnen i första raden). Resultatet returneras som ett object, som dessutom kan vara null ifall operationen inte returnerade något. Med andra ord behövs både [casting ](../../grundlaeggande/typkonvertering.md#casting)och något sätt att hantera nullvärden t.ex. via [null-coalescing](../../grundlaeggande/operatorer.md#null-coalescing).

```csharp
SqliteCommand countCommand = connection.CreateCommand();

countCommand.CommandText =
@"
  SELECT COUNT(*)
  FROM users
";

long result = 0;
object resultObj = countCommand.ExecuteScalar() ?? 0;
result = (long)resultObj;
```

### ExecuteReader()

Kör kommandot, och returnerar en SQLiteDataReader för att läsa av resultatet. Passar bäst för SELECT-kommandon som returnerar flera rader och/eller kolumner.

```csharp
SqliteCommand selectCommand = connection.CreateCommand();

selectCommand.CommandText =
@"
  SELECT (name)
  FROM users
";

using (SqliteDataReader reader = selectCommand.ExecuteReader())
{
  // kod för att läsa datan
}
```

## SqliteDataReader

Ett SqliteDataReader-objekt används för att läsa av ett resultat från en SQL-operation (ofta ett SELECT-kommando), en rad i taget.

Precis som med SqliteConnection-objekt använder man oftast ett [using-block](../../filhantering/open-close-using.md#using) för att se till så att reader-objektet tas bort ordentligt när man är klar med det.

### Read()

Flyttar readerns "läshuvud" till nästa rad, om den finns. Om den inte finns, returneras true.

```csharp
while (reader.Read())
{
  // Kod för att läsa radens data
}
```

### Get?()

Det finns många metoder som börjar med Get – till exempel GetString, GetInt32, GetFloat och GetBoolean. De tar alla emot en integer som parameter, och returnerar datan den nuvarande raden och den kolumn som anges av siffran. De försöker också konvertera (parse) datan till rätt datatyp.

```csharp
while (reader.Read())
{
  // Läser datan i den första kolumnen och tolkar den som en string
  string name = reader.GetString(0);
  
  Console.WriteLine(name);
}
```

### FieldCount

En property som talar om hur många fält (kolumner) resultatet innehåller.

### GetName()

Returnerar namnet på en specifik kolumn i resultatet.

```csharp
for (var i = 0; i < reader.FieldCount; i++)
{
  Console.WriteLine(reader.GetName(i));
}
```

