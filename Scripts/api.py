import pickle

import nltk
import pdfplumber
from flask import Flask, jsonify, request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")

# Initialize Flask app
app = Flask(__name__)

# Load the trained model, vectorizer, and label encoder
model = pickle.load(open("models\model.pkl", "rb"))
vectorizer = pickle.load(open("models\vectorizer.pkl", "rb"))
le = pickle.load(open("models\label_encoder.pkl", "rb"))


# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = " ".join(
        [word for word in text.split() if word not in stopwords.words("english")]
    )
    text = " ".join([WordNetLemmatizer().lemmatize(word) for word in text.split()])
    return text


# Predicting endpoint for resume PDFs
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the PDF file from request
        file = request.files["file"]

        # Extract text from the PDF
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        # Preprocess the extracted text
        processed_text = preprocess_text(text)

        # Vectorize the text
        vectorized_text = vectorizer.transform([processed_text]).toarray()

        # Predict using the model
        prediction = model.predict(vectorized_text)

        # Decode the category label
        category = le.inverse_transform(prediction)[0]

        return jsonify({"job_category": category})

    except Exception as e:
        return jsonify({"error": str(e)})


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
