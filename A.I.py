#Author : Yoshiki Hoshinaga
#Date : June 20

class Board:

    def __init__(self,height,width):
        """constructs a new Board object by initializing
            the following three attributes:
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object.
        """
        s = ''          # begin with an empty string 
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        s += (2*self.width +1) * '-'
        s += '\n'
        s += ' '
        for col in range(self.width):
            val= col % 10
            s += str(val)
            s += ' '
        return s
    def add_checker(self, checker, col):
        """-checker, a one-character string that specifies the checker to add to the board
            -col, an integer that specifies the index of the column to which the checker 
            should be added and that adds checker to the appropriate row in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        # put the rest of the method here
        row = 0
        while self.slots[row][col] == ' ':
            row += 1
            if row == self.height-1:
                break
        if self.slots[row][col] != ' ':
            row += -1
          
        self.slots[row][col] = checker
    
    def reset(self):
        """should reset the Board object on which 
            it is called by setting all slots to contain a space character
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
    def can_add_to(self,col):
        """returns True if it is valid to place a checker in the column
            col on the calling Board object. Otherwise, it should return False.
        """
        if col < 0:
            return False
        elif col > self.width-1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
    
    def is_full(self):
        """returns True if the called Board object is 
            completely full of checkers, and returns False otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col):
                return False    
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object.
             If the column is empty, then the method should do nothing.
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):

              
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
          
    def is_vertical_win(self, checker):
        ''' Checks for a vertical win for the specified checker.
        '''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
  
    def is_up_diagonal_win(self, checker):
        ''' Checks for a diagonal-up win for the specified checker
        '''
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        ''' Checks for a diagonal-down win for the specified checker
        '''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ccepts a parameter checker that is either 'X' or 'O', and returns 
            True if there are four consecutive slots containing 
            checker on the board. Otherwise, it should return False.
        """
        if self.is_down_diagonal_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_horizontal_win(checker) == True:
            return True
        return False


if __name__=='__main__':
#test
    s = 'I am the top line.'
    s += '\n'
    s += 'I am the second line!\n'
    print(s)
    b = Board(6, 7)
    print(b)
    print('')
    print('add_checker')
    b1 = Board(6, 7)
    b1.add_checker('X', 0)
    b1.add_checker('O', 0)
    b1.add_checker('X', 0)
    b1.add_checker('O', 3)
    b1.add_checker('O', 4)    # cheat and let O go again!
    b1.add_checker('O', 5)
    b1.add_checker('O', 6)
    print(b1)
    print('')
    print('add_checkers')
    b2 = Board(3, 3)
    b2.add_checkers('0200')
    print(b2)
    print('')
    print('can_add_to')
    b1 = Board(2, 2)
    print(b1)
    b1.add_checker('X', 0)
    b1.add_checker('O', 0)
    print(b1)
    print(b1.can_add_to(-1))
    print(b1.can_add_to(0))
    print(b1.can_add_to(1))
    print(b1.can_add_to(2))
    print('')
    print('is_full')
    b2 = Board(2, 2)
    print(b2.is_full())
    b2.add_checkers('0011')
    print(b2)
    print(b2.is_full())
    print('')
    print('remove_checker')
    b3 = Board(2, 2)
    b3.add_checkers('0011')
    b3.remove_checker(1)
    b3.remove_checker(1)
    b3.remove_checker(1)     # column empty; should have no effect
    b3.remove_checker(0)
    print(b3)
    print('')
    print('is_win_for')
    b = Board(6, 7)
    b.add_checkers('00102030')
    print(b)
    print(b.is_win_for('X'))
    print(b.is_win_for('O'))
    print('')
    b2 = Board(6, 7)
    b2.add_checkers('23344545515')
    print(b2)
    print(b2.is_win_for('X'))   # up diagonal win
    print(b2.is_win_for('O'))
