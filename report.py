"""
report.py — "Report Wrong Prediction" feedback feature for SpamShield.

Exports:
  FEEDBACK_STYLES      — <style> block for feedback UI
  init_feedback_state()— initialise session_state keys
  save_feedback()      — store a feedback entry (swap body for Supabase later)
  render_feedback()    — button + inline form, shown below the result card

Supabase-ready:
  Replace the body of save_feedback() only. Everything else stays the same.
"""

from __future__ import annotations
import uuid
from datetime import datetime
import streamlit as st


# ════════════════════════════════════════════════════════════════
# STYLES
# ════════════════════════════════════════════════════════════════

FEEDBACK_STYLES = """
<style>
  /* ── Report button ────────────────────────────────────────── */
  .feedback-zone .stButton > button {
    background: transparent !important;
    border: 1px solid rgba(128, 128, 128, 0.30) !important;
    border-radius: 7px !important;
    color: inherit !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.74rem !important;
    font-weight: 400 !important;
    padding: 0.30rem 0.85rem !important;
    box-shadow: none !important;
    opacity: 0.65;
    transition: opacity 0.15s, border-color 0.15s !important;
    margin-top: 0.6rem;
  }
  .feedback-zone .stButton > button:hover {
    opacity: 1 !important;
    border-color: rgba(128, 128, 128, 0.55) !important;
    background: rgba(128, 128, 128, 0.05) !important;
    transform: none !important;
    box-shadow: none !important;
  }

  /* ── Feedback form container ──────────────────────────────── */
  .feedback-form-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    margin-top: 0.9rem;
    opacity: 0.80;
  }

  /* ── Success message ──────────────────────────────────────── */
  .feedback-success {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.75rem;
    padding: 0.65rem 0.9rem;
    background: var(--green-bg);
    border: 1px solid var(--green-bdr);
    border-radius: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 0.76rem;
    color: var(--green);
    animation: rslide 0.22s ease;
  }
</style>
"""


# ════════════════════════════════════════════════════════════════
# DATA LAYER
# ════════════════════════════════════════════════════════════════

def save_feedback(
    email_content: str,
    predicted_label: str,
    corrected_label: str,
    confidence: float,
    feedback_text: str,
) -> None:
    """
    Save a feedback entry to local session state.
    ── Supabase swap ──────────────────────────────────────────
    supabase.table("feedback").insert({
        "id":              str(uuid.uuid4()),
        "email_content":   email_content,
        "predicted_label": predicted_label,
        "corrected_label": corrected_label,
        "confidence":      confidence,
        "feedback_text":   feedback_text,
        "created_at":      datetime.utcnow().isoformat(),
    }).execute()
    """
    entry = {
        "id":              str(uuid.uuid4()),
        "email_content":   email_content,
        "predicted_label": predicted_label,   # original model prediction
        "corrected_label": corrected_label,   # what user says it should be
        "confidence":      confidence,
        "feedback_text":   feedback_text,     # optional user note
        "created_at":      datetime.now(),
    }
    st.session_state.feedback_list.insert(0, entry)


# ════════════════════════════════════════════════════════════════
# PUBLIC API
# ════════════════════════════════════════════════════════════════

def init_feedback_state() -> None:
    """Initialise all session_state keys used by this module."""
    _keys = {
        "feedback_list":       [],    # list[dict] — stored feedback entries
        "feedback_form_open":  False, # bool — is the inline form visible
        "feedback_submitted":  False, # bool — show success banner
        "_feedback_last_email": "",   # str — tracks current email for reset
    }
    for key, default in _keys.items():
        if key not in st.session_state:
            st.session_state[key] = default


def render_feedback(
    email_content: str,
    predicted_label: str,
    confidence: float,
) -> None:
    """
    Render the 'Report Wrong Prediction' button and inline feedback form.
    Call this directly below render_result() in the right panel.
    """
    # Reset form state whenever a new email is analyzed
    if st.session_state._feedback_last_email != email_content:
        st.session_state.feedback_form_open  = False
        st.session_state.feedback_submitted  = False
        st.session_state._feedback_last_email = email_content

    # ── Success banner — shown after submission ────────────────
    if st.session_state.feedback_submitted:
        st.markdown("""
        <div class="feedback-success">
          ✓ &nbsp;Feedback submitted. Thank you for helping improve accuracy.
        </div>
        """, unsafe_allow_html=True)
        return  # hide button after submission

    # ── Toggle button ──────────────────────────────────────────
    btn_label = "✕  Cancel" if st.session_state.feedback_form_open else "⚑  Report Wrong Prediction"
    st.markdown('<div class="feedback-zone">', unsafe_allow_html=True)
    if st.button(btn_label, key="feedback_toggle"):
        st.session_state.feedback_form_open = not st.session_state.feedback_form_open
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if not st.session_state.feedback_form_open:
        return

    # ── Inline form ────────────────────────────────────────────
    st.markdown(
        '<div class="feedback-form-title">What should this email have been classified as?</div>',
        unsafe_allow_html=True,
    )

    options       = ["Spam", "Not Spam"]
    default_index = 1 if predicted_label == "Spam" else 0
    corrected     = st.radio(
        "Correct classification",
        options=options,
        index=default_index,
        horizontal=True,
        label_visibility="collapsed",
        key="feedback_correction",
    )

    feedback_text = st.text_area(
        "Additional feedback (optional)",
        placeholder="Tell us more about why this prediction was wrong…",
        height=90,
        key="feedback_text_input",
    )

    # Reuse .analyze-zone so Submit gets the same orange primary styling
    st.markdown('<div class="analyze-zone">', unsafe_allow_html=True)
    if st.button("Submit Feedback", use_container_width=True, type="primary", key="feedback_submit"):
        save_feedback(
            email_content   = email_content,
            predicted_label = predicted_label,
            corrected_label = corrected,
            confidence      = confidence,
            feedback_text   = feedback_text.strip(),
        )
        st.session_state.feedback_form_open  = False
        st.session_state.feedback_submitted  = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)