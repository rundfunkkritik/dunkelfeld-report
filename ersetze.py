# ersetze.py - ersetzt einen Text in einer Datei, nur wenn er GENAU EINMAL vorkommt.
# Aufruf: python ersetze.py DATEI "alter Text" "neuer Text"
import sys

def main():
    if len(sys.argv) != 4:
        print("Aufruf: python ersetze.py DATEI \"alter Text\" \"neuer Text\"")
        return 2
    datei, alt, neu = sys.argv[1], sys.argv[2], sys.argv[3]
    if not alt:
        print("ABBRUCH: alter Text ist leer.")
        return 1
    # newline='' erhaelt die Zeilenenden (CRLF/LF) unveraendert
    with open(datei, 'r', encoding='utf-8', newline='') as f:
        inhalt = f.read()
    n = inhalt.count(alt)
    if n != 1:
        print(f"ABBRUCH: alter Text kommt {n}x vor (erwartet: genau 1x). Datei unveraendert.")
        return 1
    with open(datei, 'w', encoding='utf-8', newline='') as f:
        f.write(inhalt.replace(alt, neu, 1))
    print(f"OK: 1 Ersetzung in {datei}")
    return 0

if __name__ == '__main__':
    sys.exit(main())