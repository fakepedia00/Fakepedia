# -*- coding: utf-8 -*-

JS = """
// ==========================================================================
// FAKEPEDIA ENGINE - JAVASCRIPT SYSTEM
// ==========================================================================

(function() {
  'use strict';

  let currentArticleKey = "Portada";
  let activeTab = "read"; // 'read', 'talk', 'edit', 'history'

  // ARTÍCULOS EN MEMORIA (CARGADOS DESDE EL DOM O OBJETO GLOBAL)
  const articles = window.FAKPEDIA_ARTICLES || {};
  const talkData = window.FAKPEDIA_TALK || {};
  const historyData = window.FAKPEDIA_HISTORY || {};

  // ELEMENTOS DEL DOM
  const firstHeading = document.getElementById('firstHeading');
  const siteSub = document.getElementById('siteSub');
  const articleBody = document.getElementById('mw-article-body');
  const talkContainer = document.getElementById('mw-talk-container');
  const editorContainer = document.getElementById('mw-editor-container');
  const historyContainer = document.getElementById('mw-history-container');
  const editorTextarea = document.getElementById('editorTextarea');

  // PESTAÑAS
  const tabRead = document.getElementById('tab-read');
  const tabTalk = document.getElementById('tab-talk');
  const tabEdit = document.getElementById('tab-edit');
  const tabHistory = document.getElementById('tab-history');

  // BUSCADOR
  const searchInput = document.getElementById('searchInput');
  const searchClear = document.getElementById('searchClear');
  const searchDropdown = document.getElementById('searchDropdown');

  // POPUPS
  const hovercard = document.getElementById('mw-hovercard');
  const hovercardImg = document.getElementById('hovercardImg');
  const hovercardTitle = document.getElementById('hovercardTitle');
  const hovercardExtract = document.getElementById('hovercardExtract');
  const hovercardLink = document.getElementById('hovercardLink');
  const refTooltip = document.getElementById('mw-ref-tooltip');

  // AUDIO
  const bgm = document.getElementById('fakepediaAudio');

  // ==========================================================================
  // ROUTING & NAVEGACIÓN
  // ==========================================================================

  function getRouteFromHash() {
    let hash = window.location.hash.replace(/^#/, '');
    if (!hash) return "Portada";
    if (hash === "Especial:PáginaAleatoria") {
      const keys = Object.keys(articles).filter(k => !k.startsWith("Especial:") && k !== "Portada");
      const randomKey = keys[Math.floor(Math.random() * keys.length)];
      window.location.hash = '#' + randomKey;
      return randomKey;
    }
    return hash;
  }

  function renderArticle(key) {
    if (!articles[key]) {
      // Página no encontrada (Red link)
      firstHeading.innerText = decodeURIComponent(key);
      siteSub.innerText = "De Fakepedia, la enciclopedia libre";
      articleBody.innerHTML = `
        <div class="ambox ambox-warning">
          <div class="ambox-icon">⚠️</div>
          <div class="ambox-content">
            <strong>Fakepedia aún no tiene un artículo con este nombre exacto.</strong><br>
            Puede <a href="javascript:void(0)" onclick="window.FakepediaEngine.openEditor()">crear esta página</a> o buscar términos relacionados en la barra superior.
          </div>
        </div>
      `;
      currentArticleKey = key;
      updateActiveSidebar(key);
      switchTab('read');
      return;
    }

    currentArticleKey = key;
    const art = articles[key];

    // Actualizar encabezados
    firstHeading.innerText = art.title;
    siteSub.innerText = art.subtitle || "De Fakepedia, la enciclopedia libre";
    document.title = `${art.title} - Fakepedia, la enciclopedia libre`;

    // Cargar contenido
    articleBody.innerHTML = art.content;

    // Actualizar wikitexto en editor
    if (editorTextarea) {
      editorTextarea.value = art.wikitext || generateWikitext(art);
    }

    // Configurar interactividades del artículo
    setupArticleInteractions();
    updateActiveSidebar(key);
    switchTab('read');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function updateActiveSidebar(key) {
    document.querySelectorAll('.mw-sidebar-item').forEach(item => {
      const link = item.querySelector('a');
      if (link && link.getAttribute('href') === '#' + key) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }

  function generateWikitext(art) {
    return `{{Ficha de entidad
| nombre = ${art.title}
| categoría = ${art.category || 'General'}
| clasificación = Nivel Ω-4
}}

== Resumen ==
${art.extract || 'Contenido archivado en Fakepedia.'}

== Historia ==
Documentación clasificada en el consorcio XXI.

== Referencias ==
{{Listaref}}
`;
  }

  // ==========================================================================
  // PESTAÑAS (READ, TALK, EDIT, HISTORY)
  // ==========================================================================

  function switchTab(tab) {
    activeTab = tab;
    [tabRead, tabTalk, tabEdit, tabHistory].forEach(t => t && t.parentElement.classList.remove('selected'));

    articleBody.style.display = 'none';
    if (talkContainer) talkContainer.style.display = 'none';
    if (editorContainer) editorContainer.style.display = 'none';
    if (historyContainer) historyContainer.style.display = 'none';

    if (tab === 'read') {
      if (tabRead) tabRead.parentElement.classList.add('selected');
      articleBody.style.display = 'block';
    } else if (tab === 'talk') {
      if (tabTalk) tabTalk.parentElement.classList.add('selected');
      renderTalkPage();
      if (talkContainer) talkContainer.style.display = 'block';
    } else if (tab === 'edit') {
      if (tabEdit) tabEdit.parentElement.classList.add('selected');
      if (editorContainer) editorContainer.style.display = 'block';
    } else if (tab === 'history') {
      if (tabHistory) tabHistory.parentElement.classList.add('selected');
      renderHistoryPage();
      if (historyContainer) historyContainer.style.display = 'block';
    }
  }

  function renderTalkPage() {
    if (!talkContainer) return;
    const threads = talkData[currentArticleKey] || [
      {
        title: "Bienvenido a la página de discusión",
        author: "Usuario:Bibliotecario_Alfa",
        date: "26 nov 2026, 00:00 (UTC)",
        body: "Este es el espacio designado para coordinar mejoras, verificar citas ocultas y debatir la neutralidad enciclopédica de esta entrada.",
        replies: []
      }
    ];

    let html = `
      <div class="mw-talk-header">
        <h2>Discusión: ${articles[currentArticleKey] ? articles[currentArticleKey].title : currentArticleKey}</h2>
        <button class="mw-btn-primary" id="newTopicBtn">+ Añadir tema</button>
      </div>
      <div class="ambox ambox-notice">
        <div class="ambox-icon">💬</div>
        <div class="ambox-content">
          <strong>Normas de discusión:</strong> Este no es un foro de debate ideológico sin fundamento. Firme sus comentarios con cuatro tildes (<code>~~~~</code>) y mantenga el respeto a la estirpe y a la investigación histórica.
        </div>
      </div>
    `;

    threads.forEach(t => {
      html += `
        <div class="mw-talk-thread">
          <div class="mw-talk-thread-title">${t.title}</div>
          <p>${t.body}</p>
          <div class="mw-talk-signature">— <strong>${t.author}</strong> <span style="color:var(--mw-text-muted);">${t.date}</span></div>
      `;
      if (t.replies && t.replies.length > 0) {
        t.replies.forEach(r => {
          html += `
            <div class="mw-talk-reply">
              <p>${r.body}</p>
              <div class="mw-talk-signature">— <strong>${r.author}</strong> <span style="color:var(--mw-text-muted);">${r.date}</span></div>
            </div>
          `;
        });
      }
      html += `</div>`;
    });

    talkContainer.innerHTML = html;

    const newTopicBtn = document.getElementById('newTopicBtn');
    if (newTopicBtn) {
      newTopicBtn.addEventListener('click', promptNewTopic);
    }
  }

  function promptNewTopic() {
    const title = prompt("Asunto del nuevo tema de discusión:");
    if (!title) return;
    const body = prompt("Escriba su mensaje:");
    if (!body) return;

    if (!talkData[currentArticleKey]) {
      talkData[currentArticleKey] = [];
    }
    talkData[currentArticleKey].push({
      title: title,
      author: "Usuario:Investigador_Invitado",
      date: new Date().toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric' }) + ", " + new Date().toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' }) + " (UTC)",
      body: body,
      replies: []
    });
    renderTalkPage();
  }

  function renderHistoryPage() {
    if (!historyContainer) return;
    const revs = historyData[currentArticleKey] || [
      { date: "26 nov 2026, 04:19", user: "Demian_Admin", bytes: "54.210", diff: "+1.420", summary: "Actualización milenaria y revisión de fuentes" },
      { date: "15 ene 2026, 12:00", user: "Bibliotecario_XXI", bytes: "52.790", diff: "+890", summary: "Catalogación bajo protocolo Ω-4" }
    ];

    let html = `
      <h2>Historial de revisiones de «${articles[currentArticleKey] ? articles[currentArticleKey].title : currentArticleKey}»</h2>
      <p style="font-size:0.85rem; color:var(--mw-text-muted);">
        Para comparar versiones, seleccione dos casillas y pulse «Comparar versiones seleccionadas».
      </p>
      <button class="mw-btn-secondary" style="margin-bottom:12px;" onclick="alert('Comparación de diferencias: Las versiones seleccionadas concuerdan con la línea temporal de la Sincronía Astral.')">Comparar versiones seleccionadas</button>
      <table class="mw-history-table">
        <thead>
          <tr>
            <th width="30"></th>
            <th>Fecha y hora</th>
            <th>Usuario</th>
            <th>Bytes</th>
            <th>Resumen de edición</th>
          </tr>
        </thead>
        <tbody>
    `;

    revs.forEach((r, idx) => {
      html += `
        <tr>
          <td><input type="radio" name="oldid" ${idx===0?'checked':''}></td>
          <td><strong>${r.date}</strong></td>
          <td><span style="color:var(--mw-link); cursor:pointer;">${r.user}</span></td>
          <td>${r.bytes} <span class="${r.diff.startsWith('+') ? 'mw-byte-pos' : 'mw-byte-neg'}">(${r.diff})</span></td>
          <td><em>${r.summary}</em></td>
        </tr>
      `;
    });

    html += `</tbody></table>`;
    historyContainer.innerHTML = html;
  }

  // ==========================================================================
  // BUSCADOR EN VIVO CON AUTOCOMPLETADO
  // ==========================================================================

  function handleSearchInput(e) {
    const val = searchInput.value.trim().toLowerCase();
    if (!val) {
      searchDropdown.classList.remove('active');
      searchDropdown.innerHTML = '';
      if (searchClear) searchClear.style.display = 'none';
      return;
    }
    if (searchClear) searchClear.style.display = 'flex';

    const matches = Object.keys(articles).filter(k => {
      const art = articles[k];
      return art.title.toLowerCase().includes(val) ||
             (art.category && art.category.toLowerCase().includes(val)) ||
             (art.extract && art.extract.toLowerCase().includes(val));
    });

    if (matches.length === 0) {
      searchDropdown.innerHTML = `
        <div style="padding:12px; font-size:0.82rem; color:var(--mw-text-muted); text-align:center;">
          No se encontraron resultados para «<strong>${escapeHtml(searchInput.value)}</strong>».<br>
          <a href="#${encodeURIComponent(searchInput.value)}" style="font-weight:bold; margin-top:4px; display:inline-block;">Crear o buscar página ➜</a>
        </div>
      `;
      searchDropdown.classList.add('active');
      return;
    }

    let html = '';
    matches.slice(0, 6).forEach(k => {
      const art = articles[k];
      html += `
        <div class="mw-search-item" data-key="${k}">
          <div class="mw-search-item-icon">${art.thumbnail || '📄'}</div>
          <div class="mw-search-item-info">
            <div class="mw-search-item-title">${art.title}</div>
            <div class="mw-search-item-desc">${art.category || 'General'} — ${art.extract || ''}</div>
          </div>
        </div>
      `;
    });
    searchDropdown.innerHTML = html;
    searchDropdown.classList.add('active');

    // Clicks en resultados
    searchDropdown.querySelectorAll('.mw-search-item').forEach(item => {
      item.addEventListener('click', () => {
        const key = item.getAttribute('data-key');
        window.location.hash = '#' + key;
        searchDropdown.classList.remove('active');
        searchInput.value = '';
        if (searchClear) searchClear.style.display = 'none';
      });
    });
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.innerText = text;
    return div.innerHTML;
  }

  // ==========================================================================
  // HOVERCARDS & TOOLTIPS
  // ==========================================================================

  function setupArticleInteractions() {
    // 1. Hovercards para enlaces internos de Fakepedia
    const wikiLinks = articleBody.querySelectorAll('.wiki-link');
    wikiLinks.forEach(link => {
      link.addEventListener('mouseenter', (e) => {
        const key = link.getAttribute('data-article');
        if (!key || !articles[key]) return;
        const art = articles[key];

        hovercardTitle.innerText = art.title;
        hovercardExtract.innerText = art.extract || "Artículo catalogado en Fakepedia.";
        hovercardImg.innerHTML = `<span style="font-size:42px;">${art.thumbnail || '📄'}</span>`;
        hovercardLink.setAttribute('href', '#' + key);

        const rect = link.getBoundingClientRect();
        let top = rect.bottom + 8;
        let left = rect.left;

        if (left + 320 > window.innerWidth) {
          left = window.innerWidth - 330;
        }
        if (top + 220 > window.innerHeight) {
          top = rect.top - 230;
        }

        hovercard.style.top = top + 'px';
        hovercard.style.left = Math.max(10, left) + 'px';
        hovercard.style.display = 'block';
      });

      link.addEventListener('mouseleave', () => {
        setTimeout(() => {
          if (!hovercard.matches(':hover')) {
            hovercard.style.display = 'none';
          }
        }, 200);
      });
    });

    if (hovercard) {
      hovercard.addEventListener('mouseleave', () => {
        hovercard.style.display = 'none';
      });
    }

    // 2. Tooltips para referencias [1], [2]
    const refs = articleBody.querySelectorAll('.mw-ref');
    refs.forEach(ref => {
      ref.addEventListener('mouseenter', (e) => {
        const refId = ref.getAttribute('href');
        const target = refId ? document.querySelector(refId) : null;
        if (!target) return;

        refTooltip.innerHTML = target.innerHTML;
        const rect = ref.getBoundingClientRect();
        refTooltip.style.top = (rect.top - 50) + 'px';
        refTooltip.style.left = Math.max(10, rect.left - 60) + 'px';
        refTooltip.style.display = 'block';
      });

      ref.addEventListener('mouseleave', () => {
        refTooltip.style.display = 'none';
      });
    });

    // 3. Índice de contenidos colapsable
    const tocToggle = document.getElementById('tocToggle');
    const tocList = document.getElementById('tocList');
    if (tocToggle && tocList) {
      tocToggle.addEventListener('click', () => {
        if (tocList.style.display === 'none') {
          tocList.style.display = 'block';
          tocToggle.innerText = 'ocultar';
        } else {
          tocList.style.display = 'none';
          tocToggle.innerText = 'mostrar';
        }
      });
    }

    // 4. Laboratorio genético interactivo (escáner)
    setupLabScanner();

    // 5. Reproductor de audio del artículo
    setupSpokenAudio();

    // 6. Terminal de login para archivos clasificados
    setupClassifiedTerminal();
  }

  // ==========================================================================
  // ESCÁNER DE ADN BIOMÉTRICO INTERACTIVO
  // ==========================================================================

  function setupLabScanner() {
    const scanner = document.getElementById('interactiveScanner');
    const status = document.getElementById('interactiveStatus');
    if (!scanner || !status) return;

    let scanTimer;

    const startScan = (e) => {
      if (e.type === 'touchstart') e.preventDefault();
      scanner.classList.add('scanning');
      status.innerText = "ANALIZANDO SECUENCIA CROMOSÓMICA...";
      status.style.color = "var(--mw-accent)";

      scanTimer = setTimeout(() => {
        const isPure = Math.random() > 0.65;
        if (isPure) {
          status.innerHTML = `<span style="color:#00c853;">✓ SANGRE PURA DETECTADA (TRIPLE HÉLICE VERIFICADA)</span>`;
        } else {
          status.innerHTML = `<span style="color:#ba0000;">✗ ACCESO DENEGADO: GENOMA CONVENCIONAL DE DOBLE ENLACE</span>`;
        }
        scanner.classList.remove('scanning');
      }, 1800);
    };

    const stopScan = () => {
      clearTimeout(scanTimer);
      scanner.classList.remove('scanning');
      if (status.innerText === "ANALIZANDO SECUENCIA CROMOSÓMICA...") {
        status.innerText = "ESTADO: ESCANEO INTERRUMPIDO";
        status.style.color = "var(--mw-text-muted)";
      }
    };

    scanner.addEventListener('mousedown', startScan);
    scanner.addEventListener('touchstart', startScan);
    scanner.addEventListener('mouseup', stopScan);
    scanner.addEventListener('touchend', stopScan);
    scanner.addEventListener('mouseleave', stopScan);
  }

  // ==========================================================================
  // REPRODUCTOR DE AUDIO SPOKEN ARTICLE
  // ==========================================================================

  function setupSpokenAudio() {
    const playBtn = document.getElementById('audioToggleBtn');
    const timeDisplay = document.getElementById('audioTimeDisplay');
    const scrubber = document.getElementById('audioScrubber');
    if (!playBtn || !bgm) return;

    playBtn.addEventListener('click', () => {
      if (bgm.paused) {
        bgm.play().then(() => {
          playBtn.innerText = '⏸';
        }).catch(err => {
          console.log("Audio play blocked by browser policy:", err);
        });
      } else {
        bgm.pause();
        playBtn.innerText = '▶';
      }
    });

    bgm.addEventListener('timeupdate', () => {
      if (!isNaN(bgm.duration)) {
        const curMins = Math.floor(bgm.currentTime / 60);
        const curSecs = Math.floor(bgm.currentTime % 60);
        const durMins = Math.floor(bgm.duration / 60);
        const durSecs = Math.floor(bgm.duration % 60);
        timeDisplay.innerText = `${String(curMins).padStart(2,'0')}:${String(curSecs).padStart(2,'0')} / ${String(durMins).padStart(2,'0')}:${String(durSecs).padStart(2,'0')}`;
        scrubber.value = (bgm.currentTime / bgm.duration) * 100;
      }
    });

    if (scrubber) {
      scrubber.addEventListener('input', () => {
        if (!isNaN(bgm.duration)) {
          bgm.currentTime = (scrubber.value / 100) * bgm.duration;
        }
      });
    }
  }

  // ==========================================================================
  // TERMINAL DE LOGIN CLASIFICADA (VAL1LO / DOWN)
  // ==========================================================================

  function setupClassifiedTerminal() {
    const termBtn = document.getElementById('termBtn');
    const termUser = document.getElementById('termUser');
    const termPass = document.getElementById('termPass');
    const termFeedback = document.getElementById('termFeedback');
    const decryptedBox = document.getElementById('decryptedSuccessors');
    if (!termBtn || !termUser || !termPass) return;

    termBtn.addEventListener('click', () => {
      const u = termUser.value.trim().toUpperCase();
      const p = termPass.value.trim().toUpperCase();

      if (u === "VAL1LO" && p === "DOWN") {
        termFeedback.innerHTML = `<span style="color:#00c853;">AUTORIZACIÓN VALHALLA CONCEDIDA. DESCIFRANDO EXPEDIENTE...</span>`;
        setTimeout(() => {
          if (decryptedBox) {
            decryptedBox.style.display = 'block';
            decryptedBox.scrollIntoView({ behavior: 'smooth' });
          }
        }, 1200);
      } else {
        termFeedback.innerHTML = `<span style="color:#ba0000;">ERROR DE AUTENTICACIÓN: CREDENCIALES RECHAZADAS.</span>`;
      }
    });
  }

  // ==========================================================================
  // WIKITEXT EDITOR (VISUAL & CODE SAVE)
  // ==========================================================================

  function setupEditor() {
    const saveBtn = document.getElementById('editorSaveBtn');
    const cancelBtn = document.getElementById('editorCancelBtn');
    const previewBtn = document.getElementById('editorPreviewBtn');

    if (saveBtn) {
      saveBtn.addEventListener('click', () => {
        const val = editorTextarea.value;
        if (!articles[currentArticleKey]) {
          articles[currentArticleKey] = {
            title: currentArticleKey,
            subtitle: "De Fakepedia, la enciclopedia libre",
            category: "General",
            thumbnail: "📄",
            extract: val.substring(0, 150) + "...",
            content: `<h2>Contenido creado por el usuario</h2><p>${escapeHtml(val).replace(/\\n/g, '<br>')}</p>`,
            wikitext: val
          };
        } else {
          articles[currentArticleKey].wikitext = val;
          // Actualizar extracto
          articles[currentArticleKey].extract = val.substring(0, 150) + "...";
        }
        alert("✓ Cambios guardados con éxito en la sesión de Fakepedia.");
        switchTab('read');
      });
    }

    if (cancelBtn) {
      cancelBtn.addEventListener('click', () => {
        switchTab('read');
      });
    }

    if (previewBtn) {
      previewBtn.addEventListener('click', () => {
        const previewWin = document.getElementById('editorPreviewArea');
        if (previewWin) {
          previewWin.innerHTML = `
            <div style="background:var(--mw-surface-2); padding:12px; border:1px solid var(--mw-border); border-radius:4px; margin-bottom:12px;">
              <strong>Previsualización:</strong>
              <div>${escapeHtml(editorTextarea.value).replace(/\\n/g, '<br>')}</div>
            </div>
          `;
        }
      });
    }

    // Botones de formato
    document.querySelectorAll('.mw-editor-btn[data-wrap]').forEach(btn => {
      btn.addEventListener('click', () => {
        const wrap = btn.getAttribute('data-wrap');
        const start = editorTextarea.selectionStart;
        const end = editorTextarea.selectionEnd;
        const text = editorTextarea.value;
        const selected = text.substring(start, end) || "texto";
        editorTextarea.value = text.substring(0, start) + wrap + selected + wrap + text.substring(end);
        editorTextarea.focus();
      });
    });
  }

  // ==========================================================================
  // CONFIGURACIÓN DE INTERFAZ GENERAL (THEME, SIZE, WIDTH, PANIC)
  // ==========================================================================

  function setupGeneralControls() {
    // 1. Dark Mode
    const themeToggle = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('fakepedia-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme');
        const next = cur === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('fakepedia-theme', next);
        updateThemeIcon(next);
      });
    }

    function updateThemeIcon(theme) {
      if (!themeToggle) return;
      themeToggle.innerText = theme === 'dark' ? '☀️' : '🌙';
    }

    // 2. Tamaño de fuente
    const fontSizeBtn = document.getElementById('fontSizeBtn');
    const sizes = ['13px', '14px', '16px'];
    let sizeIdx = 1;
    if (fontSizeBtn) {
      fontSizeBtn.addEventListener('click', () => {
        sizeIdx = (sizeIdx + 1) % sizes.length;
        document.documentElement.style.setProperty('--base-font-size', sizes[sizeIdx]);
      });
    }

    // 3. Ancho de contenido
    const widthBtn = document.getElementById('widthBtn');
    let isFullWidth = false;
    if (widthBtn) {
      widthBtn.addEventListener('click', () => {
        isFullWidth = !isFullWidth;
        document.documentElement.style.setProperty('--content-max-width', isFullWidth ? '100%' : '1200px');
      });
    }

    // 4. Botón flotante de Pánico (Brecha de Seguridad)
    const panicBtn = document.getElementById('panicFloatingBtn');
    if (panicBtn) {
      panicBtn.addEventListener('click', () => {
        document.body.classList.toggle('panic-mode');
        if (document.body.classList.contains('panic-mode')) {
          alert("¡ALERTA ROJA! PROTOCOLO DE BRECHA DE SEGURIDAD ACTIVADO. LAS DIRECCIONES IP DEL PERSONAL HAN SIDO NOTIFICADAS AL CÓNCLAVE.");
        }
      });
    }

    // 5. Sidebar Toggle para móviles
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('mwSidebar');
    if (sidebarToggle && sidebar) {
      sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
      });
    }

    // 6. Cierre de buscador al hacer click fuera
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.mw-header-center')) {
        if (searchDropdown) searchDropdown.classList.remove('active');
      }
    });

    if (searchClear) {
      searchClear.addEventListener('click', () => {
        searchInput.value = '';
        searchDropdown.classList.remove('active');
        searchClear.style.display = 'none';
        searchInput.focus();
      });
    }
  }

  // ==========================================================================
  // INICIALIZACIÓN
  // ==========================================================================

  function init() {
    setupGeneralControls();
    setupEditor();

    // Eventos de pestañas
    if (tabRead) tabRead.addEventListener('click', (e) => { e.preventDefault(); switchTab('read'); });
    if (tabTalk) tabTalk.addEventListener('click', (e) => { e.preventDefault(); switchTab('talk'); });
    if (tabEdit) tabEdit.addEventListener('click', (e) => { e.preventDefault(); switchTab('edit'); });
    if (tabHistory) tabHistory.addEventListener('click', (e) => { e.preventDefault(); switchTab('history'); });

    // Eventos de buscador
    if (searchInput) {
      searchInput.addEventListener('input', handleSearchInput);
      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          const firstItem = searchDropdown.querySelector('.mw-search-item');
          if (firstItem) {
            firstItem.click();
          } else if (searchInput.value.trim()) {
            window.location.hash = '#' + searchInput.value.trim();
            searchDropdown.classList.remove('active');
          }
        }
      });
    }

    // Router
    window.addEventListener('hashchange', () => {
      renderArticle(getRouteFromHash());
    });

    // Renderizado inicial
    renderArticle(getRouteFromHash());
  }

  // Exponer API global
  window.FakepediaEngine = {
    openEditor: () => switchTab('edit'),
    openTalk: () => switchTab('talk'),
    navigate: (key) => { window.location.hash = '#' + key; }
  };

  document.addEventListener('DOMContentLoaded', init);
})();
"""

print("JS module created.")
