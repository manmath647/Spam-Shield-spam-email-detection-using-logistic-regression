"""
components.py — HTML rendering helpers for SpamShield UI.

Structure:
  - Static constants: HEADER_HTML, IDLE_HTML
  - One builder:      result_card_html()  → returns HTML string
  - Three renderers:  render_header(), render_idle(), render_result()
"""

from __future__ import annotations  # Union type syntax on Python 3.9+
import streamlit as st


# ── Static HTML ───────────────────────────────────────────────────────────────

HEADER_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<div class="app-header">
  <div class="header-dot"></div>
  <div class="app-logo" style="font-family:'Syne',sans-serif;font-weight:800;">Spam<em>Shield</em></div>
  <div class="app-tagline" style="font-family:'DM Mono',monospace;">ML-powered · Real-time detection</div>
</div>
"""

IDLE_HTML = """
<div class="idle-state">
  <div class="idle-icon">🛡️</div>
  <div class="idle-text">Paste an email and press Analyze to see the verdict.</div>
</div>
"""


# ── HTML builder ──────────────────────────────────────────────────────────────

def result_card_html(
    label: str,
    probability: float,
    cluster: int | str,
    spam_type: str | None,
) -> str:
    """Return the full result card + advice block as an HTML string."""
    is_spam    = label == "Spam"
    cls        = "spam" if is_spam else "safe"
    icon       = "🚨"   if is_spam else "✅"
    confidence = probability if is_spam else 1 - probability
    bar_pct    = round(confidence * 100, 1)
    spam_prob  = round(probability * 100, 1)

    if is_spam:
        badge_html   = f'<span class="badge badge-spam">{spam_type or "Spam"}</span>'
        advice_label = "Action required:"
        advice_body  = (
            "Do not click any links or reply. Mark as spam and delete. "
            "If it appears to come from a known sender, verify through a "
            "separate channel before engaging."
        )
    else:
        badge_html   = '<span class="badge badge-safe">Clean</span>'
        advice_label = "Looks clean."
        advice_body  = (
            "No strong spam signals detected. Stay cautious with unexpected "
            "attachments or requests for personal information, even from "
            "trusted senders."
        )

    return f"""
    <div class="result-card result-{cls}">

      <div class="verdict-row">
        <div class="verdict-label {cls}">{icon} {label}</div>
        <div class="verdict-pct {cls}">{bar_pct}%</div>
      </div>

      <div class="verdict-sub">{badge_html}</div>

      <div class="bar-track">
        <div class="bar-fill bar-{cls}" style="width:{bar_pct}%"></div>
      </div>

      <div class="stats-grid">
        <div class="stat-box">
          <div class="stat-val {cls}">{bar_pct}%</div>
          <div class="stat-key">Confidence</div>
        </div>
        <div class="stat-box">
          <div class="stat-val neutral">{spam_prob}%</div>
          <div class="stat-key">Spam prob.</div>
        </div>
        <div class="stat-box">
          <div class="stat-val neutral">{cluster if cluster is not None else "—"}</div>
          <div class="stat-key">Cluster</div>
        </div>
      </div>

    </div>

    <div class="advice-block">
      <span class="advice-label">{advice_label}</span> {advice_body}
    </div>
    """


# ── Streamlit renderers ───────────────────────────────────────────────────────

def render_header() -> None:
    st.markdown(HEADER_HTML, unsafe_allow_html=True)


def render_idle() -> None:
    st.markdown(IDLE_HTML, unsafe_allow_html=True)


def render_result(
    label: str,
    probability: float,
    cluster: int | str,
    spam_type: str | None,
) -> None:
    st.markdown(
        result_card_html(label, probability, cluster, spam_type),
        unsafe_allow_html=True,
    )