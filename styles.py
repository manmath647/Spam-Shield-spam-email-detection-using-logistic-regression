STYLES = """
<style>
  /*
    Theme-neutral design — works on Streamlit light & dark themes.
    No background-color overrides on Streamlit containers.
    All custom elements use rgba() colors that layer correctly on any bg.
    Font loading: handled via <link> tags in HEADER_HTML (components.py).
  */

  /* ── CSS variables ────────────────────────────────────────── */
  :root {
    --accent:      #ff5f38;
    --accent-glow: rgba(255, 95, 56, 0.22);
    --green:       #16a35e;
    --green-bg:    rgba(22, 163, 94, 0.09);
    --green-bdr:   rgba(22, 163, 94, 0.28);
    --red:         #dc2626;
    --red-bg:      rgba(220, 38, 38, 0.08);
    --red-bdr:     rgba(220, 38, 38, 0.26);
    --muted-bg:    rgba(128, 128, 128, 0.06);
    --muted-bdr:   rgba(128, 128, 128, 0.14);
    --muted-line:  rgba(128, 128, 128, 0.16);
  }

  /* ── Streamlit chrome ─────────────────────────────────────── */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container {
    padding: 1.4rem 2rem 1rem !important;
    max-width: 1280px !important;
  }

  /* ── Textarea ─────────────────────────────────────────────── */
  textarea {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
    line-height: 1.65 !important;
    caret-color: var(--accent) !important;
    resize: none !important;
    border-radius: 10px !important;
    transition: border-color 0.18s, box-shadow 0.18s !important;
  }
  textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(255, 95, 56, 0.10) !important;
  }

  /* ── App header ───────────────────────────────────────────── */
  .app-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding-bottom: 1.1rem;
    border-bottom: 1px solid var(--muted-line);
    margin-bottom: 1.3rem;
  }
  .header-dot {
    width: 7px;
    height: 7px;
    background: var(--accent);
    border-radius: 50%;
    flex-shrink: 0;
    animation: hpulse 2.4s ease-in-out infinite;
  }
  @keyframes hpulse {
    0%, 100% { opacity: 1;    transform: scale(1); }
    50%       { opacity: 0.35; transform: scale(0.78); }
  }
  .app-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 800;
    letter-spacing: -0.02em;
  }
  .app-logo em { color: var(--accent); font-style: normal; }
  .app-tagline {
    font-family: 'DM Mono', monospace;
    font-size: 0.70rem;
    opacity: 0.55;
    margin-left: auto;
    letter-spacing: 0.03em;
  }

  /* ── Panel label ──────────────────────────────────────────── */
  .panel-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.67rem;
    opacity: 0.55;
    text-transform: uppercase;
    letter-spacing: 0.10em;
    margin-bottom: 0.6rem;
  }

  /* ── Char counter ─────────────────────────────────────────── */
  .char-count {
    font-family: 'DM Mono', monospace;
    font-size: 0.69rem;
    opacity: 0.50;
    text-align: right;
    margin-top: -0.4rem;
    margin-bottom: 0.55rem;
  }

  /* ── Example chip buttons ─────────────────────────────────── */
  /* .chip-zone scope prevents bleed to the Analyze button       */
  .chip-zone .stButton > button {
    background: transparent !important;
    border: 1px solid rgba(128, 128, 128, 0.35) !important;
    border-radius: 6px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.72rem !important;
    font-weight: 400 !important;
    opacity: 0.80;
    padding: 0.28rem 0.45rem !important;
    box-shadow: none !important;
    transition: opacity 0.15s, border-color 0.15s, background 0.15s !important;
  }
  .chip-zone .stButton > button:hover {
    opacity: 1 !important;
    border-color: rgba(128, 128, 128, 0.60) !important;
    background: rgba(128, 128, 128, 0.07) !important;
    transform: none !important;
    box-shadow: none !important;
  }

  /* ── Analyze button ───────────────────────────────────────── */
  /* Double selector: data-testid for reliability, .analyze-zone */
  /* as fallback in case Streamlit changes its testid naming.    */
  [data-testid="stBaseButton-primary"],
  .analyze-zone .stButton > button {
    width: 100% !important;
    background: var(--accent) !important;
    border: none !important;
    border-radius: 9px !important;
    color: #fff !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    padding: 0.65rem 1.2rem !important;
    letter-spacing: 0.03em !important;
    box-shadow: 0 2px 14px var(--accent-glow) !important;
    transition: opacity 0.16s, transform 0.13s, box-shadow 0.16s !important;
  }
  [data-testid="stBaseButton-primary"]:hover,
  .analyze-zone .stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 5px 22px rgba(255, 95, 56, 0.32) !important;
  }
  [data-testid="stBaseButton-primary"]:active,
  .analyze-zone .stButton > button:active {
    transform: translateY(0) !important;
  }

  /* ── Idle placeholder ─────────────────────────────────────── */
  .idle-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 300px;
    border: 1.5px dashed rgba(128, 128, 128, 0.35);
    border-radius: 14px;
    text-align: center;
    padding: 2rem;
    gap: 0.5rem;
    opacity: 0.72;
  }
  .idle-icon { font-size: 1.8rem; }
  .idle-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.76rem;
    line-height: 1.6;
    max-width: 190px;
    color: rgba(80, 80, 80, 0.9);
  }

  /* ── Result card ──────────────────────────────────────────── */
  .result-card {
    border-radius: 12px;
    padding: 1.2rem 1.3rem;
    border: 1px solid;
    animation: rslide 0.26s ease;
  }
  @keyframes rslide {
    from { opacity: 0; transform: translateY(5px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .result-spam { background: var(--red-bg);   border-color: var(--red-bdr); }
  .result-safe { background: var(--green-bg); border-color: var(--green-bdr); }

  .verdict-row {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin-bottom: 0.12rem;
  }
  .verdict-label {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }
  .verdict-label.spam { color: var(--red); }
  .verdict-label.safe { color: var(--green); }

  .verdict-pct {
    font-family: 'DM Mono', monospace;
    font-size: 1.05rem;
    font-weight: 500;
  }
  .verdict-pct.spam { color: var(--red); }
  .verdict-pct.safe { color: var(--green); }

  /* verdict-sub holds only the badge — no opacity here so badge  */
  /* colors aren't composited down by a dimmed parent             */
  .verdict-sub {
    margin-bottom: 0.8rem;
  }

  /* ── Badge ────────────────────────────────────────────────── */
  .badge {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 0.18rem 0.55rem;
    border-radius: 4px;
    border: 1px solid;
  }
  .badge-spam { color: var(--red);   border-color: var(--red-bdr);   background: var(--red-bg); }
  .badge-safe { color: var(--green); border-color: var(--green-bdr); background: var(--green-bg); }

  /* ── Confidence bar ───────────────────────────────────────── */
  /* Uses border + muted bg so track is visible on light & dark  */
  .bar-track {
    background: var(--muted-bg);
    border: 1px solid var(--muted-bdr);
    border-radius: 999px;
    height: 7px;
    overflow: hidden;
    margin-bottom: 0.9rem;
  }
  .bar-fill {
    height: 100%;
    border-radius: 999px;
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .bar-spam { background: var(--red); }
  .bar-safe { background: var(--green); }

  /* ── Stats grid ───────────────────────────────────────────── */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.5rem;
  }
  .stat-box {
    background: var(--muted-bg);
    border: 1px solid var(--muted-bdr);
    border-radius: 8px;
    padding: 0.6rem 0.4rem;
    text-align: center;
  }
  .stat-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.08rem;
    font-weight: 700;
    line-height: 1.1;
  }
  .stat-val.spam    { color: var(--red); }
  .stat-val.safe    { color: var(--green); }
  .stat-val.neutral { opacity: 0.50; }
  .stat-key {
    font-family: 'DM Mono', monospace;
    font-size: 0.61rem;
    opacity: 0.42;
    margin-top: 0.2rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  /* ── Advice block ─────────────────────────────────────────── */
  /*
    FIX: Previously used opacity on the container + strong { opacity:1 }.
    CSS opacity composites — a child cannot exceed its parent's opacity.
    Solution: remove opacity from container, use rgba color on text instead.
    .advice-label is a <span> styled distinctly, avoiding <strong> entirely.
  */
  .advice-block {
    margin-top: 0.75rem;
    padding: 0.8rem 1rem;
    background: var(--muted-bg);
    border: 1px solid var(--muted-bdr);
    border-radius: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    line-height: 1.65;
    color: rgba(60, 60, 60, 0.88);
    animation: rslide 0.32s ease;
  }
  .advice-label {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.80rem;
    color: rgba(30, 30, 30, 0.90);
  }

  /* ── Responsive ───────────────────────────────────────────── */
  @media (max-width: 768px) {
    .block-container { padding: 1rem 1rem 0.5rem !important; }
    .app-tagline { display: none; }
    .stats-grid { gap: 0.35rem; }
  }
</style>
"""