import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only the useful columns and rename them
df = df[["v1", "v2"]]
df.columns = ["label", "text"]

# Convert text messages into numbers the model can understand
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save the model and vectorizer to files
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")