# Swagger och OpenAPI

OpenAPI – även kallat Swagger – är ett sätt att snabbt och enkelt dokumentera det API servern tillhandahåller så att den som försöker använda APIt vet vad som kan göras och hur. Swagger UI get ett grafiskt webbgränssnitt för att förenkla testning av APIt.

Stöd för OpenAPI/Swagger sker i C# normalt genom biblioteket Swashbuckle, som ingår som standard i alla Minimal API-projekt (kolla själv i csproj-filen).

## Lägga till Swagger

Börja med att se till så att WebApplication-objektet har tillgång till rätt Services – EndpointsApiExplorer och SwaggerGen.

```csharp
WebApplicationBuilder builder = WebApplication.CreateBuilder();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Skapa en webbapplikation-instans
WebApplication app = builder.Build();
```

Därefter aktiveras Swagger enkelt genom metoden UseSwagger.

```csharp
app.UseSwagger();
```

Om man bara vill att Swagger ska vara aktiverat medan man utvecklar servern så kan man lägga in UseSwagger i en if-sats:

```csharp
if (app.Environment.IsDevelopment())
{
  app.UseSwagger();
}
```

Om man nu besöker serverns url följt av /swagger/v1/swagger.json så får man en json-representation av serverns endpoints. Den är i första hand tänkt att läsas av andra maskiner (klienter), inte människor.

```json
{
  "openapi": "3.0.1",
  "info": {
    "title": "My awesome server",
    "version": "1.0"
  },
  "paths": {
    "/": {
      "get": {
        "tags": [
          "ApiTest"
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": { }
}
```

## Konfigurera Swagger

Man kan göra inställningar som ändrar metadatan i Swagger-json-datan genom att ändra i AddSwaggerGen-metodanropet:

```csharp
builder.Services.AddSwaggerGen(c =>
  {
    c.SwaggerDoc("v1", new() { 
      Version = "1.0", 
      Title = "My awesome server" });
  }
);
```

Det man lägger till är alltså ett lambda-uttryck som matchar en delegat som tar emot ett SwaggerGenOptions-objekt (c, i det här fallet) som vi sedan kan göra ändringar i. Den ändring vi gör är att vi kör SwaggerDoc-metoden där vi lägger till ett dokument som heter "1.0" i vilken vi ändrar metadatan Version och Title.

## SwaggerUI

För att aktivera Swagger UI, anropa metoden UseSwaggerUI(). Det brukar göras på samma ställe som UseSwagger().

```csharp
app.UseSwagger();
app.UseSwaggerUI();
```

Om man nu besöker serverns URL följt av /swagger så möts man av ett snyggt UI som visar vilka endpoints etc som API:et har. Här kan man dessutom testa API:et.
