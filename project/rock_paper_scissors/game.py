import random
class Game:
    def __init__(self):
        # call the get_computer_pick() method
        self.computer_pick = self.get_computer_pick()
        self.user_pick = self.get_user_pick()
        self.result = self.get_result()
    def get_computer_pick(self):
        # get random number among 1,2, dan 3
        random_number = random.randint(1,3)

        # possible options
        options = {1: 'rock', 2:'paper', 3:'scissors'}
        return options[random_number]

    def get_user_pick(self):
        # infinite while loop for valid  user pick
        while True:
            # get input user
            user_pick = input('Enter rock/paper/scissors : ')
            # converting the user's pick to lowercase
            user_pick = user_pick.lower()
            # if user_pick is either rock or paper or scissors
            # terminate the loop
            if user_pick in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Wrong input!')

        return user_pick

    def get_result(self):
        # condition for draw
        if self.computer_pick == self.user_pick:
            return 'draw'
        # condition for the user to win
        elif self.user_pick == 'paper' and self.computer_pick == 'rock':
            return 'win'
        elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
            return 'win'
        elif self.user_pick == 'scissors' and self.computer_pick == 'paper':
            return 'win'
        # in all other condition, users lose
        else:
            return 'lose'

    def print_result(self):
        print(f"Computer's pick : {self.computer_pick}")
        print(f"Your pick : {self.user_pick}")
        print(f"You : {self.result}")

while True:
    game = Game()
    game.print_result()

    play_again = input('Do you want to play again ? (y/n) : ')
    if play_again.lower() == 'n':
        break