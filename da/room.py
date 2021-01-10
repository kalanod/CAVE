import os
import sys

import pygame

pygame.init()
size = 600, 600
screen = pygame.display.set_mode(size)
run = True


# COPY here
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


def find_room(screen, coords, id):
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


j = 0
d = 0
for i in range(1, 11):
    d += 1
    if i % 5 == 0:
        j += 1
        d = 0
    find_room(screen, (100 * d, 100 * j), i)
pygame.display.flip()
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
pygame.quit()
