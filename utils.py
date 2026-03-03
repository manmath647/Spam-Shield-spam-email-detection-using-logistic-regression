import re
import joblib
import numpy as np

# Load models once
tfidf_vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
spam_model       = joblib.load("models/spam_model.pkl")
kmeans_model     = joblib.load("models/kmeans_model.pkl")


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\bescapenumber\b', '', text)
    text = re.sub(r'\bescapelong\b', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def predict_email(text):
    cleaned    = clean_text(text)
    vectorized = tfidf_vectorizer.transform([cleaned])

    prediction  = spam_model.predict(vectorized)[0]
    probability = spam_model.predict_proba(vectorized)[0][1]

    if prediction == 1:
        label   = "Spam"
        cluster = kmeans_model.predict(vectorized)[0]
    else:
        label   = "Not Spam"
        cluster = None

    return label, probability, cluster


def get_spam_category(cluster):
    categories = {
        0: "Promotional / Marketing Spam",
        1: "Financial / Investment Spam",
        2: "Pharmacy / Medical Spam",
    }
    return categories.get(cluster, "Unknown Spam Type")