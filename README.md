## Overview

RPS Game uses a trained TensorFlow/Keras model to recognize hand gestures corresponding to Rock, Paper, and Scissors. The application integrates the trained model with a Flask backend and a web-based interface to provide an interactive gameplay experience.

## Features

- Real-time hand gesture recognition
- Rock, Paper, and Scissors classification
- TensorFlow/Keras-based machine learning model
- Flask-based web application
- Browser-based user interface
- Automated game result generation

## Technologies Used

- Python
- Flask
- TensorFlow
- Keras
- HTML
- CSS
- JavaScript

## Project Structure

```text
RPSgame/
├── app.py
├── game.py
├── tensor.py
├── keras_model.h5
├── labels.txt
├── model_summary.txt
├── templates/
├── static/
├── .gitignore
└── README.md
Installation
Clone the repository:
git clone https://github.com/Mrudul-P-Manesh/RPSgame.git
cd RPSgame
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Running the Application
Start the Flask application:
python3 app.py
Open the application in a browser at:
http://127.0.0.1:5000
Application Workflow
Camera Input
      |
      v
Image Processing
      |
      v
TensorFlow/Keras Model
      |
      v
Gesture Classification
      |
      v
Rock / Paper / Scissors
      |
      v
Game Logic
      |
      v
Game Result
Machine Learning Model
The trained model is stored in keras_model.h5.
The class labels used by the model are stored in labels.txt.
The model processes the captured input and predicts the corresponding hand gesture, which is then passed to the game logic to determine the result.
Future Improvements
- Improve gesture classification accuracy
- Add score tracking
- Implement multiplayer functionality
- Add difficulty levels
- Optimize model inference performance
- Improve the user interface
- Deploy the application for public access
Author
Mrudul P Manesh
```
