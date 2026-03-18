import streamlit as st

st.set_page_config(
    page_title="GlobalFin — Markets Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, header, footer { display: none !important; }
.block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GlobalFin — Markets Overview</title>
<meta name="description" content="Real-time global financial markets dashboard covering equities, FX, crypto, commodities, and macro indicators.">
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600,700&f[]=cabinet-grotesk@400,500,700,800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<style>
/* ─── Design Tokens ─── */
:root,[data-theme="light"]{--color-bg:#0d1117;--color-surface:#161b22;--color-surface-2:#1c2128;--color-surface-offset:#21262d;--color-divider:#30363d;--color-border:#3d444d;--color-text:#e6edf3;--color-text-muted:#8b949e;--color-text-faint:#484f58;--color-text-inverse:#0d1117;--color-primary:#2ea043;--color-primary-hover:#3fb950;--color-accent:#1f6feb;--color-accent-hover:#388bfd;--color-positive:#3fb950;--color-positive-bg:rgba(63,185,80,0.12);--color-negative:#f85149;--color-negative-bg:rgba(248,81,73,0.12);--color-neutral:#8b949e;--color-gold:#d29922;--color-orange:#e3b341;--color-purple:#a371f7;--color-teal:#39c5cf;--radius-sm:0.375rem;--radius-md:0.5rem;--radius-lg:0.75rem;--radius-xl:1rem;--transition:160ms cubic-bezier(0.16,1,0.3,1);--font-display:'Cabinet Grotesk','Helvetica Neue',sans-serif;--font-body:'Satoshi','Inter',sans-serif;--text-xs:clamp(0.75rem,0.7rem + 0.25vw,0.875rem);--text-sm:clamp(0.8rem,0.75rem + 0.3vw,0.9375rem);--text-base:clamp(0.875rem,0.8rem + 0.35vw,1rem);--text-lg:clamp(1rem,0.9rem + 0.5vw,1.25rem);--text-xl:clamp(1.25rem,1rem + 1vw,1.75rem);--space-1:0.25rem;--space-2:0.5rem;--space-3:0.75rem;--space-4:1rem;--space-5:1.25rem;--space-6:1.5rem;--space-8:2rem;--space-10:2.5rem;--space-12:3rem;--sidebar-width:220px;--shadow-sm:0 1px 3px rgba(0,0,0,0.3);--shadow-md:0 4px 12px rgba(0,0,0,0.4);}
[data-theme="dark"]{--color-bg:#0d1117;--color-surface:#161b22;--color-surface-2:#1c2128;--color-surface-offset:#21262d;--color-divider:#30363d;--color-border:#3d444d;--color-text:#e6edf3;--color-text-muted:#8b949e;--color-text-faint:#484f58;--color-text-inverse:#0d1117;}
[data-theme="light"]{--color-bg:#f6f8fa;--color-surface:#ffffff;--color-surface-2:#f6f8fa;--color-surface-offset:#eaeef2;--color-divider:#d0d7de;--color-border:#d0d7de;--color-text:#1f2328;--color-text-muted:#59636e;--color-text-faint:#9198a1;--color-text-inverse:#f6f8fa;--color-positive:#1a7f37;--color-positive-bg:rgba(26,127,55,0.1);--color-negative:#cf222e;--color-negative-bg:rgba(207,34,46,0.1);--shadow-sm:0 1px 3px rgba(31,35,40,0.12);--shadow-md:0 4px 12px rgba(31,35,40,0.15);}

/* ─── Reset ─── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{-webkit-font-smoothing:antialiased;scroll-behavior:smooth;height:100%;overflow:hidden;}
body{font-family:var(--font-body);font-size:var(--text-base);color:var(--color-text);background-color:var(--color-bg);height:100dvh;overflow:hidden;}
img,svg{display:block;}
button{cursor:pointer;background:none;border:none;font:inherit;color:inherit;}
a{text-decoration:none;color:inherit;}
table{border-collapse:collapse;width:100%;}
input,select{font:inherit;color:inherit;}

/* ─── Layout ─── */
.layout{display:grid;grid-template-columns:var(--sidebar-width) 1fr;height:100dvh;overflow:hidden;}

/* ─── Sidebar ─── */
.sidebar{background:var(--color-surface);border-right:1px solid var(--color-divider);display:flex;flex-direction:column;overflow-y:auto;overscroll-behavior:contain;}
.sidebar-header{padding:var(--space-5) var(--space-4);border-bottom:1px solid var(--color-divider);}
.logo{display:flex;align-items:center;gap:var(--space-3);}
.logo-text{font-family:var(--font-display);font-size:var(--text-lg);font-weight:800;letter-spacing:-0.02em;color:var(--color-text);}
.sidebar-nav{flex:1;padding:var(--space-4);display:flex;flex-direction:column;gap:var(--space-1);}
.nav-section-label{font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--color-text-faint);padding:var(--space-2) var(--space-3);margin-top:var(--space-2);}
.nav-item{display:flex;align-items:center;gap:var(--space-3);padding:var(--space-2) var(--space-3);border-radius:var(--radius-md);font-size:var(--text-sm);font-weight:500;color:var(--color-text-muted);transition:background var(--transition),color var(--transition);}
.nav-item:hover{background:var(--color-surface-offset);color:var(--color-text);}
.nav-item.active{background:var(--color-surface-offset);color:var(--color-text);}
.nav-item i{flex-shrink:0;}
.sidebar-footer{padding:var(--space-4);border-top:1px solid var(--color-divider);display:flex;flex-direction:column;gap:var(--space-2);}
.market-status{display:flex;align-items:center;gap:var(--space-2);font-size:var(--text-xs);font-weight:600;color:var(--color-text-muted);}
.status-dot{width:8px;height:8px;border-radius:50%;background:var(--color-positive);box-shadow:0 0 6px var(--color-positive);animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}
.last-updated{font-size:var(--text-xs);color:var(--color-text-faint);}

/* ─── Content Wrapper ─── */
.content-wrapper{display:grid;grid-template-rows:auto 1fr;overflow:hidden;min-width:0;}

/* ─── Topbar ─── */
.topbar{display:flex;align-items:center;justify-content:space-between;padding:0 var(--space-6);height:56px;border-bottom:1px solid var(--color-divider);background:var(--color-surface);gap:var(--space-4);position:sticky;top:0;z-index:10;}
.topbar-left{display:flex;align-items:baseline;gap:var(--space-4);min-width:0;}
.page-title{font-family:var(--font-display);font-size:var(--text-lg);font-weight:800;color:var(--color-text);white-space:nowrap;}
.page-date{font-size:var(--text-xs);color:var(--color-text-faint);white-space:nowrap;}
.topbar-right{display:flex;align-items:center;gap:var(--space-4);min-width:0;}
.ticker-strip{display:flex;align-items:center;gap:var(--space-6);overflow:hidden;max-width:600px;}
.ticker-item{display:flex;align-items:center;gap:var(--space-2);font-size:var(--text-xs);font-weight:600;white-space:nowrap;font-variant-numeric:tabular-nums;}
.ticker-symbol{color:var(--color-text-muted);font-weight:500;}
.ticker-price{color:var(--color-text);}
.ticker-change.pos{color:var(--color-positive);}
.ticker-change.neg{color:var(--color-negative);}
.theme-toggle{width:36px;height:36px;border-radius:var(--radius-md);display:flex;align-items:center;justify-content:center;color:var(--color-text-muted);transition:background var(--transition),color var(--transition);flex-shrink:0;}
.theme-toggle:hover{background:var(--color-surface-offset);color:var(--color-text);}

/* ─── Main ─── */
.main{overflow-y:auto;overscroll-behavior:contain;padding:var(--space-6);display:flex;flex-direction:column;gap:var(--space-6);}

/* ─── KPI Grid ─── */
.kpi-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:var(--space-4);}
@media(max-width:1400px){.kpi-grid{grid-template-columns:repeat(3,1fr);}}
@media(max-width:900px){.kpi-grid{grid-template-columns:repeat(2,1fr);}}
.kpi-card{background:var(--color-surface);border:1px solid var(--color-divider);border-radius:var(--radius-lg);padding:var(--space-4) var(--space-5);transition:border-color var(--transition),box-shadow var(--transition);position:relative;overflow:hidden;}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--color-accent);opacity:0.6;}
.kpi-card:hover{border-color:var(--color-border);box-shadow:var(--shadow-md);}
.kpi-label{font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--color-text-muted);margin-bottom:var(--space-2);}
.kpi-value{font-family:var(--font-display);font-size:var(--text-xl);font-weight:700;color:var(--color-text);font-variant-numeric:tabular-nums lining-nums;line-height:1.15;margin-bottom:var(--space-2);}
.kpi-delta{display:inline-flex;align-items:center;gap:4px;font-size:var(--text-xs);font-weight:700;padding:2px 8px;border-radius:9999px;font-variant-numeric:tabular-nums;}
.kpi-delta.positive{background:var(--color-positive-bg);color:var(--color-positive);}
.kpi-delta.negative{background:var(--color-negative-bg);color:var(--color-negative);}
.kpi-sub{font-size:var(--text-xs);color:var(--color-text-faint);margin-top:var(--space-2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}

/* ─── Charts ─── */
.charts-row{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-4);}
.charts-row:first-of-type{grid-template-columns:2fr 1fr;}
@media(max-width:1100px){.charts-row,.charts-row:first-of-type{grid-template-columns:1fr;}.charts-row .chart-card.wide{grid-column:span 1;}}
.chart-card{background:var(--color-surface);border:1px solid var(--color-divider);border-radius:var(--radius-lg);padding:var(--space-5);display:flex;flex-direction:column;gap:var(--space-4);}
.chart-header{display:flex;align-items:flex-start;justify-content:space-between;gap:var(--space-4);}
.chart-title{font-family:var(--font-display);font-size:var(--text-base);font-weight:700;color:var(--color-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.chart-subtitle{font-size:var(--text-xs);color:var(--color-text-muted);margin-top:var(--space-1);}
.chart-legend{display:flex;align-items:center;gap:var(--space-4);flex-wrap:wrap;}
.legend-item{display:flex;align-items:center;gap:6px;font-size:var(--text-xs);color:var(--color-text-muted);white-space:nowrap;}
.legend-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.chart-container{position:relative;flex:1;min-height:200px;max-height:260px;}
.charts-row.three-col{grid-template-columns:repeat(3,1fr);}
@media(max-width:1200px){.charts-row.three-col{grid-template-columns:repeat(2,1fr);}}
@media(max-width:800px){.charts-row.three-col{grid-template-columns:1fr;}}

/* ─── Tables ─── */
.tables-row{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-4);min-width:0;}
@media(max-width:1200px){.tables-row{grid-template-columns:1fr 1fr;}}
@media(max-width:800px){.tables-row{grid-template-columns:1fr;}}
.table-card{background:var(--color-surface);border:1px solid var(--color-divider);border-radius:var(--radius-lg);overflow:hidden;display:flex;flex-direction:column;min-width:0;}
.table-header{display:flex;align-items:center;justify-content:space-between;padding:var(--space-4) var(--space-5);border-bottom:1px solid var(--color-divider);}
.table-badge{font-size:var(--text-xs);font-weight:600;padding:2px 8px;border-radius:9999px;background:var(--color-positive-bg);color:var(--color-positive);}
.table-scroll{overflow-x:auto;overscroll-behavior:contain;}
thead th{font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--color-text-faint);text-align:left;padding:var(--space-3) var(--space-5);background:var(--color-surface-2);position:sticky;top:0;white-space:nowrap;}
thead th:not(:first-child){text-align:right;}
tbody tr{border-top:1px solid var(--color-divider);transition:background var(--transition);}
tbody tr:hover{background:var(--color-surface-offset);}
tbody td{padding:var(--space-3) var(--space-5);font-size:var(--text-sm);font-variant-numeric:tabular-nums;white-space:nowrap;}
tbody td:first-child{font-weight:600;color:var(--color-text);}
tbody td:not(:first-child){text-align:right;color:var(--color-text-muted);}
.pos-text{color:var(--color-positive)!important;font-weight:700;}
.neg-text{color:var(--color-negative)!important;font-weight:700;}

/* ─── Heatmap ─── */
.heatmap-section{background:var(--color-surface);border:1px solid var(--color-divider);border-radius:var(--radius-lg);padding:var(--space-5);display:flex;flex-direction:column;gap:var(--space-4);}
.section-header{display:flex;flex-direction:column;gap:var(--space-1);}
.heatmap-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:var(--space-2);}
.heatmap-cell{border-radius:var(--radius-md);padding:var(--space-4) var(--space-3);display:flex;flex-direction:column;gap:var(--space-1);cursor:default;transition:transform var(--transition),box-shadow var(--transition);position:relative;overflow:hidden;}
.heatmap-cell:hover{transform:scale(1.03);box-shadow:var(--shadow-md);}
.heatmap-cell-name{font-size:var(--text-xs);font-weight:700;color:rgba(255,255,255,0.9);}
.heatmap-cell-change{font-size:var(--text-sm);font-weight:800;color:white;font-variant-numeric:tabular-nums;}
.heatmap-cell-cap{font-size:var(--text-xs);color:rgba(255,255,255,0.6);}

/* ─── Scrollbar ─── */
::-webkit-scrollbar{width:6px;height:6px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:var(--color-divider);border-radius:3px;}
::-webkit-scrollbar-thumb:hover{background:var(--color-border);}
</style>
</head>
<body>

<div class="layout">
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="logo">
        <svg aria-label="GlobalFin" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" width="32" height="32">
          <rect width="36" height="36" rx="8" fill="var(--color-primary)"/>
          <circle cx="18" cy="18" r="9" stroke="white" stroke-width="1.8" fill="none"/>
          <ellipse cx="18" cy="18" rx="4.5" ry="9" stroke="white" stroke-width="1.8" fill="none"/>
          <line x1="9" y1="18" x2="27" y2="18" stroke="white" stroke-width="1.8"/>
        </svg>
        <span class="logo-text">GlobalFin</span>
      </div>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section-label">Markets</div>
      <a href="#" class="nav-item active" data-view="overview"><i data-lucide="layout-dashboard" width="16" height="16"></i>Overview</a>
      <a href="#" class="nav-item" data-view="equities"><i data-lucide="trending-up" width="16" height="16"></i>Equities</a>
      <a href="#" class="nav-item" data-view="fx"><i data-lucide="arrow-left-right" width="16" height="16"></i>FX / Rates</a>
      <a href="#" class="nav-item" data-view="crypto"><i data-lucide="bitcoin" width="16" height="16"></i>Crypto</a>
      <a href="#" class="nav-item" data-view="commodities"><i data-lucide="package" width="16" height="16"></i>Commodities</a>
      <div class="nav-section-label" style="margin-top:var(--space-6)">Macro</div>
      <a href="#" class="nav-item" data-view="macro"><i data-lucide="bar-chart-3" width="16" height="16"></i>Indicators</a>
      <a href="#" class="nav-item" data-view="bonds"><i data-lucide="landmark" width="16" height="16"></i>Bond Yields</a>
    </nav>
    <div class="sidebar-footer">
      <div class="market-status">
        <span class="status-dot" id="market-status-dot"></span>
        <span id="market-status-text">Markets Open</span>
      </div>
      <div class="last-updated">Updated <span id="last-updated-time">—</span></div>
    </div>
  </aside>

  <div class="content-wrapper">
    <header class="topbar">
      <div class="topbar-left">
        <h1 class="page-title">Markets Overview</h1>
        <span class="page-date" id="current-date"></span>
      </div>
      <div class="topbar-right">
        <div class="ticker-strip" id="ticker-strip"></div>
        <button class="theme-toggle" data-theme-toggle aria-label="Switch to light mode">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
      </div>
    </header>

    <main class="main">
      <section class="kpi-grid">
        <div class="kpi-card" id="kpi-sp500">
          <div class="kpi-label">S&amp;P 500</div>
          <div class="kpi-value" id="val-sp500">5,842.91</div>
          <div class="kpi-delta positive" id="delta-sp500"><i data-lucide="trending-up" width="13" height="13"></i><span>+0.74%</span></div>
          <div class="kpi-sub">YTD +11.2%</div>
        </div>
        <div class="kpi-card" id="kpi-nasdaq">
          <div class="kpi-label">NASDAQ 100</div>
          <div class="kpi-value" id="val-nasdaq">20,441.28</div>
          <div class="kpi-delta positive" id="delta-nasdaq"><i data-lucide="trending-up" width="13" height="13"></i><span>+1.12%</span></div>
          <div class="kpi-sub">YTD +8.6%</div>
        </div>
        <div class="kpi-card" id="kpi-dxy">
          <div class="kpi-label">DXY (USD Index)</div>
          <div class="kpi-value" id="val-dxy">103.42</div>
          <div class="kpi-delta negative" id="delta-dxy"><i data-lucide="trending-down" width="13" height="13"></i><span>−0.31%</span></div>
          <div class="kpi-sub">52W Range: 99.6 – 107.3</div>
        </div>
        <div class="kpi-card" id="kpi-bitcoin">
          <div class="kpi-label">Bitcoin (BTC)</div>
          <div class="kpi-value" id="val-bitcoin">$83,214</div>
          <div class="kpi-delta positive" id="delta-bitcoin"><i data-lucide="trending-up" width="13" height="13"></i><span>+2.38%</span></div>
          <div class="kpi-sub">Market Cap: $1.64T</div>
        </div>
        <div class="kpi-card" id="kpi-gold">
          <div class="kpi-label">Gold (XAU/USD)</div>
          <div class="kpi-value" id="val-gold">$2,987.40</div>
          <div class="kpi-delta positive" id="delta-gold"><i data-lucide="trending-up" width="13" height="13"></i><span>+0.55%</span></div>
          <div class="kpi-sub">ATH: $3,005.20</div>
        </div>
        <div class="kpi-card" id="kpi-10yr">
          <div class="kpi-label">US 10Y Yield</div>
          <div class="kpi-value" id="val-10yr">4.31%</div>
          <div class="kpi-delta negative" id="delta-10yr"><i data-lucide="trending-down" width="13" height="13"></i><span>−3 bps</span></div>
          <div class="kpi-sub">2Y Yield: 4.02%</div>
        </div>
      </section>

      <section class="charts-row">
        <div class="chart-card wide">
          <div class="chart-header">
            <div><div class="chart-title">Global Indices YTD Performance</div><div class="chart-subtitle">Indexed to 100 at Jan 1, 2026</div></div>
            <div class="chart-legend" id="indices-legend"></div>
          </div>
          <div class="chart-container"><canvas id="indicesChart"></canvas></div>
        </div>
        <div class="chart-card">
          <div class="chart-header">
            <div><div class="chart-title">Sector Performance</div><div class="chart-subtitle">Week-over-week change %</div></div>
          </div>
          <div class="chart-container"><canvas id="sectorChart"></canvas></div>
        </div>
      </section>

      <section class="charts-row three-col">
        <div class="chart-card">
          <div class="chart-header"><div><div class="chart-title">FX Rates vs USD</div><div class="chart-subtitle">30-day normalized change</div></div></div>
          <div class="chart-container"><canvas id="fxChart"></canvas></div>
        </div>
        <div class="chart-card">
          <div class="chart-header"><div><div class="chart-title">Crypto Market</div><div class="chart-subtitle">7-day price performance</div></div></div>
          <div class="chart-container"><canvas id="cryptoChart"></canvas></div>
        </div>
        <div class="chart-card">
          <div class="chart-header"><div><div class="chart-title">Yield Curve</div><div class="chart-subtitle">US Treasury yields by maturity</div></div></div>
          <div class="chart-container"><canvas id="yieldChart"></canvas></div>
        </div>
      </section>

      <section class="tables-row">
        <div class="table-card">
          <div class="table-header"><div class="chart-title">Commodities</div><span class="table-badge">Live</span></div>
          <div class="table-scroll"><table><thead><tr><th>Commodity</th><th>Price</th><th>1D %</th><th>1W %</th></tr></thead><tbody id="commodities-table"></tbody></table></div>
        </div>
        <div class="table-card">
          <div class="table-header"><div class="chart-title">FX Rates</div><span class="table-badge">Live</span></div>
          <div class="table-scroll"><table><thead><tr><th>Pair</th><th>Rate</th><th>1D %</th><th>1W %</th></tr></thead><tbody id="fx-table"></tbody></table></div>
        </div>
        <div class="table-card">
          <div class="table-header"><div class="chart-title">Macro Indicators</div><span class="table-badge">Latest</span></div>
          <div class="table-scroll"><table><thead><tr><th>Indicator</th><th>Value</th><th>Prior</th><th>Trend</th></tr></thead><tbody id="macro-table"></tbody></table></div>
        </div>
      </section>

      <section class="heatmap-section">
        <div class="section-header">
          <div class="chart-title">S&amp;P 500 Sector Heatmap</div>
          <div class="chart-subtitle">Market cap weighted — Today's performance</div>
        </div>
        <div class="heatmap-grid" id="heatmap"></div>
      </section>
    </main>
  </div>
</div>

<script>
'use strict';

// ─── Theme Toggle ───
(function(){
  const root=document.documentElement;
  const btn=document.querySelector('[data-theme-toggle]');
  let theme=root.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  root.setAttribute('data-theme',theme);
  function setIcon(t){
    if(!btn)return;
    btn.innerHTML=t==='dark'
      ?'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
      :'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
    btn.setAttribute('aria-label','Switch to '+(t==='dark'?'light':'dark')+' mode');
  }
  setIcon(theme);
  btn&&btn.addEventListener('click',()=>{
    theme=theme==='dark'?'light':'dark';
    root.setAttribute('data-theme',theme);
    setIcon(theme);
    updateChartTheme();
  });
})();

// ─── Date / Time ───
function updateDateTime(){
  const now=new Date();
  const dateEl=document.getElementById('current-date');
  if(dateEl)dateEl.textContent=now.toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric',year:'numeric'});
  const timeEl=document.getElementById('last-updated-time');
  if(timeEl)timeEl.textContent=now.toLocaleTimeString('en-US',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
}
updateDateTime();
setInterval(updateDateTime,1000);

function isMarketOpen(){
  const now=new Date();
  const et=new Date(now.toLocaleString('en-US',{timeZone:'America/New_York'}));
  const day=et.getDay();const hour=et.getHours();const min=et.getMinutes();
  if(day===0||day===6)return false;
  const mins=hour*60+min;
  return mins>=570&&mins<960;
}
const dot=document.getElementById('market-status-dot');
const statusText=document.getElementById('market-status-text');
if(isMarketOpen()){
  if(dot){dot.style.background='var(--color-positive)';dot.style.boxShadow='0 0 6px var(--color-positive)';}
  if(statusText)statusText.textContent='Markets Open';
}else{
  if(dot){dot.style.background='var(--color-negative)';dot.style.boxShadow='0 0 6px var(--color-negative)';}
  if(statusText)statusText.textContent='After Hours';
}

// ─── Data ───
const BASE_DATA={
  indices:{
    'S&P 500':{base:5842.91,delta:0.74,color:'#2ea043'},
    'NASDAQ 100':{base:20441.28,delta:1.12,color:'#1f6feb'},
    'DOW 30':{base:42547.23,delta:0.43,color:'#a371f7'},
    'DAX':{base:22418.35,delta:1.21,color:'#e3b341'},
    'NIKKEI 225':{base:36728.50,delta:-0.38,color:'#f85149'},
    'FTSE 100':{base:8712.40,delta:0.29,color:'#39c5cf'},
  },
  tickers:[
    {sym:'AAPL',price:'228.42',change:'+1.24%',pos:true},
    {sym:'NVDA',price:'887.21',change:'+2.81%',pos:true},
    {sym:'MSFT',price:'413.74',change:'+0.67%',pos:true},
    {sym:'TSLA',price:'288.62',change:'-1.43%',pos:false},
    {sym:'AMZN',price:'219.54',change:'+0.92%',pos:true},
    {sym:'META',price:'596.37',change:'+1.56%',pos:true},
    {sym:'GOOGL',price:'178.91',change:'+0.33%',pos:true},
    {sym:'JPM',price:'241.18',change:'+0.84%',pos:true},
  ],
  commodities:[
    {name:'Gold',price:'$2,987.40',d1:'+0.55%',w1:'+1.82%',pd:true,pw:true},
    {name:'Silver',price:'$33.42',d1:'+0.87%',w1:'+2.14%',pd:true,pw:true},
    {name:'WTI Crude',price:'$67.82',d1:'-0.63%',w1:'-2.38%',pd:false,pw:false},
    {name:'Brent Crude',price:'$71.24',d1:'-0.51%',w1:'-2.11%',pd:false,pw:false},
    {name:'Natural Gas',price:'$4.18',d1:'+1.43%',w1:'+5.62%',pd:true,pw:true},
    {name:'Copper',price:'$4.87',d1:'+0.21%',w1:'+1.14%',pd:true,pw:true},
    {name:'Platinum',price:'$1,024.50',d1:'-0.33%',w1:'-0.87%',pd:false,pw:false},
    {name:'Wheat',price:'$548.20',d1:'-1.12%',w1:'-2.45%',pd:false,pw:false},
  ],
  fx:[
    {pair:'EUR/USD',rate:'1.0845',d1:'+0.42%',w1:'+0.89%',pd:true,pw:true},
    {pair:'GBP/USD',rate:'1.2934',d1:'+0.28%',w1:'+0.53%',pd:true,pw:true},
    {pair:'USD/JPY',rate:'148.32',d1:'-0.31%',w1:'-0.74%',pd:false,pw:false},
    {pair:'USD/CHF',rate:'0.8842',d1:'-0.22%',w1:'-0.48%',pd:false,pw:false},
    {pair:'AUD/USD',rate:'0.6321',d1:'+0.19%',w1:'+0.67%',pd:true,pw:true},
    {pair:'USD/CAD',rate:'1.3847',d1:'+0.11%',w1:'-0.29%',pd:true,pw:false},
    {pair:'USD/CNY',rate:'7.2314',d1:'+0.05%',w1:'+0.14%',pd:true,pw:true},
    {pair:'USD/MXN',rate:'20.1524',d1:'-0.67%',w1:'-1.42%',pd:false,pw:false},
  ],
  macro:[
    {name:'US GDP Growth (Q4)',val:'2.3%',prior:'3.1%',trend:'down'},
    {name:'US CPI YoY',val:'2.8%',prior:'2.9%',trend:'down'},
    {name:'US Core PCE',val:'2.6%',prior:'2.7%',trend:'down'},
    {name:'US Unemployment',val:'4.1%',prior:'4.0%',trend:'up'},
    {name:'Fed Funds Rate',val:'4.25–4.50%',prior:'4.25–4.50%',trend:'flat'},
    {name:'US PMI (Mfg)',val:'52.4',prior:'51.8',trend:'up'},
    {name:'Eurozone CPI',val:'2.3%',prior:'2.5%',trend:'down'},
    {name:'China GDP YoY',val:'4.9%',prior:'5.0%',trend:'down'},
  ],
  heatmap:[
    {name:'Technology',change:+2.14,cap:'$14.2T'},
    {name:'Healthcare',change:+0.82,cap:'$5.8T'},
    {name:'Financials',change:+1.23,cap:'$7.1T'},
    {name:'Consumer Disc.',change:-0.47,cap:'$4.3T'},
    {name:'Comm. Services',change:+1.78,cap:'$3.9T'},
    {name:'Industrials',change:+0.41,cap:'$3.4T'},
    {name:'Consumer Stap.',change:-0.28,cap:'$3.1T'},
    {name:'Energy',change:-1.14,cap:'$2.8T'},
    {name:'Utilities',change:+0.19,cap:'$1.7T'},
    {name:'Real Estate',change:-0.63,cap:'$1.4T'},
    {name:'Materials',change:+0.55,cap:'$1.2T'},
  ],
};

// ─── Ticker Strip ───
const tickerEl=document.getElementById('ticker-strip');
if(tickerEl){
  BASE_DATA.tickers.forEach(t=>{
    const item=document.createElement('div');
    item.className='ticker-item';
    item.innerHTML=`<span class="ticker-symbol">${t.sym}</span><span class="ticker-price">${t.price}</span><span class="ticker-change ${t.pos?'pos':'neg'}">${t.change}</span>`;
    tickerEl.appendChild(item);
  });
}

// ─── Tables ───
function populateTable(id,rows,cols){
  const tbody=document.getElementById(id);
  if(!tbody)return;
  rows.forEach(row=>{
    const tr=document.createElement('tr');
    tr.innerHTML=cols.map(c=>{
      const val=row[c.key];
      let cls='';
      if(c.colorKey)cls=row[c.colorKey]?'pos-text':'neg-text';
      return`<td class="${cls}">${val}</td>`;
    }).join('');
    tbody.appendChild(tr);
  });
}
populateTable('commodities-table',BASE_DATA.commodities,[{key:'name'},{key:'price'},{key:'d1',colorKey:'pd'},{key:'w1',colorKey:'pw'}]);
populateTable('fx-table',BASE_DATA.fx,[{key:'pair'},{key:'rate'},{key:'d1',colorKey:'pd'},{key:'w1',colorKey:'pw'}]);

const macroTbody=document.getElementById('macro-table');
if(macroTbody){
  BASE_DATA.macro.forEach(row=>{
    const tr=document.createElement('tr');
    const trendIcon=row.trend==='up'?`<span class="neg-text">↑</span>`:row.trend==='down'?`<span class="pos-text">↓</span>`:`<span style="color:var(--color-text-faint)">→</span>`;
    tr.innerHTML=`<td>${row.name}</td><td style="text-align:right;color:var(--color-text)">${row.val}</td><td style="text-align:right">${row.prior}</td><td style="text-align:right">${trendIcon}</td>`;
    macroTbody.appendChild(tr);
  });
}

// ─── Heatmap ───
function heatColor(change){
  const abs=Math.min(Math.abs(change),3);const t=abs/3;
  if(change>0){
    const r=Math.round(26+t*(63-26));const g=Math.round(127+t*(185-127));const b=Math.round(55+t*(80-55));
    return`rgb(${r},${g},${b})`;
  }else{
    const r=Math.round(207+t*(248-207));const g=Math.round(34+t*(81-34));const b=Math.round(46+t*(73-46));
    return`rgb(${r},${g},${b})`;
  }
}
const heatmapEl=document.getElementById('heatmap');
if(heatmapEl){
  BASE_DATA.heatmap.forEach(cell=>{
    const div=document.createElement('div');
    div.className='heatmap-cell';
    div.style.background=heatColor(cell.change);
    const sign=cell.change>=0?'+':'';
    div.innerHTML=`<div class="heatmap-cell-name">${cell.name}</div><div class="heatmap-cell-change">${sign}${cell.change.toFixed(2)}%</div><div class="heatmap-cell-cap">${cell.cap}</div>`;
    heatmapEl.appendChild(div);
  });
}

// ─── Chart Theme ───
function getChartTheme(){
  const isDark=document.documentElement.getAttribute('data-theme')!=='light';
  return{
    gridColor:isDark?'rgba(255,255,255,0.06)':'rgba(0,0,0,0.06)',
    textColor:isDark?'#8b949e':'#59636e',
    bgColor:isDark?'#161b22':'#ffffff',
  };
}
Chart.defaults.font.family="'Satoshi','Inter',sans-serif";

// ─── Indices Chart ───
function generateIndexData(months){
  const data=[100];
  for(let i=1;i<months;i++){
    const prev=data[i-1];
    data.push(+(prev*(1+0.008+(Math.random()-0.48)*0.025)).toFixed(2));
  }
  return data;
}
const MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const labels=MONTHS.slice(0,3);
const indexEntries=Object.entries(BASE_DATA.indices);
let indicesChartRef=null;
function buildIndicesChart(){
  const ctx=document.getElementById('indicesChart');if(!ctx)return;
  const theme=getChartTheme();
  const datasets=indexEntries.map(([name,d])=>({
    label:name,data:generateIndexData(labels.length),borderColor:d.color,
    backgroundColor:'transparent',borderWidth:2,pointRadius:0,tension:0.4,
  }));
  const legendEl=document.getElementById('indices-legend');
  if(legendEl&&legendEl.children.length===0){
    indexEntries.forEach(([name,d])=>{
      const item=document.createElement('div');item.className='legend-item';
      item.innerHTML=`<span class="legend-dot" style="background:${d.color}"></span>${name}`;
      legendEl.appendChild(item);
    });
  }
  indicesChartRef=new Chart(ctx,{
    type:'line',data:{labels,datasets},
    options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},
      plugins:{legend:{display:false},tooltip:{backgroundColor:theme.bgColor,borderColor:'#3d444d',borderWidth:1,titleColor:theme.textColor,bodyColor:theme.textColor,padding:12,callbacks:{label:ctx=>` ${ctx.dataset.label}: ${ctx.parsed.y.toFixed(2)}`}}},
      scales:{x:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:11}}},y:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:11}}}}}
  });
}
buildIndicesChart();

// ─── Sector Chart ───
let sectorChartRef=null;
function buildSectorChart(){
  const ctx=document.getElementById('sectorChart');if(!ctx)return;
  const theme=getChartTheme();
  const slabels=BASE_DATA.heatmap.map(h=>h.name);
  const values=BASE_DATA.heatmap.map(h=>h.change);
  const colors=values.map(v=>v>=0?'#2ea043':'#f85149');
  sectorChartRef=new Chart(ctx,{
    type:'bar',data:{labels:slabels,datasets:[{data:values,backgroundColor:colors,borderRadius:4,borderSkipped:false}]},
    options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false},tooltip:{callbacks:{label:ctx=>` ${ctx.parsed.x>0?'+':''}${ctx.parsed.x.toFixed(2)}%`},backgroundColor:theme.bgColor,borderColor:'#3d444d',borderWidth:1,bodyColor:theme.textColor,padding:10}},
      scales:{x:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10}}},y:{grid:{display:false},ticks:{color:theme.textColor,font:{size:10}}}}}
  });
}
buildSectorChart();

// ─── FX Chart ───
let fxChartRef=null;
function buildFxChart(){
  const ctx=document.getElementById('fxChart');if(!ctx)return;
  const theme=getChartTheme();
  const fxLabels=['Wk1','Wk2','Wk3','Wk4','Now'];
  const fxDatasets=[
    {label:'EUR/USD',color:'#2ea043'},{label:'GBP/USD',color:'#1f6feb'},
    {label:'USD/JPY',color:'#f85149'},{label:'AUD/USD',color:'#e3b341'},{label:'USD/CAD',color:'#a371f7'},
  ].map(d=>({label:d.label,data:Array.from({length:5},()=>+((Math.random()-0.5)*2).toFixed(2)),
    borderColor:d.color,backgroundColor:'transparent',borderWidth:2,pointRadius:3,tension:0.3}));
  fxChartRef=new Chart(ctx,{
    type:'line',data:{labels:fxLabels,datasets:fxDatasets},
    options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},
      plugins:{legend:{position:'bottom',labels:{color:theme.textColor,font:{size:10},boxWidth:10,padding:10}},
        tooltip:{backgroundColor:theme.bgColor,borderColor:'#3d444d',borderWidth:1,bodyColor:theme.textColor,padding:10,
          callbacks:{label:ctx=>` ${ctx.dataset.label}: ${ctx.parsed.y>0?'+':''}${ctx.parsed.y.toFixed(2)}%`}}},
      scales:{x:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10}}},
        y:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10},callback:v=>`${v>0?'+':''}${v.toFixed(1)}%`}}}}
  });
}
buildFxChart();

// ─── Crypto Chart ───
let cryptoChartRef=null;
function buildCryptoChart(){
  const ctx=document.getElementById('cryptoChart');if(!ctx)return;
  const theme=getChartTheme();
  const assets=[{name:'BTC',change:+2.38},{name:'ETH',change:+1.84},{name:'SOL',change:+3.21},
    {name:'BNB',change:-0.47},{name:'XRP',change:+4.12},{name:'ADA',change:-1.23},
    {name:'AVAX',change:+2.76},{name:'DOT',change:-0.88}];
  cryptoChartRef=new Chart(ctx,{
    type:'bar',data:{labels:assets.map(a=>a.name),datasets:[{data:assets.map(a=>a.change),
      backgroundColor:assets.map(a=>a.change>=0?'#2ea043':'#f85149'),borderRadius:4,borderSkipped:false}]},
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false},tooltip:{callbacks:{label:ctx=>` ${ctx.parsed.y>0?'+':''}${ctx.parsed.y.toFixed(2)}% (7D)`},
        backgroundColor:theme.bgColor,borderColor:'#3d444d',borderWidth:1,bodyColor:theme.textColor,padding:10}},
      scales:{x:{grid:{display:false},ticks:{color:theme.textColor,font:{size:11}}},
        y:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10},callback:v=>`${v>0?'+':''}${v.toFixed(1)}%`}}}}
  });
}
buildCryptoChart();

// ─── Yield Curve Chart ───
let yieldChartRef=null;
function buildYieldChart(){
  const ctx=document.getElementById('yieldChart');if(!ctx)return;
  const theme=getChartTheme();
  const maturities=['1M','3M','6M','1Y','2Y','5Y','7Y','10Y','20Y','30Y'];
  const yields=[4.72,4.65,4.48,4.28,4.02,4.05,4.18,4.31,4.62,4.68];
  const yieldsYear=[5.32,5.28,5.21,5.10,4.89,4.72,4.71,4.73,4.89,4.94];
  yieldChartRef=new Chart(ctx,{
    type:'line',data:{labels:maturities,datasets:[
      {label:'Mar 2026',data:yields,borderColor:'#1f6feb',backgroundColor:'rgba(31,111,235,0.08)',fill:true,borderWidth:2,pointRadius:3,tension:0.3},
      {label:'Mar 2025',data:yieldsYear,borderColor:'#8b949e',backgroundColor:'transparent',borderWidth:1.5,borderDash:[4,4],pointRadius:2,tension:0.3}]},
    options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},
      plugins:{legend:{position:'bottom',labels:{color:theme.textColor,font:{size:10},boxWidth:10,padding:10}},
        tooltip:{backgroundColor:theme.bgColor,borderColor:'#3d444d',borderWidth:1,bodyColor:theme.textColor,padding:10,
          callbacks:{label:ctx=>` ${ctx.dataset.label}: ${ctx.parsed.y.toFixed(2)}%`}}},
      scales:{x:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10}}},
        y:{grid:{color:theme.gridColor},ticks:{color:theme.textColor,font:{size:10},callback:v=>`${v.toFixed(1)}%`}}}}
  });
}
buildYieldChart();

// ─── Update Chart Theme ───
function updateChartTheme(){
  const theme=getChartTheme();
  [indicesChartRef,sectorChartRef,fxChartRef,cryptoChartRef,yieldChartRef].forEach(chart=>{
    if(!chart)return;
    chart.options.plugins.tooltip.backgroundColor=theme.bgColor;
    chart.options.plugins.tooltip.bodyColor=theme.textColor;
    if(chart.options.plugins.tooltip.titleColor)chart.options.plugins.tooltip.titleColor=theme.textColor;
    if(chart.options.plugins.legend&&chart.options.plugins.legend.labels)
      chart.options.plugins.legend.labels.color=theme.textColor;
    if(chart.options.scales)
      Object.values(chart.options.scales).forEach(scale=>{
        if(scale.grid)scale.grid.color=theme.gridColor;
        if(scale.ticks)scale.ticks.color=theme.textColor;
      });
    chart.update('none');
  });
}

// ─── Live KPI drift ───
function randomWalk(val,pct){return val*(1+(Math.random()-0.5)*pct);}
function updateLiveKPIs(){
  [
    {id:'val-sp500',fmt:v=>v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}),base:5842.91},
    {id:'val-nasdaq',fmt:v=>v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}),base:20441.28},
    {id:'val-dxy',fmt:v=>v.toFixed(2),base:103.42},
    {id:'val-bitcoin',fmt:v=>'$'+Math.round(v).toLocaleString(),base:83214},
    {id:'val-gold',fmt:v=>'$'+v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}),base:2987.40},
    {id:'val-10yr',fmt:v=>v.toFixed(2)+'%',base:4.31},
  ].forEach(u=>{
    const el=document.getElementById(u.id);
    if(el)el.textContent=u.fmt(randomWalk(u.base,0.001));
  });
}
setInterval(updateLiveKPIs,4000);

// ─── Nav ───
document.querySelectorAll('.nav-item').forEach(item=>{
  item.addEventListener('click',e=>{
    e.preventDefault();
    document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
    item.classList.add('active');
  });
});

// ─── Init Lucide icons ───
lucide.createIcons();
</script>
</body>
</html>
"""

st.components.v1.html(html, height=920, scrolling=False)
