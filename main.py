import os
import sys

import pygame
import random

stuff = []
ticket = 0
weapons = [["нож", 1], ["кочерга", 1]]
lvl = 1
hp = 10
maxhp = 10
money = 0
seeds = {"солнечник": 0,
         "ведьмин стебель": 0,
         "хрустальник": 0}
map = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def find_room(screen, coords, id_list):
    print(map[id_list[0]][id_list[1]][0])
    id = map[id_list[0]][id_list[1]][0]
    if id == 1:
        draw_room1(screen, coords)
    elif id == 2:
        draw_room2(screen, coords)
    elif id == 3:
        draw_room3(screen, coords, id_list)
    elif id == 4:
        draw_room4(screen, coords)
    elif id == 5:
        draw_room5(screen, coords)
    elif id == 6:
        draw_room6(screen, coords)
    elif id == 7:
        draw_room7(screen, coords)
    elif id == 8:
        draw_room8(screen, coords)
    elif id == 9:
        draw_room2(screen, coords)
    elif id == 10:
        draw_room2(screen, coords)


def draw_room1(screen, coords):
    # комната с сундуком

    image = pygame.transform.scale(load_image("chest.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room2(screen, coords):
    # комната с сундуком
    image = pygame.transform.scale(load_image("monstor.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room3(screen, coords, id_cell):
    # комната с сундуком
    rand = random.randint(0, 2)
    map[id_cell[0]][id_cell[1]][1] = rand
    image = pygame.transform.scale(load_image("shop.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room4(screen, coords):
    # комната с
    image = pygame.transform.scale(load_image("PushkiPushka.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room5(screen, coords):
    # ПОТОП!
    image = pygame.transform.scale(load_image("boat.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room6(screen, coords):
    # комната с подозрительным торгашом
    image = pygame.transform.scale(load_image("person.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room7(screen, coords):
    # комната с запахом благовоний
    image = pygame.transform.scale(load_image("meditation.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room8(screen, coords):
    # богач или трупач
    image = pygame.transform.scale(load_image("show.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room9(screen, coords):
    # келья
    image = pygame.transform.scale(load_image("cells.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room10(screen, coords):
    # щель и таракан
    image = pygame.transform.scale(load_image("cockroach.png", -1), (100, 100))
    screen.blit(image, coords)


class Dungeon:
    def __init__(self, width, height):
        global map
        self.width = width
        self.height = height
        self.hp = 100
        self.hp1 = 10
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
        map = self.map
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
                    find_room(screen, (f - x1, f1 - y1,), (j, i))
                f += 200
                x += 1
            f1 += 200
            y += 1
        pygame.draw.rect(screen, (255, 255, 255),
                         (770, self.hp1, 15, self.hp))
        pygame.draw.rect(screen, (255, 0, 0),
                         (770, self.hp1, 15, self.hp))


    def generation(self):
        global karta
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
                # Сдесь
                self.map[self.cor1[0]][self.cor1[1]] = [random.randrange(1, 11), 1]

                pygame.display.flip()
                nomer += 1
                self.cor = self.cor1





pygame.init()
size = 800, 800
karta = pygame.display.set_mode((size))
screen = pygame.display.set_mode((size))
board = Dungeon(20, 20)
board.generation()
t = 9
t1 = 10
x = 1475
y = 1675
z = 500
dog_surf = pygame.image.load('data\cells.png')
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
                screen.fill((0, 0, 0))
            if event.key == pygame.K_DOWN:
                t1 += 1
                if board.map[t][t1][0]:
                    y += 200
                else:
                    t1 -= 1
                screen.fill((0, 0, 0))
            if event.key == pygame.K_LEFT:
                t -= 1
                if board.map[t][t1][0]:
                    x -= 200
                else:
                    t += 1
                screen.fill((0, 0, 0))
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
