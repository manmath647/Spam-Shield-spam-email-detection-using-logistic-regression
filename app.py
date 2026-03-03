import time
import streamlit as st

from utils import predict_email, get_spam_category
from styles import STYLES
from components import render_header, render_idle, render_result
from report import FEEDBACK_STYLES, init_feedback_state, render_feedback

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SpamShield · Email Analyzer",
    page_icon="📧",
    layout="wide",
)
st.markdown(STYLES, unsafe_allow_html=True)
st.markdown(FEEDBACK_STYLES, unsafe_allow_html=True)

# ── Example presets ───────────────────────────────────────────────────────────
EXAMPLES = {
    "💰 Lottery scam": "Congratulations! You've won $1,000,000! Click here to claim your prize immediately. Limited time offer!",
    "💊 Pharma spam":  "Buy cheap Viagra online! No prescription needed. 80% off all medications. Order now!",
    "✅ Legit email":  "Hi Sarah, just confirming our 3pm meeting tomorrow. I'll bring the Q3 reports. See you then!",
}

# ── Session state ─────────────────────────────────────────────────────────────
_defaults = {"email_text": "", "result": None, "pending_example": None}
for _key, _val in _defaults.items():
    if _key not in st.session_state:
        st.session_state[_key] = _val

init_feedback_state()  # initialises all feedback-specific state keys

# Resolve any pending example BEFORE widgets render so value= picks it up.
if st.session_state.pending_example is not None:
    st.session_state.email_text      = st.session_state.pending_example
    st.session_state.result          = None
    st.session_state.pending_example = None

# ── Header ────────────────────────────────────────────────────────────────────
render_header()

# ── Two-column layout ─────────────────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

# ── LEFT: Input panel ─────────────────────────────────────────────────────────
with left:
    st.markdown('<div class="panel-label">Email content</div>', unsafe_allow_html=True)

    # Chip buttons — .chip-zone scopes their CSS so Analyze stays unaffected
    st.markdown('<div class="chip-zone">', unsafe_allow_html=True)
    chip_cols = st.columns(len(EXAMPLES))
    for col, (lbl, txt) in zip(chip_cols, EXAMPLES.items()):
        if col.button(lbl, use_container_width=True, key=f"chip_{lbl}"):
            st.session_state.pending_example = txt
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # No key= on textarea so value= from session_state always controls it
    email_input = st.text_area(
        "Email content",
        value=st.session_state.email_text,
        height=215,
        placeholder="Paste email subject + body here…",
        label_visibility="collapsed",
    )
    st.session_state.email_text = email_input

    st.markdown(
        f'<div class="char-count">{len(email_input.strip())} chars</div>',
        unsafe_allow_html=True,
    )

    # type="primary" maps to [data-testid="stBaseButton-primary"] in CSS
    st.markdown('<div class="analyze-zone">', unsafe_allow_html=True)
    analyze = st.button("Analyze →", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

    if analyze:
        if not email_input.strip():
            st.warning("Please enter some text before analyzing.")
            st.session_state.result = None
        else:
            with st.spinner("Analyzing…"):
                time.sleep(0.35)
                label, probability, cluster = predict_email(email_input)
            st.session_state.result = (label, probability, cluster)

# ── RIGHT: Output panel ───────────────────────────────────────────────────────
with right:
    st.markdown('<div class="panel-label">Detection result</div>', unsafe_allow_html=True)

    if st.session_state.result is None:
        render_idle()
    else:
        label, probability, cluster = st.session_state.result
        spam_type  = get_spam_category(cluster) if label == "Spam" else None
        is_spam    = label == "Spam"
        confidence = probability if is_spam else 1 - probability

        render_result(label, probability, cluster, spam_type)

        # Feedback button + form — sits directly below the result card
        render_feedback(
            email_content   = email_input,
            predicted_label = label,
            confidence      = round(confidence * 100, 1),
        )