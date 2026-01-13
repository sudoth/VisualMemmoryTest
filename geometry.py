import pygame
from config import SQRT3

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Vector:
  def __init__(self, point_a : Point, point_b : Point):
    self.x = point_b.x - point_a.x
    self.y = point_b.y - point_a.y

def VectorProduct(a : Vector, b : Vector):
  return a.x * b.y - a.y * b.x

class Polygon:
  def __init__(self, x, y, color, side_size = 100):
    self.x = x
    self.y = y
    self.color = color
    self.clicked = False
    self.side_size = side_size

  def PolygonPoint(self, number):
    if (number == 0):
      return Point(-self.side_size / 2 + self.x, SQRT3 * self.side_size / 2 + self.y)
    if (number == 1):
      return Point(self.side_size / 2 + self.x, SQRT3 * self.side_size / 2 + self.y)
    if (number == 2):
      return Point(self.side_size + self.x, self.y)      
    if (number == 3):
      return Point(self.side_size / 2 + self.x, -SQRT3 * self.side_size / 2 + self.y)     
    if (number == 4):
      return Point(-self.side_size / 2 + self.x, -SQRT3 * self.side_size / 2 + self.y)
    if (number == 5):
      return Point(-self.side_size + self.x, self.y)
    
  def Draw(self, screen):
    coordinades = []
    for i in range(6):
      point = self.PolygonPoint(i)
      coordinades.append((point.x, point.y))
    pygame.draw.polygon(screen, self.color, coordinades)


  def Popal(self, x, y):
    for i in range(6):
      a = self.PolygonPoint(i)
      b = self.PolygonPoint((i + 1) % 6)
      c = Point(x, y)
      if VectorProduct(Vector(a, b), Vector(a, c)) > 0:
        return False
    return True