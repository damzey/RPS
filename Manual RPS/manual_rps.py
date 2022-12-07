import random
import time

class RPS:

    def __init__(self):   
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_wins  = 0
        self.computer_wins = 0

    def get_user_choice(self):
        while True:
            print("user option:")
            user_play = input("Enter a choice; Rock, Paper or Scissors: ")
            if user_play not in self.options:
                print(f"Please use a letter in {self.options}")  
            else:
                return user_play
        
    def get_computer_choice(self):
        return random.choice(self.options)

    def create_a_delay(self):
        self.delay = time.sleep(1)

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
    
    def keeping_track_of_scores(self):
        print(f"User score is: {self.user_wins} and Computer score is: {self.computer_wins}")

def play_game():
    game = RPS()
    while game.user_wins < 3 or game.computer_wins < 3:
        user_choice = game.get_user_choice()
        computer_choice = game.get_computer_choice()
        game.get_winner(computer_choice, user_choice)
        game.keeping_track_of_scores()
        print() 
        game.create_a_delay()
        if game.computer_wins == 3:
            print(f"You lost. The computer has {game.computer_wins} wons ")
            break
        elif game.user_wins == 3:
            print(f"You won. The user has {game.user_wins} wins")
            break

if __name__== "__main__":
    play_game()    
