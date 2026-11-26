# -*- coding: utf-8 -*-
"""
Master builder script for Fakepedia.
Generates index.html, archivos.html, and reclutas.html.
"""

import json
import os
from css_styles import CSS
from articles_data import ARTICLES, TALK_DATA, HISTORY_DATA
from js_scripts import JS

def get_svg_logo():
    return """<svg class="mw-logo-icon" width="38" height="38" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="globeGrad" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="45%" stop-color="#e8ecf1"/>
      <stop offset="80%" stop-color="#bec8d2"/>
      <stop offset="100%" stop-color="#9aa5b1"/>
    </radialGradient>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.25"/>
    </filter>
  </defs>
  <circle cx="100" cy="100" r="88" fill="url(#globeGrad)" filter="url(#shadow)"/>
  <path d="M 40 45 C 60 40 70 55 90 48 C 110 42 125 55 150 45" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 25 85 C 45 78 65 92 88 85 C 112 78 135 90 172 82" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 22 128 C 50 120 70 135 95 125 C 120 115 145 130 176 120" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 38 165 C 60 158 80 168 105 160 C 130 152 148 162 165 155" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 65 25 C 60 50 72 75 62 105 C 52 135 68 155 60 180" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 105 18 C 98 48 112 75 102 108 C 92 140 108 160 102 188" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <path d="M 145 28 C 138 55 150 82 142 115 C 134 145 146 168 140 182" stroke="#7d8895" stroke-width="2.5" fill="none"/>
  <text x="62" y="70" font-family="'Linux Libertine', Georgia, serif" font-size="28" font-weight="bold" fill="#30353b" text-anchor="middle">Ω</text>
  <text x="103" y="66" font-family="'Linux Libertine', Georgia, serif" font-size="28" font-weight="bold" fill="#20252b" text-anchor="middle">F</text>
  <text x="142" y="72" font-family="'Linux Libertine', Georgia, serif" font-size="24" font-weight="bold" fill="#3a4048" text-anchor="middle">祖</text>
  <text x="56" y="115" font-family="'Linux Libertine', Georgia, serif" font-size="25" font-weight="bold" fill="#2b3138" text-anchor="middle">И</text>
  <text x="102" y="112" font-family="'Linux Libertine', Georgia, serif" font-size="26" font-weight="bold" fill="#181d22" text-anchor="middle">Ψ</text>
  <text x="144" y="114" font-family="'Linux Libertine', Georgia, serif" font-size="25" font-weight="bold" fill="#333940" text-anchor="middle">ש</text>
  <text x="62" y="152" font-family="'Linux Libertine', Georgia, serif" font-size="22" font-weight="bold" fill="#444b54" text-anchor="middle">ف</text>
  <text x="102" y="150" font-family="'Linux Libertine', Georgia, serif" font-size="23" font-weight="bold" fill="#242930" text-anchor="middle">д</text>
  <text x="140" y="148" font-family="'Linux Libertine', Georgia, serif" font-size="22" font-weight="bold" fill="#3d444d" text-anchor="middle">ㄱ</text>
</svg>"""

def build_index():
    articles_json = json.dumps(ARTICLES, ensure_ascii=False)
    talk_json = json.dumps(TALK_DATA, ensure_ascii=False)
    history_json = json.dumps(HISTORY_DATA, ensure_ascii=False)
    svg_logo = get_svg_logo()

    html = f"""<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fakepedia, la enciclopedia libre</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml;utf8,{svg_logo.replace('"', "'")}">
  
  <!-- FUENTES FORMALES DE WIKIPEDIA -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">

  <style>
{CSS}
  </style>
</head>
<body>

  <!-- ELEMENTO DE AUDIO DE FONDO (WIKIPEDIA SPOKEN PLAYER) -->
  <audio id="fakepediaAudio" loop preload="metadata">
    <source src="music.mp3" type="audio/mpeg">
  </audio>

  <!-- HEADER OFICIAL MEDIAWIKI / VECTOR 2022 -->
  <header class="mw-header">
    <div class="mw-header-left">
      <button class="mw-sidebar-toggle" id="sidebarToggle" aria-label="Menú principal">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M3 5h14a1 1 0 010 2H3a1 1 0 010-2zm0 4h14a1 1 0 010 2H3a1 1 0 010-2zm0 4h14a1 1 0 010 2H3a1 1 0 010-2z" clip-rule="evenodd"/>
        </svg>
      </button>

      <a href="#Portada" class="mw-logo">
        {svg_logo}
        <div class="mw-logo-title-group">
          <span class="mw-logo-wordmark">FAKEPEDIA</span>
          <span class="mw-logo-tagline">La enciclopedia libre</span>
        </div>
      </a>
    </div>

    <!-- BUSCADOR -->
    <div class="mw-header-center">
      <div class="mw-search-form">
        <span class="mw-search-icon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </span>
        <input type="text" class="mw-search-input" id="searchInput" placeholder="Buscar en Fakepedia..." autocomplete="off">
        <button class="mw-search-clear" id="searchClear" title="Borrar búsqueda">×</button>
      </div>

      <!-- MENÚ DESPLEGABLE DE RESULTADOS -->
      <div class="mw-search-dropdown" id="searchDropdown"></div>
    </div>

    <!-- HERRAMIENTAS DE USUARIO Y CONFIGURACIÓN -->
    <div class="mw-header-right">
      <button class="mw-tool-btn" id="themeToggle" title="Cambiar a modo oscuro / claro">🌙</button>
      <button class="mw-tool-btn" id="fontSizeBtn" title="Ajustar tamaño de texto">A<sup>±</sup></button>
      <button class="mw-tool-btn" id="widthBtn" title="Alternar ancho de lectura">⬌</button>

      <div class="mw-user-anon">
        <span>No has iniciado sesión</span>
        <a href="#Especial:ArchivosClasificados" class="mw-tool-btn" style="text-decoration:none;">Acceder</a>
      </div>
    </div>
  </header>

  <!-- CUERPO PRINCIPAL CON SIDEBAR Y ARTÍCULO -->
  <div class="mw-page-wrapper">
    
    <!-- BARRA LATERAL (SIDEBAR DE WIKIPEDIA) -->
    <nav class="mw-sidebar" id="mwSidebar">
      <div class="mw-sidebar-section">
        <div class="mw-sidebar-heading">Navegación</div>
        <ul class="mw-sidebar-list">
          <li class="mw-sidebar-item"><a href="#Portada">Portada</a></li>
          <li class="mw-sidebar-item"><a href="#Trinidad_Albina">Trinidad Albina</a></li>
          <li class="mw-sidebar-item"><a href="#Demian">Demian (Progenitor)</a></li>
          <li class="mw-sidebar-item"><a href="#La_Sentencia_del_Vacío">La Sentencia del Vacío</a></li>
          <li class="mw-sidebar-item"><a href="#Los_Diez_Sucesores">Los Diez Sucesores</a></li>
          <li class="mw-sidebar-item"><a href="#Cónclave_de_Marfil">Cónclave de Marfil</a></li>
          <li class="mw-sidebar-item"><a href="#Especial:PáginaAleatoria">Página aleatoria</a></li>
        </ul>
      </div>

      <div class="mw-sidebar-section">
        <div class="mw-sidebar-heading">Archivos Especiales</div>
        <ul class="mw-sidebar-list">
          <li class="mw-sidebar-item"><a href="#Especial:ArchivosClasificados">Archivos Secretos (Ω-4)</a></li>
          <li class="mw-sidebar-item"><a href="#Especial:RegistroReclutas">Registro de Reclutas</a></li>
          <li class="mw-sidebar-item"><a href="#Especial:CambiosRecientes">Cambios recientes</a></li>
          <li class="mw-sidebar-item"><a href="#Fakepedia:Acerca_de">Acerca de Fakepedia</a></li>
        </ul>
      </div>

      <div class="mw-sidebar-section">
        <div class="mw-sidebar-heading">Imprimir / Exportar</div>
        <ul class="mw-sidebar-list">
          <li class="mw-sidebar-item"><a href="javascript:window.print()">Descargar como PDF</a></li>
          <li class="mw-sidebar-item"><a href="javascript:window.print()">Versión para imprimir</a></li>
        </ul>
      </div>

      <div class="mw-sidebar-section">
        <div class="mw-sidebar-heading">En otros idiomas</div>
        <ul class="mw-sidebar-list">
          <li class="mw-sidebar-item"><a href="#Portada">English</a></li>
          <li class="mw-sidebar-item"><a href="#Portada">Français</a></li>
          <li class="mw-sidebar-item"><a href="#Portada">Deutsch</a></li>
          <li class="mw-sidebar-item"><a href="#Portada">Latina</a></li>
          <li class="mw-sidebar-item"><a href="#Portada">日本語</a></li>
        </ul>
      </div>
    </nav>

    <!-- ÁREA DE CONTENIDO DEL ARTÍCULO -->
    <main class="mw-body-container">
      <article class="mw-article-wrapper">

        <!-- PESTAÑAS SUPERIORES DE WIKIPEDIA -->
        <div class="mw-tabs-container">
          <ul class="mw-tabs-left">
            <li class="mw-tab-item selected" id="tab-read"><a href="#">Artículo</a></li>
            <li class="mw-tab-item" id="tab-talk"><a href="#">Discusión</a></li>
          </ul>

          <ul class="mw-tabs-right">
            <li class="mw-tab-item" id="tab-edit"><button class="mw-tab-btn">Editar código</button></li>
            <li class="mw-tab-item" id="tab-history"><button class="mw-tab-btn">Ver historial</button></li>
            <li class="mw-tab-item"><button class="mw-tab-btn" onclick="alert('Página añadida a su lista de seguimiento.');">⭐ Seguir</button></li>
          </ul>
        </div>

        <!-- TÍTULO Y SUBTÍTULO -->
        <h1 class="firstHeading" id="firstHeading">Cargando...</h1>
        <div class="siteSub" id="siteSub">De Fakepedia, la enciclopedia libre</div>

        <!-- CUERPO DEL ARTÍCULO (DINÁMICO) -->
        <div id="mw-article-body"></div>

        <!-- PÁGINA DE DISCUSIÓN (VISTA ALTERNATIVA) -->
        <div class="mw-talk-container" id="mw-talk-container"></div>

        <!-- EDITOR DE WIKITEXTO (VISTA ALTERNATIVA) -->
        <div class="mw-editor-container" id="mw-editor-container">
          <div class="mw-editor-toolbar">
            <button class="mw-editor-btn" data-wrap="'''">Negrita</button>
            <button class="mw-editor-btn" data-wrap="''">Cursiva</button>
            <button class="mw-editor-btn" data-wrap="[[">Enlace</button>
            <button class="mw-editor-btn" data-wrap="==">Encabezado</button>
            <button class="mw-editor-btn" data-wrap="&lt;ref&gt;">Cita</button>
            <button class="mw-editor-btn" data-wrap="{{">Plantilla</button>
          </div>
          <textarea class="mw-editor-textarea" id="editorTextarea"></textarea>
          <div id="editorPreviewArea"></div>
          <div class="mw-editor-actions">
            <button class="mw-btn-primary" id="editorSaveBtn">Guardar cambios</button>
            <button class="mw-btn-secondary" id="editorPreviewBtn">Mostrar previsualización</button>
            <button class="mw-btn-secondary" id="editorCancelBtn">Cancelar</button>
          </div>
        </div>

        <!-- HISTORIAL DE VERSIONES (VISTA ALTERNATIVA) -->
        <div class="mw-history-container" id="mw-history-container"></div>

        <!-- CATEGORÍAS (FOOTER DEL ARTÍCULO) -->
        <div class="catlinks" id="catlinks">
          <span><strong>Categorías:</strong></span>
          <ul>
            <li><a href="#Trinidad_Albina">Trinidad Albina</a></li>
            <li><a href="#Portada">Especies trascendentes</a></li>
            <li><a href="#Especial:ArchivosClasificados">Clasificación Ω-4</a></li>
            <li><a href="#Los_Diez_Sucesores">Historia oculta de Europa</a></li>
            <li><a href="#Portada">1026</a></li>
          </ul>
        </div>

      </article>
    </main>

  </div>

  <!-- BOTÓN FLOTANTE DE PÁNICO (BRECHA DE SEGURIDAD) -->
  <button class="mw-panic-floating-btn" id="panicFloatingBtn" title="Protocolo de pánico / Alerta roja">☠️</button>

  <!-- HOVERCARD FLOTANTE (PREVIEW DE ARTÍCULO ESTILO WIKIPEDIA) -->
  <div class="mw-hovercard" id="mw-hovercard">
    <div class="mw-hovercard-image" id="hovercardImg"></div>
    <div class="mw-hovercard-body">
      <div class="mw-hovercard-title" id="hovercardTitle"></div>
      <div class="mw-hovercard-extract" id="hovercardExtract"></div>
    </div>
    <div class="mw-hovercard-footer">
      <a href="#" id="hovercardLink">Leer artículo completo en Fakepedia ➜</a>
    </div>
  </div>

  <!-- TOOLTIP FLOTANTE DE REFERENCIAS -->
  <div class="mw-ref-tooltip" id="mw-ref-tooltip"></div>

  <!-- PIE DE PÁGINA (MEDIAWIKI FOOTER) -->
  <footer class="mw-footer">
    <div class="mw-footer-container">
      <div>
        <p>Esta página se editó por última vez el 26 nov 2026 a las 04:19 (UTC).</p>
        <p>El texto está disponible bajo la <a href="#Fakepedia:Acerca_de">Licencia Creative Commons Atribución-CompartirIgual 4.0</a> y los protocolos de preservación del consorcio XXI. Pueden aplicarse cláusulas adicionales de confidencialidad.</p>
        <ul class="mw-footer-links">
          <li><a href="#Fakepedia:Acerca_de">Política de privacidad</a></li>
          <li><a href="#Fakepedia:Acerca_de">Acerca de Fakepedia</a></li>
          <li><a href="#Fakepedia:Acerca_de">Exoneración de responsabilidad</a></li>
          <li><a href="#Especial:RegistroReclutas">Código de conducta</a></li>
          <li><a href="#Especial:ArchivosClasificados">Desarrolladores</a></li>
          <li><a href="#Especial:CambiosRecientes">Estadísticas</a></li>
        </ul>
      </div>

      <div class="mw-footer-logos">
        <div style="font-family:var(--font-serif); font-size:1.1rem; font-weight:bold; color:var(--mw-text-muted);">
          POWERED BY <span style="color:var(--mw-accent);">FAKPEDIA MEDIAWIKI</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- DATOS Y SCRIPTS -->
  <script>
    window.FAKPEDIA_ARTICLES = {articles_json};
    window.FAKPEDIA_TALK = {talk_json};
    window.FAKPEDIA_HISTORY = {history_json};
  </script>
  <script>
{JS}
  </script>

</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html created successfully.")

def build_redirect_page(filename, target_hash, title):
    svg_logo = get_svg_logo()
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=index.html#{target_hash}">
  <title>{title} - Redirigiendo a Fakepedia</title>
  <script>
    window.location.href = "index.html#{target_hash}";
  </script>
</head>
<body style="font-family:sans-serif; text-align:center; padding:50px; background:#f8f9fa;">
  <p>Redirigiendo a <a href="index.html#{target_hash}">Fakepedia: {title}</a>...</p>
</body>
</html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{filename} created successfully.")

if __name__ == "__main__":
    build_index()
    build_redirect_page("archivos.html", "Especial:ArchivosClasificados", "Archivos Clasificados")
    build_redirect_page("reclutas.html", "Especial:RegistroReclutas", "Registro de Reclutas")
    print("All Fakepedia files generated.")
