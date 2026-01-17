import pandas as pd
import pickle
import os
import json
import time
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

os.makedirs("models", exist_ok=True)

TRAIN_SEED = os.getenv("TRAIN_SEED")
RANDOM_STATE = int(TRAIN_SEED) if TRAIN_SEED and TRAIN_SEED.isdigit() else 42

def _validate(df):
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("Dataset must contain 'text' and 'label' columns")
    df = df.dropna(subset=["text", "label"])
    return df

def train_model():
    data_path = "data/synthetic_resumes.csv"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run generate_data.py first.")
        return

    started_at = time.time()
    run_id = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    print("Loading data...")
    df = pd.read_csv(data_path)
    df = _validate(df)

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    print("Vectorizing text...")
    tfidf = TfidfVectorizer(stop_words="english", max_features=3000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    print("Training Naive Bayes classifier...")
    clf = MultinomialNB()
    clf.fit(X_train_tfidf, y_train)

    print("Evaluating model...")
    y_pred = clf.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    base_model_path = "models/resume_classifier.pkl"
    base_vec_path = "models/tfidf_vectorizer.pkl"

    versioned_model_path = f"models/resume_classifier_{run_id}.pkl"
    versioned_vec_path = f"models/tfidf_vectorizer_{run_id}.pkl"

    print("Saving model and vectorizer...")
    with open(base_model_path, "wb") as f:
        pickle.dump(clf, f)

    with open(base_vec_path, "wb") as f:
        pickle.dump(tfidf, f)

    with open(versioned_model_path, "wb") as f:
        pickle.dump(clf, f)

    with open(versioned_vec_path, "wb") as f:
        pickle.dump(tfidf, f)

    run_meta = {
        "run_id": run_id,
        "data_path": data_path,
        "samples": len(df),
        "random_state": RANDOM_STATE,
        "accuracy": round(accuracy, 5),
        "started_at": datetime.utcnow().isoformat(),
        "training_time_sec": round(time.time() - started_at, 3),
        "artifacts": {
            "model": versioned_model_path,
            "vectorizer": versioned_vec_path
        }
    }

    with open(f"models/run_{run_id}.json", "w", encoding="utf-8") as f:
        json.dump(run_meta, f, indent=2)

    print("Done! Model saved.")
    print(f"Run metadata written to models/run_{run_id}.json")

if __name__ == "__main__":
    train_model()
