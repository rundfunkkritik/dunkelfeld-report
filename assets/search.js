(() => {
  'use strict';

  // document.currentScript funktioniert nur, solange es synchron ganz am
  // Anfang des Skripts ausgelesen wird - deshalb hier oben, vor jedem await.
  const scriptEl = document.currentScript;

  // Fix: der Index-Pfad wurde bisher hart auf "/search-index.json" gesetzt.
  // Das ist bei einer eigenen Domain korrekt, bricht aber bei GitHub-Project-Pages
  // (username.github.io/repository) und musste bisher von Hand angepasst werden.
  // Jetzt wird der Pfad automatisch aus dem Speicherort dieses Skripts abgeleitet:
  // .../assets/search.js -> eine Ebene höher -> Repo-Wurzel + search-index.json.
  const autoIndexUrl = (() => {
    try {
      return new URL('../search-index.json', scriptEl.src).pathname;
    } catch {
      return '/search-index.json';
    }
  })();

  const CONFIG = {
    indexUrl: autoIndexUrl, // bei Bedarf hier weiterhin manuell überschreibbar
    minChars: 2,
    maxResults: 20,
    debounceMs: 120
  };

  const form = document.querySelector('[data-local-search-form]');
  const input = document.querySelector('[data-local-search-input]');
  const results = document.querySelector('[data-local-search-results]');
  const status = document.querySelector('[data-local-search-status]');

  if (!form || !input || !results) return;

  let index = [];
  let loaded = false;
  let timer;

  const normalize = (value = '') => value
    .toLocaleLowerCase('de-DE')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9äöüß\s-]/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();

  const escapeHtml = (value = '') => value.replace(/[&<>'"]/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
  }[char]));

  const loadIndex = async () => {
    if (loaded) return;
    // Fix: 'force-cache' ließ Browser tage-/wochenlang eine veraltete Indexdatei
    // benutzen, selbst nachdem die GitHub Action einen neuen Index gebaut hat.
    // 'no-cache' erzwingt eine Prüfung beim Server (ETag/Last-Modified), sodass
    // ein neuer Index sofort nach dem nächsten Push ankommt.
    const response = await fetch(CONFIG.indexUrl, {
      credentials: 'same-origin',
      cache: 'no-cache'
    });
    if (!response.ok) throw new Error('Suchindex konnte nicht geladen werden.');
    index = await response.json();
    loaded = true;
  };

  const scoreEntry = (entry, terms) => {
    const title = normalize(entry.title);
    const text = normalize(`${entry.excerpt || ''} ${entry.content || ''}`);
    const tags = normalize((entry.tags || []).join(' '));
    let score = 0;

    for (const term of terms) {
      if (!title.includes(term) && !text.includes(term) && !tags.includes(term)) return 0;
      if (title === term) score += 80;
      if (title.startsWith(term)) score += 40;
      if (title.includes(term)) score += 25;
      if (tags.includes(term)) score += 12;
      if (text.includes(term)) score += 4;
    }

    return score;
  };

  const render = (query) => {
    const cleaned = normalize(query);
    results.innerHTML = '';

    if (cleaned.length < CONFIG.minChars) {
      if (status) status.textContent = `Mindestens ${CONFIG.minChars} Zeichen eingeben.`;
      return;
    }

    const terms = cleaned.split(' ').filter(Boolean);
    const matches = index
      .map(entry => ({ entry, score: scoreEntry(entry, terms) }))
      .filter(item => item.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, CONFIG.maxResults);

    if (status) status.textContent = `${matches.length} Treffer`;

    if (!matches.length) {
      results.innerHTML = '<p class="local-search__empty">Keine passenden Inhalte gefunden.</p>';
      return;
    }

    const fragment = document.createDocumentFragment();
    for (const { entry } of matches) {
      const article = document.createElement('article');
      article.className = 'local-search__result';
      article.innerHTML = `
        <h2><a href="${escapeHtml(entry.url)}">${escapeHtml(entry.title)}</a></h2>
        ${entry.date ? `<time datetime="${escapeHtml(entry.date)}">${escapeHtml(entry.date)}</time>` : ''}
        ${entry.excerpt ? `<p>${escapeHtml(entry.excerpt)}</p>` : ''}
      `;
      fragment.appendChild(article);
    }
    results.appendChild(fragment);
  };

  const performSearch = async () => {
    try {
      if (status) status.textContent = 'Suche wird geladen …';
      await loadIndex();
      render(input.value);
    } catch (error) {
      console.error(error);
      if (status) status.textContent = 'Die Suche ist momentan nicht verfügbar.';
    }
  };

  form.addEventListener('submit', event => {
    event.preventDefault();
    performSearch();
  });

  input.addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(performSearch, CONFIG.debounceMs);
  });

  const params = new URLSearchParams(window.location.search);
  const initial = params.get('q');
  if (initial) {
    input.value = initial;
    performSearch();
  }
})();
