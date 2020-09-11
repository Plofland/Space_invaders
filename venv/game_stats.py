
class GameStats():
    '''Track stats for Python Invaders.'''
    def __init__(self, pi_settings):
        '''Initialize stats.'''
        self.pi_settings = pi_settings
        self.reset_stats()

        # Start Invaders from Python in an active state.
        self.game_active = False

        # High score should never be reset
        self.high_score = 0


    def reset_stats(self):
        '''Initialize stats that can change during the game.'''
        self.ships_left = self.pi_settings.ship_limit
        self.score = 0
        self.level = 1