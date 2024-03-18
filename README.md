## Fish Weight Prediction

This repository contains a Flask web application that predicts the weight of a fish based on its measurements.

## Project Structure

The project has two main components:

1. `model.py`: This script loads the fish dataset, trains a Linear Regression model, evaluates its performance, and saves the trained model.
2. `app.py`: This is the main Flask application script. It loads the trained model and uses it to make predictions.

## Setup and Installation

1. Clone the repository:
    ```
    git clone https://github.com/abedy101/fish-weight-prediction.git
    ```
2. Navigate to the project directory:
    ```
    cd fish-weight-prediction
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the model script to train and save the model:
    ```
    python model.py
    ```
5. Start the Flask application:
    ```
    python app.py
    ```

## Usage

Once the Flask application is running, navigate to `http://localhost:5000` in your web browser. Enter the fish measurements into the form and click 'Predict' to get the predicted weight.

## License

This project is licensed under the MIT License.
