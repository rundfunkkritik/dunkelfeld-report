# dunkelfeld.report — Aufräum- & Doubletten-Prüfliste

Stand: Juli 2026. Alles per GitHub-Weboberfläche machbar (Datei öffnen → Papierkorb-Symbol → „Commit"). Nichts hier wurde automatisch gelöscht — du entscheidest.

## 1. Toter Link auf der Startseite (wichtig, zuerst)
`index.html` verlinkt `dossier-002-jahrzehnte-des-schweigens.html` — **diese Datei existiert nicht** (404).
→ Link ändern auf **`dossier-002.html`** (Titel „Jahrzehnte des Schweigens"). Erledige ich mit, sobald wir index.html anfassen.

## 2. Backup-Dateien löschen (sicher)
- `index-dunkelfeld-info.html` (alte Startseite)
- `index_170626.html` (Backup vom 17.06.)

## 3. Snippets — nur löschen, wenn ungenutzt (vorher prüfen)
Diese werden evtl. per JavaScript in Seiten eingebunden. Erst prüfen, ob ein `fetch(...)`/`include` darauf zeigt:
- `nav-hamburger-snippet.html`
- `suche-share-snippet.html`

## 4. Echte Doubletten (Inhalt schon unter anderem Namen vorhanden)
Kandidaten zum Löschen — die jeweils genannte Datei ist die, die bleibt:

| löschen | bleibt / Grund |
|---|---|
| `artikel-sprache-sichtbarkeit-struktur.html` | = `artikel-015-sprache-sichtbarkeit-struktur.html` |
| `artikel-wie-viele-nuernbergs.html` | = `artikel-023-wie-viele-nuernbergs.html` |
| `linke-gewalt-dunkelfeld.html` | = `artikel-025-linke-gewalt.html` |
| `rechte-gewalt-dunkelfeld.html` | = `artikel-024-rechte-gewalt-nsu-hanau.html` |
| `dunkelfeld_artikel19_fabrik_der_traumata.html` | = `artikel-031-fabrik-der-traumata.html` |
| `dossier-005-dynastien.html` | = `dossier-006-dynastien.html` (gleicher Titel „Die Dynastien") |
| `dunkelfeld_extremismus_geschaeft-1.html` | = `dunkelfeld_extremismus_geschaeft.html` |
| `dunkelfeld_gruenes_kartell_teil2-1.html` | = `dunkelfeld_gruenes_kartell_teil2.html` |
| `dunkelfeld_gruenes_kartell_teil4-1.html` | = `dunkelfeld_gruenes_kartell_teil4.html` |
| `dunkelfeld_justiz_150jahre-1.html` | = `dunkelfeld_justiz_150jahre.html` |
| `dunkelfeld_justiz_150jahre-2.html` | = `dunkelfeld_justiz_150jahre.html` |
| `fachkraefte-widerspruch-1.html` | = `fachkraefte-widerspruch.html` |
| `ifg-transparenz-netzausbau-smartmeter-1.html` | = `ifg-transparenz-netzausbau-smartmeter.html` |
| `kaelte-hitze-mortalitaet-asymmetrie-2.html` | = `kaelte-hitze-mortalitaet-asymmetrie-1.html` |
| `kurswechsel_klimakaste_reisefreiheit-1.html` | = `kurswechsel_klimakaste_reisefreiheit.html` |
| `operation-condor-1.html` | = `operation-condor.html` |
| `bildung-gehorsam-fleischwolf-2.html` | = `bildung-gehorsam-fleischwolf-1.html` (bestätigt: identischer Titel + Textanfang) |

## Tipp: Reihenfolge
1. Toten Link fixen (Pkt. 1)
2. `themen.html` + `fonts.css` + `/fonts/` hochladen
3. Backups (Pkt. 2) löschen
4. Doubletten (Pkt. 4) löschen — pro Datei ein kleiner Commit reicht

Wenn du eine der „bleibt"-Dateien schon von außen verlinkt hast, sag Bescheid; sonst ist die Auswahl konfliktfrei.
