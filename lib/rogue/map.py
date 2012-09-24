class Map(object):
    ''' The Map keeps track of what we have on our game map. This includes things like where our 
        treasure is, where monsters are, and where the player is.
    '''
    def __init__(self):
        ''' Sets all squares to uncleared.
        '''
        self.player = [0,0]

    def set_current_position(self, position):
        self.player = position
