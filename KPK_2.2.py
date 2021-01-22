import os
import sys
import pygame
import random

stuff = []
ticket = 0
weapons = [["нож", 1], ["кочерга", 1]]
lvl = 1
hp = 10
hp1 = 10
maxhp = 10
maxhp1 = 10
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
    if len(map[id_list[0]][id_list[1]]) == 1:
        return
    id = map[id_list[0]][id_list[1]][0]
    coords = (coords[0] + 50, coords[1] + 10)
    if id == 1:
        draw_room1(screen, coords, id_list)
    elif id == 2:
        draw_room2(screen, coords)
    elif id == 3:
        draw_room3(screen, coords, id_list)
    elif id == 4:
        draw_room4(screen, coords)
    elif id == 5:
        draw_room5(screen, coords)
    elif id == 6:
        draw_room6(screen, coords, id_list)
    elif id == 7:
        draw_room7(screen, coords, id_list)
    elif id == 8:
        draw_room8(screen, coords)
    elif id == 9:
        draw_room9(screen, coords, id_list)
    elif id == 10:
        draw_room10(screen, coords)


def draw_room1(screen, coords, id):
    # комната с сундуком
    if map[id[0]][id[1]][1] == 0:
        image = pygame.transform.scale(load_image("chest2.png", -1), (80, 80))
    else:
        image = pygame.transform.scale(load_image("chest.png", -1), (80, 80))
    screen.blit(image, coords)


def draw_room2(screen, coords):
    # комната с сундуком
    image = pygame.transform.scale(load_image("monstor.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room3(screen, coords, id_cell):
    # комната с сундуком
    if map[id_cell[0]][id_cell[1]][1] >= 0:
        rand = random.randint(-2, -1)
        map[id_cell[0]][id_cell[1]][1] = rand
    image = pygame.transform.scale(load_image("shop.png", -1), (100, 100))
    screen.blit(image, (coords[0] + 10, coords[1] + 10))


def draw_room4(screen, coords):
    # комната с
    image = pygame.transform.scale(load_image("PushkiPushka.png", -1), (150, 150))
    screen.blit(image, coords)


def draw_room5(screen, coords):
    # ПОТОП!
    image = pygame.transform.scale(load_image("boat.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room6(screen, coords, id):
    # комната с подозрительным торгашом
    if map[id[0]][id[1]][1] != False:
        map[id[0]][id[1]][1] = random.randint(1, 2)
    if map[id[0]][id[1]][1]:
        image = pygame.transform.scale(load_image("person.png", -1), (100, 100))
    else:
        image = pygame.transform.scale(load_image("person2.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room7(screen, coords, id):
    # комната с запахом благовоний
    if map[id[0]][id[1]][1] > 0:
        map[id[0]][id[1]][1] = random.randint(-4, -1)
    image = pygame.transform.scale(load_image("meditation.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room8(screen, coords):
    # богач или трупач
    image = pygame.transform.scale(load_image("show.png", -1), (100, 100))
    screen.blit(image, coords)


def draw_room9(screen, coords, id):
    if map[id[0]][id[1]][1]:
        image = pygame.transform.scale(load_image("cells.png", -1), (150, 100))
    else:
        image = pygame.transform.scale(load_image("cells2.png", -1), (150, 100))
    screen.blit(image, coords)


def draw_room10(screen, coords):
    # щель и таракан
    image = pygame.transform.scale(load_image("cockroach.png", -1), (100, 100))
    screen.blit(image, coords)


def ask_room(screen, coords, id_list):
    if len(map[id_list[0]][id_list[1]]) == 1:
        return
    was = map[id_list[0]][id_list[1]][1]
    id = map[id_list[0]][id_list[1]][0]
    if was:
        if id == 1:
            ask_room1(screen, coords, id_list)
        elif id == 2 or True:
            ask_room2(screen, coords)
        elif id == 3:
            ask_room3(screen, coords, id_list)
        elif id == 4:
            ask_room4(screen, coords)
        elif id == 5:
            ask_room5(screen, coords, id_list)
        elif id == 6:
            ask_room6(screen, coords, id_list)
        elif id == 7:
            ask_room7(screen, coords, id_list)
        elif id == 8:
            ask_room8(screen, coords, id_list)
        elif id == 9:
            ask_room9(screen, coords, id_list)
        elif id == 10:
            ask_room10(screen, coords)
        elif id == 11:
            ask_room11(screen)
        elif id == 32:
            ask_room12(screen)


def ask_room1(screen, coords, idcell):
    drop = random.choice(weapons)
    stuff.append(drop)
    font = pygame.font.Font(None, 50)
    line = font.render(str("Вы получили: " + drop[0]), True, pygame.Color("Blue"))
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    screen.blit(line, line_rect)
    map[idcell[0]][idcell[1]][1] = 0


def ask_room2(screen, coords):  
    global x
    global y
    global hp
    global t
    global t1
    global map
    global bonus_power
    attack_power = 2
    hp_monstor = 10
    maxhp_monstor = 10
    screen1 = pygame.display.set_mode(size)
    dog_surf1 = load_image('monstor.png', -1)
    fight = False
    col = 10
    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if fight:
                        fight = False
                        damage = col // (760 // hp_monstor)
                        if damage > hp_monstor / 2:
                            damage = hp_monstor / 2 - (damage - hp_monstor / 2)
                        print(damage + bonus_power)
                        hp_monstor -= damage * 2 + bonus_power
                        if hp_monstor <=  0:
                            close = False
                        hp -= attack_power
                        if hp <= 0:
                            pass
                            # сдесь экран смерти
                        col = 10
                    else:
                        fight = True
        screen.fill((0, 0, 0))
        dog_rect1 = dog_surf1.get_rect(bottomright=(240, 180))
        dog_rect = dog_surf.get_rect(bottomright=(770, 170))
        screen1.blit(dog_surf1, dog_rect1)
        screen1.blit(dog_surf, dog_rect)
        if fight:
            col = board.render_fight_1(screen, x, y, col, maxhp_monstor, hp_monstor)
        else:
            board.render_fight(screen, x, y, maxhp_monstor, hp_monstor)
        pygame.display.flip()
    screen.fill((0, 0, 0))
    map[t][t1][0] = 12
    board.render(screen, x, y)
    bonus_power += 1




def ask_room3(screen, coords, atribut):
    global money
    # Продаём оружее
    atribut = map[atribut[0]][atribut[1]][1]
    if atribut == -1:
        if len(stuff) >= 1:
            renderText(screen, "Вы продали: " + stuff[-1][0] + " за 5 монет")
            stuff.pop(-1)
            money += 5
    else:
        if money >= 8:
            money -= 8
            stuff.append(random.choice[weapons])
            renderText(screen, str("Вы купили: " + stuff[-1][0] + " за 8 монет"))


def ask_room4(screen, coords):
    global hp, maxhp
    rand = random.randint(0, 5)
    if rand == 0:
        renderText(screen, "Ты истинное порождение тьмы! я помогу тебе")
        maxhp += 2
    else:
        renderText(screen, "Вас пронзила тысяча теневых клинков")
        hp -= 4


def ask_room5(screen, coords, id):
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


def ask_room6(screen, coords, id):
    global hp
    # подозрительный
    if map[id[0]][id[1]][1] == 1:
        hp -= 4
        stuff.append(random.choice(weapons))
        renderText(screen, str(stuff[-1][0] + " Впился вам в бок забрав 4 хп,"))
        renderText(screen, "но силуэт исчез, и похоже, теперь оружее ваше", (40, 300))
        map[id[0]][id[1]][1] = 0
    if map[id[0]][id[1]][1] == 2:
        if len(stuff) >= 1:
            renderText(screen, str("Ваш " + stuff[-1][0] + " был украден"))
            stuff.pop(-1)
            hp = maxhp
            map[id[0]][id[1]][1] = 0


def renderText(screen, text, coords=False):
    font = pygame.font.Font(None, 50)
    line = font.render(text, True, pygame.Color("Blue"))
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    if coords:
        line_rect.top = coords[1]
        line_rect.left = coords[0]
        pygame.draw.rect(screen, (255, 0, 0), (*coords, line_rect.width + 20, line_rect.height + 10))
    else:
        pygame.draw.rect(screen, (255, 0, 0),
                         (line_rect.x - 10, line_rect.y, line_rect.width + 20, line_rect.height + 10))
    screen.blit(line, line_rect)


def ask_room7(screen, coords, id):
    global maxhp, lvl
    rand = random.randint(0, 5)
    map[id[0]][id[1]][1] += 1

    font = pygame.font.Font(None, 50)
    if rand == 0:
        line = font.render(str("Вы потянули лодыжку -1 ур "), True, pygame.Color("Blue"))
        lvl -= 1
    else:
        maxhp += 1
        line = font.render(str("Ваш максимальный хп теперь " + str(maxhp)), True, pygame.Color("Blue"))
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    pygame.draw.rect(screen, (255, 0, 0), (*coords, 150, 30))
    screen.blit(line, line_rect)


def ask_room8(screen, coords, id):
    pass


def ask_room9(screen, coords, id):
    global hp, money
    rand = random.randint(0, 5)
    if rand < 2:
        money += 1
        renderText(screen, "Это не зелье, это монета!")
    elif rand < 5:
        hp -= 2
        renderText(screen, "Горько! это было зелье вреда!")
    elif rand == 5:
        hp -= 5
        renderText(screen, "Горько! это было большое зелье вреда!")
    map[id[0]][id[1]][1] = False


def ask_room10(screen, coords):
    pygame.draw.rect(screen, (255, 0, 0), coords, 50, 10)


def ask_room11(screen):
    renderText(screen, "Получено семечно солнечника")
    seeds["солнечник"] += 1


def ask_room12(screen):
    global transition
    transition = True


class Dungeon:
    def __init__(self, width, height):
        global map
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
                find_room(screen, (f - x1, f1 - y1,), (i, j))
                f += 200
                x += 1
            f1 += 200
            y += 1

        pygame.draw.rect(screen, (255, 255, 255),
                         (770, maxhp1, 15, maxhp * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (770, hp1, 15, hp * 10))
        image = pygame.transform.scale(load_image("door.png", -1), (150, 150))
        screen.blit(image, [self.colekt_room[self.id_exit][0] - x1, self.colekt_room[self.id_exit][1] - y1])
        self.map[self.colekt_room[self.id_exit][-1][0]][self.colekt_room[self.id_exit][-1][1]] = [32, 1]
        y22 = 0
        for i in stuff:
            renderText(screen, i[0], (0, y22))
            y22 += 50

    def render_fight(self, screen, x1, y1, maxhp_monstor, hp_monstor):
        pygame.draw.rect(screen, (255, 255, 255),
                         (770, maxhp1, 15, maxhp * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (770, hp1, 15, hp * 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (10, 10, 15, maxhp_monstor * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (10, 10, 15, hp_monstor * 10))
        font = pygame.font.Font(None, 50)
        text = font.render('Нажмите X для боя.', True, (255, 0, 0))
        place = text.get_rect(center=(200, 600))
        screen.blit(text, place)

    def render_fight_1(self, screen, x1, y1, col, maxhp_monstor, hp_monstor):
        pygame.draw.rect(screen, (255, 255, 255),
                         (770, maxhp1, 15, maxhp * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (770, hp1, 15, hp * 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (10, 10, 15, maxhp_monstor * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (10, 10, 15, hp_monstor * 10))
        pygame.draw.rect(screen, (255, 255, 255), 
                 (10, 600, 775, 75), 8)
        pygame.draw.rect(screen, (255, 0, 0), 
                 (385, 600, 15, 75), 0)
        pygame.draw.rect(screen, (0, 255, 0), 
                 (col, 600, 15, 75), 0)
        col += 0.2
        return col

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
                self.cor1[0] = 1
            if self.cor1[1] > 20:
                self.cor1[1] = 19
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
                    self.colekt_room[nomber_room] = [self.cor1[0] * 200 + 25, self.cor1[1] * 200 + 25, self.cor1]
                self.map[self.cor1[0]][self.cor1[1]] = [random.randrange(1, 31), 1]
                pygame.display.flip()
                nomer += 1
                self.cor = self.cor1
        self.id_exit = random.choice(list(self.colekt_room.keys()))


floor = 1
bonus_power = 0
while floor != 6:
    pygame.init()
    size = 800, 700
    karta = pygame.display.set_mode((size))
    screen = pygame.display.set_mode((size))
    board = Dungeon(20, 20)
    x = 1475
    y = 1675
    board.generation()
    t = 9
    t1 = 10
    z = 500
    transition = False
    x1, y1 = 9, 10
    dog_surf = load_image('Седнев.jpg', -1)
    board.render(screen, x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    t1 -= 1
                    if board.map[t][t1][0]:
                        y -= 200
                        y1 -= 1
                    else:
                        t1 += 1
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                if event.key == pygame.K_DOWN:
                    t1 += 1
                    if board.map[t][t1][0]:
                        y += 200
                        y1 += 1
                    else:
                        t1 -= 1
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                if event.key == pygame.K_LEFT:
                    t -= 1
                    if board.map[t][t1][0]:
                        x -= 200
                        x1 -= 1
                    else:
                        t += 1
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                if event.key == pygame.K_RIGHT:
                    t += 1
                    if board.map[t][t1][0]:
                        x += 200
                        x1 += 1
                    else:
                        t -= 1
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                if event.key == pygame.K_z:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    ask_room(screen, (600, 600), (x1, y1))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    exit()
        if transition:
            floor += 1
            transition = False
            break
        dog_rect = dog_surf.get_rect(bottomright=(z, z))
        screen.blit(dog_surf, dog_rect)
        pygame.display.flip()
