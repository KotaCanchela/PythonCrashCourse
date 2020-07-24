from random import choice

# To make random decisions, we’ll store possible moves in a list and use the choice() function,
# from the random module, to decide which move to make each time a step is taken ➊. We then set
# the default number of points in a walk to 5000, which is large enough to generate some interesting
# patterns but small enough to generate walks quickly ➋. Then at ➌ we make two lists to hold the
# x- and y-values, and we start each walk at the point (0, 0).”
class RandomWalk:
    """A class to randomize walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
            