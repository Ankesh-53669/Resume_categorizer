# Resume Classification Project

## **Overview**
This project involves building a multi-class text classification model to categorize resumes into their corresponding job categories. The trained model will assist Human Resources (HR) processes by automating resume categorization, improving efficiency in job placement.

---

## **Problem Statement**
The objective is to train a model using a provided dataset of resumes and deploy it to predict the job category for new resumes. This task includes:
1. **Data Preprocessing**: Extract textual content from PDFs.
2. **Feature Engineering**: Process the extracted text to generate meaningful features.
3. **Model Training**: Build and evaluate a multi-class classification model.
4. **Deployment**: Deploy the trained model to predict the job category of new resumes automatically.

---

## **Dataset Description**
The dataset comprises resumes stored in 24 directories, each representing a job category. Key details:
- Total categories: 24
- Each directory contains PDF resumes specific to a job category.
- Examples of categories: Accountant, Advocate, IT, Engineering, etc.

---

## **Workflow**

### **1. Data Preprocessing**
- **Text Extraction**:
  - Extract textual content from PDF resumes using tools like `pdfplumber`, `PyMuPDF`, or `Tika`.
  - Handle issues like missing text, corrupt files, or scanned PDFs.
  
- **Data Cleaning**:
  - Remove stop words, special characters, and irrelevant text.
  - Normalize the text (lowercasing, stemming, or lemmatization).

- **Error Handling**:
  - Log corrupt or unprocessable files for later review.

### **2. Feature Engineering**
- **Vectorization**:
  - Use techniques like TF-IDF or Word2Vec to transform textual data into numerical features.

- **Dimensionality Reduction**:
  - Apply methods like PCA if the feature space is too large.

### **3. Model Training**
- **Algorithm Selection**:
  - Random Forest, Logistic Regression, or Support Vector Machines for multi-class classification.

- **Evaluation**:
  - Use metrics like accuracy, F1-score, precision, and recall.
  - Perform cross-validation to ensure model robustness.

### **4. Deployment**
- **API Development**:
  - Create RESTful APIs using Flask or FastAPI to serve the model.

- **Prediction Workflow**:
  - Input: New resume PDFs.
  - Output: Predicted job category.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8+
- Libraries: `pdfplumber`, `scikit-learn`, `pandas`, `numpy`, `Flask`, `requests`

### **Installation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up directories:
   - Ensure the dataset is placed in the `data/` directory.
   - Structure: `data/<job_category>/<resumes>`

### **Run the Project**
1. **Data Preprocessing**:
   - Execute the script to extract and clean text from PDFs:
     ```bash
     python Assignments/Scripts/data_preprocessing.py.py
     ```

2. **Model Training**:
   - Train the classification model:
     Training.ipynb
     

3. **Model Deployment**:
   - Start the Flask API:
     ```bash
     python app.py
     ```

4. **Prediction**:
   - Use the API to upload a new resume PDF and get its predicted category.

---

## **Key Considerations**
- **Large Dataset Handling**:
  - Process files in smaller batches.
  - Save intermediate results to avoid reprocessing.

- **Error Handling**:
  - Log unprocessable files for further debugging.

- **Performance Optimization**:
  - Limit text extraction to relevant sections (e.g., first 2-3 pages).
  - Optimize model parameters using GridSearchCV.

---

## **Future Enhancements**
1. Incorporate Optical Character Recognition (OCR) for scanned PDFs.
2. Improve text cleaning using advanced NLP techniques.
3. Integrate the solution into existing HR management systems.

