# XAML\*

XAML är ett språk som används i bl.a WPF-program för att beskriva det grafiska gränssnittet. Det liknar delvis HTML och andra XML-släktingar, i det att man skapar element genom att använda start- och sluttagar samt attribut som (ofta) skrivs i starttaggarna.

Installera gärna [NoesisGUI XAML-extension](../../mjukvara/visual-studio-code/extensions.md#bonus) i Visual Studio Code för extra hjälp att skriva koden.

## Element

Elementen är UIts byggstenar; de är saker som knappar och textrutor. En del av dem är rena layoutelement, som t.ex. StackPanel som man lägger andra element inuti. Varje element kan olika _attribut_. Ibland kallas elementen också _kontroller_. De kan skrivas med start- och sluttagg eller som självavslutande taggar.

```xml
<TextBlock>Kolla här!</TextBlock>
<Button>Klicka på mig!</Button>
```

```xml
<TextBlock Text="Kolla här!" />
<Button Content="Klicka på mig!" />
```

## Attribut

Det finns många olika attribut tillgängliga för olika element. De kan skrivas antingen inuti starttaggen för elementet eller som child-taggar.

```xml
<TextBlock FontSize="28" Text="Kolla här" />
```

```xml
<TextBlock>
  <TextBlock.FontSize>28</TextBlock.FontSize>
  <TextBlock.Text>Kolla här!</TextBlock.Text>
</TextBlock>
```

### x:Name

Ger elementet ett unikt namn

```xml
<TextBlock x:Name="NameText">Hello</TextBlock>
```

### Text/Content

Get elementet ett innehåll, eller en text. Vissa typer av element har text, men de flesta har Content istället.

```xml
<TextBlock Text="Hello"/>
```

### FontSize

Anger textens storlek.

```xml
<TextBlock FontSize="56" Text="Hello"/>
```

### Margin

Lägger till utrymme kring elementet.

```xml
<TextBlock Margin="10">Hello</TextBlock>
```

## Events

Varje element har ett antal events som kod kan reagera på – t.ex. att en knapp klickas på eller att en kryssruta kryssas i eller ur.

Ett sätt att göra detta är genom att ange event i XAML och sedan ha en matchande metod i fönstrets cs-fil.

{% code title="MainWindow.xaml" %}
```xml
<Button x:Name="mainButton" Click="OnMainClick" Margin="10">What</Button>
```
{% endcode %}

<pre class="language-csharp" data-title="MainWindow.xaml.cs"><code class="lang-csharp"><strong>private void OnMainClick(object sender, RoutedEventArgs e)
</strong>{
  MessageBox.Show("Yes");
}
</code></pre>

Genom att analysera **sender** kan man få veta mer – om t.ex. en och samma metod anropas från flera olika objekt kan det vara bra att veta vilket.

```csharp
if (sender is FrameworkElement obj)
{
  MessageBox.Show(obj.Name);
}
```

### Eventbindning i kod

För att helt separera kod från XAML kan man sköta bindningen i C# istället. Det gör också att man kan få flera olika metoder att anropas när en event sker.

Man behöver en referens till objektet; den kan man t.ex. skaffa genom att använda FindName för att hitta objektet man vill lägga till en bindning till, och casta objektet till rätt datatyp.

Sedan utnyttjar man att alla events ligger inlagda i datatypen som [delegates](../../grundlaeggande/delegates.md).

```csharp
if (FindName("mainButton") is Button button)
{
  button.Click += (object sender, RoutedEventArgs e) => {
    MessageBox.Show("Yes");
  };
}
```

## FindName

En metod som letar igenom alla sub-objekt efter något med angivet `x:Name`. Det man får som resultat är alltid bara ett generellt object, så resultatet behöver castas.

```csharp
if (FindName("mainButton") is Button button)
{
  button.Content = "New text for button";
}
```

## &lt;Button>

En knapp som man kan klicka på. Har Click-event.

```
<Button Click="ClickTheButton">Click Me</Button>
```

## &lt;TextBlock>

Ett block som innehåller text.

```
<TextBlock Text="Hello" FontSize="56" />
<TextBlock>Goodbye</TextBlock>
```

## &lt;StackPanel>

En container-panel som används för att stapla andra element.  Orientation avgör i vilken riktning; default är Vertical (elementen staplas uppifrån och ner).

Man kan lägga in vilka element som helst i en StackPanel – inklusive andra StackPanels.

```xml
<StackPanel Margin="10" Orientation="Horizontal" Spacing="10">

</StackPanel>
```

## &lt;CheckBox>

Kryssrutor, där flera kan vara ikryssade samtidigt. Har eventen Checked och Unchecked.

```xml
<CheckBox>Candle</CheckBox>
<CheckBox>Sword</CheckBox>
<CheckBox>Shield</CheckBox>
```

## &lt;RadioButton>

Liknande Checkbox, men bara en kan vara ifylld i taget. Bra när användare ska få välja mellan olika saker, och bara får välja en av dem. Har också eventen Checked och Unchecked.

```xml
<RadioButton>Warrior</RadioButton>
<RadioButton>Mage</RadioButton>
<RadioButton>Rogue</RadioButton>
```

## &lt;Image>

Lägger in en bild! Har attributen Source, Width och Height som kan vara användbara. Source behöver deklareras som en [resursfil](../../filhantering/resursfiler.md), eller på annat sätt placeras i samma mapp som exe-filen när programmet kompilerats.

```xml
<Image Width="200" Height="200" Source="cat.jpg" />
```

## &lt;ListBox>

En lista med text-items dit man kan lägga in nya saker eller ta bort gamla. Det finns C#-metoder för att manipulera listans innehåll, och ett SelectionChanged-event som kan bindas till C#-kod. SelectionMode-attributet används för att göra det möjligt för användare att markera flera saker i listan samtidigt.

{% code title="MainWindow.xaml" %}
```xml
<ListBox x:Name="list" SelectionMode="Multiple">
  <ListBoxItem>Health Potion</ListBoxItem>
  <ListBoxItem>Broadsword</ListBoxItem>
  <ListBoxItem>Vase with flowers</ListBoxItem>
</ListBox>
```
{% endcode %}

{% code title="MainWindow.xaml.cs" %}
```csharp
if (FindName("list") is ListBox listBox)
{
  listBox.SelectionChanged += (object sender, SelectionChangedEventArgs e) =>
  {
    MessageBox.Show(listBox.SelectedItems.Count.ToString());
  };
}
```
{% endcode %}

## &lt;Grid>\*

<pre class="language-xml"><code class="lang-xml">&#x3C;Grid>
  &#x3C;Grid.RowDefinitions>
    &#x3C;RowDefinition/>
    &#x3C;RowDefinition/>
  &#x3C;/Grid.RowDefinitions>
  &#x3C;Grid.ColumnDefinitions>
    &#x3C;ColumnDefinition/>
    &#x3C;ColumnDefinition/>
  &#x3C;/Grid.ColumnDefinitions>
  
  &#x3C;TextBlock Grid.Row="1" Grid.Column="1">Hello&#x3C;/TextBlock>
<strong>&#x3C;/Grid>
</strong></code></pre>

### &lt;Grid.Rowdefinitions>

```xml
<Grid.RowDefinitions>
  <RowDefinition Width="200"/>
  <RowDefinition Width="auto"/>
  <RowDefinition Width="*"/>
</Grid.RowDefinitions>
```

### &lt;Grid.Columndefinitions>

```xml
<Grid.ColumnDefinitions>
  <ColumnDefinition Width="200"/>
  <ColumnDefinition Width="auto"/>
  <ColumnDefinition Width="*"/>
</Grid.ColumnDefinitions>
```

### Element i ett grid

När man lägger in andra element i ett grid, så anger man vilken kolumn och vilken rad, alltså vilken position, elementet ska läggas i genom Grid.Row och Grid.Column.

```xml
<TextBlock Grid.Row="0" Grid.Column="1">Hello</TextBlock>
```
