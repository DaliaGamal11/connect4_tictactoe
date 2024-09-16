import random
from collections import Counter
from itertools import chain
from Game import *

class Connect4(Game):
    '''Connect4 game formulation.'''
    
    PLAYERS = ('A', 'C')
    
    def _won(self, state, player):
        '''Auxiliary function for checking if a player has won.'''
        return any(any(all([state[i][j+k] is player for k in range(4)])for i in range(6)) for j in range(4)) \
            or any(any(all([state[i+k][j] is player for k in range(4)])for i in range(3)) for j in range(7)) \
            or any(any(all([state[i+k][j+k] is player for k in range(4)])for i in range(3)) for j in range(4)) \
            or any(any(all([state[i+k][6-(j+k)] is player for k in range(4)])for i in range(3)) for j in range(4))
            
    def __init__(self):
        self.init_state = ((None,) * 7,) * 6
    
    def player(self, state):
        counter = Counter(chain(*state))
        return Connect4.PLAYERS[0] if counter[Connect4.PLAYERS[0]] == counter[Connect4.PLAYERS[1]] else Connect4.PLAYERS[1]
    
    def random_action(self, state):
        return random.choice(list(self.actions(state)))
    
    def actions(self, state):
        return ((j,i) for i in range(7) if state[0][i] is None for j in [[k for k in range(6) if state[k][i] is None][-1]])
    
    def result(self, state, action):
        mutable_grid = list(state)
        mutable_row = list(mutable_grid[action[0]])
        mutable_row[action[1]] = self.player(state)
        mutable_grid[action[0]] = tuple(mutable_row)
        return tuple(mutable_grid)
    
    def terminal_test(self, state):
        return all(state[i][j] is not None for i in range(6) for j in range(7)) or any(self._won(state, player) for player in Connect4.PLAYERS)
    
    def utility(self, state, player):
        for p in Connect4.PLAYERS:
            if self._won(state, p):
                return 1 if p is player else -1
        return 0
    
    def heuristic(self, state, player):
        r1,r2,r3,b1,b2,b3 = 0,0,0,0,0,0
        # count Rs and Bs in the rows
        for row in state:
            rCount = row.count('R')
            bCount = row.count('B')
            if  (rCount==1 and bCount==0): r1+=1
            elif(rCount==2 and bCount==0): r2+=1
            elif(rCount==3 and bCount==0): r3+=1
            if  (bCount==1 and rCount==0): b1+=1
            elif(bCount==2 and rCount==0): b2+=1
            elif(bCount==3 and rCount==0): b3+=1
        
        # count Rs and Bs in the columns
        for j in range(7):
            try:
                rCount = sum([1 for i in range(6) if state[i][j] == 'X'])
                bCount = sum([1 for i in range(6) if state[i][j] == 'O'])
            except:
                print(state)
            if  (rCount==1 and bCount==0): r1+=1
            elif(rCount==2 and bCount==0): r2+=1
            elif(rCount==3 and bCount==0): r3+=1
            if  (bCount==1 and rCount==0): b1+=1
            elif(bCount==2 and rCount==0): b2+=1
            elif(bCount==3 and rCount==0): b3+=1
        # count the Xs and Os in the diagonals
        Diagonals = [''.join(filter(None,[state[i+k][j+k] for k in range(4)])) for i in range(3) for j in range(4)] \
        +[''.join(filter(None,[state[i+k][6-(j+k)] for k in range(4)])) for i in range(3) for j in range(4)]
        for d in Diagonals:
            rCount = d.count('X')
            bCount = d.count('O')
            if  (rCount==1 and bCount==0): r1+=1
            elif(rCount==2 and bCount==0): r2+=1
            elif(rCount==3 and bCount==0): r3+=1
            if  (bCount==1 and rCount==0): b1+=1
            elif(bCount==2 and rCount==0): b2+=1
            elif(bCount==3 and rCount==0): b3+=1
        return (3*r3 + 2*r2 + r1 - (3*b3 + 2*b2 + b1))