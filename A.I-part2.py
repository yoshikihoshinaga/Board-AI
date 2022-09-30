
#Author: Yoshiki Hoshinaga
#Date: June 20
#Title: ps13pr2

from ps13pr1 import Board

class Player:
    
    def __init__(self, checker):
        """constructs a new Player object by initializing the following two attributes"""
        if checker in "XO":
            self.checker = checker
            self.num_moves = 0
        else:
            print('Your checker must be either "X" or "O" (case sensitive).')
              
    def __repr__(self):
        """returns a string representing a Player object. 
            The string returned should indicate which checker the Player object is using
        """
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
    
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns
             the column where the player wants to make the next move
        """  
        while True:
            vals = int(input('Enter a column: '))
            if 0<=vals and vals<b.width and b.can_add_to(vals):
                self.num_moves +=1
                return vals
            else:
                print('Try again!')

if __name__=='__main__':
#test
    p1 = Player('X')
    print(p1)
    p2 = Player('O')
    print(p2)
    print('')
    p = Player('X')
    print(p.opponent_checker())
    print('')
    p = Player('X')
    b1 = Board(6, 7)    # valid column numbers are 0 - 6
    print(p.next_move(b1))
