import { useState } from "react";

const data = {
  hero: {
    title: "Was wir wissen.",
    subtitle: "Was wir nicht sehen.",
    description: "Eine nüchterne Dokumentation globaler Ausbeutungssysteme — basierend auf Gerichtsakten, UN-Berichten, BKA-Statistiken und investigativen Recherchen.",
  },
  stats: [
    { value: "27,6 Mio.", label: "Menschen in Zwangsarbeit weltweit", source: "ILO 2021" },
    { value: "1,8 Mio.", label: "Kinder jährlich Opfer von Kinderhandel", source: "UNODC" },
    { value: "576", label: "Ermittlungsverfahren Menschenhandel Deutschland 2024", source: "BKA 2025" },
    { value: "~1:370", label: "Verhältnis identifizierte zu tatsächlichen Opfern", source: "ILO/UNODC" },
  ],
  sections: [
    {
      id: "deutschland",
      title: "Deutschland",
      color: "#e8c547",
      icon: "🇩🇪",
      facts: [
        { label: "BKA Lagebild 2024", text: "576 abgeschlossene Ermittlungsverfahren — Höchststand seit 2000. 209 Verfahren mit minderjährigen Opfern. Anstieg um 13,2 % gegenüber Vorjahr." },
        { label: "Sachsensumpf", text: "2007: Verfassungsschutzdossier zu pädophilen Netzwerken mit Richtern und Staatsanwälten in Sachsen. ZDF-Journalist Fassbender gefoltert. 20 Journalisten strafrechtlich verfolgt. Akten verschwunden." },
        { label: "Entwicklungshilfe", text: "33,9 Mrd. € ODA 2022. Bundesrechnungshof: Mangelnde Kontrollmechanismen. Schätzung: 10–30% durch Korruption verloren = bis zu 12 Mrd. €/Jahr. 25% des Geldes verlässt Deutschland nicht." },
        { label: "Deutschen Institut für Menschenrechte 2025", text: "Spezialisierte Schutzunterkünfte für Kinder fehlen. Nur 8 Bundesländer finanzieren Schutzunterkünfte für Menschenhandelsopfer." },
      ]
    },
    {
      id: "epstein",
      title: "Epstein & Netzwerke",
      color: "#e84747",
      icon: "🔗",
      facts: [
        { label: "Rechtskräftig verurteilt", text: "Ghislaine Maxwell: 20 Jahre Haft wegen Menschenhandels mit Minderjährigen. Epstein: starb 2019 in Untersuchungshaft unter ungeklärten Umständen." },
        { label: "Epstein Files Transparency Act", text: "November 2025: 427:1 Stimmen im US-Repräsentantenhaus. Freigabe von 3,5 Mio. Seiten, 2.000 Videos, 180.000 Bildern. Staatsanwalt Acosta: 'Mir wurde gesagt, Epstein gehört zu Geheimdiensten.'" },
        { label: "Whitney Webb — One Nation Under Blackmail", text: "Dokumentiert: Verbindungen zwischen organisierten Verbrechen, Geheimdiensten (CIA/Mossad) und Erpressungsnetzwerken seit den 1950ern. 2022, Quellenbasiert." },
        { label: "Franklin Skandal 1988–91", text: "Nebraska: Pädophilenring für US-Eliten. Ermittler Gary Caradori mit Sohn bei Flugzeugabsturz gestorben, Beweismaterial verschwunden. Washington Times: 'Call Boys toured White House at midnight.'" },
      ]
    },
    {
      id: "institutionen",
      title: "Institutionen & NGOs",
      color: "#47a3e8",
      icon: "🏛️",
      facts: [
        { label: "Oxfam Haiti/Kongo", text: "Nach Katastrophenhilfe Haiti 2010: Sexuelle Ausbeutung hilfsbedürftiger Frauen durch Mitarbeiter. Kongo: 11 Mitarbeiter, Direktoren und Führungskräfte seit 2015. Britisches Parlament: 'Wir torkeln von Skandal zu Skandal.'" },
        { label: "WHO & Gates Foundation", text: "Gates Foundation: zweitgrößter WHO-Geldgeber (10% Budget). Alle Mittel zweckgebunden — WHO kann nicht frei entscheiden. Privatisierung der globalen Gesundheitsagenda ohne demokratische Kontrolle." },
        { label: "Libysche Küstenwache", text: "EU zahlte 2015–2022: 700 Mio. € an Libyen. Davon finanzierte Küstenwache fängt Flüchtlinge ab und bringt sie in Folterlager zurück. 2023: 15.057 Abfangoperationen. UN: 'Verbrechen gegen die Menschlichkeit.'" },
        { label: "UN-Verurteilungsrate", text: "Seit 2017 sinkt die globale Verurteilungsrate von Menschenhändlern stetig — besonders in Subsahara-Afrika und Südasien. Staatliche Institutionen versagen systematisch." },
      ]
    },
    {
      id: "asien",
      title: "Asien & Pazifik",
      color: "#e88947",
      icon: "🌏",
      facts: [
        { label: "Thailand", text: "400.000–800.000 Kinder jährlich sexuell ausgebeutet (Tourismuswirtschaft). Im Norden: Dörfer ohne weibliche Kinder über 12 Jahren. Quelle: WHO, ECPAT." },
        { label: "Philippinen", text: "500.000 Frauen in Prostitution. Über 80% des in Deutschland angebotenen Kinderpornomaterials zeigt Kinder von dort. Europol dokumentiert Online-Missbrauch durch Webcam-Direktübertragung." },
        { label: "Nordkorea", text: "Global Slavery Index: >10% der Bevölkerung in moderner Sklaverei — Platz 1 weltweit. 50.000 Zwangsarbeiter in Russland. Staatlich organisierter Menschenhandel als Devisenquelle." },
        { label: "Bacha Bazi — Afghanistan/Pakistan", text: "Jahrhundertealte Praxis: Jungen als Sexsklaven für Mächtige. US-Militär angewiesen, nicht einzugreifen. Taliban sehen es als Sünde wegen Homosexualität — nicht als Verbrechen am Kind." },
      ]
    },
    {
      id: "golfstaaten",
      title: "Golfstaaten & Nahost",
      color: "#8e47e8",
      icon: "🕌",
      facts: [
        { label: "Kafala-System", text: "Katar: 2 Mio. Arbeitsmigranten = 95% der Erwerbsbevölkerung. Saudi-Arabien: 3,7 Mio. Hausangestellte ohne Arbeitsrechte. Pässe konfisziert, Ausreiseverbot, 16+ Stunden täglich. Amnesty: 'Zwangsarbeit.'" },
        { label: "Jesidischer Völkermord 2014", text: "IS: 7.000+ Frauen und Mädchen entführt, als Sexsklavinnen auf Märkten in Mossul und Raqqa verkauft. Preis: 200–1.500 USD. 2024: 3.200 noch immer vermisst. UN: Völkermord." },
        { label: "Iran: Kinderheirat", text: "2017–2022: 184.000 Mädchen unter 15 Jahren verheiratet. Dunkelziffer deutlich höher. Revolutionsgarde zwingt laut US-Außenministerium afghansiche Flüchtlinge zur Zwangsarbeit in Syrien/Irak." },
        { label: "Irak: Gesetzgebung", text: "2024: Irakische Parlamentarier versuchten, Heiratsalter auf 9 Jahre zu senken. Human Rights Watch: 'Niemand mit Verstand würde sagen: Sie sollten heiraten.'" },
      ]
    },
    {
      id: "strukturen",
      title: "Systeme & Strukturen",
      color: "#47e8a3",
      icon: "⚙️",
      facts: [
        { label: "Economic Hit Man — John Perkins", text: "Ehem. NSA-Berater dokumentiert: Entwicklungsländer werden bewusst in Schuldenfallen gelockt. Kredit → US-Firmen bauen → Land verschuldet → IWF erzwingt Privatisierung → Ressourcenzugang für USA. Seit 1970: Schulden von 46 Mrd. $ auf 8,7 Billionen $." },
        { label: "IWF-Strukturanpassungen", text: "Seit 1980: Entwicklungsländer zahlten 4,2 Billionen $ allein an Zinsen. IWF bevorzugt undemokratische Regierungen, die 'Straßenproteste leichter niederschlagen können' (Cheryl Payer, 1974)." },
        { label: "Tied Aid", text: "OECD 2023: Fast 12% der Entwicklungshilfe gebunden — Empfängerland muss Waren und Dienstleistungen aus dem Geberland kaufen. Geld fließt zurück. Deutschland: 20% der ODA bleibt im eigenen Land." },
        { label: "Das Eisbergprinzip", text: "UNODC erfasst ~75.000 Menschenhandelopfer/Jahr. ILO schätzt 27,6 Mio. Zwangsarbeitssklaven. Verhältnis identifiziert:real ≈ 1:370. Was wir sehen, ist 5–10% der Realität." },
      ]
    },
  ],
  sources: [
    "BKA Bundeslagebild Menschenhandel 2024 (August 2025)",
    "UNODC Global Report on Trafficking in Persons 2024",
    "ILO Forced Labour Report 2022",
    "Amnesty International — Saudi Arabia Domestic Workers Report 2025",
    "Human Rights Watch — Jesidenverfolgung 2015",
    "Bundesrechnungshof Bemerkungen 2022/2023",
    "John Perkins: Confessions of an Economic Hit Man (2004)",
    "Whitney Webb: One Nation Under Blackmail (2022)",
    "Epstein Files Transparency Act, US-Kongress Nov. 2025",
    "ECPAT Deutschland — Dossier Kinderhandel",
    "EU-Finanzierung libyscher Küstenwache — ILMR 2025",
    "Cheryl Payer: The Debt Trap (1974)",
  ]
};

const COLORS = {
  bg: "#0a0a0b",
  surface: "#111114",
  border: "#1e1e24",
  text: "#e8e8ec",
  muted: "#6b6b7a",
  accent: "#e8c547",
};

function StatCard({ value, label, source }) {
  return (
    <div style={{
      borderLeft: `3px solid ${COLORS.accent}`,
      paddingLeft: "1.5rem",
      paddingTop: "1rem",
      paddingBottom: "1rem",
    }}>
      <div style={{ fontSize: "2.5rem", fontFamily: "'Georgia', serif", fontWeight: "700", color: COLORS.accent, lineHeight: 1 }}>{value}</div>
      <div style={{ fontSize: "0.9rem", color: COLORS.text, marginTop: "0.4rem", lineHeight: 1.4 }}>{label}</div>
      <div style={{ fontSize: "0.75rem", color: COLORS.muted, marginTop: "0.3rem" }}>Quelle: {source}</div>
    </div>
  );
}

function FactCard({ label, text }) {
  const [open, setOpen] = useState(false);
  return (
    <div
      onClick={() => setOpen(!open)}
      style={{
        background: COLORS.surface,
        border: `1px solid ${COLORS.border}`,
        borderRadius: "4px",
        padding: "1.2rem 1.4rem",
        cursor: "pointer",
        transition: "border-color 0.2s",
        borderColor: open ? "#333340" : COLORS.border,
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "1rem" }}>
        <span style={{ fontSize: "0.85rem", fontWeight: "700", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.08em" }}>{label}</span>
        <span style={{ color: COLORS.muted, fontSize: "1.1rem", flexShrink: 0, marginTop: "-2px" }}>{open ? "−" : "+"}</span>
      </div>
      {open && (
        <p style={{ marginTop: "0.8rem", fontSize: "0.92rem", color: COLORS.text, lineHeight: 1.7, marginBottom: 0 }}>{text}</p>
      )}
    </div>
  );
}

function Section({ section, isActive, onClick }) {
  return (
    <div style={{ borderBottom: `1px solid ${COLORS.border}` }}>
      <button
        onClick={onClick}
        style={{
          width: "100%",
          background: "none",
          border: "none",
          padding: "1.5rem 2rem",
          display: "flex",
          alignItems: "center",
          gap: "1rem",
          cursor: "pointer",
          textAlign: "left",
        }}
      >
        <span style={{
          width: "10px",
          height: "10px",
          borderRadius: "50%",
          background: isActive ? section.color : COLORS.border,
          flexShrink: 0,
          transition: "background 0.2s",
        }} />
        <span style={{ fontSize: "0.8rem", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.1em", marginRight: "auto" }}>
          {section.icon} {section.title}
        </span>
        <span style={{ color: COLORS.muted, fontSize: "1.2rem" }}>{isActive ? "▲" : "▼"}</span>
      </button>

      {isActive && (
        <div style={{ padding: "0 2rem 2rem", display: "grid", gap: "0.75rem" }}>
          {section.facts.map((fact, i) => (
            <FactCard key={i} {...fact} />
          ))}
        </div>
      )}
    </div>
  );
}

export default function App() {
  const [activeSection, setActiveSection] = useState(null);
  const [showSources, setShowSources] = useState(false);

  const toggle = (id) => setActiveSection(prev => prev === id ? null : id);

  return (
    <div style={{ background: COLORS.bg, minHeight: "100vh", color: COLORS.text, fontFamily: "'Georgia', 'Times New Roman', serif" }}>

      {/* Header */}
      <header style={{
        borderBottom: `1px solid ${COLORS.border}`,
        padding: "1.5rem 2rem",
        display: "flex",
        alignItems: "center",
        gap: "1rem",
        position: "sticky",
        top: 0,
        background: COLORS.bg,
        zIndex: 100,
      }}>
        <div style={{ width: "8px", height: "8px", background: COLORS.accent, borderRadius: "50%" }} />
        <span style={{ fontSize: "0.75rem", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.12em" }}>
          Dokumentation · Fakten · Quellen
        </span>
        <div style={{ marginLeft: "auto", fontSize: "0.7rem", color: COLORS.muted }}>Stand: Mai 2026</div>
      </header>

      {/* Hero */}
      <section style={{ padding: "5rem 2rem 4rem", maxWidth: "900px", margin: "0 auto" }}>
        <div style={{ fontSize: "0.75rem", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.15em", marginBottom: "2rem" }}>
          Globale Ausbeutungssysteme — Quellenbasierte Dokumentation
        </div>
        <h1 style={{
          fontSize: "clamp(2.8rem, 6vw, 5rem)",
          fontWeight: "700",
          lineHeight: 1.05,
          marginBottom: "1.5rem",
          color: COLORS.text,
        }}>
          {data.hero.title}<br />
          <span style={{ color: COLORS.muted }}>{data.hero.subtitle}</span>
        </h1>
        <p style={{ fontSize: "1.1rem", color: COLORS.muted, lineHeight: 1.7, maxWidth: "600px", marginBottom: "3rem" }}>
          {data.hero.description}
        </p>

        {/* Stats */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "2rem" }}>
          {data.stats.map((s, i) => <StatCard key={i} {...s} />)}
        </div>
      </section>

      {/* Divider */}
      <div style={{ borderTop: `1px solid ${COLORS.border}`, margin: "0 2rem" }} />

      {/* Eisberg Grafik */}
      <section style={{ padding: "4rem 2rem", maxWidth: "900px", margin: "0 auto" }}>
        <div style={{ fontSize: "0.75rem", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.12em", marginBottom: "1.5rem" }}>
          Das Eisbergprinzip
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1px", background: COLORS.border }}>
          {[
            { pct: "5–10%", label: "Sichtbar", desc: "Verurteilungen, Berichte, Statistiken, dokumentierte Fälle", color: COLORS.text },
            { pct: "15–20%", label: "Bekannt, unbewiesen", desc: "Netzwerkverbindungen, politische Schutzstrukturen, Geheimdienstlinks", color: "#c8c8d0" },
            { pct: "25%", label: "Strukturell ahnbar", desc: "Wo Macht ist, ist Missbrauch. Wo Armut ist, ist Vulnerabilität.", color: COLORS.muted },
            { pct: "50–55%", label: "Vollständig unsichtbar", desc: "Was nie dokumentiert wird — weil Täter mächtig genug sind", color: "#3a3a48" },
          ].map((item, i) => (
            <div key={i} style={{ background: COLORS.surface, padding: "1.8rem" }}>
              <div style={{ fontSize: "2rem", fontFamily: "'Georgia', serif", fontWeight: "700", color: item.color }}>{item.pct}</div>
              <div style={{ fontSize: "0.8rem", fontWeight: "700", textTransform: "uppercase", letterSpacing: "0.08em", color: item.color, marginTop: "0.4rem" }}>{item.label}</div>
              <div style={{ fontSize: "0.85rem", color: COLORS.muted, marginTop: "0.6rem", lineHeight: 1.5 }}>{item.desc}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Divider */}
      <div style={{ borderTop: `1px solid ${COLORS.border}`, margin: "0 2rem" }} />

      {/* Sections */}
      <section style={{ maxWidth: "900px", margin: "0 auto", padding: "2rem 0" }}>
        <div style={{ padding: "2rem 2rem 1rem", fontSize: "0.75rem", color: COLORS.muted, textTransform: "uppercase", letterSpacing: "0.12em" }}>
          Themenbereiche — klicken zum Öffnen
        </div>
        {data.sections.map(section => (
          <Section
            key={section.id}
            section={section}
            isActive={activeSection === section.id}
            onClick={() => toggle(section.id)}
          />
        ))}
      </section>

      {/* Quellen */}
      <section style={{ maxWidth: "900px", margin: "0 auto", padding: "2rem 2rem 0" }}>
        <div style={{ borderTop: `1px solid ${COLORS.border}`, paddingTop: "2rem" }}>
          <button
            onClick={() => setShowSources(!showSources)}
            style={{ background: "none", border: `1px solid ${COLORS.border}`, color: COLORS.muted, padding: "0.7rem 1.5rem", cursor: "pointer", fontSize: "0.8rem", textTransform: "uppercase", letterSpacing: "0.1em", borderRadius: "2px" }}
          >
            {showSources ? "Quellen ausblenden" : "Quellen & Belege anzeigen"}
          </button>
          {showSources && (
            <div style={{ marginTop: "1.5rem", display: "grid", gap: "0.5rem" }}>
              {data.sources.map((src, i) => (
                <div key={i} style={{ display: "flex", gap: "1rem", alignItems: "baseline" }}>
                  <span style={{ color: COLORS.accent, fontSize: "0.75rem", flexShrink: 0 }}>→</span>
                  <span style={{ fontSize: "0.85rem", color: COLORS.muted }}>{src}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer style={{ padding: "4rem 2rem 3rem", maxWidth: "900px", margin: "0 auto", borderTop: `1px solid ${COLORS.border}`, marginTop: "3rem" }}>
        <div style={{ fontSize: "0.75rem", color: COLORS.muted, lineHeight: 1.8 }}>
          <p>Alle dargestellten Informationen basieren auf öffentlich zugänglichen Quellen: Gerichtsakten, UN-Berichten, Behördenpublikationen und investigativen Recherchen.</p>
          <p style={{ marginTop: "0.5rem" }}>Diese Seite erhebt keinen Anspruch auf Vollständigkeit. Das Eisbergprinzip gilt auch hier: Was wir dokumentieren können, ist ein Bruchteil der Realität.</p>
          <p style={{ marginTop: "1.5rem", color: COLORS.accent, fontSize: "0.8rem" }}>
            Hilfsorganisationen: ECPAT Deutschland · KOK gegen Menschenhandel · Terre des Hommes · Erlassjahr.de
          </p>
        </div>
      </footer>

    </div>
  );
}
