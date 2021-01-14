import pygame
import random



def find_room(screen, coords, id_list):
    pass


class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
                    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]
        self.cor = [9, 10]
        self.colekt_room = {}

    def render(self, screen, x1, y1):
        f1 = 0
        y = 0
        for j in range(20):
            f = 0
            x = 0
            for i in range(20):
                if self.map[x][y][0]:
                    pygame.draw.rect(screen, (255, 255, 255), (f - x1, f1 - y1, 200, 200), 1)
                f += 200
                x += 1
            f1 += 200
            y += 1

    def generation(self):
        nomer = 0
        max_n = 4
        nomber_room = 0
        while nomer < 20:
            col_sos = 0
            d = random.randrange(0, 2)
            d1 = random.randrange(0, 2)
            if d == 1:
                if d1 == 1:
                    self.cor1 = [self.cor[0], self.cor[1] + 1]
                else:
                    self.cor1 = [self.cor[0], self.cor[1] - 1]
            else:
                if d1 == 1:
                    self.cor1 = [self.cor[0] + 1, self.cor[1]]
                else:
                    self.cor1 = [self.cor[0] - 1, self.cor[1]]
            if self.cor1[0] < 0:
                self.cor1[0] = 0
            if self.cor1[1] > 20:
                self.cor1[1] = 20
            print(*board.map, sep='\n')
            print('---')
            if self.map[self.cor1[0] + 1][self.cor1[1]][0]:
                col_sos += 1
            if self.map[self.cor1[0] - 1][self.cor1[1]][0]:
                col_sos += 1
            if self.map[self.cor1[0]][self.cor1[1] + 1][0]:
                col_sos += 1
            if self.map[self.cor1[0]][self.cor1[1] - 1][0]:
                col_sos += 1
            if self.map[self.cor1[0] + 1][self.cor1[1] - 1][0]:
                col_sos += 1
            if self.map[self.cor1[0] - 1][self.cor1[1] + 1][0]:
                col_sos += 1
            if self.map[self.cor1[0] + 1][self.cor1[1] + 1][0]:
                col_sos += 1
            if self.map[self.cor1[0] - 1][self.cor1[1] - 1][0]:
                col_sos += 1
            if col_sos < max_n:
                if not self.map[self.cor1[0]][self.cor1[1]][0]:
                    nomber_room += 1
                    self.colekt_room[nomber_room] = [self.cor1[0] * 200, self.cor1[1] * 200]
                self.map[self.cor1[0]][self.cor1[1]] = [random.randrange(1, 11), 1]
                find_room(screen, self.colekt_room, self.cor)
                nomer += 1
                self.cor = self.cor1


pygame.init()
screen = pygame.display.set_mode((800, 800))
board = Dungeon(20, 20)
board.generation()
t = 9
t1 = 10
x = 1475
y = 1675
z = 500
dog_surf = pygame.image.load('data\cheast.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                t1 -= 1 
                if board.map[t][t1][0]:
                    y -= 200
                else:
                    t1 += 1
            if event.key == pygame.K_DOWN:
                t1 += 1 
                if board.map[t][t1][0]:
                    y += 200
                else:
                    t1 -= 1
            if event.key == pygame.K_LEFT:
                t -= 1 
                if board.map[t][t1][0]:
                    x -= 200
                else:
                    t += 1
            if event.key == pygame.K_RIGHT:
                t += 1 
                if board.map[t][t1][0]:
                    x += 200
                else:
                    t -= 1

    screen.fill((0, 0, 0))
    dog_rect = dog_surf.get_rect(bottomright=(z, z))
    screen.blit(dog_surf, dog_rect)
    board.render(screen, x, y)
    pygame.display.flip()