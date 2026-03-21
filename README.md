# Game-Softeng-Block-Breaker
Block Breaker game voor Software Engineering KI


# Nederlands 
Block Breaker is een spel, geïnspireerd door Breakout van Atari, waarbij de spelers met een beweegbare paddle een balletje moeten zien te sturen om vijftig steentjes te vernietigen. 
## Het spel opstarten 
#### installatie 
Om het spel te kunnen spelen moet python geïnstalleerd zijn op uw computer. Daarnaast moet u ook pygame, zmq en pyparsing installeren. Dat kan door in de terminal de volgende commando's uit te voeren nadat Python is geïnstalleerd:
`$ pip install pygame`

`$ pip install zmq`

`$ pip install pyparsing`

#### Spelen op de eigen computer
**Server opstarten:**
Als u op één computer Block Breaker wilt spelen, moet u eerst de server opstarten door in de terminal het volgende commando uitvoeren:

`$ python mygame_server.py `

Als het opstarten van de server is gelukt, ziet u de volgende tekst verschijnen op de terminal (versienummers kunnen verschillen):
``` 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '2345' on host '127.0.0.1'.
``` 

**Spelers toevoegen:**
De volgende stap is het toevoegen van spelers aan het spel. Dat kan door in een **nieuw tabblad van de terminal** het volgende commando uit te voeren:

`python mygame_client.py <naam speler>  ` 

Als het toevoegen van een speler is gelukt is, ziet u de volgende tekst verschijnen op de terminal: 
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to port '2345' of host '127.0.0.1'.
```
Daarnaast opent ook een mygame-venster met het startscherm, zodat u kunt beginnen met spelen (zie afbeelding).  Meer spelers toevoegen kan op dezelfde manier als hierboven beschreven. 
![](/screenshot_start_screen.png)






#### Spelen met meerdere computers 
**Voorbereiding**
Als u op meerdere computers tegelijk Block breaker wilt spelen, moet u er allereerst voor zorgen dat alle computers verbonden zijn met hetzelfde wifi-netwerk. Het maakt niet uit of deze verbinding via kabel of draadloos gemaakt wordt. 

Voordat u de server op start moet u eerst het IP-addres achterhalen van de computer waarop u de server wilt starten. 
Afhankelijk van uw operating system kunt u een van de volgende commando's gebruiken om het IP-address op te vragen:

Linux: ` $ ip a `

Windows: `ipconfig `

**Server opstarten**
Zodra u het IP-addres weet, kunt u met het onderstaande commando de server starten. Als port kunt u ieder getal boven 2000 invullen, bijvoorbeeld 2345. 

`$ python mygame_server.py <port>  < uw IP-addres >  ` 

Als het opstarten van de server is gelukt, ziet u de volgende tekst verschijnen op de terminal (versienummers kunnen verschillen):
``` 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '<port>' on host '<IP-adress>'.
``` 

**Spelers toevoegen**
Spelers toevoegen kan door het onderstaande commando uit te voeren, in de terminal van een andere computer op hetzelfde wifi-netwerk of in een nieuw tabblad van de terminal. let hierbij goed op dat de port en het IP-addres overeenkomen met die van de server. 

`python mygame_client.py <naam speler>  <port> <IP-addres server>  ` 

Als het toevoegen van een speler is gelukt is, ziet u de volgende tekst verschijnen op de terminal: 
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to port '<port>' of host '< IP-address >'.
```
Daarnaast opent ook een mygame-venster met het startscherm op de computer van deze speler, zodat u kunt beginnen met spelen.  Meer spelers toevoegen kan op dezelfde manier als hierboven beschreven. 
![](/screenshot_start_screen.png)

## Spelonderdelen
#### paddles:
Elke speler in het spel bestuurt een eigen paddle. Deze paddle kan horizontaal bewegen; naar links (met 'a' of  '<' ) en naar rechts (met 'd' of '>').  Als speler heb je alleen controle over de **acceleratie**  van de paddle,  de paddle rolt dus uit nadat je de keys loslaat. Het doel van de speler is deze paddle onder het balletje te manoevreren. 
#### balletjes 
Met balletjes kan je als speler de steentjes proberen te vernietigen. Het spel begint met een enkel balletje. Door het raken van de gele steentjes, komen er meer balletjes in het spel. Balletjes stuiteren tegen de randen van het speelveld, de paddle en de steentjes, waardoor ze regelmatig van richting veranderen.
#### steentjes
Er zijn in deze versie van Block Breaker in totaal vijf rijen van tien steentjes.  Elk van deze vijftig steentjes heeft een kleur, die de eigenschappen van dit steentje bepalen. Deze kleur wordt willekeurig bepaald aan de hand van een vastgelegde kansverdeling, waardoor de precieze verdeling voor elk potje varieert. 

**groene steentjes:** Deze steentjes worden vernietigd nadat ze één keer door een balletje zijn geraakt. De kans op een groen steentje is 60% . Deze balletjes zijn ieder  1 punt waard.

**blauwe steentjes** Deze steentjes worden vernietigd nadat ze drie keer door een balletje zijn geraakt. De kans op een blauw steentje is 30%. Deze balletjes zijn ieder  5 punten waard.

**gele steentjes** Deze steentjes worden vernietigd nadat ze één keer door een balletje zijn geraakt. Gele steentjes voegen een extra balletje toe aan het spel als ze vertnietigd worden. De kans op een geel steentje is 10% . Deze balletjes zijn ieder 10 punten waard.



## 
# English 