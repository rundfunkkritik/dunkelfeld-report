# -*- coding: utf-8 -*-
import html, json

ALLFILES = """15-minuten-staedte-oxford-c40 aegypten-sadat-bruderschaft-sisi amla-ueberwachungsinfrastruktur anthrax-biodefense-corona
artikel-007-geld-herrschaftsinstrument artikel-009-great-taking-wem-gehoert-depot artikel-010-reich-zu-bund artikel-011-divide-et-impera
artikel-012-faktenchecker-system artikel-013-empoerung-auf-bestellung artikel-014-drehbuch-auf-bestellung artikel-015-sprache-sichtbarkeit-struktur
artikel-016-lamberty-wef-quellennotiz artikel-017-bezmenov-stille-zerstoerung artikel-018-infrastruktur-der-kontrolle artikel-019-who-privatisierte-weltgesundheit
artikel-020-ukraine-medien artikel-021-zwei-seiten-eine-agenda artikel-022-sbgg-zwei-geschlechter artikel-023-wie-viele-nuernbergs
artikel-024-rechte-gewalt-nsu-hanau artikel-025-linke-gewalt artikel-026-demokratie artikel-027-ressourcenkriege
artikel-028-migration-governance artikel-029-unsichtbares-netzwerk artikel-030-neue-hirten artikel-031-fabrik-der-traumata
artikel-sprache-sichtbarkeit-struktur artikel-wie-viele-nuernbergs atomwaffen-doppelstandard-pakistan-indien-iran bevoelkerung
bilderberg-vt-praxis bildung-gehorsam-fleischwolf-1 bildung-gehorsam-fleischwolf-2 bin-laden-mythos-und-beleg
bitcoin-mausefalle blackrock-aladdin boeser-russe bohley-kontrollinfrastruktur
chile-1973-track-ii-allende cui-bono-kriegswirtschaft das-gesetz-das-ihm-gefaehrlich-wurde-df datenschutz
demokratie-leben-selbstevaluation der-fonds-der-nie-kam der-kampf-ums-korn-df der-unterzeichner
deutsche-schuld-strukturanalyse digitaler-euro-infrastruktur ditib-diyanet-einflussnahme dossier-001-grooming-uk
dossier-002-ausbeutungssysteme dossier-002 dossier-003-uk-grooming-gangs dossier-004-westminster-establishment
dossier-005-dynastien dossier-005-post-office-horizon dossier-006-dynastien dossier-boehmermann-huber
dossier-kentler dossier-nanotech-robotik dossier-uap-priming dossier-xxx-paragraph188
dossier_institutionen dossier_palantir dunkelfeld_GFF_AfD_Gutachten dunkelfeld_artikel19_fabrik_der_traumata
dunkelfeld_dossier_unterhaltungsindustrie dunkelfeld_extremismus_geschaeft-1 dunkelfeld_extremismus_geschaeft dunkelfeld_gesundheit2
dunkelfeld_grooming_schweigen-1 dunkelfeld_gruenes_kartell_teil1 dunkelfeld_gruenes_kartell_teil2-1 dunkelfeld_gruenes_kartell_teil2
dunkelfeld_gruenes_kartell_teil3 dunkelfeld_gruenes_kartell_teil4-1 dunkelfeld_gruenes_kartell_teil4 dunkelfeld_justiz_150jahre-1
dunkelfeld_justiz_150jahre-2 dunkelfeld_justiz_150jahre dunkelfeld_kindesmissbrauch dunkelfeld_report_artikel8
dunkelfeld_strukturen endzeit-lobbying-teil1-cufi endzeit-lobbying-teil2-tempelberg entwicklungshilfe-mythos-und-mechanik
epstein-netzwerk ethereum-wef-favorit eu-lobbyismus-exkurs-esg-management eu-lobbyismus-zahlen-fakten
exportware-mensch fachkraefte-widerspruch-1 fachkraefte-widerspruch fluechtlingslager-macht-alltag
gaza-board-of-peace-technokratie geheimdienst-aktive-massnahmen gen-insekten-vektorkontrolle golfstaaten-moscheefinanzierung
grossprojekte-strategische-kostenluege gruene-teil1 gruene-teil2 guatemala-1954-united-fruit
houellebecq-soumission-realitaetscheck ifg-transparenz-netzausbau-smartmeter-1 ifg-transparenz-netzausbau-smartmeter impressum
index-dunkelfeld-info index index_170626 insel-riems
irak-doppelter-sturz is-camp-bucca-ursprung israel-hamas-blowback kaelte-hitze-mortalitaet-asymmetrie-1
kaelte-hitze-mortalitaet-asymmetrie-2 kinderschutz-infrastruktur kirche-arbeitsrecht kirche-kinderheime-verscharrung
kirche-kirchentage-queer kirche-konkordate kirche-macht-reichtum kirche-mafia-verbindungen
kirche-missbrauch-aufarbeitung kirche-politik-einfluss kirche-vatikanbank kuba-castro-anklage-invasion-2026
kuba-schweinebucht-embargo-2026 kult-checkliste kurswechsel_du_sollst_nicht_reisen kurswechsel_klimakaste_reisefreiheit-1
kurswechsel_klimakaste_reisefreiheit libyen-2011-rat-line-syrien linke-gewalt-dunkelfeld marokko-muster
mavi-vatan-blaues-vaterland meldestellen-justizbelastung muezzin-ruf-genehmigungspraxis mutter-teresa-mythos
nahrung-akteure nahrung-biontech-prinzip nahrung-gentechnik nahrung-insekten
nahrung-kleinbauern nahrung-konzentration nahrung-konzerne-handel nahrung-laborfleisch
nahrung-mercosur nahrung-naehrstoffe-stress nahrung-saatgut nahrung-skandale
nahrung-vertical nahrung-wasser nav-hamburger-snippet ngo-files-demokratie-leben
oerr-islam-blinder-fleck-1 operation-ajax-iran-1953 operation-condor-1 operation-condor
operation-cyclone-afghan-trap original-play-kitas palantir-integrator plattformkontrolle
ppp-gewinne-privat-verluste-sozial protokolle-von-zion-faelschung raf-kontinuitaet-palaestina raf-pflp-connection
rechte-gewalt-dunkelfeld replacement-migration-realitaetscheck schuldenfalle-hitman-vs-struktur sdg-pin-mythos-1
suche-share-snippet superklasse-machtzirkel syrien-vom-terroristen-zum-staatsgast talmud-mythos
tschetschenien-dagestan-putins-aufstieg ueberwachungsinfrastruktur venezuela-heute-2026 venezuela-sanktionen-guaido-2019
ventotene verschwoerungstheorie-zur-verschwoerungserzaehlung w-social-2 waechteramt
who-sexualaufklaerung-standards wikipedia-macht wk1-kriegsschuld-fischer-kontroverse wk2-konzerne-nazi-deutschland
worldcoin-trump-coin zensurkomplex""".split()
ALLFILES = [f + ".html" for f in ALLFILES]

LINKED = set(f + ".html" for f in """artikel-007-geld-herrschaftsinstrument artikel-009-great-taking-wem-gehoert-depot artikel-010-reich-zu-bund
artikel-011-divide-et-impera artikel-012-faktenchecker-system artikel-013-empoerung-auf-bestellung artikel-014-drehbuch-auf-bestellung
artikel-015-sprache-sichtbarkeit-struktur artikel-016-lamberty-wef-quellennotiz artikel-017-bezmenov-stille-zerstoerung
artikel-018-infrastruktur-der-kontrolle artikel-019-who-privatisierte-weltgesundheit artikel-020-ukraine-medien artikel-021-zwei-seiten-eine-agenda
artikel-022-sbgg-zwei-geschlechter artikel-023-wie-viele-nuernbergs artikel-024-rechte-gewalt-nsu-hanau artikel-025-linke-gewalt
artikel-026-demokratie artikel-027-ressourcenkriege artikel-028-migration-governance artikel-029-unsichtbares-netzwerk
artikel-030-neue-hirten artikel-031-fabrik-der-traumata dossier-001-grooming-uk dossier-003-uk-grooming-gangs
dossier-004-westminster-establishment dossier-006-dynastien dossier-005-post-office-horizon dossier-boehmermann-huber
dossier-kentler dossier-uap-priming dossier-xxx-paragraph188 dossier_palantir dunkelfeld_dossier_unterhaltungsindustrie
gruene-teil1 gruene-teil2""".split())

EXCLUDE = set(f + ".html" for f in
    "index index-dunkelfeld-info index_170626 nav-hamburger-snippet suche-share-snippet".split())

DOUBLETS = {
 "artikel-sprache-sichtbarkeit-struktur.html": "Doublette von artikel-015-sprache-sichtbarkeit-struktur.html",
 "artikel-wie-viele-nuernbergs.html": "Doublette von artikel-023-wie-viele-nuernbergs.html",
 "linke-gewalt-dunkelfeld.html": "Doublette von artikel-025-linke-gewalt.html",
 "rechte-gewalt-dunkelfeld.html": "Doublette von artikel-024-rechte-gewalt-nsu-hanau.html",
 "dunkelfeld_artikel19_fabrik_der_traumata.html": "Doublette von artikel-031-fabrik-der-traumata.html",
 "dossier-005-dynastien.html": "Doublette von dossier-006-dynastien.html (gleicher Titel)",
 "dunkelfeld_extremismus_geschaeft-1.html": "Kopie von dunkelfeld_extremismus_geschaeft.html",
 "dunkelfeld_gruenes_kartell_teil2-1.html": "Kopie von dunkelfeld_gruenes_kartell_teil2.html",
 "dunkelfeld_gruenes_kartell_teil4-1.html": "Kopie von dunkelfeld_gruenes_kartell_teil4.html",
 "dunkelfeld_justiz_150jahre-1.html": "Kopie von dunkelfeld_justiz_150jahre.html",
 "dunkelfeld_justiz_150jahre-2.html": "Kopie von dunkelfeld_justiz_150jahre.html",
 "fachkraefte-widerspruch-1.html": "Kopie von fachkraefte-widerspruch.html",
 "ifg-transparenz-netzausbau-smartmeter-1.html": "Kopie von ifg-transparenz-netzausbau-smartmeter.html",
 "kaelte-hitze-mortalitaet-asymmetrie-2.html": "Kopie von kaelte-hitze-mortalitaet-asymmetrie-1.html",
 "kurswechsel_klimakaste_reisefreiheit-1.html": "Kopie von kurswechsel_klimakaste_reisefreiheit.html",
 "operation-condor-1.html": "Kopie von operation-condor.html",
 "bildung-gehorsam-fleischwolf-2.html": "PRUEFEN: 2-Teiler oder Doublette von -1.html",
}

E = [
 ("artikel-007-geld-herrschaftsinstrument","Geld als Herrschaftsinstrument","geld"),
 ("artikel-009-great-taking-wem-gehoert-depot","Wem gehört dein Depot? (The Great Taking)","geld"),
 ("artikel-010-reich-zu-bund","Reich zu Bund","geld"),
 ("blackrock-aladdin","Aladdin – BlackRocks Wunderlampe","geld"),
 ("bitcoin-mausefalle","Bitcoin – eine Mausefalle?","geld"),
 ("ethereum-wef-favorit","Ethereum – der Favorit von WEF & Co.?","geld"),
 ("worldcoin-trump-coin","Worldcoin & Trump Coin","geld"),
 ("digitaler-euro-infrastruktur","Der digitale Euro: Infrastruktur & Strukturproblem","geld"),
 ("amla-ueberwachungsinfrastruktur","Die AMLA: Europas Datenzentrale gegen Geldwäsche","geld"),
 ("schuldenfalle-hitman-vs-struktur","Die Schuldenfalle: Hitman-Erzählung vs. Struktur","geld"),
 ("der-fonds-der-nie-kam","Der Fonds, der nie kam","geld"),
 ("ppp-gewinne-privat-verluste-sozial","PPP: Gewinne privatisiert, Verluste sozialisiert","geld"),
 ("eu-lobbyismus-zahlen-fakten","Lobbyismus in der EU – Zahlen, Fakten, Mechanismen","geld"),
 ("eu-lobbyismus-exkurs-esg-management","Warum Manager mitmachen (ESG)","geld"),
 ("cui-bono-kriegswirtschaft","Cui bono? Wer an der Aufrüstung verdient","geld"),
 ("grossprojekte-strategische-kostenluege","Großprojekte: Unfähigkeit oder System?","geld"),
 ("superklasse-machtzirkel","Superklasse & Machtzirkel","geld"),
 ("bilderberg-vt-praxis","Die Bilderberg-Konferenzen: VT und Praxis","geld"),
 ("bevoelkerung","Sie haben es uns gesagt – Philanthropen & die Zahl","geld"),
 ("der-unterzeichner","Der Unterzeichner","geld"),

 ("artikel-011-divide-et-impera","Divide et impera 2.0","medien"),
 ("artikel-012-faktenchecker-system","Das Faktenchecker-System","medien"),
 ("artikel-013-empoerung-auf-bestellung","Empörung auf Bestellung","medien"),
 ("artikel-014-drehbuch-auf-bestellung","Drehbuch auf Bestellung","medien"),
 ("artikel-015-sprache-sichtbarkeit-struktur","Sprache, Sichtbarkeit, Struktur","medien"),
 ("artikel-016-lamberty-wef-quellennotiz","Quellennotiz: Lamberty / WEF","medien"),
 ("artikel-020-ukraine-medien","Was wir über die Ukraine wussten","medien"),
 ("boeser-russe","Der böse Russe","medien"),
 ("zensurkomplex","Der Zensurkomplex","medien"),
 ("meldestellen-justizbelastung","Der Meldungstrichter: Meldestellen & Justiz","medien"),
 ("verschwoerungstheorie-zur-verschwoerungserzaehlung","Vom Theorie-Wort zum Kampfbegriff","medien"),
 ("protokolle-von-zion-faelschung","„Protokolle der Weisen von Zion“: Anatomie einer Fälschung","medien"),
 ("talmud-mythos","Der Talmud: Was drinsteht, was erfunden wurde","medien"),
 ("wikipedia-macht","Die dunkle Seite der Wikipedia","medien"),
 ("w-social-2","W Social – Europas Antwort auf X","medien"),
 ("kult-checkliste","Wie erkenne ich eine Echokammer?","medien"),
 ("houellebecq-soumission-realitaetscheck","„Soumission“ im Realitätscheck 2026","medien"),
 ("demokratie-leben-selbstevaluation","„Demokratie leben!“: Die Evaluation evaluiert sich selbst","medien"),
 ("ngo-files-demokratie-leben","NGO-Files & der Umbau von „Demokratie leben!“","medien"),
 ("dunkelfeld_GFF_AfD_Gutachten","Wer hat das AfD-Gutachten bestellt?","medien"),
 ("dunkelfeld_extremismus_geschaeft","Das Extremismus-Geschäft","medien"),

 ("artikel-018-infrastruktur-der-kontrolle","Infrastruktur der Kontrolle","kontrolle"),
 ("artikel-029-unsichtbares-netzwerk","Das unsichtbare Netzwerk","kontrolle"),
 ("ueberwachungsinfrastruktur","Was Geheimdienste über Sie gespeichert haben","kontrolle"),
 ("bohley-kontrollinfrastruktur","„Effektiver als die Stasi“","kontrolle"),
 ("plattformkontrolle","Plattformkontrolle","kontrolle"),
 ("geheimdienst-aktive-massnahmen","Aktive Maßnahmen: Der Staat als Quelle","kontrolle"),
 ("palantir-integrator","Palantir – Der unsichtbare Integrator","kontrolle"),
 ("dossier_palantir","Dossier: Palantir – Infrastruktur, Manifest, Geopolitik","kontrolle"),
 ("15-minuten-staedte-oxford-c40","Die 15-Minuten-Stadt","kontrolle"),
 ("dunkelfeld_report_artikel8","Die Fäden zusammengeführt: Identität, Geld, Überwachung","kontrolle"),
 ("kinderschutz-infrastruktur","Kinderschutz als Infrastruktur","kontrolle"),
 ("waechteramt","Wächteramt","kontrolle"),

 ("artikel-024-rechte-gewalt-nsu-hanau","NSU, Hanau, V-Männer","gewalt"),
 ("artikel-025-linke-gewalt","Das linke Gewaltproblem","gewalt"),
 ("raf-pflp-connection","Baader-Meinhof International: RAF & PFLP","gewalt"),
 ("raf-kontinuitaet-palaestina","Vom Ausbildungslager zur Demo: RAF & Palästina","gewalt"),

 ("artikel-022-sbgg-zwei-geschlechter","Zwei Geschlechter unter Polizeischutz (SBGG)","staat"),
 ("artikel-023-wie-viele-nuernbergs","Wie viele Nürnbergs?","staat"),
 ("artikel-026-demokratie","„Unsere Demokratie“","staat"),
 ("das-gesetz-das-ihm-gefaehrlich-wurde-df","Das Gesetz, das ihm gefährlich wurde","staat"),
 ("dossier-xxx-paragraph188","Dossier: Der Staat klagt – § 188","staat"),
 ("dunkelfeld_justiz_150jahre","150 Jahre Justiz – und nichts gelernt","staat"),
 ("deutsche-schuld-strukturanalyse","Die ewige Schuld: Struktur & Befund","staat"),
 ("bildung-gehorsam-fleischwolf-1","Bildung, Gehorsam, Fleischwolf","staat"),
 ("ifg-transparenz-netzausbau-smartmeter","Transparenz gegen Netzausbau & Smart Meter","staat"),
 ("ventotene","Das Manifest von Ventotene","staat"),
 ("dossier_institutionen","Dossier: Auf wessen Schultern stehen wir?","staat"),
 ("dunkelfeld_strukturen","Das Krankmachersystem","staat"),
 ("dossier-002","Dossier: Jahrzehnte des Schweigens","staat"),

 ("artikel-028-migration-governance","Wer steuert die Ströme?","migration"),
 ("ditib-diyanet-einflussnahme","DITIB und Diyanet","migration"),
 ("golfstaaten-moscheefinanzierung","Golfstaaten-Finanzierung deutscher Moscheen","migration"),
 ("muezzin-ruf-genehmigungspraxis","Der Muezzin-Ruf","migration"),
 ("oerr-islam-blinder-fleck-1","ÖRR und Islam: Der blinde Fleck","migration"),
 ("fachkraefte-widerspruch","Der Fachkräfte-Widerspruch","migration"),
 ("replacement-migration-realitaetscheck","Replacement Migration: Realitätscheck","migration"),
 ("fluechtlingslager-macht-alltag","Flüchtlingslager: hinter dem Fernsehbild","migration"),
 ("exportware-mensch","Exportware Mensch","migration"),
 ("entwicklungshilfe-mythos-und-mechanik","Entwicklungshilfe: Mythos und Mechanik","migration"),

 ("artikel-030-neue-hirten","Neue Hirten","kirche"),
 ("kirche-macht-reichtum","Wie die Kirche zu Macht und Reichtum kam","kirche"),
 ("kirche-vatikanbank","Die Vatikanbank","kirche"),
 ("kirche-konkordate","Konkordate: Die Staatsverträge der Kirche","kirche"),
 ("kirche-arbeitsrecht","Kirchliches Arbeitsrecht","kirche"),
 ("kirche-politik-einfluss","Kirche: Einfluss in Parlament, Rundfunk, Universität","kirche"),
 ("kirche-mafia-verbindungen","Kirche und Mafia","kirche"),
 ("kirche-missbrauch-aufarbeitung","Missbrauch in beiden großen Kirchen","kirche"),
 ("kirche-kinderheime-verscharrung","Die verscharrten Kinder","kirche"),
 ("kirche-kirchentage-queer","Kirchentage und Queer-Theologie","kirche"),
 ("mutter-teresa-mythos","Mutter Teresa: Mythos und Aktenlage","kirche"),

 ("artikel-031-fabrik-der-traumata","Fabrik der Traumata","kinder"),
 ("dossier-001-grooming-uk","Dossier 001: Großbritannien – Skandal und Schweigen","kinder"),
 ("dossier-003-uk-grooming-gangs","Dossier 003: UK Grooming Gangs","kinder"),
 ("dossier-004-westminster-establishment","Dossier 004: Westminster & Establishment","kinder"),
 ("dossier-002-ausbeutungssysteme","Dossier 002: Globale Ausbeutungssysteme","kinder"),
 ("dossier-kentler","Dossier: Das Kentler-Netzwerk","kinder"),
 ("dossier-boehmermann-huber","Dossier: Böhmermann gegen Michaela Huber","kinder"),
 ("dunkelfeld_dossier_unterhaltungsindustrie","Dossier: Machtmissbrauch in der Unterhaltungsindustrie","kinder"),
 ("dunkelfeld_grooming_schweigen-1","250.000 Mädchen","kinder"),
 ("dunkelfeld_kindesmissbrauch","Sexualisierte Gewalt gegen Kinder: Hell-/Dunkelfeld","kinder"),
 ("original-play-kitas","Original Play: Methode & Missbrauchsverdacht","kinder"),
 ("epstein-netzwerk","Epstein: Macht, Geld und Schweigen","kinder"),
 ("dossier-005-post-office-horizon","Dossier: Post Office / Horizon","kinder"),

 ("gruene-teil1","Die dunkle Seite der Grünen (I)","gruene"),
 ("gruene-teil2","Die dunkle Seite der Grünen (II)","gruene"),
 ("dunkelfeld_gruenes_kartell_teil1","Grünes Kartell (I): Sie haben es unterschrieben","gruene"),
 ("dunkelfeld_gruenes_kartell_teil2","Grünes Kartell (II): Grün ist die neue Betonfarbe","gruene"),
 ("dunkelfeld_gruenes_kartell_teil3","Grünes Kartell (III): Die Angst, die man vererbt","gruene"),
 ("dunkelfeld_gruenes_kartell_teil4","Grünes Kartell (IV): Wenn Milliarden das Korrektiv abschalten","gruene"),
 ("kurswechsel_du_sollst_nicht_reisen","Du sollst nicht reisen","gruene"),
 ("kurswechsel_klimakaste_reisefreiheit","Für die Auserwählten gelten andere Regeln","gruene"),
 ("sdg-pin-mythos-1","Die 17 Ziele: Wortlaut, Mythos, Realität","gruene"),

 ("artikel-019-who-privatisierte-weltgesundheit","Die privatisierte Weltgesundheit (WHO)","nahrung"),
 ("who-sexualaufklaerung-standards","Die WHO-Standards für Sexualaufklärung","nahrung"),
 ("der-kampf-ums-korn-df","Der Kampf ums Korn","nahrung"),
 ("nahrung-akteure","Wer taucht überall auf? (Nahrung)","nahrung"),
 ("nahrung-biontech-prinzip","Das BioNTech-Prinzip","nahrung"),
 ("nahrung-gentechnik","Die stille Gentechnik-Revolution","nahrung"),
 ("nahrung-insekten","Novel Food: Insekten auf dem Teller","nahrung"),
 ("nahrung-kleinbauern","Höfesterben & Verdrängung","nahrung"),
 ("nahrung-konzentration","Das stille Imperium (Konzentration)","nahrung"),
 ("nahrung-konzerne-handel","Das stille Imperium (Konzerne & Handel)","nahrung"),
 ("nahrung-laborfleisch","Laborfleisch","nahrung"),
 ("nahrung-mercosur","Das Mercosur-Abkommen","nahrung"),
 ("nahrung-naehrstoffe-stress","Stress als Nährstoff","nahrung"),
 ("nahrung-saatgut","Wer die Saat hat","nahrung"),
 ("nahrung-skandale","Einst empfohlen, heute bekannt","nahrung"),
 ("nahrung-vertical","Die kontrollierte Ernte (Vertical Farming)","nahrung"),
 ("nahrung-wasser","Wasser","nahrung"),
 ("gen-insekten-vektorkontrolle","Gen-Insekten gegen Malaria","nahrung"),
 ("kaelte-hitze-mortalitaet-asymmetrie-1","Kälte vs. Hitze: Mortalitätsstatistik","nahrung"),
 ("dunkelfeld_gesundheit2","Die verschwiegene Rechnung","nahrung"),

 ("artikel-021-zwei-seiten-eine-agenda","Zwei Seiten, eine Agenda? (Russland/Ukraine/WEF)","geo"),
 ("artikel-027-ressourcenkriege","Ressourcenkriege","geo"),
 ("artikel-017-bezmenov-stille-zerstoerung","Der Mann, der es vorausgesagt hat (Bezmenov)","geo"),
 ("chile-1973-track-ii-allende","Chile 1973: Track II gegen Allende","geo"),
 ("guatemala-1954-united-fruit","Guatemala 1954: Sturz Arbenz’ & United Fruit","geo"),
 ("operation-ajax-iran-1953","Operation Ajax (Iran 1953)","geo"),
 ("operation-condor","Operation Condor","geo"),
 ("operation-cyclone-afghan-trap","Operation Cyclone: Der Afghan Trap","geo"),
 ("irak-doppelter-sturz","Der doppelte Sturz (Irak)","geo"),
 ("libyen-2011-rat-line-syrien","Libyen 2011: Rat Line nach Syrien","geo"),
 ("syrien-vom-terroristen-zum-staatsgast","Syrien: Vom „Terroristen“ zum Staatsgast","geo"),
 ("venezuela-heute-2026","Venezuela heute (2026)","geo"),
 ("venezuela-sanktionen-guaido-2019","Venezuela: Guaidó, Sanktionen, PDVSA","geo"),
 ("kuba-castro-anklage-invasion-2026","Kuba 2026: Anklage gegen Raúl Castro","geo"),
 ("kuba-schweinebucht-embargo-2026","Kuba: Vom Schweinebucht-Fiasko zum Öl-Blockade-Winter","geo"),
 ("tschetschenien-dagestan-putins-aufstieg","Der Preis der Macht (Putins Aufstieg)","geo"),
 ("marokko-muster","Das Marokko-Muster","geo"),
 ("mavi-vatan-blaues-vaterland","Blaues Vaterland (Mavi Vatan)","geo"),
 ("aegypten-sadat-bruderschaft-sisi","Sadat, die Bruderschaft und Sisi","geo"),
 ("atomwaffen-doppelstandard-pakistan-indien-iran","Zwei Bomben geduldet, eine verhindert","geo"),
 ("wk1-kriegsschuld-fischer-kontroverse","Griff nach der Weltmacht (Fischer-Kontroverse)","geo"),
 ("wk2-konzerne-nazi-deutschland","Geschäfte über Grenzen: US-Konzerne & NS","geo"),
 ("bin-laden-mythos-und-beleg","Die Bin-Laden-Story","geo"),
 ("is-camp-bucca-ursprung","Der IS: Geboren in Camp Bucca","geo"),
 ("israel-hamas-blowback","Blowback: Israel & Hamas’ Vorläufer","geo"),
 ("gaza-board-of-peace-technokratie","Das Reißbrett von Gaza","geo"),
 ("anthrax-biodefense-corona","Von Amerithrax zu Corona","geo"),
 ("insel-riems","Die Insel, die nie ganz aufgeklärt wurde","geo"),

 ("endzeit-lobbying-teil1-cufi","Endzeit-Lobbying (I): Christlicher Zionismus","endzeit"),
 ("endzeit-lobbying-teil2-tempelberg","Endzeit-Lobbying (II): Tempelberg","endzeit"),

 ("dossier-nanotech-robotik","Dossier: Nanotechnologie & Robotik","technik"),
 ("dossier-uap-priming","Dossier: Das UAP-Narrativ","technik"),
 ("dossier-006-dynastien","Dossier: Die Dynastien","technik"),

 ("impressum","Impressum","seiten"),
 ("datenschutz","Datenschutzerklärung","seiten"),
]

CATS = [
 ("geld","Geld, Digitalwährung & Wirtschaftsmacht"),
 ("medien","Medien, Narrative & Zensur"),
 ("kontrolle","Überwachung & Kontrolle"),
 ("gewalt","Politische Gewalt & Extremismus"),
 ("staat","Deutschland: Staat, Justiz & Bildung"),
 ("migration","Islam, Moscheen & Migration"),
 ("kirche","Kirche, Religion & Missbrauch"),
 ("kinder","Kindesmissbrauch, Grooming & Ausbeutung"),
 ("gruene","Grüne & Klima-Kartell"),
 ("nahrung","Ernährung, Landwirtschaft & Gesundheit"),
 ("geo","Geopolitik & Regime-Change"),
 ("endzeit","Naher Osten & Endzeit-Lobbying"),
 ("technik","Wissenschaft, Technik & Zukunft"),
 ("seiten","Seiten & Rechtliches"),
]

# VERIFY
entry_files_list = [f + ".html" for (f,_,_) in E]
entry_files = set(entry_files_list)
dups = sorted(set(x for x in entry_files_list if entry_files_list.count(x) > 1))
assert not dups, "Duplicate in E: %s" % dups
union = entry_files | set(DOUBLETS) | EXCLUDE
allset = set(ALLFILES)
missing = allset - union
extra = union - allset
assert not missing, "MISSING: %s" % sorted(missing)
assert not extra, "EXTRA: %s" % sorted(extra)
assert len(ALLFILES) == 190
print("OK: 190 files. archive=%d doublets=%d exclude=%d" % (len(E), len(DOUBLETS), len(EXCLUDE)))
for code,label in CATS:
    print("  %-10s %2d  %s" % (code, sum(1 for e in E if e[2]==code), label))
missing_cat = [e for e in E if e[2] not in dict(CATS)]
assert not missing_cat, "bad cat: %s" % missing_cat

# normalize helper for search (strip umlauts)
def norm(s):
    return (s.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
            .replace("ß","ss").replace("„","").replace("“","").replace("–","-"))

# Build cards HTML per category
def esc(s): return html.escape(s, quote=True)
sections = []
for code,label in CATS:
    items = [e for e in E if e[2]==code]
    cards = []
    for f,t,_ in items:
        fn = f + ".html"
        neu = fn not in LINKED and code != "seiten"
        search = norm(t + " " + f)
        badge = '<span class="neu">neu</span>' if neu else ''
        cards.append(
            f'<a class="card" href="{esc(fn)}" data-s="{esc(search)}">'
            f'<span class="ct">{esc(t)}</span>{badge}'
            f'<span class="cf">{esc(fn)}</span></a>'
        )
    sections.append(
        f'<section class="cat" data-cat="{code}">'
        f'<h2 class="cat-h">{esc(label)} <span class="cat-n">{len(items)}</span></h2>'
        f'<div class="grid">{"".join(cards)}</div></section>'
    )
sections_html = "\n".join(sections)

total = len(E)
neu_count = sum(1 for f,t,c in E if (f+".html") not in LINKED and c!="seiten")

HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Themen &amp; Archiv — dunkelfeld.report</title>
<meta name="description" content="Vollständiges Archiv aller Artikel und Dossiers von dunkelfeld.report. Nach Themen sortiert, mit lokaler Volltextsuche ohne Datenabfluss.">
<link rel="stylesheet" href="fonts.css">
<style>
:root{{
  --bg:#09090b; --surface:#111113; --text:#d4d4d8; --head:#f4f4f5;
  --gold:#e8c547; --gold-dim:#b89a2f; --border:#1f1f24; --border2:#2a2a30;
  --muted:#8a8a92; --rot:#e5675b; --gruen:#5cb87a;
  --serif:"Crimson Pro",Georgia,"Times New Roman",serif;
  --display:"Playfair Display",Georgia,serif;
  --mono:"JetBrains Mono","Courier New",monospace;
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:var(--serif);font-size:1.05rem;line-height:1.6;-webkit-font-smoothing:antialiased}}
a{{color:var(--gold);text-decoration:none}}
.wrap{{max-width:860px;margin:0 auto;padding:0 1.25rem}}
header.site{{border-bottom:1px solid var(--border);padding:1.6rem 0 1.2rem}}
.site-name{{font-family:var(--mono);font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}}
.dot{{display:inline-block;width:8px;height:8px;background:var(--gold);border-radius:50%;margin-right:8px;vertical-align:middle}}
.site-tag{{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:#52525b;margin-top:5px}}
.hero{{padding:2.4rem 0 1.4rem;border-bottom:1px solid var(--border)}}
.hero h1{{font-family:var(--display);font-weight:700;font-size:clamp(1.9rem,5vw,2.7rem);color:var(--head);line-height:1.15;letter-spacing:-.01em}}
.hero p{{color:var(--muted);margin-top:.9rem;max-width:620px}}
.stats{{margin-top:1.2rem;display:flex;gap:.5rem;flex-wrap:wrap}}
.stat{{font-family:var(--mono);font-size:.66rem;letter-spacing:.1em;color:var(--gold);background:rgba(232,197,71,.08);padding:.3rem .65rem;border:1px solid var(--border2)}}
.searchbox{{position:sticky;top:0;z-index:20;background:linear-gradient(var(--bg) 78%,rgba(9,9,11,0));padding:1.1rem 0 .9rem}}
.searchbox .inner{{display:flex;border:1px solid var(--border2);border-radius:4px;overflow:hidden;background:var(--surface)}}
#q{{flex:1;background:transparent;border:none;outline:none;color:var(--text);font-family:var(--mono);font-size:.9rem;padding:.8rem 1rem;letter-spacing:.02em}}
#q::placeholder{{color:#4b4b52}}
#clear{{background:transparent;border:none;color:var(--muted);font-family:var(--mono);font-size:1.1rem;padding:0 1rem;cursor:pointer}}
#clear:hover{{color:var(--gold)}}
.searchbox .inner:focus-within{{border-color:var(--gold)}}
.count{{font-family:var(--mono);font-size:.66rem;letter-spacing:.08em;color:var(--muted);margin-top:.55rem;min-height:1em}}
main{{padding:1rem 0 4rem}}
.cat{{margin:2.2rem 0}}
.cat-h{{font-family:var(--mono);font-size:.7rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--border);padding-bottom:.5rem;margin-bottom:1rem;display:flex;align-items:center;gap:.6rem}}
.cat-n{{color:#52525b;font-size:.62rem}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:6px}}
.card{{display:flex;flex-direction:column;gap:3px;padding:.7rem .85rem;background:var(--surface);border:1px solid var(--border);border-radius:3px;color:inherit;transition:border-color .12s,background .12s}}
.card:hover{{border-color:var(--gold);background:#16161a}}
.ct{{font-family:var(--display);color:var(--head);font-size:1rem;line-height:1.25}}
.cf{{font-family:var(--mono);font-size:.6rem;color:#4b4b52;letter-spacing:.02em;word-break:break-all}}
.neu{{align-self:flex-start;font-family:var(--mono);font-size:.52rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gruen);border:1px solid var(--gruen);border-radius:3px;padding:1px 5px}}
.noresult{{display:none;color:var(--muted);font-family:var(--mono);font-size:.8rem;padding:2rem 0;text-align:center}}
footer.site{{border-top:1px solid var(--border);padding:1.8rem 0 3rem;font-family:var(--mono);font-size:.62rem;color:#3f3f46;letter-spacing:.06em;line-height:1.9}}
footer.site a{{color:var(--gold-dim)}}
.back{{font-family:var(--mono);font-size:.66rem;letter-spacing:.1em;text-transform:uppercase}}
@media(max-width:640px){{
  .grid{{grid-template-columns:1fr}}
  .cf{{display:none}}
  body{{font-size:1rem}}
}}
</style>
</head>
<body>
<header class="site">
  <div class="wrap">
    <div><span class="dot"></span><span class="site-name">dunkelfeld.report</span></div>
    <div class="site-tag">Fakten · Quellen · Dokumentation — keine Schlussfolgerungen</div>
  </div>
</header>

<div class="wrap">
  <section class="hero">
    <h1>Themen &amp; Archiv</h1>
    <p>Das vollständige Verzeichnis aller Artikel und Dossiers — nach Themen geordnet. Die Suche läuft vollständig in deinem Browser, es werden keine Daten übertragen.</p>
    <div class="stats">
      <span class="stat">{total} Beiträge</span>
      <span class="stat">{len(CATS)} Rubriken</span>
      <span class="stat">Lokale Volltextsuche</span>
    </div>
  </section>

  <div class="searchbox">
    <div class="inner">
      <input type="text" id="q" placeholder="Suchen … (z. B. Palantir, WHO, BlackRock, Kirche, Kuba)" autocomplete="off" autofocus>
      <button id="clear" title="Leeren" aria-label="Leeren">×</button>
    </div>
    <div class="count" id="count"></div>
  </div>

  <main>
    {sections_html}
    <div class="noresult" id="noresult">Keine Treffer. Anderen Suchbegriff versuchen.</div>
  </main>
</div>

<footer class="site">
  <div class="wrap">
    <a class="back" href="index.html">← Zur Startseite</a><br><br>
    dunkelfeld.report &nbsp;·&nbsp; Keine Cookies · Kein Tracking · DSGVO-konform &nbsp;·&nbsp;
    Alle Angaben quellenbasiert — Unschuldsvermutung gilt bei laufenden Verfahren &nbsp;·&nbsp;
    <a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a>
  </div>
</footer>

<script>
(function(){{
  var q=document.getElementById('q'),
      cnt=document.getElementById('count'),
      clr=document.getElementById('clear'),
      nores=document.getElementById('noresult'),
      cards=[].slice.call(document.querySelectorAll('.card')),
      cats=[].slice.call(document.querySelectorAll('.cat')),
      total=cards.length;
  function norm(s){{return s.toLowerCase().replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').replace(/ß/g,'ss').replace(/[„“–]/g,'');}}
  function run(){{
    var terms=norm(q.value.trim()).split(/\\s+/).filter(Boolean);
    var shown=0;
    cards.forEach(function(c){{
      var hay=c.getAttribute('data-s');
      var ok=terms.every(function(t){{return hay.indexOf(t)>-1;}});
      c.style.display=ok?'':'none';
      if(ok)shown++;
    }});
    cats.forEach(function(sec){{
      var any=sec.querySelector('.card:not([style*="none"])');
      sec.style.display=any?'':'none';
    }});
    nores.style.display=shown?'none':'block';
    cnt.textContent = terms.length ? (shown+' von '+total+' Beiträgen') : (total+' Beiträge');
  }}
  q.addEventListener('input',run);
  clr.addEventListener('click',function(){{q.value='';run();q.focus();}});
  run();
}})();
</script>
</body>
</html>
"""

with open("themen.html","w",encoding="utf-8") as fh:
    fh.write(HTML)
print("W