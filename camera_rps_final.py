import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RPS:

    def __init__(self):
        self.model = load_model('Teachable_Machine/keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.options = ["Rock", "Paper", "Scissors", "Nothing"]
        self.prediction = self.model.predict(self.data)
        self.computer_wins = 0
        self.user_wins = 0

    def get_user_choice(self):
        stop_time = time.time() + 2
        while stop_time > time.time(): 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            user_play = np.argmax(prediction[0])
            user_choice = self.options[user_play]
            return user_choice
        
    def get_computer_choice(self):
        return random.choice(self.options[0:3])

    @staticmethod
    def countdown(t):
    
        while t:
            mins, secs = divmod(t, 60)
            timer = (f"{mins}, {secs}")
            print(secs, end="\r")
            cv2.waitKey(800)
            t -= 1

    def get_winner(self, computer_choice, user_choice):
        print(f"You chose {user_choice} whereas the computer chose {computer_choice}")
        if user_choice == computer_choice:
                print(f"Both players selected {computer_choice}. It's a draw")
        elif user_choice == "Rock":
                if computer_choice == "Scissors":
                    print("Rock beats Scissors. You win")
                    self.user_wins += 1
                else:
                    print("Paper covers Rock. You lose")
                    self.computer_wins += 1
        elif user_choice == "Paper":
                if computer_choice == "Rock":
                    print("Paper covers Rock. You win")
                    self.user_wins += 1
                else:
                    print("Scissors cuts Paper. You lose")
                    self.computer_wins += 1
        elif user_choice == "Scissors":
                if computer_choice == "Rock":
                    print("Rock beats scissors. You lose")
                    self.computer_wins += 1
                else:
                    print("Scissors cuts paper. You win")
                    self.user_wins += 1

def play_game():
    game = RPS()
    while game.user_wins < 3 or game.computer_wins < 3:
        game.countdown(4)
        user_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()
        game.get_winner(computer_choice, user_choice)
        if game.computer_wins == 3:
            print(f"You lost. The computer has {game.computer_wins} ")
            break
        elif game.user_wins == 3:
            print(f"You won. The user has {game.user_wins}")
            break
    game.cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__== "__main__":
    play_game()    

