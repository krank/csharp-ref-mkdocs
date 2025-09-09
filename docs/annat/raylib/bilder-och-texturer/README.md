# Bilder och texturer

## Bilder och texturer

I Raylib skiljer man på _Images_ och _Textures_.

Skillnaden är att Images kan _redigeras_. Textures kan _ritas ut till skärmen_.

### Filformat som stöds

* png
* bmp
* tga
* gif (dock ej animationer)
* dds, hdr, ktx, astc

!!! info

	**Observera** att det saknas stöd för jpg – detta eftersom jpg är väldigt ovanligt i spel.
	

!!! info

	**Observera** att alla bilder är [**resursfiler**](../../../filhantering/resursfiler.md). Det betyder att du måste[ krångla lite](../../../filhantering/resursfiler.md#loesning-3-kopiera-filerna-automatiskt-till-malmappen) för att vara säker på att programmet kan hitta dem.&#x20;
	

## [Texture](texture.md)

En Texture är en bild som är sparad i grafikkortets minne (VRAM), och är redo att ritas ut på skärmen. Man kan skapa en Texture utifrån en [Image ](./#image)eller läsa in en bildfil från hårddisken direkt.

## [Image](image.md)

En Image är en bild som är sparad i datorns arbetsminne (RAM), och kan redigeras på olika sätt.

För att man ska kunna rita ut den till fönstret behöver man sedan konvertera den till en [texture](./#texture). Det gör man genom [LoadTextureFromImage](./#loadtexturefromimage).



