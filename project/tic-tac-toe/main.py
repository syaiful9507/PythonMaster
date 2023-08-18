class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, type):
        # if a player selects position n, n-1 index should be updated
        # if the position is not already filled, update the board
        if self.board[position - 1] == ' ':
            self.board[position - 1] = type
            return True
        else:
            print('Position already selected, Select another position.')
            return False

    def check_winner(self, type):
        if (self.board[0] == type and self.board[1] == type and self.board[2] == type or
                self.board[3] == type and self.board[4] == type and self.board[5] == type or
                self.board[6] == type and self.board[7] == type and self.board[8] == type or
                self.board[0] == type and self.board[3] == type and self.board[6] == type or
                self.board[1] == type and self.board[4] == type and self.board[7] == type or
                self.board[2] == type and self.board[5] == type and self.board[8] == type or
                self.board[0] == type and self.board[4] == type and self.board[8] == type or
                self.board[2] == type and self.board[4] == type and self.board[6] == type):
            return True
        else:
            return False

    # if all field are selected and there is no winner, it's draw
    # returning True id it's draw
    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False


# board = Board()
# board.print_board()


class Player:
    def __init__(self, type):
        self.type = type
        self.name = self.get_name()

    def get_name(self):
        if self.type == 'X':
            name = input('Player selecting X, enter your name : ')
        else:
            name = input('Player selecting 0, enter your name : ')
        return name


# player1 = Player('X')
# player2 = Player('O')
# print(player1.name, player1.type)
# print(player2.name, player2.type)
class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1

    def play(self):
        # using an infinite loop to run the game
        # we will later add conditions to terminate the loop
        while True:
            try:
                message = f'{self.current_player.name}, enter the position (1-9) : '
                position = int(input(message))
                # the update_board() method return True if
                # the user selected position is not already filled
                if self.board.update_board(position, self.current_player.type):
                    self.board.print_board()

                    # checking winner each time after updating the board
                    if self.board.check_winner(self.current_player.type):
                        print(self.current_player.name, 'wins!')
                        break
                    # checking draw each time after updating the board
                    elif self.board.check_draw():
                        print('Game is Draw!')
                        break
                    # change current player when board is updated
                    if self.current_player == self.player1:
                        self.current_player = self.player2
                    else:
                        self.current_player = self.player1
            except:
                print('Invalid input! Enter a number between 1 and 9')

game = Game()
game.play()
