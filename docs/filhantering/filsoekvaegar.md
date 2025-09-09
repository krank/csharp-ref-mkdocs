# Filsökvägar

## Filsökvägar

En filsökväg i windows kan t.ex. se ut så här:

```
c:\temp\exempel.txt
```

Det betyder:

* Filen finns på enhet C.
* I C finns det en mapp som heter temp.
* I mappen temp finns en fil som heter exempel.
* exempel-filens filändelse är txt.

Med andra ord används \ för att separera enheter, mappar och filnamn. I filnamn används punkt för att separera namn från filändelse.

Eftersom \ redan används som "escape"-tecken i C#, för att t.ex. göra radbrytning \n, så måste man ange filsökvägar så här:

```
string path = @"c:\temp\exempel.txt";
```

@-tecknet gör att \\-tecknen inte tolkas, utan [tas bokstavligt](../grundlaeggande/datatyper/#literal-strings).

### Filer i samma mapp som programmet <a href="#h.p_gkvdjqel-lgi" id="h.p_gkvdjqel-lgi"></a>

När det gäller filer som ligger i samma mapp som programmet så behöver man inte ange mapp eller enhet.

```
string path = @"localfile.txt";
```

För er som läst webbutveckling bör detta vara bekant.
