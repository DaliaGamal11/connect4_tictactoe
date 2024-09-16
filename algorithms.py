from math import inf

def minimax(game, state):
    '''Minimax implementation.'''
    player = game.player(state)
    
    def max_value(state):
        if game.terminal_test(state): return game.utility(state, player)
        maxi = -inf
        for action in game.actions(state):
            maxi = max(maxi, min_value(game.result(state, action)))
        return maxi
    
    def min_value(state):
        if game.terminal_test(state): return game.utility(state, player)
        mini = +inf
        for action in game.actions(state):
            mini = min(mini, max_value(game.result(state, action)))
        return mini
    
    best_action, best_value = None, None
    for action in game.actions(state):
        print(action)
        action_value = min_value(game.result(state, action))
        if best_value is None or best_value < action_value:
            best_action = action
            best_value = action_value
    return best_action


def alpha_beta(game, state):
    '''Alpha-Beta Pruning implementation.'''
    player = game.player(state)
    
    def max_value(state, alpha, beta):
        if game.terminal_test(state): return game.utility(state, player)
        maxi = -inf
        for action in game.actions(state):
            maxi = max(maxi, min_value(game.result(state, action), alpha, beta))
            alpha = max(alpha, maxi)
            if alpha >= beta: return maxi
        return maxi
    
    def min_value(state, alpha, beta):
        if game.terminal_test(state): return game.utility(state, player)
        mini = +inf
        for action in game.actions(state):
            mini = min(mini, max_value(game.result(state, action), alpha, beta))
            beta = min(beta, mini)
            if alpha >= beta: return mini
        return mini
    
    best_action, best_value = None, None
    for action in game.actions(state):
        action_value = min_value(game.result(state, action), -inf, +inf)
        if best_value is None or best_value < action_value:
            best_action = action
            best_value = action_value
    return best_action

def H_minimax(game, state, maxd):
    '''Minimax implementation.'''
    player = game.player(state)
    
    def max_value(state, d):
        if d == maxd: return game.heuristic(state, player)
        if game.terminal_test(state): return game.utility(state, player)
        maxi = -inf
        for action in game.actions(state):
            maxi = max(maxi, min_value(game.result(state, action),d+1))
        return maxi
    
    def min_value(state, d):
        if d == maxd: return game.heuristic(state, player)
        if game.terminal_test(state): return game.utility(state, player)
        mini = +inf
        for action in game.actions(state):
            mini = min(mini, max_value(game.result(state, action),d+1))
        return mini
    
    best_action, best_value = None, None
    for action in game.actions(state):
        action_value = min_value(game.result(state, action), 1)
        if best_value is None or best_value < action_value:
            best_action = action
            best_value = action_value
    return best_action

def H_alpha_beta(game, state,maxd):
    '''Alpha-Beta Pruning implementation.'''
    player = game.player(state)
    
    def max_value(state,d, alpha, beta):
        if d == maxd: return game.heuristic(state, player)
        if game.terminal_test(state): return game.utility(state, player)
        maxi = -inf
        for action in game.actions(state):
            maxi = max(maxi, min_value(game.result(state, action),d+1, alpha, beta))
            alpha = max(alpha, maxi)
            if alpha >= beta: return maxi
        return maxi
    
    def min_value(state,d, alpha, beta):
        if d == maxd: return game.heuristic(state, player)
        if game.terminal_test(state): return game.utility(state, player)
        mini = +inf
        for action in game.actions(state):
            mini = min(mini, max_value(game.result(state, action),d+1, alpha, beta))
            beta = min(beta, mini)
            if alpha >= beta: return mini
        return mini
    
    best_action, best_value = None, None
    for action in game.actions(state):
        action_value = min_value(game.result(state, action),1, -inf, +inf)
        if best_value is None or best_value < action_value:
            best_action = action
            best_value = action_value
    return best_action