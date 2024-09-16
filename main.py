from Connect4 import *
from TicTacToe import *
from algorithms import *

def visualize(state):
    for row in state:
        for cell in row:
            print(cell, end='\t')
        print()
    print('--------------------')


while(True):
    print("Enter the game that you want to play (1 for Connect4 and 2 for Tic Tac Toe otherwise exit)")
    game_type = input()
    if game_type =='1' :
        game = Connect4()
    elif game_type =='2':
        game = TicTacToe()
    else:
        break
    
    print("Enter the Agent type that you want (1 for MiniMax otherwise AlphaBeta)")
    Agent_type = input()
    
    print("Enter the max depth that you want (please entre an integar number pleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeese)")
    d = int(input())
    
    state = game.init_state
    while(not game.terminal_test(state)):
        print("Agent Move")
        
        if Agent_type == '1' :
            action = H_minimax(game, state,d)
        else:
            action = H_alpha_beta(game, state,d)
            
        state = game.result(state, action)
        
        visualize(state)
        
        if(game._won(state,game.PLAYERS[0])):
            print("Agent wins")
            break
        
        
        print("Computer Move")
        action = game.random_action(state)
        
        state = game.result(state, action)
        
        visualize(state)
        
        if(game._won(state,game.PLAYERS[1])):
            print("Computer wins")
            break