# So veroeffentlichst du eine Änderung

1. Sag Claude Code: „Ändere X in Datei Y“ (Claude erledigt Text ersetzen, Diff zeigen, Commit, Push, Live-Prüfung).
2. Selbst machen: Text ändern mit `python ersetze.py datei.html "alter Text" "neuer Text"` (bricht ab, wenn der alte Text nicht genau einmal vorkommt).
3. Danach `.\veroeffentlichen.ps1 "Kurze Nachricht"` – holt den Stand, committet, pusht und meldet HTTP 200 für die geänderte Seite.