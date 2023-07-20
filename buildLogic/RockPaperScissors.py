import random


def get_computer_choice():
    random_number = random.randint(1, 3)
    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    computer_choice = options[random_number]
    return computer_choice


def get_input_user():
    user_input = input("Enter rock/paper/scissors: ")
    user_input = user_input.lower()
    return user_input


def get_result(user_pick, computer_pick):
    # condition for draw
    if user_pick == computer_pick:
        print('draw')
    elif user_pick == 'paper' and computer_pick == 'rock':
        print('win')
    elif user_pick == 'rock' and computer_pick == 'scissors':
        print('win')
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('win')
    else:
        print('lose')

while True:
    user_picks = get_input_user()
    if user_picks in ['rock','paper','scissors']:
        break

get_result(user_picks, get_computer_choice())