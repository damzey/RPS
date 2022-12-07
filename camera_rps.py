import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('Teachable_Machine/keras_model.h5', compile = False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

options = ["Rock", "Paper", "Scissors"]


    
def get_prediction():
    prediction = model.predict(data)
    arr = np.array(prediction)
    global predicted
    predicted = (arr.argmax())

def get_computer_choice():
    return predicted

def get_user_choice():
    while True:
        print("user option:")
        global user_play
        user_play = input("Enter a choice; Rock, Paper or Scissors: ")
        if user_play not in options:
            print(f"Please use a letter in {options}")  
        else:
            return user_play

def get_winner(computer_option, user_option):
    print(computer_option)
    print(user_option)
    print(f" You chose {user_option}, whereas the computer chose {computer_option} ")
    if user_option == computer_option:
        print(f"Both players selected {computer_option}. It's a draw")
    elif user_option == "Rock":
        if computer_option == "scissors":
            print("Rock beats Scissors. You win")
        else:
            print("Paper covers Rock. You lose")
    elif user_option == "Paper":
        if computer_option == "Rock":
            print("Paper covers Rock. You win")
        else:
            print("Scissors cuts Paper. You lose")
    elif user_option == "Scissors":
        if computer_option == "Rock":
            print("Rock beats scissors. You lose")
        else:
            print("Scissors cuts paper. You win")


def play():
    get_prediction()
    computer_option = get_computer_choice()
    user_option = get_user_choice()
    get_winner(computer_option, user_option)

    

