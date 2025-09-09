# Operatorer

## Matematiska

### + Addition och konkatenering

{% code lineNumbers="true" %}
```csharp
int x = 4 + 6; // Addition
string s = "hej " + "då" // Konkatenering
string s2 = "Värdet på x är " + x;
```
{% endcode %}

### - Subtraktion.

```csharp
int x = 6 - 4;
```

### / Division.

```csharp
int x = 6 / 3;
```

OBS: Om man delar ett heltal (int eller long) med ett annat heltal blir resultatet alltid ett heltal – decimaler trunkeras bort.

### \* Multiplikation.

```csharp
int x = 2 * 3;
```

### % Modulus

Räknar ut resten.

```csharp
int x = 5 % 2;
```

x blir lika med 1, eftersom det är vad man får kvar när man delat 5 med 2.

## Tilldelning

### = Tilldela ett värde till en variabel

```csharp
i = 6;
```

### += Addera något till variabelns värde.

```csharp
i += 5;
```

### ++ Lägg till 1 till variabelns värde.

```csharp
i++;
```

### -= Subtrahera något från variabelns värde.

```csharp
i -= 5; 
```

### -- Dra ifrån 1 från variabelns värde.

```csharp
i--;
```

## Boolska



### == Lika med

Är operanderna **likadana**?

```csharp
bool x = 4 == 4; // true eftersom 4 är samma som 4
```

### != Inte lika med

Är operanderna **olika**?

```csharp
bool x = 4 != 5; // true eftersom det stämmer att 4 och 5 är olika
```

### > < Större än, mindre än.

```csharp
bool x = 4 > 3;
```

### <= >= Större än eller lika med, Mindre än eller lika med

```csharp
bool x = 4 >= 4; // Blir true eftersom fyra är större än eller lika med fyra

bool y = 3 <= 10;
```

## Logiska

### && And (Och)

True om **båda** operanderna är true, dvs det är true på båda sidorna om &&.

```csharp
bool x = true && true; // resultatet är true
```

```csharp
bool y = true && false; // resultatet är false
```

### || Or (Eller)

True om **minst en** av operanderna är true.

```csharp
bool x = true || false; // true; det räcker om den ena är true.
bool y = false || false; // false
bool z = (3 == 2) || x; // true; x är true även om 3 inte är samma som 2.
```

## Specialoperatorer

### . Member access

Används för att komma åt variabler och metoder som ingår i andra objekt. Varje string har till exempel en inbyggd egenskap, en "medlem", som heter Length.

```csharp
string s = "Hello";
Console.WriteLine(s.Length); // 5
Console.WriteLine("Worlds".Length); // 6
```

### .? Null conditional

Används precis som Member access-operatorn men gör att man inte får ett [runtime-fel](fel.md#runtime-fel-exceptions) ifall objektet är null.

```csharp
string s = null;
Console.WriteLine("Längd: " + s?.Length); // Längd: 
Console.WriteLine("Längd: " + s.Length); // Runtime-fel
```

### ? : Ternary

Ternary-operatorn fungerar som en förkortad if-sats och består av tre delar – ett villkor, ett värde som gäller ifall villkoret är sant och ett värde som gäller ifall villkoret är falskt.

```csharp
int i = 1;

// Om i == 1 så blir name lika med "Micke", annars blir name lika med "Mira".
string name = i == 1 ? "Micke" : "Mira";
```

### ?? Null-coalescing

Null-coalescing-operatorn används när det finns en risk för att ett värde är null, och gör så att ett alternativt värde kan tilldelas.

```csharp
// actualName får samma värde som name, förutsatt att name inte är null.
// om name är null så blir actualName "Micke" istället.
string actualName = name ?? "Micke";
```

