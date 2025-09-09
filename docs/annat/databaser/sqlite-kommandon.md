# SQLite-kommandon

## CREATE TABLE

Skapar en tabell.&#x20;

```sql
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	password TEXT NOT NULL,
	email TEXT NOT NULL
);
```

Ovanstående skapar tabellen **users** med kolumnerna **id**, **name**, **password** och **email**.

* **INTEGER** betyder att kolumnen bara kan innehålla siffror, på samma sätt som en integer-variabel i C#..
* **TEXT** betyder att kolumnen bara kan innehålla text, lite som en string.
* **PRIMARY KEY** betyder att det är värdet i den kolumnen som är unikt och används för att identifiera varje rad.
* **AUTOINCREMENT** betyder att om man lägger till en rad i tabellen utan att ange ett värde för denna kolumn så ges den ett automatiskt nytt värde.
* **NOT NULL** betyder att man inte får lämna kolumnen tom.

<table><thead><tr><th width="86">id🔑</th><th width="134">name</th><th width="153">password</th><th>email</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td></tr></tbody></table>

## DROP TABLE

Raderar en tabell.

```
DROP TABLE users;
```

## ALTER TABLE

Gör ändringar i en existerande tabell

### RENAME

Byter namn på tabellen.

```sql
ALTER TABLE users
RENAME TO students;
```

### ADD COLUMN

Lägger till en ny kolumn

```
ALTER TABLE users
ADD COLUMN twitter_handle TEXT;
```

### DROP COLUMN

Tar bort en kolumn (och all data som finns i den). Fungerar inte för alla kolumner – till exempel kan man inte ta bort de som är primärnycklar.

```
ALTER TABLE users
DROP COLUMN twitter_handle;
```

### RENAME COLUMN

Byter namn på en kolumn

```sql
ALTER TABLE users
RENAME COLUMN name TO username;
```

## INSERT INTO

Lägger till en rad i en tabell.

```sql
INSERT INTO users (name,password,email)
VALUES('Mikael Bergström','12345','fake@bullshit.com');
```

Ovanstående stoppar in en rad i tabellen **users**.

* **(name,password,email)** betyder att det är de tre kolumnerna som värden ska stoppas in i.
* **VALUES('Mikael Bergström','12345','fake@bullshit.com')** betyder att texten "Mikael Bergström" läggs in i den första angivna kolumnen (name), "12345" läggs in i den andra kolumnen (password) och att "fake@bullshit.com" läggs in i den tredje (email).

En av tabellens fyra kolumner, "id", anges inte och får inget värde. Eftersom den är AUTOINCREMENT får den ändå ett värde, automatiskt.

<table><thead><tr><th width="86">id🔑</th><th width="166">name</th><th width="153">password</th><th>email</th></tr></thead><tbody><tr><td>1</td><td>Mikael Bergström</td><td>12345</td><td>fake@bullshit.com</td></tr></tbody></table>

Observera att man använder ' för att avgränsa texter (strings).&#x20;

## SELECT

Hämtar data från en tabell

```sql
SELECT * FROM users;
```

Ovanstående hämtar alla rader och alla kolumner från tabellen.

<table><thead><tr><th width="86">id🔑</th><th width="166">name</th><th width="153">password</th><th>email</th></tr></thead><tbody><tr><td>1</td><td>Mikael Bergström</td><td>12345</td><td>fake@bullshit.com</td></tr><tr><td>2</td><td>Jacob Marley</td><td>money$</td><td>moneyman@scroogemarley.com</td></tr></tbody></table>

```sql
SELECT name,email FROM users;
```

Ovanstående hämtar alla rader, men bara kolumnerna **name** och **email**.

<table><thead><tr><th width="199">name</th><th>email</th></tr></thead><tbody><tr><td>Mikael Bergström</td><td>fake@bullshit.com</td></tr><tr><td>Jacob Marley</td><td>moneyman@scroogemarley.com</td></tr></tbody></table>

### AS

Gör att kolumner kan ges nya namn i resultatet.

```sql
SELECT name AS namn FROM users;
```

<table><thead><tr><th width="199">namn</th></tr></thead><tbody><tr><td>Mikael Bergström</td></tr><tr><td>Jacob Marley</td></tr></tbody></table>

### WHERE

Gör att man kan vara mer specifik med vilken eller vilka rader man vill läsa av.

```sql
SELECT name,email FROM users WHERE id=1;
```

Ovanstående hämtar bara kolumnerna name och email, och bara de rader där kolumnen id har värdet 0.

<table><thead><tr><th width="218">name</th><th>email</th></tr></thead><tbody><tr><td>Mikael Bergström</td><td>fake@bullshit.com</td></tr></tbody></table>

### AND

Gör att man kan sätta ihop flera olika kriterier i en WHERE.

```
SELECT name FROM users WHERE email='fake@bullshit.com' AND password='12345';
```

### COUNT

Räknar antalet rader som innehåller ett värde.

```sql
SELECT COUNT(*) FROM users WHERE id=0;
```

## DELETE

Tar bort en eller flera rader från en tabell, baserat på ett eller flera kriterier.

```sql
DELETE FROM users WHERE id=0;
```

Kriterierna anges via WHERE, precis som för SELECT.

## UPDATE

Ändrar information i en eller flera celler, baserat på ett eller flera kriterier.

```sql
UPDATE users
SET email = 'deep@fake.com'
WHERE id=0;
```

Ovanstående kod ändrar email-kolumnens data till "deep@fake.com" för alla rader där id-kolumnen innehåller en nolla.

<table><thead><tr><th width="86">id🔑</th><th width="166">name</th><th width="153">password</th><th>email</th></tr></thead><tbody><tr><td>0</td><td>Mikael Bergström</td><td>12345</td><td>deep@fake.com</td></tr><tr><td>1</td><td>Jacob Marley</td><td>money$</td><td>moneyman@scroogemarley.com</td></tr></tbody></table>

## Avancerat: Relationer

En viktig funktion i _relationella databaser_, som MySQL eller SQLite, är _relationer_. Relationer är ett sätt att slippa dubletter av data. Ett exempel kan vara en databas där man håller reda på elever och klasser. För varje elev ska databasen hålla reda på förnamn, efternamn och personnummer. För varje klass ska databasen hålla reda på klassens namn och vilken lärare som är klassens mentor.

Dessutom behöver databasen hålla reda på _vilken elev som går i vilken klass_. Var lagras den informationen? Ett sätt vore att ha allting i en enda jättetabell:

**students**

<table><thead><tr><th width="83.33333333333331">id🔑</th><th width="123">name</th><th width="134">surname</th><th width="144">pnumber</th><th width="87">classname</th><th>mentor</th></tr></thead><tbody><tr><td>0</td><td>Mikael</td><td>Bergström</td><td>XXXXXX-XXXX</td><td>TE00A</td><td>Mira Belle</td></tr><tr><td>1</td><td>Mohammad</td><td>Mohammadi</td><td>XXXXXX-XXXX</td><td>TE00B</td><td>Kevin McAllister</td></tr><tr><td>2</td><td>Anna-Karin</td><td>Karlsson</td><td>XXXXXX-XXXX</td><td>TE00A</td><td>Mira Belle</td></tr></tbody></table>

Nackdelen blir att vi får dubletter – klassnamnen och mentorernas namn står dubbelt! För att undvika detta skapar man generellt istället två olika tabeller – en för elever och en för klasser – som har en _relation_.

**students**

<table><thead><tr><th width="85.33333333333331">id🔑</th><th width="132">name</th><th width="134">surname</th><th>pnumber</th><th>classid</th></tr></thead><tbody><tr><td>1</td><td>Mikael</td><td>Bergström</td><td>XXXXXX-XXXX</td><td>1</td></tr><tr><td>2</td><td>Mohammad</td><td>Mohammadi</td><td>XXXXXX-XXXX</td><td>2</td></tr><tr><td>3</td><td>Anna-Karin</td><td>Karlsson</td><td>XXXXXX-XXXX</td><td>1</td></tr></tbody></table>

**classes**

<table><thead><tr><th width="88.33333333333331">id🔑</th><th width="141">name</th><th>mentor</th></tr></thead><tbody><tr><td>1</td><td>TE00A</td><td>Mira Belle</td></tr><tr><td>2</td><td>TE00B</td><td>Kevin McAllister</td></tr></tbody></table>

Här är relationen att kolumnen **classid** i tabellen **students** innehåller siffror som hör ihop med kolumnen **id** i tabellen **classes**. Observera att det är classes-tabellens **primärnyckel** som används.

För att hindra användare från att lägga in icke-giltiga värden classid-kolumnen så kan relationen skrivas in i tabellens definition när den skapas (Det kan INTE göras i efterhand!):

```sql
CREATE TABLE classes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	mentor TEXT NOT NULL
);

CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	surname TEXT NOT NULL,
	pnumber TEXT NOT NULL,
	class_id INTEGER NOT NULL,
	FOREIGN KEY(class_id) REFERENCES classes(id)
);
```

Med andra ord lägger man helt enkelt till `FOREIGN KEY(x) REFERENCES table(y)` för att koppla kolumnen x till kolumnen y i tabellen "table"

## Avancerat: JOIN

Joins är ett sätt att sätta ihop tabeller som har en relation, när man efterfrågar data med SELECT.

<pre class="language-sql"><code class="lang-sql">SELECT students.name AS student_name, classes.name AS class
<strong>	FROM students
</strong>	INNER JOIN classes
<strong>	ON students.classid = classes.id;
</strong></code></pre>

Det finns flera sorters JOIN, men INNER JOIN är den vanligaste. Man anger först som vanligt vilka kolumner man vill ha med, sedan FROM en första tabell. Sedan lägger man till INNER JOIN en annan tabell, och så ON vilka kolumner som ska kopplas ihop.

| student\_name | class |
| ------------- | ----- |
| Mikael        | TE00A |
| Mohammad      | TE00B |
| Anna-Karin    | TE00A |

Observera att man alltså måste specifiera vilken tabell varje kolumn kommer från i första delen av SELECT-kommandot, framför allt när kolumner i båda tabellerna har samma namn.
