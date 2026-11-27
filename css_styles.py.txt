# -*- coding: utf-8 -*-

CSS = """
/* ==========================================================================
   FAKEPEDIA - MEDIAWIKI VECTOR 2022 THEME SYSTEM
   ========================================================================== */

:root {
  --mw-bg: #f8f9fa;
  --mw-content-bg: #ffffff;
  --mw-text: #202122;
  --mw-text-muted: #54595d;
  --mw-border: #a2a9b1;
  --mw-border-subtle: #eaecf0;
  --mw-border-tabs: #c8ccd1;
  --mw-link: #3366cc;
  --mw-link-visited: #6b4ba1;
  --mw-link-red: #ba0000;
  --mw-hover-bg: #f0f2f5;
  --mw-accent: #3366cc;
  --mw-header-bg: #ffffff;
  --mw-infobox-bg: #f8f9fa;
  --mw-infobox-header: #eaecf0;
  --mw-toc-bg: #f8f9fa;
  --mw-notice-bg: #fcfcfc;
  --mw-code-bg: #f8f9fa;
  --mw-shadow: rgba(0, 0, 0, 0.1);
  --mw-card-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  --content-max-width: 1200px;
  --font-serif: 'Linux Libertine', 'Georgia', 'Times New Roman', serif;
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Liberation Sans', Helvetica, Arial, sans-serif;
  --font-mono: 'Menlo', 'Consolas', 'Courier New', monospace;
  --base-font-size: 14px;
}

[data-theme="dark"] {
  --mw-bg: #101418;
  --mw-content-bg: #1a1e24;
  --mw-text: #eaecf0;
  --mw-text-muted: #9aa0a7;
  --mw-border: #40444b;
  --mw-border-subtle: #2d3139;
  --mw-border-tabs: #40444b;
  --mw-link: #6b9eff;
  --mw-link-visited: #b39ddb;
  --mw-link-red: #ff7878;
  --mw-hover-bg: #262c35;
  --mw-accent: #6b9eff;
  --mw-header-bg: #1a1e24;
  --mw-infobox-bg: #21262d;
  --mw-infobox-header: #2d333b;
  --mw-toc-bg: #21262d;
  --mw-notice-bg: #21262d;
  --mw-code-bg: #21262d;
  --mw-shadow: rgba(0, 0, 0, 0.5);
  --mw-card-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: var(--base-font-size);
  scroll-behavior: smooth;
}

body {
  background-color: var(--mw-bg);
  color: var(--mw-text);
  font-family: var(--font-sans);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background-color 0.2s ease, color 0.2s ease;
}

/* Enlaces estilo Wikipedia */
a {
  color: var(--mw-link);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
a:visited {
  color: var(--mw-link-visited);
}
a.new, a.redlink {
  color: var(--mw-link-red);
}
a.external::after {
  content: ' ↗';
  font-size: 0.8em;
  opacity: 0.7;
}

/* ==========================================================================
   HEADER / TOP BAR
   ========================================================================== */

.mw-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: var(--mw-header-bg);
  border-bottom: 1px solid var(--mw-border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  height: 52px;
  box-shadow: 0 1px 3px var(--mw-shadow);
}

.mw-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.mw-sidebar-toggle {
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  border-radius: 4px;
  color: var(--mw-text);
  display: flex;
  align-items: center;
  justify-content: center;
}
.mw-sidebar-toggle:hover {
  background-color: var(--mw-hover-bg);
}

.mw-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--mw-text);
  text-decoration: none !important;
}
.mw-logo:hover {
  text-decoration: none !important;
}

.mw-logo-icon {
  width: 38px;
  height: 38px;
  flex-shrink: 0;
}

.mw-logo-title-group {
  display: flex;
  flex-direction: column;
}

.mw-logo-wordmark {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  line-height: 1.1;
  color: var(--mw-text);
}

.mw-logo-tagline {
  font-size: 0.68rem;
  color: var(--mw-text-muted);
  letter-spacing: 0.3px;
  line-height: 1;
}

/* BUSCADOR */
.mw-header-center {
  flex: 1;
  max-width: 540px;
  margin: 0 20px;
  position: relative;
}

.mw-search-form {
  position: relative;
  display: flex;
  align-items: center;
}

.mw-search-input {
  width: 100%;
  height: 34px;
  padding: 0 36px 0 34px;
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  border-radius: 18px;
  font-size: 0.9rem;
  color: var(--mw-text);
  outline: none;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
.mw-search-input:focus {
  border-color: var(--mw-accent);
  box-shadow: 0 0 0 2px rgba(51, 102, 204, 0.2);
}

.mw-search-icon {
  position: absolute;
  left: 11px;
  color: var(--mw-text-muted);
  pointer-events: none;
  display: flex;
  align-items: center;
}

.mw-search-clear {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  color: var(--mw-text-muted);
  cursor: pointer;
  display: none;
  font-size: 16px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  align-items: center;
  justify-content: center;
}
.mw-search-clear:hover {
  background-color: var(--mw-hover-bg);
  color: var(--mw-text);
}

/* RESULTADOS DE AUTOCOMPLETADO */
.mw-search-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 4px;
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  border-radius: 8px;
  box-shadow: 0 4px 14px var(--mw-shadow);
  display: none;
  overflow: hidden;
  z-index: 1100;
  max-height: 380px;
  overflow-y: auto;
}

.mw-search-dropdown.active {
  display: block;
}

.mw-search-item {
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  border-bottom: 1px solid var(--mw-border-subtle);
  transition: background-color 0.1s;
}
.mw-search-item:last-child {
  border-bottom: none;
}
.mw-search-item:hover, .mw-search-item.selected {
  background-color: var(--mw-hover-bg);
}

.mw-search-item-icon {
  width: 32px;
  height: 32px;
  background-color: var(--mw-surface-2);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}

.mw-search-item-info {
  flex: 1;
  min-width: 0;
}

.mw-search-item-title {
  font-weight: 600;
  color: var(--mw-text);
  font-size: 0.92rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mw-search-item-desc {
  font-size: 0.76rem;
  color: var(--mw-text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* HEADER DERECHO / ACCIONES */
.mw-header-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.mw-tool-btn {
  background: none;
  border: 1px solid transparent;
  color: var(--mw-text-muted);
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.84rem;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
}
.mw-tool-btn:hover {
  background-color: var(--mw-hover-bg);
  color: var(--mw-text);
  border-color: var(--mw-border-subtle);
}

.mw-user-anon {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.8rem;
  color: var(--mw-text-muted);
  padding-left: 6px;
  border-left: 1px solid var(--mw-border-subtle);
}

/* ==========================================================================
   LAYOUT PRINCIPAL
   ========================================================================== */

.mw-page-wrapper {
  display: flex;
  flex: 1;
  max-width: 1440px;
  width: 100%;
  margin: 0 auto;
  position: relative;
}

/* BARRA LATERAL (SIDEBAR) */
.mw-sidebar {
  width: 210px;
  flex-shrink: 0;
  padding: 16px 12px 30px 16px;
  font-size: 0.84rem;
  border-right: 1px solid var(--mw-border-subtle);
  background-color: var(--mw-bg);
  transition: transform 0.25s ease, width 0.25s ease;
}

@media (max-width: 900px) {
  .mw-sidebar {
    position: fixed;
    top: 52px;
    bottom: 0;
    left: 0;
    z-index: 990;
    transform: translateX(-100%);
    box-shadow: 2px 0 10px var(--mw-shadow);
  }
  .mw-sidebar.open {
    transform: translateX(0);
  }
}

.mw-sidebar-section {
  margin-bottom: 20px;
}

.mw-sidebar-heading {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--mw-text-muted);
  padding: 4px 8px;
  margin-bottom: 4px;
}

.mw-sidebar-list {
  list-style: none;
}

.mw-sidebar-item a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 8px;
  color: var(--mw-link);
  border-radius: 4px;
  line-height: 1.3;
}
.mw-sidebar-item a:hover {
  background-color: var(--mw-hover-bg);
  text-decoration: none;
}
.mw-sidebar-item.active a {
  font-weight: bold;
  background-color: var(--mw-hover-bg);
  color: var(--mw-text);
}

/* CONTENEDOR DE ARTÍCULO Y TOC */
.mw-body-container {
  flex: 1;
  min-width: 0;
  display: flex;
  justify-content: center;
  padding: 0 16px 40px;
}

.mw-article-wrapper {
  width: 100%;
  max-width: var(--content-max-width);
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border-subtle);
  border-top: none;
  min-height: calc(100vh - 52px);
  padding: 24px 36px 60px;
}

@media (max-width: 600px) {
  .mw-article-wrapper {
    padding: 16px 14px 40px;
    border-left: none;
    border-right: none;
  }
}

/* ==========================================================================
   PESTAÑAS DE WIKIPEDIA (VECTOR TABS)
   ========================================================================== */

.mw-tabs-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid var(--mw-border-tabs);
  margin-bottom: 18px;
  font-size: 0.86rem;
}

.mw-tabs-left, .mw-tabs-right {
  display: flex;
  gap: 4px;
  list-style: none;
}

.mw-tab-item {
  margin-bottom: -1px;
}

.mw-tab-item a, .mw-tab-item button {
  background: none;
  border: 1px solid transparent;
  border-bottom: none;
  padding: 8px 12px;
  cursor: pointer;
  color: var(--mw-link);
  font-family: inherit;
  font-size: inherit;
  display: inline-block;
  border-radius: 4px 4px 0 0;
  text-decoration: none;
}
.mw-tab-item a:hover, .mw-tab-item button:hover {
  background-color: var(--mw-hover-bg);
  text-decoration: none;
}
.mw-tab-item.selected a, .mw-tab-item.selected button {
  background-color: var(--mw-content-bg);
  border-color: var(--mw-border-tabs);
  border-bottom-color: var(--mw-content-bg);
  color: var(--mw-text);
  font-weight: 600;
}

/* ENCABEZADOS DE ARTÍCULO */
.firstHeading {
  font-family: var(--font-serif);
  font-size: 2rem;
  font-weight: 400;
  line-height: 1.25;
  border-bottom: 1px solid var(--mw-border);
  padding-bottom: 6px;
  margin-bottom: 6px;
  color: var(--mw-text);
  word-break: break-word;
}

.siteSub {
  font-size: 0.8rem;
  color: var(--mw-text-muted);
  margin-bottom: 16px;
}

/* ==========================================================================
   CAJAS DE AVISO (AMBOX / TEMPLATES)
   ========================================================================== */

.ambox {
  border: 1px solid var(--mw-border);
  background-color: var(--mw-notice-bg);
  margin: 12px 0 18px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 0.85rem;
  border-radius: 3px;
  border-left-width: 6px;
}

.ambox-notice {
  border-left-color: #3366cc;
}
.ambox-warning {
  border-left-color: #e67e22;
  background-color: rgba(230, 126, 34, 0.08);
}
.ambox-protection {
  border-left-color: #ba0000;
  background-color: rgba(186, 0, 0, 0.08);
}

.ambox-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.ambox-content {
  flex: 1;
}

.disambig-notice {
  font-style: italic;
  font-size: 0.85rem;
  color: var(--mw-text-muted);
  margin-bottom: 14px;
  padding-left: 18px;
  position: relative;
}
.disambig-notice::before {
  content: 'ℹ';
  position: absolute;
  left: 0;
  font-style: normal;
  color: var(--mw-accent);
}

/* ==========================================================================
   FICHA / INFOBOX
   ========================================================================== */

.infobox {
  border: 1px solid var(--mw-border);
  background-color: var(--mw-infobox-bg);
  color: var(--mw-text);
  float: right;
  clear: right;
  margin: 0 0 16px 20px;
  padding: 6px;
  width: 310px;
  font-size: 0.83rem;
  line-height: 1.45;
  border-radius: 4px;
  box-shadow: 0 1px 4px var(--mw-shadow);
}

@media (max-width: 720px) {
  .infobox {
    float: none;
    width: 100%;
    margin: 16px 0;
  }
}

.infobox th, .infobox td {
  padding: 5px 8px;
  vertical-align: top;
  border-bottom: 1px solid var(--mw-border-subtle);
}

.infobox-title {
  background-color: var(--mw-infobox-header);
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-weight: 700;
  text-align: center;
  padding: 8px 4px;
  border-radius: 2px;
  color: var(--mw-text);
}

.infobox-subtitle {
  text-align: center;
  font-style: italic;
  font-size: 0.85rem;
  color: var(--mw-text-muted);
  padding: 3px 0 6px;
  border-bottom: 2px solid var(--mw-border);
}

.infobox-image {
  text-align: center;
  padding: 10px 4px;
  background-color: var(--mw-content-bg);
}

.infobox-image svg, .infobox-image img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}

.infobox-caption {
  font-size: 0.78rem;
  color: var(--mw-text-muted);
  text-align: center;
  padding: 4px 6px;
}

.infobox-header {
  background-color: var(--mw-infobox-header);
  font-weight: 700;
  text-align: center;
  font-size: 0.85rem;
  padding: 5px 4px;
}

.infobox-label {
  font-weight: 600;
  width: 38%;
  color: var(--mw-text);
}

.infobox-data {
  width: 62%;
}

/* ==========================================================================
   ÍNDICE DE CONTENIDOS (TOC)
   ========================================================================== */

.toc {
  background-color: var(--mw-toc-bg);
  border: 1px solid var(--mw-border);
  padding: 12px 16px;
  display: inline-block;
  min-width: 250px;
  max-width: 480px;
  margin: 16px 0 24px;
  font-size: 0.85rem;
  border-radius: 4px;
}

.toctitle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 700;
  margin-bottom: 8px;
  border-bottom: 1px solid var(--mw-border-subtle);
  padding-bottom: 4px;
}

.toctogglelink {
  font-size: 0.75rem;
  font-weight: 400;
  color: var(--mw-link);
  cursor: pointer;
  background: none;
  border: none;
}

.toc ul {
  list-style: none;
  padding-left: 0;
}

.toc ul ul {
  padding-left: 18px;
}

.toc li {
  margin: 4px 0;
}

.tocnumber {
  color: var(--mw-text-muted);
  margin-right: 6px;
}

/* ==========================================================================
   ESTRUCTURA DE TEXTO Y SECCIONES
   ========================================================================== */

h2 {
  font-family: var(--font-serif);
  font-size: 1.45rem;
  font-weight: 400;
  border-bottom: 1px solid var(--mw-border);
  margin: 32px 0 14px;
  padding-bottom: 4px;
  color: var(--mw-text);
}

h3 {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 22px 0 10px;
  color: var(--mw-text);
}

h4 {
  font-size: 1rem;
  font-weight: 600;
  margin: 16px 0 8px;
  color: var(--mw-text);
}

p {
  margin-bottom: 14px;
  line-height: 1.7;
}

blockquote {
  border-left: 4px solid var(--mw-border);
  margin: 18px 0;
  padding: 12px 20px;
  background-color: var(--mw-notice-bg);
  font-style: italic;
  border-radius: 0 4px 4px 0;
}

blockquote cite {
  display: block;
  font-style: normal;
  font-size: 0.85rem;
  color: var(--mw-text-muted);
  margin-top: 8px;
  text-align: right;
}

ul.wikilist, ol.wikilist {
  margin: 12px 0 16px 26px;
}
ul.wikilist li, ol.wikilist li {
  margin-bottom: 6px;
}

/* ==========================================================================
   REPRODUCTOR DE AUDIO (WIKIPEDIA SPOKEN ARTICLE)
   ========================================================================== */

.mw-spoken-audio-box {
  background-color: var(--mw-surface-2);
  border: 1px solid var(--mw-border);
  border-radius: 6px;
  padding: 10px 14px;
  margin: 14px 0 20px;
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.mw-audio-icon {
  font-size: 26px;
  color: var(--mw-accent);
}

.mw-audio-info {
  flex: 1;
  min-width: 220px;
}

.mw-audio-title {
  font-weight: 600;
  font-size: 0.88rem;
  color: var(--mw-text);
}

.mw-audio-desc {
  font-size: 0.76rem;
  color: var(--mw-text-muted);
}

.mw-audio-player {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  border-radius: 20px;
  padding: 4px 12px;
}

.mw-audio-play-btn {
  background: none;
  border: none;
  color: var(--mw-accent);
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mw-audio-time {
  font-size: 0.75rem;
  font-family: var(--font-mono);
  color: var(--mw-text-muted);
}

.mw-audio-progress {
  width: 90px;
  cursor: pointer;
}

/* ==========================================================================
   LABORATORIO GENÉTICO INTERACTIVO (ESCÁNER DE ADN)
   ========================================================================== */

.mw-lab-container {
  border: 1px solid var(--mw-border);
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(51, 102, 204, 0.05), rgba(0, 0, 0, 0.02));
  padding: 20px;
  margin: 24px 0;
  text-align: center;
}

.mw-lab-title {
  font-family: var(--font-mono);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: var(--mw-text);
  margin-bottom: 6px;
}

.mw-lab-desc {
  font-size: 0.82rem;
  color: var(--mw-text-muted);
  max-width: 500px;
  margin: 0 auto 18px;
}

.mw-lab-scanner {
  width: 96px;
  height: 96px;
  margin: 0 auto 14px;
  border: 2px dashed var(--mw-border);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background-color: var(--mw-content-bg);
  transition: all 0.3s ease;
  user-select: none;
}
.mw-lab-scanner:hover {
  border-color: var(--mw-accent);
  transform: scale(1.04);
}
.mw-lab-scanner.scanning {
  border-color: #00bcd4;
  box-shadow: 0 0 20px rgba(0, 188, 212, 0.3);
}

.mw-lab-laser {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #00f0ff;
  box-shadow: 0 0 10px #00f0ff;
  opacity: 0;
}
.mw-lab-scanner.scanning .mw-lab-laser {
  opacity: 1;
  animation: laserScan 1.2s infinite linear;
}
@keyframes laserScan {
  0% { top: 0; }
  100% { top: 100%; }
}

.mw-lab-status {
  font-family: var(--font-mono);
  font-size: 0.84rem;
  font-weight: 700;
  min-height: 22px;
  color: var(--mw-text-muted);
}

/* ==========================================================================
   REFERENCIAS Y NOTAS
   ========================================================================== */

sup.reference {
  font-size: 0.72rem;
  padding-left: 1px;
  line-height: 1;
}

.mw-references-list {
  font-size: 0.82rem;
  column-count: 2;
  column-gap: 28px;
  margin-top: 14px;
  list-style: decimal;
  padding-left: 20px;
}

@media (max-width: 700px) {
  .mw-references-list {
    column-count: 1;
  }
}

.mw-references-list li {
  margin-bottom: 8px;
  break-inside: avoid;
}

.mw-reference-backlink {
  color: var(--mw-link);
  margin-right: 4px;
  cursor: pointer;
}

/* POPUP DE REFERENCIAS (FOOTNOTE HOVER) */
.mw-ref-tooltip {
  position: fixed;
  z-index: 2000;
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  box-shadow: 0 4px 16px var(--mw-shadow);
  padding: 10px 14px;
  border-radius: 6px;
  max-width: 320px;
  font-size: 0.8rem;
  line-height: 1.4;
  display: none;
  pointer-events: none;
  animation: fadeIn 0.15s ease;
}

/* ==========================================================================
   HOVERCARD DE ARTÍCULO (WIKIPEDIA ARTICLE PREVIEW)
   ========================================================================== */

.mw-hovercard {
  position: fixed;
  z-index: 2100;
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  border-radius: 8px;
  box-shadow: 0 8px 24px var(--mw-shadow);
  width: 310px;
  overflow: hidden;
  display: none;
  pointer-events: auto;
  animation: fadeIn 0.18s ease;
}

.mw-hovercard-image {
  height: 120px;
  background-color: var(--mw-surface-2);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.mw-hovercard-body {
  padding: 12px 14px;
}

.mw-hovercard-title {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--mw-text);
  margin-bottom: 6px;
}

.mw-hovercard-extract {
  font-size: 0.8rem;
  color: var(--mw-text-muted);
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.mw-hovercard-footer {
  padding: 8px 14px;
  border-top: 1px solid var(--mw-border-subtle);
  font-size: 0.74rem;
  color: var(--mw-link);
  font-weight: 600;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ==========================================================================
   CATEGORÍAS (FOOTER CATLINKS)
   ========================================================================== */

.catlinks {
  border: 1px solid var(--mw-border);
  background-color: var(--mw-toc-bg);
  padding: 8px 12px;
  margin-top: 36px;
  font-size: 0.8rem;
  border-radius: 3px;
}

.catlinks ul {
  display: inline;
  list-style: none;
  padding: 0;
}

.catlinks li {
  display: inline;
}

.catlinks li::after {
  content: ' | ';
  color: var(--mw-border);
}
.catlinks li:last-child::after {
  content: '';
}

/* ==========================================================================
   PORTADA DE FAKEPEDIA (MAIN PAGE WIKIPEDIA STYLE)
   ========================================================================== */

.mw-portada-banner {
  background: linear-gradient(to right, rgba(51, 102, 204, 0.08), rgba(0, 0, 0, 0.02));
  border: 1px solid var(--mw-border);
  border-radius: 6px;
  padding: 18px 24px;
  margin-bottom: 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.mw-portada-welcome h1 {
  font-family: var(--font-serif);
  font-size: 1.8rem;
  font-weight: 400;
  margin-bottom: 4px;
}

.mw-portada-stats {
  font-size: 0.84rem;
  color: var(--mw-text-muted);
}

.mw-portada-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 20px;
}

@media (max-width: 860px) {
  .mw-portada-grid {
    grid-template-columns: 1fr;
  }
}

.mw-portada-card {
  border: 1px solid var(--mw-border);
  border-radius: 4px;
  background-color: var(--mw-content-bg);
  margin-bottom: 20px;
  overflow: hidden;
}

.mw-portada-card-header {
  background-color: var(--mw-infobox-header);
  border-bottom: 1px solid var(--mw-border);
  padding: 8px 14px;
  font-family: var(--font-serif);
  font-size: 1.05rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mw-portada-card-body {
  padding: 14px 16px;
  font-size: 0.88rem;
  line-height: 1.6;
}

/* ==========================================================================
   EDITOR DE CÓDIGO WIKITEXTO
   ========================================================================== */

.mw-editor-container {
  display: none;
}

.mw-editor-toolbar {
  display: flex;
  gap: 4px;
  padding: 6px;
  background-color: var(--mw-surface-2);
  border: 1px solid var(--mw-border);
  border-bottom: none;
  border-radius: 4px 4px 0 0;
  flex-wrap: wrap;
}

.mw-editor-btn {
  background: var(--mw-content-bg);
  border: 1px solid var(--mw-border-subtle);
  padding: 4px 10px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 3px;
  color: var(--mw-text);
}
.mw-editor-btn:hover {
  background-color: var(--mw-hover-bg);
  border-color: var(--mw-border);
}

.mw-editor-textarea {
  width: 100%;
  height: 420px;
  padding: 12px;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  line-height: 1.5;
  color: var(--mw-text);
  background-color: var(--mw-content-bg);
  border: 1px solid var(--mw-border);
  resize: vertical;
  outline: none;
}
.mw-editor-textarea:focus {
  border-color: var(--mw-accent);
}

.mw-editor-actions {
  display: flex;
  gap: 10px;
  margin-top: 12px;
  align-items: center;
}

.mw-btn-primary {
  background-color: var(--mw-accent);
  color: white;
  border: none;
  padding: 8px 18px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
.mw-btn-primary:hover {
  opacity: 0.92;
}

.mw-btn-secondary {
  background: none;
  border: 1px solid var(--mw-border);
  color: var(--mw-text);
  padding: 8px 18px;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
}
.mw-btn-secondary:hover {
  background-color: var(--mw-hover-bg);
}

/* ==========================================================================
   PÁGINA DE DISCUSIÓN (TALK PAGE)
   ========================================================================== */

.mw-talk-container {
  display: none;
}

.mw-talk-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.mw-talk-thread {
  border: 1px solid var(--mw-border-subtle);
  border-radius: 6px;
  padding: 16px;
  margin-bottom: 18px;
  background-color: var(--mw-notice-bg);
}

.mw-talk-thread-title {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  margin-bottom: 8px;
  color: var(--mw-text);
}

.mw-talk-reply {
  margin-left: 24px;
  border-left: 2px solid var(--mw-border);
  padding-left: 12px;
  margin-top: 10px;
  font-size: 0.85rem;
}

.mw-talk-signature {
  font-size: 0.76rem;
  color: var(--mw-text-muted);
  margin-top: 4px;
}

/* ==========================================================================
   HISTORIAL DE VERSIONES (HISTORY)
   ========================================================================== */

.mw-history-container {
  display: none;
}

.mw-history-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  margin-top: 14px;
}

.mw-history-table th, .mw-history-table td {
  padding: 7px 10px;
  border-bottom: 1px solid var(--mw-border-subtle);
  text-align: left;
}

.mw-history-table th {
  background-color: var(--mw-surface-2);
  font-weight: 600;
}

.mw-byte-pos {
  color: #27ae60;
  font-weight: 600;
}
.mw-byte-neg {
  color: #c0392b;
  font-weight: 600;
}

/* ==========================================================================
   FOOTER (MEDIAWIKI STYLE)
   ========================================================================== */

.mw-footer {
  background-color: var(--mw-header-bg);
  border-top: 1px solid var(--mw-border-subtle);
  padding: 24px 20px 40px;
  margin-top: auto;
  font-size: 0.78rem;
  color: var(--mw-text-muted);
  line-height: 1.6;
}

.mw-footer-container {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.mw-footer-links {
  display: flex;
  gap: 16px;
  list-style: none;
  flex-wrap: wrap;
  margin-top: 10px;
}

.mw-footer-logos {
  display: flex;
  gap: 14px;
  align-items: center;
}

/* ==========================================================================
   MODO PÁNICO Y TERMINAL CLASIFICADA
   ========================================================================== */

body.panic-mode {
  --mw-bg: #220000 !important;
  --mw-content-bg: #110000 !important;
  --mw-text: #ff8888 !important;
  --mw-border: #ff2222 !important;
  --mw-border-subtle: #660000 !important;
  --mw-header-bg: #1a0000 !important;
  filter: contrast(1.15);
}

.mw-panic-floating-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 44px;
  height: 44px;
  background-color: #ba0000;
  color: white;
  border-radius: 50%;
  border: 2px solid white;
  box-shadow: 0 4px 14px rgba(186, 0, 0, 0.4);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  z-index: 1500;
  transition: transform 0.2s;
}
.mw-panic-floating-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(186, 0, 0, 0.7);
}

/* Print styles */
@media print {
  .mw-header, .mw-sidebar, .mw-tabs-container, .mw-panic-floating-btn, .mw-footer-logos {
    display: none !important;
  }
  .mw-article-wrapper {
    border: none !important;
    padding: 0 !important;
  }
  body {
    background: white !important;
    color: black !important;
  }
}
"""

print("CSS module created.")
