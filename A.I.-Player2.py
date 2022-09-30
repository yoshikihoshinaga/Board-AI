
import random
from A.I-part3 import * # to use the connect_four and process_move functions

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object."""
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board,
            and that returns the index of the column with the maximum score. 
            If one or more columns are tied for the maximum score, the method 
            should apply the called AIPlayer‘s tiebreaking strategy to break the tie.
            Make sure that you return the index of the appropriate column, and not the column’s score.
        """
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)

    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for the columns in board."""
        scores = [10] * len(range(board.width))

        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                other_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                other_scores = other_player.scores_for(board)
                if max(other_scores) == 0:
                    scores[col] = 100
                elif max(other_scores) == 100:
                    scores[col] = 0
                elif max(other_scores) == 50:
                    scores[col] = 50
                    
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """the next_move method that is inherited from Player. 
            Rather than asking the user for the next move, 
            this version of next_move should return the called AIPlayer‘s 
            judgment of its best possible move. This method won’t need to do much work, 
            because it should use your scores_for and max_score_column methods to determine 
            the column number that should be returned.
        """
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)
    
if __name__=='__main__':
    p1 = AIPlayer('X', 'LEFT', 1)
    print(p1)
    p2 = AIPlayer('O', 'RANDOM', 2)
    print(p2)
    print()
    scores = [0, 0, 50, 0, 50, 50, 0]
    p1 = AIPlayer('X', 'LEFT', 1)
    print(p1.max_score_column(scores))
    p2 = AIPlayer('X', 'RIGHT', 1)
    print(p2.max_score_column(scores))
    print()
    b = Board(6, 7)
    b.add_checkers('1211244445')
    print(b)
    # A lookahead of 0 doesn't see threats!
    print(AIPlayer('X', 'LEFT', 0).scores_for(b))
    # A lookahead of 1 sees immediate wins.
    # (O would win if it put a checker in column 3.)
    print(AIPlayer('O', 'LEFT', 1).scores_for(b))
    # But a lookahead of 1 doesn't see possible losses!
    # (X doesn't see that O can win if column 3 is left open.)
    print(AIPlayer('X', 'LEFT', 1).scores_for(b))
    # A lookahead of 2 sees possible losses.
    # (All moves by X other than column 3 leave it open to a loss.
    # note that X's score for 3 is 50 instead of 100, because it
    # assumes that O will follow X's move to 3 with its own move to 3,
    # which will block X's possible horizontal win.)
    print(AIPlayer('X', 'LEFT', 2).scores_for(b))
    # A lookahead of 3 sees set-up wins!
    # (If X chooses column 3, O will block its horizontal win, but
    # then X can get a diagonal win by choosing column 3 again!)
    print(AIPlayer('X', 'LEFT', 3).scores_for(b))
    # With a lookahead of 3, O doesn't see the danger of not
    # choosing 3 for its next move (hence the 50s in columns
    # other than column 3).
    print(AIPlayer('O', 'LEFT', 3).scores_for(b))
    # With a lookahead of 4, O **does** see the danger of not
    # choosing 3 for its next move (hence the 0s in columns
    # other than column 3).
    print(AIPlayer('O', 'LEFT', 4).scores_for(b))
    print()
    b = Board(6, 7)
    b.add_checkers('1211244445')
    print(b)
    # With a lookahead of 1, gives all columns a score of 50, and its
    # tiebreaking strategy leads it to pick the leftmost one.
    print(AIPlayer('X', 'LEFT', 1).next_move(b))
    # Same lookahead means all columns are still tied, but a different
    # tiebreaking stategy that leads it to pick the rightmost column.
    print(AIPlayer('X', 'RIGHT', 1).next_move(b))
    # With the larger lookahead, X knows it must pick column 3!
    print(AIPlayer('X', 'LEFT', 2).next_move(b))     
    # The tiebreaking strategy doesn't matter if there's only one best move!
    print(AIPlayer('X', 'RIGHT', 2).next_move(b))      
    print(AIPlayer('X', 'RANDOM', 2).next_move(b))
    print()
    print(connect_four(AIPlayer('X', 'LEFT', 0), AIPlayer('O', 'LEFT', 0)))
    # omitting everything but the final result...
    print(connect_four(AIPlayer('X', 'LEFT', 1), AIPlayer('O', 'LEFT', 1)))
    # omitting everything but the final result...
    print(connect_four(AIPlayer('X', 'LEFT', 3), AIPlayer('O', 'LEFT', 2)))
    # omitting everything but the final result...
