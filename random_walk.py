from random import choice

class RandowWalks:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        """Initializes the attributes of the walk"""
        self.num_points = num_points

        #All walks starts at 0
        self.x_values = [0]
        self.y_values = [0] 
       
    def fill_walk(self):
        """Calculate all the points of the walk"""
        
        while self.x_values < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * X_distance 

            y_direction = choice([1, -1])
            y_distance= ([1, 2, 3, 4])
            y_step = y_direction * y_distance 

            #Reject moves that go nowhere
            if x_step == o and y_step == 0:
                continue

           #Calculate the final moves
           x = self.x_values[-1] + x_step
           y = self.y_values[-1] + y_step 


        

