from flask import Flask, render_template, request
import joblib
import numpy as np
import os


# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
nb_model = joblib.load("fake_news_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Define route for the home page
@app.route('/')
def home():
    return render_template("index.html")

# Define route for predicting news
@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        # Get the text input from the form
        new_text = request.form['news_text']

        # Transform the input text using the TF-IDF vectorizer
        new_text_tfidf = tfidf_vectorizer.transform([new_text])

        # Predict with the trained model
        prediction = nb_model.predict(new_text_tfidf)
        prediction_prob = nb_model.predict_proba(new_text_tfidf)

        # Prepare the result to send back to the user
        result = {
            'prediction': 'Real' if prediction[0] == 1 else 'Fake',
            'fake_prob': prediction_prob[0][0],
            'real_prob': prediction_prob[0][1]
        }

        return render_template("index.html", result=result)

if __name__ == '__main__':
    # Fetch the port from the environment variable (Render assigns it automatically)
    port = os.getenv('PORT', 5000)  # Default to 5000 if the environment variable isn't set
    app.run(host='0.0.0.0', port=int(port), debug=True)  # Listen on 0.0.0.0 for external access