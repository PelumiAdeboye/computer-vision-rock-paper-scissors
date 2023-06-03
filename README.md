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

## Game Implementation
The Rock-Paper-Scissors game consists of the following components:

`get_computer_choice`: This function randomly selects an option between "Rock", "Paper", and "Scissors" using the random.choice function. It returns the chosen option.

`get_user_choice`: This function prompts the user to input their choice and validates the input. It keeps asking until a valid choice of "Rock", "Paper", or "Scissors" is entered. The input is capitalized using the capitalize method to match the format of the options.

`get_winner`: This function takes the computer's choice and the user's choice as arguments and determines the winner based on the classic rules of Rock-Paper-Scissors. It compares the choices using if-elif-else statements and prints the outcome of the game.

`play`: This function calls the other functions (`get_computer_choice`, `get_user_choice`, and `get_winner`) to play a game of Rock-Paper-Scissors. It obtains the computer's choice, prompts the user for their choice, and determines the winner based on the choices made.

To play the game, run the script by executing the following command:

```python
python manual_rps.py
