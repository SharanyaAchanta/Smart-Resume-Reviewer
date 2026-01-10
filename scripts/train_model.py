import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

def train_model():
    data_path = "data/synthetic_resumes.csv"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run generate_data.py first.")
        return

    print("Loading data...")
    df = pd.read_csv(data_path)
    
    # Preprocessing
    # (Basic for now: TF-IDF handles most of it, but we can add more later)
    X = df["text"]
    y = df["label"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorization
    print("Vectorizing text...")
    tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    # Train Model (Naive Bayes is good for text classification with small data)
    print("Training Naive Bayes classifier...")
    clf = MultinomialNB()
    clf.fit(X_train_tfidf, y_train)

    # Evaluate
    print("Evaluating model...")
    y_pred = clf.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Save artifacts
    print("Saving model and vectorizer...")
    with open("models/resume_classifier.pkl", "wb") as f:
        pickle.dump(clf, f)
    
    with open("models/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(tfidf, f)
        
    print("Done! Model saved to models/resume_classifier.pkl")

if __name__ == "__main__":
    train_model()
