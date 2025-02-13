from flask import Flask, request, jsonify, render_template
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)[0]
    result = "FAKE NEWS" if prediction == 1 else "REAL NEWS"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
