# Game-Softeng-Block-Breaker
Block Breaker game voor Software Engineering KI



# Nederlands 
Block Breaker is een spel, geïnspireerd door Breakout van Atari, waarbij de spelers met een beweegbare paddle een balletje moeten zien te sturen om vijftig steentjes te vernietigen. 
## Het spel opstarten 
#### Installatie 
Om het spel te kunnen spelen moet python geïnstalleerd zijn op uw computer. Daarnaast moet u ook pygame, zmq en pyparsing installeren. Dat kan door in de terminal de volgende commando's uit te voeren nadat Python is geïnstalleerd:

`$ pip install pygame`

`$ pip install zmq`

`$ pip install pyparsing`

#### Spelen op de eigen computer
**server opstarten:**

Als u op één computer Block Breaker wilt spelen, moet u eerst de server opstarten door in de terminal het onderstaande commando uitvoeren. Let hierbij op dat u in de juiste directory/folder zit.

`$ python mygame_server.py `

Als het opstarten van de server is gelukt, ziet u de volgende tekst verschijnen op de terminal (versienummers kunnen verschillen):
``` 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '2345' on host '127.0.0.1'.
``` 

**spelers toevoegen:**

De volgende stap is het toevoegen van spelers aan het spel. Dat kan door in een **nieuw tabblad van de terminal** het volgende commando uit te voeren:

`python mygame_client.py <naam speler>  ` 

Als het toevoegen van een speler is gelukt is, ziet u de volgende tekst verschijnen op de terminal: 
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to port '2345' of host '127.0.0.1'.
```
Daarnaast opent ook een mygame-venster met het startscherm, zodat u kunt beginnen met spelen (zie afbeelding).  Meer spelers toevoegen kan op dezelfde manier als hierboven beschreven. 

![](/Screenshot_start_screen.png)






#### Spelen op meerdere computers 
**voorbereiding:**

Als u op meerdere computers tegelijk Block breaker wilt spelen, moet u er allereerst voor zorgen dat alle computers verbonden zijn met hetzelfde wifi-netwerk. Het maakt niet uit of deze verbinding via kabel of draadloos gemaakt wordt. 

Voordat u de server op start moet u eerst het IP-addres achterhalen van de computer waarop u de server wilt starten. 
Afhankelijk van uw operating system kunt u een van de volgende commando's gebruiken om het IP-address op te vragen:

Linux: ` $ ip a `

Windows: `ipconfig `

**de server opstarten:**

Zodra u het IP-addres weet, kunt u met het onderstaande commando de server starten. Let hierbij op dat u wel in de juiste directory/folder zit. Als port kunt u ieder getal boven 2000 invullen, bijvoorbeeld 2345. 

`$ python mygame_server.py <port>  < uw IP-addres >  ` 

Als het opstarten van de server is gelukt, ziet u de volgende tekst verschijnen op de terminal (versienummers kunnen verschillen):
``` 
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '<port>' on host '<IP-adress>'.
``` 

**spelers toevoegen:**

Spelers toevoegen kan door het onderstaande commando uit te voeren, in de terminal van een andere computer op hetzelfde wifi-netwerk of in een nieuw tabblad van de terminal. let hierbij goed op dat de port en het IP-addres overeenkomen met die van de server en dat u de juiste directory gebruikt.

`python mygame_client.py <naam speler>  <port> <IP-addres server>  ` 

Als het toevoegen van een speler is gelukt is, ziet u de volgende tekst verschijnen op de terminal: 
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to port '<port>' of host '< IP-address >'.
```
Daarnaast opent ook een mygame-venster met het startscherm op de computer van deze speler, zodat u kunt beginnen met spelen (zie afbeelding).  Meer spelers toevoegen kan op dezelfde manier als hierboven beschreven. 

![](/Screenshot_start_screen.png)

## Het spel spelen

#### startscherm
Nadat u het spel heeft opgestart, zien u en uw medespelers het startscherm. Onderin zijn de paddles te zien met daarboven de gebruikersnaam van de bijbehorende speler. U kunt alvast wennen aan de bediening door met `a` en `d`  of  `<` en `>` de paddles te bewegen.

U kunt op het startscherm de keuze maken tussen vier 'levels', in volgorde van oplopende moeilijkheidsgraad zijn dat *slow,* *normal,*  *fast* en *very fast*.  Zoals de namen al suggereren, bepaalt dit de snelheid van het balletje.  De standaardinstelling is *normal*. U kunt het gewenste level selecteren met de toetsen `1`, `2`, `3` en `4` of door met uw muis op een van de vier knoppen te klikken. Het geselecteerde niveau wordt groen. 

Met `s` kunt u  het spel starten zodra u daar klaar voor bent. 

#### tijdens het spel

Zodra het spel gestart is, begint het balletje meteen op volle snelheid door het scherm te vliegen. Het is nu aan u en uw medespelers de taak om de paddle(s) op het juiste moment onder het balletje te krijgen, zodat het balletje terugstuitert en niet aan de onderkant uit het scherm vliegt.U beweegt de paddle naar links met `a` of  `<` en de paddle naar rechts met `d` of `>`.  

Op elk moment tijdens het spel kunt u besluiten het spel af te breken en terug te gaan naar het startscherm, dat doet u met `r`.  

Voor elk blokje dat u of uw medespelers vertnietigen krijgt u punten. Het totaal aantal punten wordt linksboven weergegeven. U heeft het spel gewonnen zodra u met het balletje alle steentjes heeft vertnietigd. 
Meer over de verschillende regels en objecten in het spel leest u in het hoofdstuk *spelonderdelen*. 

![](/Screenshot_gameplay.png)

## Spelonderdelen
#### paddles:
Elke speler in het spel bestuurt een eigen paddle. Deze paddle kan horizontaal bewegen; naar links (met `a` of  `<` ) en naar rechts (met `d` of `>`).  De speler heeft alleen controle over de **acceleratie**  van de paddle,  de paddle rolt dus uit nadat de speler de keys loslaat. Het doel van de speler is deze paddle onder het balletje te manoevreren. 
#### balletjes 
Met balletjes kan de speler de steentjes proberen te vernietigen. Het spel begint met een enkel balletje. Door het raken van de gele steentjes, komen er meer balletjes in het spel. Balletjes stuiteren tegen de randen van het speelveld, de paddle en de steentjes, waardoor ze regelmatig van richting veranderen. Alleen als een balletje de onderzijde van het scherm bereikt, verdwijnt het uit het spel.
#### steentjes
Er zijn in deze versie van Block Breaker in totaal vijf rijen van tien steentjes.  Elk van deze vijftig steentjes heeft een kleur, die de eigenschappen van dit steentje bepalen. Deze kleur wordt willekeurig bepaald aan de hand van een vastgelegde kansverdeling, waardoor de precieze verdeling voor elk potje varieert. 

**groene steentjes:** Deze steentjes worden vernietigd nadat ze één keer door een balletje zijn geraakt. De kans op een groen steentje is 60% . Deze balletjes zijn ieder  1 punt waard.

**blauwe steentjes** Deze steentjes worden vernietigd nadat ze drie keer door een balletje zijn geraakt. De kans op een blauw steentje is 30%. Deze balletjes zijn ieder  5 punten waard.

**gele steentjes** Deze steentjes worden vernietigd nadat ze één keer door een balletje zijn geraakt. Gele steentjes voegen een extra balletje toe aan het spel als ze vertnietigd worden. De kans op een geel steentje is 10% . Deze balletjes zijn ieder 10 punten waard.




# English
Block Breaker is a game, inspired by Breakout by Atari, in which players must use a movable paddle to direct a ball in order to destroy fifty blocks.

## Starting the game

#### Installation
To play the game, Python must be installed on your computer. Additionally, you must install pygame, zmq, and pyparsing. You can do this by running the following commands in the terminal after installing Python:

`$ pip install pygame`

`$ pip install zmq`

`$ pip install pyparsing`

#### Playing on your own computer
**Starting the server:**

If you want to play Block Breaker on a single computer, you must first start the server by running the following command in the terminal. Make sure you're in the correct directory. 

`$ python mygame_server.py `

If the server starts successfully, you will see the following text in the terminal (version numbers may vary):
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '2345' on host '127.0.0.1'.
```

**Adding players:**

The next step is adding players to the game. This can be done by running the following command in a **new terminal tab**:

`python mygame_client.py <player name>  `

If a player is added successfully, you will see the following text in the terminal:
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
```
Connecting to port '2345' of host '127.0.0.1'.

Additionally, a mygame window opens with the start screen, allowing you to begin playing (see image). More players can be added in the same way as described above.

![](/Screenshot_start_screen.png)

#### Playing on multiple computers
**Preparation:**

To play Block Breaker on multiple computers simultaneously, all computers must be connected to the same Wi-Fi network.

Before starting the server, you must first find the IP address of the computer on which you want to run the server. Depending on your operating system, you can use one of the following commands to find the IP address:

Linux: ` $ ip a `

Windows: `ipconfig `

**Starting the server:**

Once you know the IP address, start the server with the command below. For the port, you can use any number above 2000, e.g., 2345. 

`$ python mygame_server.py <port>  <your IP address>  `

If the server starts successfully, you will see the following text in the terminal (version numbers may vary):
```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Waiting for clients on port '<port>' on host '<IP-address>'.
```

**Adding players:**

Players can be added by running the following command in the terminal of another computer on the same Wi-Fi network or in a new terminal tab. Make sure the port and IP address match those of the server and that you're using the correct directory. 

`python mygame_client.py <player name>  <port> <server IP address>  `

If a player is added successfully, you will see the following text in the terminal:

```
pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to port '<port>' of host '<IP-address>'.
```
Additionally, a mygame window opens with the start screen on that player's computer, allowing them to begin playing (see image). More players can be added in the same way as described above.

![](/Screenshot_start_screen.png)

## Playing the game

#### Start screen
After starting the game, all players will see the start screen. At the bottom, the paddles are visible with the corresponding player's username above them. You can practice the controls by moving the paddles with `a` and `d` or `<` and `>`.

On the start screen, you can choose between four 'levels', in increasing difficulty: *slow*, *normal*, *fast*, and *very fast*. As the names suggest, the level determines the ball's speed. The default is *normal*. You can select the desired level with keys `1`, `2`, `3`, and `4` or by clicking one of the four buttons with your mouse. The selected level turns green.

Press `s` to start the game whenever you're ready.

#### During the game
Once the game starts, the ball immediately flies across the screen at full speed. You and your fellow players must position the paddle(s) under the ball so it bounces back and does not fall off the bottom of the screen. Move the paddle left with `a` or `<` and right with `d` or `>`.

At any time during the game, you can stop and return to the start screen with `r`.

You earn points for each brick you or your fellow players destroy. The total points are shown in the top-left corner. You win the game once all bricks are destroyed. You can find more information about rules and objects in the game is in the chapter *Game Components*.

![](/Screenshot_gameplay.png)

## Game Components

#### Paddles:
Each player controls a paddle. The paddle moves horizontally: left (with `a` or `<`) and right (with `d` or `>`). Players only control the **acceleration**; the paddle continues moving after releasing keys. The goal is to maneuver the paddle under the ball.

#### Balls:
Balls are used to destroy bricks. The game starts with a single ball. Hitting yellow bricks adds more balls to the game. Balls bounce off the edges of the playing field, the paddle, and bricks, regularly changing direction. A ball only disappears if it reaches the bottom of the screen.

#### Bricks:
In this version of Block Breaker, there are five rows of ten bricks, each with a color determining its properties. Colors are randomly assigned based on a fixed probability distribution, making each game slightly different.

**Green bricks:** Destroyed after one hit. 60% chance. Each worth 1 point.  
**Blue bricks:** Destroyed after three hits. 30% chance. Each worth 5 points.  
**Yellow bricks:** Destroyed after one hit. Add an extra ball when destroyed. 10% chance. Each worth 10 points.

