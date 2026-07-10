/* dunkelfeld.report — Serien- & Reihen-Navigation
   Eine Datei, alle Artikel. Einbau: <script src="serien.js" defer></script> vor </body>.
   Fuegt nur dann einen Block ein, wenn die aktuelle Seite Teil einer definierten
   Serie/Reihe ist. Rein clientseitig, keine externen Aufrufe, DSGVO-konform. */
(function () {
  "use strict";

  /* Geordnete Serien: feste Reihenfolge, mit "Teil X von Y" + Zurueck/Weiter. */
  var SERIEN = [
    { name: "Grünes Kartell", parts: [
      ["dunkelfeld_gruenes_kartell_teil1.html", "Teil 1 — Sie haben es unterschrieben"],
      ["dunkelfeld_gruenes_kartell_teil2.html", "Teil 2 — Grün ist die neue Betonfarbe"],
      ["dunkelfeld_gruenes_kartell_teil3.html", "Teil 3 — Die Angst, die man vererbt"],
      ["dunkelfeld_gruenes_kartell_teil4.html", "Teil 4 — Wenn Milliarden das Korrektiv abschalten"]
    ]},
    { name: "Die dunkle Seite der Grünen", parts: [
      ["gruene-teil1.html", "Teil 1 — Die Gründungsgeschichte"],
      ["gruene-teil2.html", "Teil 2 — Gegenwart"]
    ]},
    { name: "Endzeit-Lobbying", parts: [
      ["endzeit-lobbying-teil1-cufi.html", "Teil 1 — Christlicher Zionismus (CUFI)"],
      ["endzeit-lobbying-teil2-tempelberg.html", "Teil 2 — Der Tempelberg"]
    ]},
    { name: "Kurswechsel — Reisefreiheit", parts: [
      ["kurswechsel_du_sollst_nicht_reisen.html", "Teil 1 — Du sollst nicht reisen"],
      ["kurswechsel_klimakaste_reisefreiheit.html", "Teil 2 — Für die Auserwählten gelten andere Regeln"]
    ]},
    { name: "UK-Grooming & institutionelles Schweigen", parts: [
      ["dossier-001-grooming-uk.html", "Dossier 001 — Großbritannien: Skandal und Schweigen"],
      ["dossier-002.html", "Dossier 002 — Jahrzehnte des Schweigens"],
      ["dossier-003-uk-grooming-gangs.html", "Dossier 003 — Grooming Gangs UK, dokumentiert"],
      ["dossier-004-westminster-establishment.html", "Dossier 004 — Westminster & Establishment"]
    ]}
  ];

  /* Thematische Reihen: ohne feste Reihenfolge, als "Mehr aus dieser Reihe". */
  var REIHEN = [
    { name: "Reihe: Ernährung & Landwirtschaft", parts: [
      ["nahrung-akteure.html", "Wer taucht überall auf?"],
      ["nahrung-konzentration.html", "Das stille Imperium (Konzentration)"],
      ["nahrung-konzerne-handel.html", "Das stille Imperium (Konzerne & Handel)"],
      ["nahrung-saatgut.html", "Wer die Saat hat"],
      ["nahrung-gentechnik.html", "Die stille Gentechnik-Revolution"],
      ["nahrung-biontech-prinzip.html", "Das BioNTech-Prinzip"],
      ["nahrung-laborfleisch.html", "Laborfleisch"],
      ["nahrung-insekten.html", "Novel Food: Insekten auf dem Teller"],
      ["nahrung-vertical.html", "Die kontrollierte Ernte (Vertical Farming)"],
      ["nahrung-kleinbauern.html", "Höfesterben & Verdrängung"],
      ["nahrung-mercosur.html", "Das Mercosur-Abkommen"],
      ["nahrung-skandale.html", "Einst empfohlen, heute bekannt"],
      ["nahrung-naehrstoffe-stress.html", "Stress als Nährstoff"],
      ["nahrung-wasser.html", "Wasser"],
      ["der-kampf-ums-korn-df.html", "Der Kampf ums Korn"],
      ["gen-insekten-vektorkontrolle.html", "Gen-Insekten gegen Malaria"]
    ]},
    { name: "Reihe: Kirche & Religion", parts: [
      ["kirche-macht-reichtum.html", "Wie die Kirche zu Macht und Reichtum kam"],
      ["kirche-vatikanbank.html", "Die Vatikanbank"],
      ["kirche-konkordate.html", "Konkordate: Die Staatsverträge der Kirche"],
      ["kirche-arbeitsrecht.html", "Kirchliches Arbeitsrecht"],
      ["kirche-politik-einfluss.html", "Kirche: Einfluss in Parlament, Rundfunk, Universität"],
      ["kirche-mafia-verbindungen.html", "Kirche und Mafia"],
      ["kirche-missbrauch-aufarbeitung.html", "Missbrauch in beiden großen Kirchen"],
      ["kirche-kinderheime-verscharrung.html", "Die verscharrten Kinder"],
      ["kirche-kirchentage-queer.html", "Kirchentage und Queer-Theologie"],
      ["mutter-teresa-mythos.html", "Mutter Teresa: Mythos und Aktenlage"]
    ]},
    { name: "Reihe: Regime-Change — Operationen", parts: [
      ["operation-ajax-iran-1953.html", "Operation Ajax (Iran 1953)"],
      ["operation-condor.html", "Operation Condor"],
      ["operation-cyclone-afghan-trap.html", "Operation Cyclone: Der Afghan Trap"],
      ["guatemala-1954-united-fruit.html", "Guatemala 1954: Sturz Arbenz’ & United Fruit"],
      ["chile-1973-track-ii-allende.html", "Chile 1973: Track II gegen Allende"]
    ]},
    { name: "Reihe: Kuba", parts: [
      ["kuba-schweinebucht-embargo-2026.html", "Vom Schweinebucht-Fiasko zum Öl-Blockade-Winter"],
      ["kuba-castro-anklage-invasion-2026.html", "Kuba 2026: Anklage gegen Raúl Castro"]
    ]},
    { name: "Reihe: Venezuela", parts: [
      ["venezuela-sanktionen-guaido-2019.html", "Guaidó, Sanktionen, PDVSA"],
      ["venezuela-heute-2026.html", "Venezuela heute (2026)"]
    ]},
    { name: "Reihe: EU-Lobbyismus", parts: [
      ["eu-lobbyismus-zahlen-fakten.html", "Zahlen, Fakten, Mechanismen"],
      ["eu-lobbyismus-exkurs-esg-management.html", "Warum Manager mitmachen (ESG)"]
    ]}
  ];

  // aktuellen Dateinamen ermitteln
  var path = location.pathname.split("/").pop() || "index.html";
  if (path === "") path = "index.html";

  function findGroup(list) {
    for (var i = 0; i < list.length; i++) {
      var parts = list[i].parts;
      for (var j = 0; j < parts.length; j++) {
        if (parts[j][0] === path) return { group: list[i], idx: j };
      }
    }
    return null;
  }

  var ordered = findGroup(SERIEN);
  var themed = ordered ? null : findGroup(REIHEN);
  if (!ordered && !themed) return;

  // Styles einmalig einfuegen
  var css = ""
    + ".df-serie{max-width:720px;margin:2.5rem auto 1rem;padding:1.2rem 1.3rem;"
    + "background:#0e0e14;border:1px solid #2a2a30;border-radius:5px;"
    + "font-family:Georgia,'Times New Roman',serif;color:#d4d4d8;line-height:1.5}"
    + ".df-serie-h{font-family:'JetBrains Mono','Courier New',monospace;font-size:.62rem;"
    + "letter-spacing:.18em;text-transform:uppercase;color:#e8c547;margin-bottom:.9rem}"
    + ".df-serie-h b{color:#f4f4f5;font-weight:600}"
    + ".df-serie ol{list-style:none;margin:0;padding:0}"
    + ".df-serie li{margin:0;border-top:1px solid #1f1f24}"
    + ".df-serie li:first-child{border-top:none}"
    + ".df-serie a{display:block;padding:.5rem .2rem;color:#e8c547;text-decoration:none;font-size:.95rem}"
    + ".df-serie a:hover{color:#f4f4f5}"
    + ".df-serie .cur{color:#8a8a92;padding:.5rem .2rem;font-size:.95rem}"
    + ".df-serie .cur::before{content:'▸ ';color:#e8c547}"
    + ".df-nav{display:flex;justify-content:space-between;gap:1rem;margin-top:1rem;"
    + "font-family:'JetBrains Mono','Courier New',monospace;font-size:.7rem;letter-spacing:.05em}"
    + ".df-nav a{color:#b89a2f;text-decoration:none}.df-nav a:hover{color:#e8c547}"
    + ".df-nav span{color:#3f3f46}";
  var st = document.createElement("style");
  st.textContent = css;
  document.head.appendChild(st);

  var box = document.createElement("div");
  box.className = "df-serie";

  if (ordered) {
    var g = ordered.group, idx = ordered.idx, parts = g.parts;
    var html = '<div class="df-serie-h">Serie · <b>' + esc(g.name) + '</b> · Teil ' +
      (idx + 1) + ' von ' + parts.length + '</div><ol>';
    for (var i = 0; i < parts.length; i++) {
      if (i === idx) {
        html += '<li><span class="cur">' + esc(parts[i][1]) + '</span></li>';
      } else {
        html += '<li><a href="' + esc(parts[i][0]) + '">' + esc(parts[i][1]) + '</a></li>';
      }
    }
    html += '</ol><div class="df-nav">';
    html += idx > 0
      ? '<a href="' + esc(parts[idx - 1][0]) + '">← Vorheriger Teil</a>'
      : '<span>← Anfang</span>';
    html += idx < parts.length - 1
      ? '<a href="' + esc(parts[idx + 1][0]) + '">Nächster Teil →</a>'
      : '<span>Ende →</span>';
    html += '</div>';
    box.innerHTML = html;
  } else {
    var g2 = themed.group, cur = themed.idx, p2 = g2.parts;
    var h2 = '<div class="df-serie-h">Mehr aus der <b>' + esc(g2.name.replace(/^Reihe:\s*/, "")) + '</b></div><ol>';
    for (var k = 0; k < p2.length; k++) {
      if (k === cur) continue;
      h2 += '<li><a href="' + esc(p2[k][0]) + '">' + esc(p2[k][1]) + '</a></li>';
    }
    h2 += '</ol>';
    box.innerHTML = h2;
  }

  // vor dem Footer einfuegen, sonst ans Ende des Body
  var footer = document.querySelector("footer");
  if (footer && footer.parentNode) {
    footer.parentNode.insertBefore(box, footer);
  } else {
    document.body.appendChild(box);
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
})();
