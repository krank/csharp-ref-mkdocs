# Threading

!!! info

	**OBSERVERA:** Threading är definitivt överkurs och ingår varken i Programmering 1 eller 2.
	

Threading innebär att kod kan köras asynkront – det vill säga att två bitar kod exekveras samtidigt, i olika "trådar" i CPUn. Vanliga användningsområden inkluderar:

* Se till så att ett grafiskt gränssnitt inte låser sig medan det väntar på svar från något på internet, eller på att något laddas in från hårddisken.
* Dela upp något som kräver mycket datorkraft på flera processorkärnor, och därmed utnyttja datorns kraft mer effektivt.

Normalt körs ett C#-program bara i en enda tråd. Det betyder att den bara körs på en enda processorkärna – en kärna kan köra flera trådar, men en tråd kan inte delas upp på flera kärnor.

Om det arbete en tråd utför är väldigt tungt så begränsas tråden av sin processor – det syns till exempel i att en processorkärna arbetar till 100% medan övriga knappt gör något alls. Vill man då öka hastigheten på körningen behöver man dela upp arbetet på flera processorer.

**Den stora nackdelen** med threading är att det blir svårt att dela data på ett säkert sätt mellan olika delar av programmet. Om två trådar till exempel försöker komma åt samma resurs finns risk att något går fel.

## Debugging

När man debuggar ett program som använder threading, så kan man under Call Stack se alla trådar som körs. Standard är att huvudtråden för programmet heter "Main Thread". Andra trådar visas som "&lt;No Name>" om man inte gett dem ett namn via [Name](./#name)-propertyn.

![](../../images/image-9.png)

Om trådarna inte syns under Call Stack, testa att klicka på några av variablerna under Variables så bör de dyka upp.

##
