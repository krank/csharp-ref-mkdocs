# Entity Framework Core

Entity Framework Core är ett ramverk som gör att man slipper skriva SQL-kommandon själv. EF fungerar som en mellanhand – vi kan säga åt EF hur datan som ska sparas ser ut och vad som ska göras med den, och EF förvandlar det till databaskommandon åt oss, och sköter interaktionen med databasen.

## Installation

Kör följande kommando för att installera EF-verktygen på din dator:

```powershell
dotnet tool install --global dotnet-ef
```

Lägg till NuGet-paketet Microsoft.EntityFrameworkCore till ditt projekt via [NuGet gallery](../../grundlaeggande/anvaenda-bibliotek-using.md#nuget-gallery) eller via [kommandot](../../grundlaeggande/anvaenda-bibliotek-using.md#nuget-via-terminalen):

```
dotnet add package Microsoft.EntityFrameworkCore
```

## Modellen

Skapa en klass för varje typ av objekt som ska lagras i databasen. Det enda som lagras i databasen är klassernas [properties](../../klasser-och-objektorientering/inkapsling-och-properties.md#properties). Tillsammans bildar alla dessa klasser "modellen" för databasen.

{% code title="User.cs" %}
```csharp
public class User
{
  public int UserId { get; set; }
  public string Username { get; set; } = "";
  public string Password { get; set; } = "";
}
```
{% endcode %}

Tabellen som skapas för att lagra användare kommer att döpas till samma sak som klassen plus en plural-ändelse (Users). Som primärnyckel för tabellen används första bästa property som antingen heter Id eller klassens namn plus Id.

Modellen kan inkludera [komposition](../../klasser-och-objektorientering/komposition.md), vilket automatiskt leder till att en [relation ](./#relation)skapas i databasen.

{% code title="Group.cs" %}
```csharp
public class Group
{
  public int Id { get; set; }
  public string Name { get; set; } = "";

  // Eftersom relationen är en en-till-många-relation, skapas automatiskt en
  // kolumn i User-tabellen som innehåller rätt grupps Id.
  // Man kan också få samma effekt genom att ha en Group-property i User-klassen.
  public List<User> Members { get; set; } = new();
}
```
{% endcode %}

### Attribut

Man kan använda _attribut_ för att få mer kontroll över databastabellerna som skapas för att motsvara modellen. För att få använda attributen måste man inkludera rätt namespaces:

```csharp
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
```

#### \[Table]

Används för att ange tabellens namn.

```csharp
[Table("UserInfo")]
public class User
{
  // ...
}
```

#### \[Column]

Används för att ange kolumnegenskaper t.ex. namn och vilken ordning kolumnen ska ha i tabellen.

```csharp
public class User
{
  [Column("Id", Order = 1)]
  public int UserId { get; set; }
  
  [Column("Name")]
  public string Username { get; set; } = "";
  
  public string Password { get; set; } = "";
}
```

#### \[NotMapped]

Används för att ange att en viss property inte ska ingå i modellen.

```csharp
public class User
{
  public int UserId { get; set; }
  public string Username { get; set; } = "";
  public string Password { get; set; } = "";

  [NotMapped]
  public string CurrentHitpoints { get; set; }
}
```

#### \[Required]

Används för att ange att en viss property måste ges ett värde och inte får vara tom. Motsvarar [NOT NULL](sqlite-kommandon.md#create-table).

```csharp
public class User
{
  [Required]
  public int UserId { get; set; }
  
  // ... 
}
```

## DbContext

En klass som representerar kopplingen till en databas, och som kommunikationen med database sker genom. Detta kallas en databas-kontext.

Man skapar en egen databaskontext, med egna inställningar, genom att skapa en klass som ärver från DbContext.

{% code title="DatabaseContext.cs" %}
```csharp
public class DatabaseContext : DbContext
{
  public DbSet<User> Users { get; set; }

  protected override void OnConfiguring (DbContextOptionsBuilder optionsBuilder)
  {
    optionsBuilder.UseSqlite("Data Source=ef_users.sqlite");
  }
}
```
{% endcode %}

Sedan skapar man en instans av sin nya DbContext-klass, och via denna instans kan man sedan göra [CRUD-operationer](./#crud) mot databasen.

{% code title="program.cs" %}
```csharp
using (var context = new DatabaseContext())
{
  User user = new User() { Username = "Micke", Password = "12345" };

  context.Users.Add(user);

  context.SaveChanges();
}
```
{% endcode %}

### DbSet

Varje klass som ingår i modellen läggs in som en DbSet-property i klassen som ärver från DbContext.

```csharp
public class DatabaseContext : DbContext
{
  public DbSet<User> Users { get; set; }
  public DbSet<Group> Users { get; set; }
  public DbSet<Post> Users { get; set; }
}
```

### OnConfiguring

För att göra egna inställningar i databas-kontexten, gör en [override ](../../klasser-och-objektorientering/polymorfism/virtual-override.md)av basklassens OnConfiguring-metod.

```csharp
protected override void OnConfiguring (DbContextOptionsBuilder optionsBuilder)
{
  optionsBuilder.UseSqlite("Data Source=ef_users.sqlite");
}
```

Objektet optionsbuilder används sedan för att göra diverse inställningar. Den viktigaste här är UseSqlite, som gör att databaskontexten kommer att kopplas till en SqLite-databas. Där anges också databasens filnamn.

## Migrations

Migrations används för att antingen generera en databasfil från klasser eller tvärtom. När man genererar en databas utifrån klasser kallas det att man arbetar "code first".

För att skapa och köra migrations behöver man använda **terminalen**, och man behöver vara i samma mapp som csproj-filen. I Visual Studio Code kan man med andra ord behöva byta till den mappen, t.ex:

```powershell
PS C:\Programming\EFDemo> cd EFDemo
PS C:\Programming\EFDemo\EFDemo>
```

### Skapa en migration

En migration är, lite förenklat, en _databasförändring_. Det betyder att man gör en stor migration i början när man först skapat sin modell, och sedan kan göra förändringar i form av fler migrationer i efterhand.

```powershell
dotnet ef migrations add CreateDB
```

I exemplet ovan skapas en migration med namnet CreateDB. Alla migrationer behöver ha ett unikt namn. Namnet bestämmer man själv, men undvik mellanslag.

### Uppdatera databasen

När en ny migration skapats behöver databasen uppdateras.

<pre class="language-powershell"><code class="lang-powershell"><strong>dotnet ef database update
</strong></code></pre>

Om modellen uppdateras behöver alltså en ny migration skapas och därefter behöver databasen uppdateras.

## Hämta data

Man hämtar data från databasen genom att använda sig av olika metoder som ingår i respektive DbSet. Ofta används [Linq-metoder](../linq/linq-metoder.md) eller [Linq-queries](../linq/linq-queries.md). Vanligast är [Where](../linq/linq-metoder.md#where).

```csharp
// Hämtar användaren Micke, förutsatt att hans lösenord är 12345.
User u = context.Users.Where(
  u => u.Username == "Micke" &&
  u.Password == "12345")
  .FirstOrDefault();
```

### Include()

När datan som ska hämtas är lagrad i flera tabeller (dvs det finns en [relation](./#relation)), behöver man använda Include() för att den extra datan ska laddas in. Resultatet blir då att [kompositionen ](../../klasser-och-objektorientering/komposition.md)fungerar.

```csharp
// Hämtar grupp 1 & fyller dess Members-lista med instanser av User-klassen
//  som får sin data från Users-tabellen.
Group coolGroup = context.Groups
  .Where(g => g.Id == 1)
  .Include(g => g.Members)
  .FirstOrDefault();
```

### FromSql()

Om man vill kan man skriva sina egna SQL-frågor istället för att gå via Linq. Det gör man då via FromSql-metoden. Den tar emot en formaterbar string som parameter, så använd $ framför första citattecknet. Lägg också till @ ifall du vill dela upp SQL-frågan på flera rader.

```csharp
  User u = context.Users.FromSql(@$"
    Select * 
    from Users 
    where Username = 'Micke' 
    and Password == '12345'
    ").FirstOrDefault();
```

## Modifiera data

När det gäller CUD-operationer (Create, Update och Delete) så innebär de att datan i den lokala databaskontexten först ändras, och sedan måste synkroniseras mot databasen. Synkroniseringen sker via metoden SaveChanges().

```csharp
using (var context = new DatabaseContext())
{
  // Kod som gör ändringar

  context.SaveChanges();
}
```

Körs inte SaveChanges så försvinner alltså ändringarna när programmet avslutas.

### Stoppa in data

Eftersom DbSets är generiska samlingar så är det ganska enkelt att lägga in ny data i dem:

```csharp
using (var context = new DatabaseContext())
{
  User micke = new() { Username = "Micke", Password = "12345" };
  Group group = new() { Name = "Coola klubben" };
  group.Members.Add(micke);

  context.Groups.Add(group);
  context.Users.Add(micke);
  
  context.SaveChanges();
}
```

### Modifiera data

Börja med att hämta det som ska ändras. Ändra på instansen. Det är allt som krävs! Entity Framework håller reda på objekt som hämtats ut, och ser till att synkronisera deras data med databasen automatiskt.

```csharp
using (var context = new DatabaseContext())
{
  User u = context.Users.FromSql(@$"
    Select * 
    from Users 
    where Username = 'Amanda' 
    ").FirstOrDefault();

  u.Password = "password1";
  context.SaveChanges();
}
```

### Ta bort data

Börja med att hämta det som ska tas bort. Använd därefter Remove()-metoden för att ta bort det ur databasen.

```csharp
using (var context = new DatabaseContext())
{
    User u = context.Users.FromSql(@$"
    Select * 
    from Users 
    where Username = 'Micke' 
    ").FirstOrDefault();

  context.Users.Remove(u);
  context.SaveChanges();
}
```
