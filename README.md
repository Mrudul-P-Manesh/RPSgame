# RPS Game

A web-based Rock Paper Scissors application using computer vision and machine learning for real-time hand gesture recognition.

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

## Setup and Usage

### 1. Clone the Repository

git clone https://github.com/Mrudul-P-Manesh/RPSgame.git
cd RPSgame

### 2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

python3 app.py

The application will be available at:

http://127.0.0.1:5000

## Model

The application uses a trained Keras model (`keras_model.h5`) to classify Rock, Paper, and Scissors hand gestures.

Class labels are defined in `labels.txt`. The Flask application processes the model predictions and integrates them with the game logic to determine the outcome.

## Author

Mrudul P Manesh
