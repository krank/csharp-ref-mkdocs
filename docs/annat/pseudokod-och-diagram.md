# Pseudokod och diagram

## Pseudokod

"Pseudo-" beskriver något som ser ut som, men inte riktigt är, något annat – pseudovetenskap är inte vetenskap, men ser ofta ut som vetenskap.

Pseudokod är text som ser ut som kod, och beskriver logik, men som inte är körbar kod. Det finns inga regler för hur pseudokod ska skrivas, utan det är mer ett sätt att planera sin kod innan man skriver den – utan att behöva komma ihåg syntax eller bry sig om exakt hur språket fungerar.

Ett exempel:

> Slumpa ett tal.
>
> Läs in en siffra
>
> Kolla om siffran är lägre än talet
>
> &#x20;   Säg att spelaren måste gissa högre
>
> Kolla om siffran är högre än talet
>
> &#x20;   Säg att spelaren måste gissa högre
>
> Kolla om siffran är exakt rätt
>
> &#x20;   Gratulera spelaren
>
> Om den inte är rätt, läs in en ny siffra

Ingenstans finns några if-satser eller några WriteLines, men det är ändå tydligt att det är en algoritm – och att den skulle kunna skrivas, med lite modifikationer, i C# eller valfritt annat programmeringsspråk.

### Mer formell pseudokod

Det finns de som vill ha mer formaliserad pseudokod. Man lägger sig då närmare "riktig" kod.

> **WHILE** tal ≠ siffra
>
> &#x20;   tal = slump()
>
> &#x20;   **INPUT** siffra
>
> &#x20;   **IF** siffra < tal **THEN**
>
> &#x20;       **OUTPUT** "Du måste gissa högre!
>
> &#x20;   **ELSE IF** siffra > tal **THEN**
>
> &#x20;       **OUTPUT** "Du måste gissa lägre!"
>
> &#x20;   **ELSE**
>
> &#x20;       **OUTPUT** "Grattis!

## Flödesscheman / aktivitetsdiagram

Flödesscheman är ett mer grafiskt sätt att anteckna inför kodning.&#x20;

**Aktiviteter** – Saker som utförs – ritas normalt ut som rektanglar

**Beslut** – punkter där programmet ska göra ett val mellan två (eller flera) alternativ – ritas ut som romber

**Pilar** visar hur flödet går.

<figure><img src="../images/Flödesschema exempel.drawio (1).png" alt=""><figcaption><p>Finns det något sätt att förbättra algoritmen ovan?</p></figcaption></figure>

