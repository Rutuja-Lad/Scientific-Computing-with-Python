import random

# Hat class
class Hat:
    def __init__(self, **ball_colors):
        self.contents = []
        for color, count in ball_colors.items():
            # For each color, add the appropriate number of balls to the contents list
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        # If there are fewer balls to draw than in the hat, draw all remaining balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []  # Empty the hat after drawing all balls
            return drawn_balls
        # Otherwise, draw `num_balls` randomly from the hat
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

# Experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Create a copy of the hat to simulate a new experiment each time
        hat_copy = Hat(**{color: hat.contents.count(color) for color in hat.contents})
        
        # Draw the balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the occurrences of each ball color in the drawn balls
        drawn_balls_count = {color: drawn_balls.count(color) for color in drawn_balls}
        
        # Check if the drawn balls meet or exceed the expected ball counts
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < expected_count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    # Return the estimated probability
    return successful_experiments / num_experiments

# Example usage:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={'red': 1, 'green': 2},
                         num_balls_drawn=4,
                         num_experiments=2000)
print(f"Estimated Probability: {probability:.3f}")
