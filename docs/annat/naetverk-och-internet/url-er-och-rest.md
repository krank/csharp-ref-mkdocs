# URL:er och REST

En URL på internet har kan till exempel se ut såhär:

```
http://test.stapi.co/api/v1/rest/animal?uid=ANMA0000032338
```

Den består av följande delar:

* **Protokollet:** `http`
* **Domänen:** `test.stapi.co`
  * **Domännamn:** `stapi`
  * **Underdomän:** `test`
  * **Toppdomän:** `co`
* **Mappar:** `api, v1, rest`
* **Resurs:** `animal`
* **Parametrar:** `uid=ANMA0000032338`

## REST-endpoint

En "REST-endpoint" är den delen av REST-URL:en som är gemensam för alla anrop till API:et. För Star Trek-API:t är endpointen denna:

```
http://test.stapi.co/api/v1/rest/
```

Den består alltså av protokoll, domännamn och ofta en eller flera mappar.

## REST-resurs

En REST-resurs är den del av databasen eller systemet som API:et ger tillgång till som man vill hämta information från. Ett exempel från Star Trek API:t är t.ex. "animal". Om man då lägger ihop endpoint plus resurs så får man då:

```
http://test.stapi.co/api/v1/rest/animal
```

I vissa API:er används bara endpoints och resurser. I PokeApi till exempel anger man namnet på den pokemon man vill ha information om som en resurs:

```
https://pokeapi.co/api/v2/pokemon/ditto
```

## Parametrar och REST

Parametrar kan ge ytterligare information om t.ex. Det är generellt här man anger sin API-nyckel för databaser som kräver en sådan. Det finns API:er som använder parametrar för att specificera vilken resurs man vill hämta eller modifiera, men det är strikt taget inte riktigt REST då.

Parametrar skrivs genom att man först har ett frågetecken som separerar parametrarna från resten, och sedan par av parameter+värde. Paren separeras från varandra med & och parametern separeras från värdet med ett likamed-tecken.

```
http://stapi.co/api/v1/rest/animal?uid=ANMA0000032338
```
