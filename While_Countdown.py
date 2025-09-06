# Importiert das 'time'-Modul, um Zugriff auf zeitbezogene Funktionen zu erhalten,
# insbesondere auf time.sleep(), um das Programm zu pausieren.
import time

# Initialisiert eine Variable 'countdown' mit dem Startwert 10.
# Diese Variable wird in der Schleife heruntergezählt.
countdown = 10

# Startet eine while-Schleife, die so lange läuft, wie der Wert von 'countdown' größer als 0 ist.
while countdown > 0:
    # Gibt den aktuellen Wert des Countdowns in einem formatierten String aus.
    print(f"Countdown: {countdown}")
    
    # Verringert den Wert von 'countdown' um 1. Dies ist der Schritt des Herunterzählens.
    countdown -= 1
    
    # Pausiert die Ausführung des Programms für genau eine Sekunde.
    # Dies erzeugt den Effekt eines echten, sekundengenauen Countdowns.
    time.sleep(1)

# Nachdem die Schleife beendet ist (weil 'countdown' 0 erreicht hat),
# wird diese abschließende Nachricht ausgegeben.
print("Zündung!")