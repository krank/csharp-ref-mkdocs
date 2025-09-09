# Lathund – koda WPF-applikationer

## Appens fönster

```xml
<Window ...
        Title="MinApp"
        MaxWidth="800" MaxHeight="450"
        SizeToContent="WidthAndHeight">
    <!-- Innehållet i fönstret -->
</Window>
```

## Vanliga kontroller och attribut i XAML

### Layoutkontroller – StackPanel
En layoutkontroll som ordnar sina barnkontroller i en vertikal eller horisontell stapel.  

```xml
    <StackPanel Background="#EEE" Orientation="Horizontal">
        <!-- Barnkontroller -->
    </StackPanel>
```

### Vanliga kontroller

```xml
<Label Margin="10" FontSize="24" Foreground="#FFF">Ange ditt namn</Label>
<Button Margin="10" Padding="10" Background="Red" FontWeight="Bold" Width="100">Spara</Button>
<TextBox Margin="10" Padding="10" Height="100"></TextBox>
<ListBox Margin="10" Padding="10"></ListBox>
```

Andra användbara attribut för `TextBox`-kontrollen:
- `ReadOnly="True"` – gör textfältet skrivskyddat
- `TextWrapping="Wrap"` – gör att texten bryts om den är för lång för att få plats i fältet
- `AcceptsReturn="True"` – gör att användaren kan trycka på Enter för att skapa en ny rad

## Koppla kontroller till C#-kod

### click-event och event-metoder
När en användare klickar på en knapp utlöses ett `click`-event. 

```xml
<Button Click="KlickSpara" Margin="10" Padding="10">Spara</Button>
```

```csharp
void KlickSpara(object sender, RoutedEventArgs e)
{
    MessageBox.Show("Du sparade dina ändringar!");
}
```

### Referens till kontroller: Name-attributet
Med `Name`-attributet kan vi referera till kontroller i C#-koden:

```xml
<TextBox Name="txbResultat" Margin="10" Padding="10"></TextBox>
```

```csharp
// Läs innehållet i textfältet
string innehall = txbResultat.Text;

// Sätt nytt innehåll i textfältet
txbResultat.Text = "Nytt innehåll visas här!";
```

### Visa en list i en ListBox
Innehållet i en lista kan visas i en `ListBox`-kontroll:

```xml
<ListBox Name="lbResultat" Margin="10" Padding="10"></ListBox>
```

```csharp
List<string> namnLista =["Anna", "Bertil", "Cecilia"];

// Sätt listan som källa för ListBox-kontrollen
lbResultat.ItemsSource = namnLista;

// Uppdatera ListBox-kontrollen med ny data
lbResultat.Items.Refresh();
```