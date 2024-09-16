import random
from collections import Counter
from itertools import chain
from Game import *

class TicTacToe(Game):
    '''Tic-tac-toe game formulation.'''
    
    PLAYERS = ('X', 'O')
    
    def _won(self, state, player):
        '''Auxiliary function for checking if a player has won.'''
        return any(all(state[i][j] is player for i in range(3)) for j in range(3)) \
            or any(all(state[j][i] is player for i in range(3)) for j in range(3)) \
            or all(state[i][i]   is player for i in range(3))                      \
            or all(state[i][2-i] is player for i in range(3))
    
    def __init__(self):
        self.init_state = ((None,) * 3,) * 3
    
    def player(self, state):
        counter = Counter(chain(*state))
        return TicTacToe.PLAYERS[0] if counter[TicTacToe.PLAYERS[0]] == counter[TicTacToe.PLAYERS[1]] else TicTacToe.PLAYERS[1]
    
    def random_action(self, state):
        return random.choice(list(self.actions(state)))
    
    def actions(self, state):
        return ((i, j) for i, row in enumerate(state) for j, player in enumerate(row) if not player)
    
    def result(self, state, action):
        mutable_grid = list(state)
        mutable_row = list(mutable_grid[action[0]])
        mutable_row[action[1]] = self.player(state)
        mutable_grid[action[0]] = tuple(mutable_row)
        return tuple(mutable_grid)
    
    def terminal_test(self, state):
        return all(state[i][j] is not None for i in range(3) for j in range(3)) or any(self._won(state, player) for player in TicTacToe.PLAYERS)
    
    def utility(self, state, player):
        for p in TicTacToe.PLAYERS:
            if self._won(state, p):
                return 1 if p is player else -1
        return 0
    
    def heuristic(self, state, player):
        x1,x2,o1,o2 = 0,0,0,0
        # count Xs and Os in the rows
        for row in state:
            xCount = row.count('X')
            oCount = row.count('O')
            if  (xCount==1 and oCount==0): x1+=1
            elif(xCount==2 and oCount==0): x2+=1
            if  (oCount==1 and xCount==0): o1+=1
            elif(oCount==2 and xCount==0): o2+=1
        
        # count Xs and Os in the columns
        for j in range(3):
            try:
                xCount = sum([1 for i in range(3) if state[i][j] == 'X'])
                oCount = sum([1 for i in range(3) if state[i][j] == 'O'])
            except:
                print(state)
            if  (xCount==1 and oCount==0): x1+=1
            elif(xCount==2 and oCount==0): x2+=1
            if  (oCount==1 and xCount==0): o1+=1
            elif(oCount==2 and xCount==0): o2+=1
        # count the Xs and Os in the diagonals
        Diagonals = [''.join(filter(None, (state[0][0],state[1][1],state[2][2]))),''.join(filter(None, (state[0][2],state[1][1],state[2][0])))]
        
        for d in Diagonals:
            xCount = d.count('X')
            oCount = d.count('O')
            if  (xCount==1 and oCount==0): x1+=1
            elif(xCount==2 and oCount==0): x2+=1
            if  (oCount==1 and xCount==0): o1+=1
            elif(oCount==2 and xCount==0): o2+=1
        return (3*x2 + x1 - (3*o2 + o1))