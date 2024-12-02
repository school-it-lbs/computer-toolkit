# Aufgaben

## Aufgabe 1: Neuen Gegner hinzufügen

1. In __sprite_module.py__ kopiere die Klasse `class Alien`
2. Benenne die kopierte Klasse in `class Ufo` um
3. Benenne die Konstante `ALIEN_SPEED` um zu `UFO_SPEED` und setze den Wert auf `5`
4. Erstelle eine weitere Konstante `KEEP_DIRECTION_IN_SEC = 1`
5. Im Konstruktor `__init__` ergänze folgende Zeile vor `draw()`
   ```python
    self.heading = [-45, -90, -135]
    self.timer = time.time()
    self.last_heading = self.heading[1]
   ``` 
6. In der Funktion `draw` 
    - ändere `shape` von `turtle` auf `square`
    - entferne den Aufruf `self.sprite.setheading`
    - tausche bei setposition + mit - und anders herum, um die Ufos nicht zu nahe am Rand zu erzeugen
7. Ersetze den Inhalt der Funktion `move` mit
   ```python
    self.sprite.forward(self.BOX_SPEED)
    now = time.time()        
    if(now - self.timer > self.KEEP_DIRECTION_SEC):
        self.timer = now
        self.last_heading = self.heading[random.randint(0, 2)] 
    self.sprite.setheading(self.last_heading)
   ``` 
8. Ganz oben in der Datei ergänze `import time`

### Klasse Ufo

```python
#...
import time
#...

class Ufo:
    UFO_SPEED = 5
    KEEP_DIRECTION_IN_SEC = 1

    def __init__(self, dimensions):
        self.sprite = turtle.Turtle()
        self.dimensions = dimensions
        self.heading = [-45, -90, -135]
        self.timer = time.time()
        self.last_heading = self.heading[1]
        self.draw()

    def draw(self):
        self.sprite.penup()
        self.sprite.turtlesize(1.5)
        self.sprite.setposition(
            random.randint(
                int(self.dimensions.left - self.dimensions.gutter),
                int(self.dimensions.right + self.dimensions.gutter),
            ),
            self.dimensions.top,
        )
        self.sprite.shape("square")
        
        self.sprite.color(random.random(), random.random(), random.random())

    def move(self):
        self.sprite.forward(self.UFO_SPEED)
        now = time.time()        
        if(now - self.timer > self.KEEP_DIRECTION_IN_SEC):
            self.timer = now
            self.last_heading = self.heading[random.randint(0, 2)]                 
        self.sprite.setheading(self.last_heading)
    #...
```

### Als Gegner registrieren

9. Öffne `game_module.py`
10. Ganz oben in der Datei ergänze `import random`
11. Ergänze die Funktion `spawn_enemies`
```python
    # ...
    def spawn_enemies(self):
        if time.time() - self.enemy_timer > self.ALIEN_SPAWN_INTERVAL:
            if(random.randint(0, 10) >= 9):
                enemy = sprite_module.Ufo(self.dimensions)
            else:
                enemy = sprite_module.Alien(self.dimensions)            
            self.enemy_array.append(enemy)
            self.enemy_timer = time.time()
    #...
```

## Weitere Aufgaben

Wähle eins:

- Erstelle einen weiteren Gegnertyp
- Definiere eine neue Waffe, z.B. Super-Bomb das alle Gegner zerstört
- Füge 3 Extra-Leben zum Spiel
