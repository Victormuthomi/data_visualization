from random import choice

class RandowWalks:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        """Initializes the attributes of the walk"""
        self.num_points = num_points

        #All walks starts at 0
        self.x_valus = [0]
        self.y_values = [0] 
        
