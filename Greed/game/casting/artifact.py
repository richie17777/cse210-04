from game.casting.actor import Actor

class Artifact(Actor):
    '''A collection of gems and stones falling from the top of screen.
    The responsibility of gems is to add, and remove them.  '''
    
    def __init__(self):
        '''Constructs a new gem or stone.'''
        super().__init__()
        self._is_alive = True
        self._score = 0
            