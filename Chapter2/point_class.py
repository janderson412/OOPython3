import math

class Point:
  """ Point class for use in chapter 2 examples. """

  def __init__(self, x=0, y=0):
    """ Initialize the position of the point to X,Y.
      Default posiiton is x=0, y=0."""
    self.move(x, y)

  def move(self, x, y):
    """ Move to X, Y. """
    self.x = x
    self.y = y

  def reset(self):
    """ Reset position to x=0, y=0."""
    self.x = 0
    self.y = 0

  def calculate_distance(self, other):
    """ Calculate distance between this point and another. """
    return math.sqrt(
      (self.x - other.x) ** 2 +
      (self.y - other.y) ** 2)

