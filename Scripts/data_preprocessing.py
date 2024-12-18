import os

import nltk
import pandas as pd
import pdfplumber
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Directory path where the PDFs are stored (replace with your path)
base_path = "C:\\Users\\admin\\insurance_api\\data"


# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stop_words])
    # Lemmatize words
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])
    return text


# List to store resume data
data = []

# Loop through each directory (category)
for category in os.listdir(base_path):
    category_path = os.path.join(base_path, category)
    if os.path.isdir(category_path):
        # Loop through each PDF file in the directory
        for file in os.listdir(category_path):
            file_path = os.path.join(category_path, file)
            if file.endswith(".pdf"):
                try:
                    # Extract text from the PDF file
                    with pdfplumber.open(file_path) as pdf:
                        text = ""
                        for page in pdf.pages:
                            text += page.extract_text()
                            print("done")

                    # If the file is not empty, preprocess and add it to the data list
                    if text.strip():
                        data.append(
                            {"Resume": preprocess_text(text), "Category": category}
                        )
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to CSV for future use
df.to_csv("processed_resumes.csv", index=False)
