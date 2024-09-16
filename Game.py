class Game:
    '''
    Abstract game class for game formulation.
    It declares the expected methods to be used by an adversarial search algorithm.
    All the methods declared are just placeholders that throw errors if not overriden by child "concrete" classes!
    '''
    
    def __init__(self):
        '''Constructor that initializes the game. Typically used to setup the initial state, number of players and, if applicable, the terminal states and their utilities.'''
        self.init_state = None
    
    def player(self, state):
        '''Returns the player whose turn it is.'''
        raise NotImplementedError
    
    def actions(self, state):
        '''Returns an iterable with the applicable actions to the given state.'''
        raise NotImplementedError
    
    def result(self, state, action):
        '''Returns the resulting state from applying the given action to the given state.'''
        raise NotImplementedError
    
    def terminal_test(self, state):
        '''Returns whether or not the given state is a terminal state.'''
        raise NotImplementedError
    
    def utility(self, state, player):
        '''Returns the utility of the given state for the given player, if possible (usually, it has to be a terminal state).'''
        raise NotImplementedError

    def heuristic(self, state, player):
        '''Returns the heuristic of the given state for the given player.'''
        raise NotImplementedError