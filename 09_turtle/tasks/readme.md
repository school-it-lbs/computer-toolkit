# Turtle

Turtle ist ein Python Modul um Bilder in 2D zu zeichnen.

## Modul laden

Module können mit dem Befehl __import__ eingebunden werden, wenn sie auf dem Computer installiert sind.  
__turtle__ ist ein Standardmodul und ist bei der Installation von Python dabei.

```python
import turtle
```

## Fenster erstellen

Um zu Zeichnen erzeugen wir ein __Turtle__ Objekt.  

- turtle (kleingeschrieben) ist der Package-Name, 
- Turtle (großgeschrieben) ist "Constructor" um ein Objekt zu erzeugen

Diese Anwendung wird ein Fenster öffnen mit einem Zeiger (der _Turtle_) in der Mitte.

```python
import turtle

pen = turtle.Turtle()

turtle.done()
```

| Code |  Kommentar | 
|-|-|
| `turtle.Turtle()` | Erzeugt ein Turtle-Objekt |
| `pen` | Variable das auf Objekt zeigt. Name ist beliebig, hier "pen" für "Zeichenstift"  |
| `turtle.done()` | Wir sind mit Zeichnen fertig und übergeben die Kontrolle an das Fenster. Verhindert das es direkt geschlossen wird, |

> siehe Script: __01_window.py__

zum starten in der Konsole:
```console
py .\01_window.py
```

## Erste Zeichnung

Nachdem wir ein Turtle-Objekt erzeugt haben können wir Zeichenbefehle geben.  
Diese Befehle werden nacheinander ausgeführt und wir können den Stift beim zeichnen zusehen.  
Es können nur Zeichenlänge in Pixel und Drehungen in Grad angegeben werden.

```
pen.forward(100)
pen.left(90)
pen.forward(100)
```

Hier sagen wir das eine 100 Pixel lange Linie gezeichnet werden soll. Dann soll sich der Zeiger 90 Grad nach Links drehen und erneut 100 Pixle zeichnen.

> siehe Script: __02_line.py__

| Befehl | Parameter | Kommentar |
|-|-|-|
| `forward()` oder `fd()` | Pixel | gehe n Pixel weiter |
| `backward()` oder `bk()` |  Pixel | gehe n Pixel zurück |
| `left()` oder `lt()` | Grad | drehe n Grad nack Links |
| `right()` oder `rt()` | Grad | drehe n Grad nack rechts |

### Aufgabe 1
- Zeichne eine Kiste
- Optional: Benutze eine Schleife

## Koordinatensystem

Turtle startet in dem Mitte vom Fenster bei X,Y Koordinate 0,0  
Um z.B. unten Links zu zeichnen wäre die Kordinate x = -100, Y = -100

> siehe Script: __03_coord.py__

In diesen Script wurden Zeichenbefehle in Funktionen ausgelagert (z.B. `draw_line()`).

Es werden auch weitere Befehle verwendet:

| Befehl | Kommentar |
|-|-|
| `stamp()` | Macht einen "Stempel" vom Zeiger |
| `position()` | Gibt die aktuelle Position vom zeiger zurück |
| `write()` | Schreibt Text auf Bildschirm, siehe unten __Text schreiben__ für Details |
| `home()` | Schicke den Zeiger zurück zum Ursprung, hier x=0 y=0 |
| `hideturtle()` | Verstecke den Zeiger |
| `goto()` | Schicke Zeiger zu Koordindaten x,y |
| `color()` | Setze die Stiftfarbe, siehe unten __Farben__ für Details |
| `dot()` | Zeichne einen n Pixel großen Punkt |

### Text schreiben
```python
pen.write(f" pos: {pen.position()}", font=("Courier", 12, "bold"))
```
- der erste Parameter ist der Text
    - hier wird ein "formattierter String" (_f-string_) verwendet  
    der Präfix __f__ erlaubt die Verwendung von Platzhaltern mit __{ }__
- der zweite Parameter setzt die Schriftart
    - der Parameter ist Optional und wird mit dem Namen des Parameters aufgerufen, hier __font__
        - "Courier" ist eine Schriftart
        - 12 ist die Schriftgröße
        - "bold" = fette Schrift

### Farben

Es können Farben mit Namen oder Hex-Code gesetzt werden

| Code | Farbe | 
| - | - |
| "red" | rot |
| "black" | schwarz | 
| "#cccccc" | grau | 
| "#006269" | "petrol" |


### Aufgabe 2
- Setze einen blauen Punkt an Koordinate x=80 y=70


## Kreise Zeichnen

Mit dem Befehl `circle` können Kreise gezeichnet werden.  
Der Parameter gibt den Durchmesser an.
Optionale Parameter `extent` gibt an wie weit der Kreis gezeichnet werden soll. 
`steps` gibt die Zeichenschritte an und erlaubt es z.B. ein Fünfeck zu zeichnen.

```python
pen.circle(100, extent=180, steps=5)
```


> siehe Script: __04_circle.py__

| Befehl | Kommentar |
|-|-|
| `bgcolor()` | setzt die Hintergrundfarbe vom Fenster, siehe __Farben__ |
| `pensize()` | setzt die Stiftgröße in Pixel |


### Aufgaben 3

1. Zeichne einen Kreis von 400 Pixel durchmesse  
   - In diesen Kreis zeichnen weitere Kreise mit Durchmesser 300, 200, 100, 50 Pixel
   - Der erste Kreis soll einen Linienbreite von 10 Pixel haben
   - Reduziere die Linienbreite und ändere die Farbe für jeden Kreis

2. Optional (Schwierig): Zeichne die Kreise von Aufgabe 1 in der Mitte des Bildschirms
    - Wichtig: Benutzte die Befehle `penup()` und `pendown()` um den Stift zu bewegen ohne das eine Linie gezeichnet wird


## Flächen füllen

Mit `fillcolor()` wird eine Füllfarbe definiert.  
Zeichenbefehle zwischen den Aufrufen `begin_fill()` und `end_fill()` werden ausgefüllt.

```python
t.fillcolor("orange")

t.begin_fill()
# ...
t.end_fill()

```
__Hinweis:__ Die Zeichnung muss nicht abgeschlossen werden. Es wird die Fläche vom Start- bis Endpunkt ausgefüllt

> siehe Script: __05_fill.py__

### Aufgabe 4

1. Zeichne einen gefüllten Rechteck 
2. Zeichne einen beliebigen gefüllten Polygon
3. Optional (Schwierig): Zeichne einen Stern
    - Die Winkel bei einen Stern mit fünf Zacken sind 72 Grad, bzw 144 Grad beim Rotieren
    - Nur die Spitzen werden gefüllt wenn sich die Linien überkreuzen