from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__, template_folder=os.path.abspath('.'))
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = pd.DataFrame([features])
    prediction = model.predict(final_features)
    prediction_in_grams = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Predicted Weight: {} grams'.format(prediction_in_grams))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use 5000 as default if $PORT not set
    app.run(host='0.0.0.0', port=port)
