import os
import random
import sys

import pygame

pygame.init()
size = 600, 600
screen = pygame.display.set_mode(size)
run = True

# COPY here
map = [[1, 1, ], [2, 1], [3, 1],
       [4, 1], [5, 12], [6, 1],
       [7, False], [False, False], [False, False],
       [False, False]]

stuff = []
ticket = 0
weapons = [["нож", 1], ["кочерга", 1]]
lvl = 1
hp = 10
maxhp = 10
money = 0


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
    id = map[id_list][0]
    if id == 1:
        draw_room1(screen, coords)
    elif id == 2:
        draw_room2(screen, coords)
    elif id == 3:
        draw_room3(screen, coords)
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


def draw_room3(screen, coords):
    # комната с сундуком
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


def ask_room(screen, coords, idcell):
    was = map[idcell][1]
    id = map[idcell][0]
    if was:
        if id == 1:
            ask_room1(screen, coords, idcell)
        elif id == 2:
            ask_room2(screen, coords)
        elif id == 3:
            ask_room3(screen, coords, idcell)
        elif id == 4:
            ask_room4(screen, coords)
        elif id == 5:
            ask_room5(screen, coords)
        elif id == 6:
            ask_room6(screen, coords)
        elif id == 7:
            ask_room7(screen, coords)
        elif id == 8:
            ask_room8(screen, coords)
        elif id == 9:
            ask_room9(screen, coords)
        elif id == 10:
            ask_room10(screen, coords)


def ask_room1(screen, coords, idcell):
    drop = random.choice(weapons)
    stuff.append(drop)
    font = pygame.font.Font(None, 50)
    line = font.render(str("Вы получили: " + drop[0]), True, pygame.Color("Blue"))
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
    screen.blit(line, line_rect)
    map[idcell][1] = False


def ask_room2(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), (*coords, 50, 10))


def ask_room3(screen, coords, atribut):
    global money
    # Продаём оружее
    if len(stuff) >= 1:
        font = pygame.font.Font(None, 50)
        line = font.render(str("Вы продали: " + stuff[-1] + " за 5 монет"), True, pygame.Color("Blue"))
        line_rect = line.get_rect()
        line_rect.top = size[1] / 2 - 100
        line_rect.left = size[0] / 2 - line_rect.width / 2
        pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
        screen.blit(line, line_rect)
        stuff.pop(-1)
        money += 5


def ask_room4(screen, coords):
    global money
    # Покупаем оружее

    if money >= 8:
        money -= 8
        stuff.append(random.choice[weapons])
        font = pygame.font.Font(None, 50)
        line = font.render(str("Вы купили: " + stuff[-1] + " за 8 монет"), True, pygame.Color("Blue"))
        line_rect = line.get_rect()
        line_rect.top = size[1] / 2 - 100
        line_rect.left = size[0] / 2 - line_rect.width / 2
        pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
        screen.blit(line, line_rect)


def ask_room5(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


def ask_room6(screen, coords):
    global money, ticket
    if money >= 1:
        money -= 1
        ticket -= 1
        font = pygame.font.Font(None, 50)
        line = font.render(str("Спасибо! куда плывём?"), True, pygame.Color("Blue"))
        line_rect = line.get_rect()
        line_rect.top = size[1] / 2 - 100
        line_rect.left = size[0] / 2 - line_rect.width / 2
        pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
        screen.blit(line, line_rect)



def ask_room7(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


def ask_room8(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


def ask_room9(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


def ask_room10(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


j = 0
d = 0
for i in range(1, 6):
    d += 1
    if i % 5 == 0:
        j += 1
        d = 0
    find_room(screen, (100 * d, 100 * j), i)
ask_room(screen, (50 * 1, 50 * 1), 3)

pygame.display.flip()
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
pygame.quit()
