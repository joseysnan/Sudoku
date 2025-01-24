# README.md

# Sudoku Game

Dieses Projekt ist ein einfaches Sudoku-Spiel, das in Python entwickelt wurde und grundlegende Programmierkonzepte wie objektorientiertes Design, Vererbung und Persistenzierung demonstriert.

## Funktionen
- **4x4-Sudoku:** Eine kleinere Variante des klassischen Sudoku.
- **Spielstand speichern/laden:** Über JSON.
- **Validierung:** Spielerzüge werden geprüft.
- **Tests:** Zwei Tests für gültige und ungültige Züge.
- **Modularisierung:** Der Code ist in mehreren Module aufgeteilt.
- **Interaktivität:** Spieler können Züge in Echtzeit über die Konsole eingeben.
- **Objektorientierung:** Nutzung von Vererbung für klare und wiederverwendbare Logik.


## Projektstruktur
Die Projektdateien sind folgendermaßen organisiert:

sudoku/
│
├── src/
│   └── sudoku_package/
│       ├── sudoku_base.py      # Basisklasse für das Sudoku-Logik-Framework.
│       ├── sudoku_game.py      # Erweiterung der Basisklasse: Spiel-Logik.
│       └── sudoku_main.py      # Startpunkt für das Spiel. Verknüpft alle Module.
│
├── test/
│   └── (Unit-Tests für das Sudoku-Spiel können hier eingefügt werden)
│
├── sudokuenv/                  # Virtuelle Umgebung für das Projekt.
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg              # Konfigurationsdatei für die virtuelle Umgebung.
│
├── LICENSE                     # Lizenz für das Projekt.
├── README.md                   # Dokumentation des Projekts.
├── requirements.txt            # Abhängigkeiten des Projekts.
├── setup.py                    # Installationsskript für das Sudoku-Paket.
└── sudoku.json                 # Beispielhafte JSON-Datei mit einem Sudoku-Rätsel.


## Installation
### Virtuelle Umgebung erstellen
Vorrausstzungen: 
- Python 3.7 oder höher
Es wird empfohlen, eine virtuelle Umgebung zu verwenden:
```bash
python -m sudokuenv env
source env/bin/activate # Mac/Linux
env\Scripts\activate   # Windows
```

### Paket installieren
Führe den folgenden Befehl im Projektordner aus, um das Sudoku-Spiel zu installieren:
```bash
pip install .
```

### Spiel starten
Nach der Installation kann das Spiel mit folgendem Befehl gestartet werden:
```bash
sudoku_game
```

## Nutzung
1. Das Spiel generiert ein 4x4-Sudoku.
2. Der Spieler gibt Züge ein im Format `row column number` (z. B. `0 1 3`).
3. Ungültige Züge werden abgelehnt, und es wird eine Rückmeldung gegeben.
4. Ziel ist es, das Sudoku korrekt zu lösen.
5. Zum Beenden des Spiels kann `quit` eingegeben werden.

## Entwicklung
### Lösungsgenerierung:
 Die Methode `fill_board` generiert mithilfe eines Backtracking-Algorithmus eine vollständige und gültige Sudoku-Lösung.
### Maskierung: 
Die Methode `mask_cells` entfernt zufällige Zahlen aus der Lösung, um ein spielbares Puzzle zu erstellen.
### Vererbung: 
Die Klasse `SudokuBase` enthält allgemeine Methoden, während SudokuGame die Spiellogik implementiert und die Basisklasse erweitert.


## Veröffentlichung
### GitHub
**1.Repository erstellen:** Lade den Quellcode hoch und füge diese README hinzu.
**2. Sicherstellen, dass `README.md`und `setup.py`enthalten sind.:** 

### PyPI
1. **Build erstellen:** Stelle sicher, dass die Datei `setup.py` korrekt konfiguriert ist 
`python setup.py sdist`.
2. **Hochladen:** Nutze Tools wie `twine`, um das Paket hochzuladen:
```bash
twine upload dist/*
```

## Tests
Das Spiel führt automatische Tests durch:
- **Gültiger Zug:** Ein korrekter Zug wird akzeptiert.
- **Ungültiger Zug:** Ein ungültiger Zug wird abgelehnt.

Bei Fragen oder Feedback: jnangmo0@gmail.com