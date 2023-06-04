# Computer Vision RPS
This project utilizes an image classification model trained using Teachable Machine. The model is designed to classify images into different classes of Rock, Paper, Scissors and Nothing. The model is saved in the TensorFlow format with the filename `keras_model.h5`, and the corresponding labels are stored in the `labels.txt` file.

## Environment Setup
To set up the environment for running the Rock-Paper-Scissors game, follow these steps:

Ensure you have Python installed on your machine. You can download the latest version of Python from the official website: `python.org`.

Clone the GitHub repository containing the project using the following command:

```python
git clone https://github.com/PelumiAdeboye/computer-vision-rock-paper-scissors
```

Create a virtual environment to isolate project dependencies. This step is recommended to keep the project dependencies separate from your global Python environment

Install the project dependencies by running the following command:

```python
pip install -r requirements.txt
```

This will install the required packages, including random, necessary for running the game.

Place your trained TensorFlow model file (`keras_model.h5`) and the corresponding label file (`labels.txt`) in the project directory.

## Game Implementation
The Rock-Paper-Scissors game consists of the following components:

`get_computer_choice`: This function randomly selects an option between "Rock", "Paper", and "Scissors" using the random.choice function. It returns the chosen option.

`get_user_choice`: This function prompts the user to input their choice and validates the input. It keeps asking until a valid choice of "Rock", "Paper", or "Scissors" is entered. The input is capitalized using the capitalize method to match the format of the options.

`get_winner`: This function takes the computer's choice and the user's choice as arguments and determines the winner based on the classic rules of Rock-Paper-Scissors. It compares the choices using if-elif-else statements and prints the outcome of the game.

`play`: This function calls the other functions (`get_computer_choice`, `get_user_choice`, and `get_winner`) to play a game of Rock-Paper-Scissors. It obtains the computer's choice, prompts the user for their choice, and determines the winner based on the choices made.

## Usage
To start the game, run the `camera_rps.py` file. The game will display the webcam feed, and the user should show their hand gesture to the camera within the specified countdown period. The computer will randomly choose its hand gesture, and the winner will be determined based on the classic Rock Paper Scissors rules. The game will continue until either the computer or the user wins three rounds.

## Integration with the Model
The game integrates a pre-trained TensorFlow model (`keras_model.h5`) to recognize the user's hand gesture from the camera input. The model is loaded using the `load_model()` function from the Keras library. The webcam feed is continuously captured, and each frame is resized to match the input shape of the model. The resized frame is then fed into the model to obtain the prediction. The class with the highest probability is considered as the user's hand gesture. The prediction and confidence score are displayed in the terminal.

### Possible Improvements
There are several ways to further improve the functionality of the game:

Implement a more advanced hand gesture recognition model to enhance accuracy and support additional gestures.

Add graphical user interface (GUI) elements to provide a more interactive and visually appealing game experience.

Include audio effects or background music to enhance the gaming atmosphere.

Implement a game mode where the user can play against another human player locally or online.

Provide an option to customize the countdown duration or allow the user to trigger the gesture recognition manually.



## Conclusion
The Rock Paper Scissors game with computer vision integration provides an engaging and interactive gaming experience. By leveraging the power of computer vision and machine learning, the game enables the user to compete against the computer by showing hand gestures to the camera. With further enhancements and customizations, the game can be extended to create more immersive and enjoyable gameplay.
