
<div align="center">

<img src="assets/spam shield logo.png" height="40" alt="SpamShield" />

</div>

<div align="center">

# 🛡️ SpamShield · Email Analyzer

**ML-powered spam detection with real-time classification, confidence scoring, and user feedback.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

<br/>

[![View Demo](https://img.shields.io/badge/🚀__View_Live_Demo-FF5F38?style=for-the-badge&logoColor=white)](https://spam-shield-mk64spdts.streamlit.app/)

<br/>
</div>

---

## Overview

SpamShield analyzes email content and instantly classifies it as **Spam** or **Not Spam** using a trained machine learning pipeline. It identifies the spam category, displays a confidence score, and lets users report wrong predictions — structured for a future Supabase integration.

---

## ✦ Features

| | Feature | Description |
|---|---|---|
| ⚡ | **Real-Time Detection** | Instant verdict the moment you hit Analyze |
| 📊 | **Confidence Scoring** | Visual bar with exact percentage and spam probability |
| 🏷️ | **Spam Categorization** | Clusters spam into Promotional, Financial, or Pharmacy types |
| ⚑ | **Wrong Prediction Reports** | Inline feedback form |
| 🎨 | **Theme-Neutral UI** | Works on both Streamlit light and dark themes |
| 🧪 | **Example Presets** | One-click examples for instant testing |

---

## 🗂️ Project Structure
```
spamshield/
│
├── app.py              ← Entry point — layout, routing, analyze logic
├── components.py       ← HTML renderers: header, result card, idle state
├── styles.py           ← Global CSS injected at page load
├── report.py           ← Feedback form, state management, data layer
├── utils.py            ← ML pipeline: clean → vectorize → predict → cluster
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   ├── spam_model.pkl
│   └── kmeans_model.pkl
│
└── requirements.txt
```

---

## 🤖 ML Pipeline
```
Raw Email Text
      │
      ▼
┌─────────────────────┐
│    Text Cleaning    │  lowercase · strip punctuation · normalize whitespace
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   TF-IDF Transform  │  fitted tfidf_vectorizer.pkl
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Classification    │  binary prediction + probability → spam_model.pkl
└──────────┬──────────┘
           │
      ┌────┴────┐
    Spam     Not Spam
      │
      ▼
┌─────────────────────┐
│  KMeans Clustering  │  assign spam category → kmeans_model.pkl
└─────────────────────┘
```

**Spam clusters:**

| Cluster | Category |
|:---:|---|
| `00` | Promotional / Marketing Spam |
| `01` | Financial / Investment Spam |
| `02` | Pharmacy / Medical Spam |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.9+
```bash
# 1. Clone the repository
git clone https://github.com/your-username/spamshield.git
cd spamshield

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

**`requirements.txt`**
```
streamlit
scikit-learn
joblib
numpy
```

---

## 👤 Author
<div align="center">
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/manmath647.png" width="88" style="border-radius:50%"/><br/><br/>
      <b>Manmath Kornule</b><br/>
      <sub>Learning AI Everyday</sub><br/><br/>
      <a href="https://github.com/your-username">
        <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
      </a>&nbsp;
      <a href="https://linkedin.com/in/your-profile">
        <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>
      </a>&nbsp;
      <a href="https://your-portfolio.com">
        <img src="https://img.shields.io/badge/Portfolio-FF5F38?style=flat-square&logo=firefox&logoColor=white" alt="Portfolio"/>
      </a>
    </td>
  </tr>
</table>
</div>
<div align="center">

---

Built with ❤️ using **Streamlit** · **scikit-learn** · **Python**


</div>
