import tensorflow as tf
import cv2
import numpy as np
import random

# Load Teachable Machine model
model = tf.keras.models.load_model(
    "keras_model.h5",
    compile=False
)

# Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ")[1] for line in f.readlines()]

print("Classes:", labels)

choices = ["rock", "paper", "scissor"]


def get_winner(player, computer):
    if player == computer:
        return "Draw"

    if (player == "rock" and computer == "scissor") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissor" and computer == "paper"):
        return "You Win!"

    return "Computer Wins!"


# Open webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize image for Teachable Machine
    img = cv2.resize(frame, (224, 224))

    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Prediction
    prediction = model.predict(img, verbose=0)

    index = np.argmax(prediction)
    confidence = prediction[0][index]

    player_move = labels[index]

    # Computer move
    computer_move = random.choice(choices)

    # Result
    result = get_winner(player_move, computer_move)


    # Display output
    cv2.putText(
        frame,
        f"You: {player_move}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Computer: {computer_move}",
        (20, 80),
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

    cv2.putText(
        frame,
        f"Confidence: {confidence:.2f}",
        (20,160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )


    cv2.imshow("Rock Paper Scissors AI", frame)


    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()