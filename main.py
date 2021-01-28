import pygame
import random


class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
             False, False, False, False, False]]
        self.cor = [9, 10]

    def render(self, screen):
        f1 = 0
        y = 0
        for j in range(20):
            f = 0
            x = 0
            for i in range(20):
                print(x, y)
                if self.map[x][y]:
                    pygame.draw.rect(screen, (255, 255, 255), (f, f1, 50, 50), 1)
                f += 50
                x += 1
            f1 += 50
            y += 1

    def generation(self):
        for i in range(20):
            d = random.randrange(0, 2)
            d1 = random.randrange(0, 2)
            if d == 1:
                if d1 == 1:
                    self.cor = [self.cor[0], self.cor[1] + 1]
                else:
                    self.cor = [self.cor[0], self.cor[1] - 1]
            else:
                if d1 == 1:
                    self.cor = [self.cor[0] + 1, self.cor[1]]
                else:
                    self.cor = [self.cor[0] - 1, self.cor[1]]
            if self.cor[0] < 0:
                self.cor[0] = 0
            if self.cor[1] < 0:
                self.cor[1] = 0
            self.map[self.cor[0]][self.cor[1]] = True
        print(*self.map, sep='\n')


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
board = Dungeon(20, 20)
board.generation()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()