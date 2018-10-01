import pygame
import math


class Bob:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r)


class Line:
    def __init__(self, basex, basey, tox, toy):
        self.basex = basex
        self.basey = basey
        self.x = tox
        self.colour = (0, 255, 0)
        self.y = toy
        self.length = math.sqrt((tox-basex)**2 + (toy-basey)**2)

    def display(self, screen):
        pygame.draw.line(screen, self.colour, [
                         self.basex, self.basey], [self.x, self.y], 3)


background_colour = (255, 255, 255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
x = 300
y = 150
thita = 15
particle = Bob(x, y, 30)


basex = 300
basey = 400
line = Line(basex, basey, x, y)

pygame.display.flip()
running = True

i = 0


while running:
    screen.fill((255, 255, 255))

    thita = thita+1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = line.length * math.sin(math.radians(thita+180))+basex
    y = line.length * math.cos(math.radians(thita+180))+basey

    line.x = round(x)
    line.y = round(y)
    particle.x = line.x
    particle.y = line.y

    line.display(screen)
    particle.display(screen)
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()
