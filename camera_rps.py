import random
import cv2
import numpy as np
import time
from keras.models import load_model

class RockPaperScissorsGame:
    
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.model = None
        self.class_names = []

    def load_model(self, model_path, labels_path):
        # Load the model
        self.model = load_model(model_path)

        # Load the labels
        with open(labels_path, "r") as f:
            self.class_names = f.read().splitlines()

    def get_computer_choice(self):
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)

    def get_prediction(self):
        # Create a new capture from the webcam
        cap = cv2.VideoCapture(0)

        # Start the countdown
        countdown = 3
        start_time = time.time()

        while countdown > 0:
            # Grab the frame from the webcam
            ret, frame = cap.read()

            # Resize the frame to the input shape of the model
            resized_frame = cv2.resize(frame, (224, 224))

            # Convert the frame to a numpy array and reshape it to the model's input shape
            image = np.asarray(resized_frame, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image
            image = image / 127.5 - 1

            # Make the prediction
            prediction = self.model.predict(image)
            class_index = np.argmax(prediction)
            class_name = self.class_names[class_index]
            confidence_score = prediction[0][class_index]

            # Print the countdown and prediction
            elapsed_time = int(time.time() - start_time)
            print(f"Countdown: {countdown - elapsed_time}")
            print(f"You chose: {class_name[2:]}\n")

            # Show the frame with countdown
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f"Countdown: {countdown - elapsed_time}", (20, 50), font, 1, (0, 255, 0), 2)
            cv2.imshow("Webcam Image", frame)

            # Listen to the keyboard for presses
            keyboard_input = cv2.waitKey(1)

            # Update the countdown
            if elapsed_time >= countdown or keyboard_input == ord("c"):
                break

        # Clean up
        cap.release()
        cv2.destroyAllWindows()

        return class_name[2:]

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            print("It is a tie!")
            return "tie"
        elif (
            (computer_choice == "Rock" and user_choice == "Scissors")
            or (computer_choice == "Paper" and user_choice == "Rock")
            or (computer_choice == "Scissors" and user_choice == "Paper")
        ):
            print("You lost!")
            return "computer"
        else:
            print("You won!")
            return "user"

    def play(self):
        while self.computer_wins < 3 and self.user_wins < 3:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()
            winner = self.get_winner(computer_choice, user_choice)

            if winner == "computer":
                self.computer_wins += 1
            elif winner == "user":
                self.user_wins += 1

            print(f"Computer Wins: {self.computer_wins}")
            print(f"User Wins: {self.user_wins}\n")

        if self.computer_wins > self.user_wins:
            print("Computer wins the game!")
        else:
            print("Congratulations! You win the game!")


# Create an instance of the game
game = RockPaperScissorsGame()

# Load the model and labels
game.load_model("keras_Model.h5", "labels.txt")

# Start playing the game
game.play()

