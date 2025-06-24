## ❤️ Heart Disease Prediction with Web App

A machine learning-based web application to predict the 10-year risk of coronary heart disease (CHD) using logistic regression. Integrated with a clean, responsive frontend built using HTML and CSS, and a Flask backend for real-time user interaction.

---

<img width="949" alt="Image" src="https://github.com/user-attachments/assets/f62c75ea-152e-4065-8d6b-b9a86c900113" />

---

## 📊 Dataset

* **Source**: https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset
* Predicts whether a patient will develop CHD within 10 years.
  
* **Features used**:

  * Age
  * Sex (Male/Female)
  * Cigarettes per Day
  * Total Cholesterol
  * Systolic Blood Pressure
  * Glucose

---

## 🚀 Features

* ✅ Logistic Regression model trained on real patient data
* ✅ Predict CHD risk based on 6 medical features
* ✅ Scaled input via `StandardScaler`
* ✅ Clean and mobile-responsive UI
* ✅ Red/Green prediction message styling
* ✅ Error handling for invalid inputs

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask, Joblib
* **Machine Learning**: Scikit-learn, Pandas, NumPy
* **Frontend**: HTML5, CSS3 (inline + image background support)

---

## 📁 Project Structure

```

├── HeartDiseasePrediction/
│   ├── app.py                      # Flask backend
│   ├── HeartDiseasePrediction.pkl  # Trained ML model
│   ├── scaler.pkl                  # Saved StandardScaler
│   ├── static/
│   │   └── image/
│   │       └── background.jpg      # Background image
│   └── templates/
│       └── index.html              # Frontend UI
```

---

## 🧠 Model Details

* **Model**: Logistic Regression
* **Data Preprocessing**:

  * Removed null values
  * Dropped non-essential columns
  * Scaled inputs using `StandardScaler`
* **Evaluation**: Accuracy, Confusion Matrix, Classification Report

---

## ▶️ How to Run

- create folder - HeartDiseasePrediction
- Inside this folder place app.py, HeartDiseasePrediction.pkl,scaler.pkl, templates/index_csv.html, static/images/
- Inside project folder open command prompt - run app.py
- command to run - python app.py
- open link provided in the console 

---

## 📝 To Train Model Yourself

Use this structure:

```
HeartDiseasePrediction/
├── HeartDiseasePrediction.ipnyb       # Training script
├── framingham.csv       # Dataset
 
```

---

## ⚠️ Limitations

While the project demonstrates a working machine learning pipeline and web app integration, it has a few limitations worth noting:

* **Imbalanced Dataset**:
  The Framingham dataset is highly imbalanced, with far fewer positive CHD cases (label `1`). This can cause the logistic regression model to be biased toward predicting the majority class (`0` - Low Risk), reducing sensitivity to actual high-risk patients.

* **Simple Model Choice**:
  Logistic regression, while interpretable and fast, may underperform compared to more complex models like Random Forests or Gradient Boosting, especially with nonlinear relationships.

* **Feature Selection**:
  Only six medical features were used. In real-world scenarios, more detailed and personalized medical data (e.g., family history, BMI, physical activity) would lead to better predictions.

---

