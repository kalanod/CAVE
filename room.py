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
seeds = {"солнечник": 0,
         "ведьмин стебель": 0,
         "хрустальник": 0}

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


def draw_room3(screen, coords, id_cell):
    # комната с сундуком
    rand = random.randint(0, 2)
    map[id_cell][1] = rand
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
            ask_room5(screen, coords, idcell)
        elif id == 6:
            ask_room6(screen, coords)
        elif id == 7:
            ask_room7(screen, coords, idcell)
        elif id == 8:
            ask_room8(screen, coords, idcell)
        elif id == 9:
            ask_room9(screen, coords, idcell)
        elif id == 10:
            ask_room10(screen, coords)
        elif id == 11:
            ask_room11(screen)


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
    pass


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


def ask_room5(screen, coords, id):
    global maxhp, lvl
    # благовония
    if map[id][1] == 0:
        map[id][1] = False
    else:
        rand = random.randint(0, 5)
        map[id][1] -= 1

        font = pygame.font.Font(None, 50)
        if rand == 0:
            line = font.render(str("Вы потянули лодышку -1 ур "), True, pygame.Color("Blue"))
            lvl -= 1
        else:
            maxhp += 1
            line = font.render(str("Ваш максимальный хп теперь " + str(maxhp)), True, pygame.Color("Blue"))
        line_rect = line.get_rect()
        line_rect.top = size[1] / 2 - 100
        line_rect.left = size[0] / 2 - line_rect.width / 2
        pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
        screen.blit(line, line_rect)


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


def renderText(screen, text):
    font = pygame.font.Font(None, 50)
    line = font.render(text, True, pygame.Color("Blue"))
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    pygame.draw.rect(screen, (255, 0, 0), (300, 300, 150, 30))
    screen.blit(line, line_rect)


def ask_room7(screen, coords, id):
    global hp
    # подозрительный
    if map[id][1] == 1:
        hp -= 4
        stuff.append(random.choice(weapons))
        renderText(screen, str(stuff[-1] + "Впился вам в бок забрав 4 хп, но силуэт исчез, и похоже, теперь он ваш"))
    if map[id][1] == 2:
        if len(stuff) >= 1:
            renderText(screen, str(stuff[-1] + "Ваш " + stuff[-1] + " был украден"))
            stuff.pop(-1)
            hp = maxhp


def ask_room8(screen, coords, id):
    global hp, maxhp
    rand = random.randint(0, 5)
    if rand == 0:
        renderText(screen, "Ты истинное пораждение тьмы! я помогу тебе")
        maxhp += 2
    else:
        renderText(screen, "Вас пронзила тысяча теневых клинков")
        hp -= 4


def ask_room9(screen, coords, id):
    global hp, money
    rand = random.randint(0, 5)
    if rand < 2:
        money += 1
        renderText(screen, "Это не зелье это монета!")
    elif rand < 5:
        hp -= 2
        renderText(screen, "Горько! это было зелье вреда!")
    elif rand == 5:
        hp -= 5
        renderText(screen, "Горько! это было большое зелье вреда!")
    map[id][1] = False


def ask_room10(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)

def ask_room11(screen):
    renderText(screen, "Получено семечно солнечнико")
    seeds["солнечник"] += 1


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
