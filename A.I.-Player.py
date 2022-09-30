#Author:Yoshiki Hoshinaga
#Date: June 22
#
# An RandomPlayer for use in Connect Four


import random
from A.I-part3.py import * # to use the connect_four and process_move functions

class RandomPlayer(Player):

    def next_move(self, board):
        """ overrides the next_move method that is inherited from Player. 
        Rather than asking the user for the next move, this version of next_move 
        should choose at random from the columns in the specified board that are not yet full,
        and return the index of that randomly selected column. You may assume that this method 
        will only be called in cases in which there is at least one available column.
        """
        self.num_moves += 1
        while True:
            vals = random.randint(0, 6)
            if board.can_add_to(vals):
                return vals
        # make a list of colums that allowed to and use random.choice to pick solution



if __name__=='__main__':
    p = RandomPlayer('X')
    print(p)
    print(p.opponent_checker())
    b = Board(2, 4)
    b.add_checkers('001223')
    print(b)
    print(p.next_move(b))
    print(p.next_move(b))
    print(p.next_move(b))
    b.add_checker('O', 1)
    print(b)
    print(p.next_move(b))
    print(p.next_move(b))
    b.add_checker('X', 3)
    b.remove_checker(2)
    print(b)
    print(p.next_move(b))
    print(p.next_move(b))

