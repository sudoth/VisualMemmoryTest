import pygame
import random
from config import (
  SIN,
  ORANGE,
  YELLOW,
  CLICK_HIGHLIGHT,
  BACKGROUND,
  EDGE,
  WIDTH,
  HEIGHT,
  DISTANCE,
  DELAY,
  CLICK_DELAY,
)
from geometry import Polygon


class Honeycomb:

  def init(self):
    pygame.init()
    screen_info = pygame.display.Info()
    self.width, self.height = WIDTH, HEIGHT
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

  def CreateHoneycombs(self):
    self.screen.fill(BACKGROUND)
    x_0 = WIDTH // 2
    y_0 = HEIGHT // 2
    honeycombs = []
    honeycombs.append(Polygon(x_0, y_0, EDGE))
    dist = DISTANCE + 2 * honeycombs[0].side_size * SIN
    honeycombs.append(Polygon(x_0 - SIN * dist, y_0 - 1 / 2 * dist, EDGE))
    honeycombs.append(Polygon(x_0, y_0 - dist, EDGE))
    honeycombs.append(Polygon(x_0 + SIN * dist, y_0 - 1 / 2 * dist, EDGE))
    honeycombs.append(Polygon(x_0 + SIN * dist, y_0 + 1 / 2 * dist, EDGE))
    honeycombs.append(Polygon(x_0, y_0 + dist, EDGE))
    honeycombs.append(Polygon(x_0 - SIN * dist, y_0 + 1 / 2 * dist, EDGE))
    self.DrawHoneycombs(honeycombs)
    return honeycombs

  def DrawHoneycombs(self, honeycombs):
    for i in range(len(honeycombs)):
      honeycombs[i].Draw(self.screen)
      new_polygon = Polygon(honeycombs[i].x, honeycombs[i].y, ORANGE, 82)
      new_polygon.Draw(self.screen)
    pygame.display.update()

  def ShowSequence(self, sequence, honeycombs):
    pygame.event.pump()
    for i in sequence:
      new_polygon = Polygon(honeycombs[i].x, honeycombs[i].y, YELLOW, 80)
      new_polygon.Draw(self.screen)
      pygame.display.flip()
      pygame.event.pump()
      pygame.time.delay(DELAY)
      self.DrawHoneycombs(honeycombs)
      pygame.event.pump()
      pygame.time.delay(DELAY)

  def HighlightHoneycomb(self, honeycomb, honeycombs):
    new_polygon = Polygon(honeycomb.x, honeycomb.y, CLICK_HIGHLIGHT, 80)
    new_polygon.Draw(self.screen)
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(CLICK_DELAY)
    self.DrawHoneycombs(honeycombs)

  def Run(self):
    game_over = False
    snd1 = pygame.mixer.Sound("snd1.wav")
    snd3 = pygame.mixer.Sound("snd3.wav")
    honeycombs = self.CreateHoneycombs()
    sequence = [random.randint(0, 6)]
    queue = [sequence[0]]
    self.ShowSequence(sequence, honeycombs)
    print(sequence)

    while not game_over:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = False
          pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = pygame.mouse.get_pos()
          clicked_index = None
          for i in range(len(honeycombs)):
            if honeycombs[i].Popal(x, y):
              clicked_index = i
              self.HighlightHoneycomb(honeycombs[i], honeycombs)
              break
          if clicked_index is None or clicked_index != queue[-1]:
            pygame.mixer.Sound.play(snd3)
            pygame.event.pump()
            pygame.time.delay(4 * DELAY)
            game_over = True
          else:
            pygame.mixer.Sound.play(snd1)
            queue.pop()
            if len(queue) == 0:
              sequence.append(random.randint(0, 6))
              self.ShowSequence(sequence, honeycombs)
              queue = sequence.copy()
              queue.reverse()
              print(sequence)
