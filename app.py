from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the saved model and scaler using joblib
model = joblib.load('HeartDiseasePrediction.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input values from form
    try:
        int_features = [float(request.form[field]) for field in ['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']]
    except ValueError:
        return render_template('index.html', prediction_text="Please enter valid numeric inputs.")

    # convert those features into 2D array
    final_features = np.array(int_features).reshape(1, -1)

    # Scale the input using the same scaler used during training
    scaled_features = scaler.transform(final_features)

    prediction = model.predict(scaled_features)

    output = 'High risk of future coronary heart disease (CHD)' if prediction[0] == 1 else 'Low risk of future coronary heart disease (CHD)'
    color = 'red' if output == 'High risk of future coronary heart disease (CHD)' else 'green' 

    return render_template('index.html', prediction_text=f'{output}',color=color)

if __name__ == "__main__":
    app.run(debug=True)
