import tensorflow as tf
import cv2
import numpy as np
import random

from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)


# Load model
model = tf.keras.models.load_model(
    "keras_model.h5",
    compile=False
)


# Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ")[1] for line in f.readlines()]


moves = ["rock", "paper", "scissor"]


def winner(player, computer):

    if player == computer:
        return "Draw"

    if (player == "rock" and computer == "scissor") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissor" and computer == "paper"):
        return "You Win"

    return "Computer Wins"



camera = cv2.VideoCapture(0)



def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break


        img = cv2.resize(frame,(224,224))

        img = np.asarray(img)
        img = np.expand_dims(img,axis=0)
        img = img/255.0


        prediction = model.predict(
            img,
            verbose=0
        )


        index = np.argmax(prediction)

        player = labels[index]

        confidence = prediction[0][index]


        computer = random.choice(moves)

        result = winner(
            player,
            computer
        )


        cv2.putText(
            frame,
            f"You: {player}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )


        cv2.putText(
            frame,
            f"Computer: {computer}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )


        cv2.putText(
            frame,
            result,
            (20,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )


        _, buffer = cv2.imencode(
            '.jpg',
            frame
        )


        frame = buffer.tobytes()


        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )



@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route("/video")
def video():

    return Response(
        generate_frames(),
        mimetype=
        "multipart/x-mixed-replace; boundary=frame"
    )



if __name__=="__main__":

    app.run(
        debug=True
    )