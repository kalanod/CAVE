import os
import sys
import pygame
import random

stuff = [["кочерга", 1]]
ticket = 0
weapons = [["старый шарф", 1], ["кочерга", 1], ["игрушечный нож", 1], ["молоток", 1],
           ["трамбон", 2], ["поребрик", 2], ["фен", 2],
           ["шпага", 3], ["скверный бластер", 3]]
artefact = [["БАТИНКИ ОСЛЕПИТЕЛЬНОЙ СКОРОСТИ"], ["СТАРЫЙ ШАРФ"], ["СОЛОМЕННАЯ ШЛЯПА"]]
lvl = 1
hp = 10
hp1 = 10
hill = 0  # зелья исцеления
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


def draw_floor(screen, coords, id_list):
    if len(map[id_list[0]][id_list[1]]) == 1:
        return
    up, down, left, right = False, False, False, False
    if len(map[id_list[0]][id_list[1] + 1]) > 1:
        down = True
    if len(map[id_list[0] - 1][id_list[1]]) > 1:
        left = True
    if len(map[id_list[0] + 1][id_list[1]]) > 1:
        right = True
    if len(map[id_list[0]][id_list[1] - 1]) > 1:
        up = True
    if up:
        if down:
            if right:
                if left:
                    screen.blit(floorImage[8], coords)
                else:
                    screen.blit(floorImage[0], coords)
            elif left:
                screen.blit(floorImage[1], coords)
            else:
                screen.blit(floorImage[3], coords)
        elif right:
            if left:
                screen.blit(floorImage[6], coords)
            else:
                screen.blit(floorImage[14], coords)
        elif left:
            screen.blit(floorImage[5], coords)
        else:
            screen.blit(floorImage[13], coords)

    elif down:
        if right:
            if left:
                screen.blit(floorImage[2], coords)
            else:
                screen.blit(floorImage[7], coords)
        elif left:
            screen.blit(floorImage[4], coords)
        else:
            screen.blit(floorImage[10], coords)
    elif left:
        if right:
            screen.blit(floorImage[12], coords)
        else:
            screen.blit(floorImage[15], coords)
    else:
        screen.blit(floorImage[11], coords)


def find_room(screen, coords, id_list):
    if len(map[id_list[0]][id_list[1]]) == 1:
        return
    draw_floor(screen, coords, id_list)

    id = map[id_list[0]][id_list[1]][0]
    coords = (coords[0] + 50, coords[1] + 50)
    if id == 1:
        draw_room1(screen, coords, id_list)
    elif id == 2:
        draw_room2(screen, coords, id_list)
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
    elif id == 11:
        draw_room11(screen, coords, id_list)
    elif id == 13:
        draw_room13(screen, coords)
    elif id == 14:
        draw_room14(screen, coords)


def draw_room1(screen, coords, id):
    # комната с сундуком
    if map[id[0]][id[1]][1] == 0:
        image = pygame.transform.scale(load_image("chest2.png", -1), (80, 80))
    else:
        image = pygame.transform.scale(load_image("chest.png", -1), (80, 80))
    screen.blit(image, coords)


def draw_room2(screen, coords, id):
    # комната с сундуком

    if map[id[0]][id[1]][1] == 1:
        monstor = int(random.randint(1, len(monsters))) * -1
        map[id[0]][id[1]][1] = monstor
    image = monsters[abs(map[id[0]][id[1]][1]) - 1]
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
    if map[id[0]][id[1]][1] == 1:
        map[id[0]][id[1]][1] = random.randint(-2, -1)

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


def draw_room13(screen, coords):
    image = pygame.transform.scale(load_image("trap.png", -1), (30, 30))
    screen.blit(image, (coords[0] + 20, coords[1] + 20))


def draw_room14(screen, coords):
    image = pygame.transform.scale(load_image("alhimiy.png", -1), (100, 100))
    screen.blit(image, (coords[0] + 20, coords[1] + 20))


def draw_room11(screen, coords, id):
    if map[id[0]][id[1]][1] == 1:
        map[id[0]][id[1]][1] = random.randint(-3, -1)
    if map[id[0]][id[1]][1] == -1:
        image = pygame.transform.scale(load_image("s1.png", -1), (30, 30))
        screen.blit(image, (coords[0] + 20, coords[1] + 20))
    elif map[id[0]][id[1]][1] == -2:
        image = pygame.transform.scale(load_image("s2.png", -1), (30, 30))
        screen.blit(image, (coords[0] + 20, coords[1] + 20))
    elif map[id[0]][id[1]][1] == -3:
        image = pygame.transform.scale(load_image("s3.png", -1), (30, 30))
        screen.blit(image, (coords[0] + 20, coords[1] + 20))


def ask_room(screen, coords, id_list):
    if len(map[id_list[0]][id_list[1]]) == 1:
        return
    was = map[id_list[0]][id_list[1]][1]
    id = map[id_list[0]][id_list[1]][0]
    # id = 3
    if was and was != -20:
        if id == 1:
            ask_room1(screen, coords, id_list)
        elif id == 2:
            ask_room2(screen, id_list)
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
            ask_room10(screen, coords, id_list)
        elif id == 11:
            ask_room11(screen, id_list)
        elif id == 32:
            ask_room12(screen)
        elif id == 13:
            ask_room13(screen)
        elif id == 14:
            ask_room14(screen)


def ask_room1(screen, coords, idcell):
    global money, hill
    drop = random.randint(0, 6)
    #drop = 6
    if drop < 2:
        renderText(screen, str("Монетка! теперь твоя"))
        mony = random.randint(0, 3)
        money += mony
        map[idcell[0]][idcell[1]][1] = 0
    elif drop < 5:
        hill += 1
        renderText(screen, str("Красное зелье, пригодится!"))
        map[idcell[0]][idcell[1]][1] = 0
    elif drop == 5:
        drop = random.choice(weapons)
        if len(stuff) <= 5 and len(stuff) <= lvl // 10 + 1:
            stuff.append(drop)
            renderText(screen, str("Вы получили: " + drop[0]))
            map[idcell[0]][idcell[1]][1] = 0
        else:
            renderText(screen, str("у вас нет места!"))
    else:
        renderText(screen, str("О нет! это мимик!"))
        mimic(screen)


def ask_room2(screen, id, hp_monstor=15, attack_power=False, pobag=True):
    lb = 0
    global x, money, lvl, hill, bonus_dam, bonus_def
    mainTheme.stop()
    if not attack_power:
        attack_power = (abs(map[id[0]][id[1]][1]) // 3) + 1 + lvl // 30
    else:
        attack_power = lvl // 20 + 1
    dog_surf1 = monsters[abs(map[id[0]][id[1]][1]) - 1]
    battleTheme.set_volume(0.1)
    battleTheme.play()
    global y
    global hp
    global t
    global t1
    global bonus_power
    pobeg = True
    flag = False
    flag_1 = False
    hp_monstor = random.randint(5 + lvl // 20, 10 + lvl // 20)
    maxhp_monstor = hp_monstor
    screen1 = pygame.display.set_mode(size)
    if not dog_surf1:
        dog_surf1 = load_image('monstor.png', -1)
    fight = False
    col = 1
    ld = 0
    close = True
    damage = 0
    v = False
    if pobag:
        pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
        renderText(screen, "Побег", (570, 615), 30)
    pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
    renderText(screen, "Бой", (170, 615), 30)
    pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
    renderText(screen, "Хил", (370, 615), 30)
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))

                if event.pos[0] in range(100, 300) and event.pos[1] in range(600, 650):
                    pygame.draw.rect(screen, (100, 50, 0), (100, 600, 200, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
                renderText(screen, "Бой", (170, 615), 30)

                if event.pos[0] in range(300, 500) and event.pos[1] in range(600, 650):
                    pygame.draw.rect(screen, (100, 50, 0), (300, 600, 200, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
                renderText(screen, "Хил", (370, 615), 30)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(100, 300) and event.pos[1] in range(600, 650):
                    if fight:
                        fight = False
                        damage = 1
                        hp_monstor -= damage + bonus_power + bonus_dam
                        bonus_dam = 0
                        if hp_monstor <= 0:
                            close = False
                        else:
                            if attack_power * 0.5 < bonus_def:
                                damageNow = attack_power - int(attack_power * 0.5)
                                bonus_def -= int(attack_power * 0.5)
                                ld = attack_power - damageNow
                                hp -= damageNow
                            else:
                                damageNow = attack_power - bonus_def
                                bonus_def = 0
                                hp -= damageNow
                        if hp <= 0:
                            close = False
                        col = 10
                    else:
                        v = True
                        fight = True
                if event.pos[0] in range(300, 500) and event.pos[1] in range(600, 650):
                    if hill >= 1:
                        hill -= 1
                        hp += 3
                if pobag:
                    if event.pos[0] in range(500, 700) and event.pos[1] in range(600, 650):
                        if pobag:
                            close = False
                            pobeg = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if fight:
                        fight = False
                        damage = 1
                        lb = damage + bonus_power + bonus_dam  # урон от еффекта
                        ld = 0  # защита от щита
                        print(damage + bonus_power + bonus_dam)
                        hp_monstor -= damage + bonus_power + bonus_dam
                        bonus_dam = 0
                        if hp_monstor <= 0:
                            close = False
                        else:
                            if attack_power * 0.5 < bonus_def:
                                damageNow = attack_power - int(attack_power * 0.5)
                                bonus_def -= int(attack_power * 0.5)
                                ld = attack_power - damageNow
                                hp -= damageNow
                            else:
                                damageNow = attack_power - bonus_def
                                ld = attack_power - damageNow
                                bonus_def = 0
                                hp -= damageNow
                        v = False
                        if hp <= 0:
                            close = False
                        col = 10
                        screen.fill((0, 0, 0))

                if event.key == pygame.K_a:
                    if pobag:
                        close = False
                        pobeg = False
                        lvl -= 10
                        hp -= 2
                if event.key == pygame.K_s:
                    if hill >= 1:
                        hill -= 1
                        hp += 3
            if pobag:
                pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
                renderText(screen, "Побег", (570, 615), 30)
            pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
            renderText(screen, "Бой", (170, 615), 30)
            pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
            renderText(screen, "Хил", (370, 615), 30)
        if v:
            screen.fill((0, 0, 0))
        if flag_1:
            font = pygame.font.Font(None, 50)
            if not ld:
                text = font.render(
                    'Вы нанесли ' + str(damage * 2 + bonus_power + lb) + ' урона. Вам нанесли ' + str(attack_power),
                    True,
                    (255, 0, 0))
                place = text.get_rect(center=(400, 400))
                screen.blit(text, place)
            else:
                text = font.render(
                    'Вы нанесли ' + str(damage * 2 + bonus_power + lb) + ' урона.', True,
                    (255, 0, 0))
                place = text.get_rect(center=(400, 400))
                screen.blit(text, place)
                text = font.render('Вам нанесли ' + str(attack_power) + ", но " + str(ld)
                                   + " сдержал щит", True, (255, 0, 0))
                place = text.get_rect(center=(400, 450))
                screen.blit(text, place)
        dog_rect1 = dog_surf1.get_rect(bottomright=(240, 180))
        dog_rect = dog_surf.get_rect(bottomright=(770, 170))
        screen1.blit(dog_surf1, dog_rect1)
        screen1.blit(load_image("hero.png", -1), dog_rect)
        if fight:
            if col >= 770:
                flag = True
            if col <= 10:
                flag = False
            flag_1 = True
            col = board.render_fight_1(screen, x, y, col, maxhp_monstor * 2, hp_monstor * 2, flag)
        else:
            board.render_fight(screen, x, y, maxhp_monstor * 2, hp_monstor * 2, pobag)
        pygame.display.flip()

        '''
        pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
        renderText(screen, "Бой", (570, 615), 30)

        pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
        renderText(screen, "Хил", (370, 615), 30)

        if pobag:
            pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
            renderText(screen, "Побег", (170, 615), 30)
        '''

    screen.fill((0, 0, 0))
    map[t][t1][0] = 12
    board.render(screen, x, y)

    if pobeg:
        drop = random.randint(0, 5)
        drop += ((abs(map[id[0]][id[1]][1]) - 1) // 2)
        if drop < 4:
            renderText(screen, "Вы пoбедили! и присвоили золотую монету")
            money += 1
        elif 4 < drop < 7:
            renderText(screen, "В сокровищах вы нашли зелье!")
            hill += 1
        else:
            if len(stuff) <= lvl // 10 + 1:
                drop2 = random.choice(weapons)
                renderText(screen, str("Отличный " + drop2[0] + " теперь твой!"))
                stuff.append(drop2)
            else:
                renderText(screen, "В сокровищах вы нашли зелье!")
                hill += 1
        lvl += 7
    battleTheme.stop()
    mainTheme.play()


def mimic(screen, pobag=True):
    mainTheme.stop()
    text = False
    ld = 0
    lb = 0
    global x, money, lvl, hill, maxhp, bonus_def, bonus_dam
    attack_power = (lvl // 10 + 3) // 2
    dog_surf1 = pygame.transform.scale(load_image("chest.png", -1), (100, 100))
    battleTheme.set_volume(0.1)
    battleTheme.play()
    global y
    global hp
    global t
    global t1
    global bonus_power
    pobeg = True
    flag = False
    flag_1 = False
    maxhp_monstor = maxhp / 2

    hp_monstor = maxhp_monstor
    screen1 = pygame.display.set_mode(size)
    fight = False
    col = 10
    close = True
    damage = 0
    v = False
    if pobag:
        pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
        renderText(screen, "Побег", (570, 615), 30)
    pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
    renderText(screen, "Бой", (170, 615), 30)
    pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
    renderText(screen, "Хил", (370, 615), 30)
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))

                if event.pos[0] in range(100, 300) and event.pos[1] in range(600, 650):
                    pygame.draw.rect(screen, (100, 50, 0), (100, 600, 200, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
                renderText(screen, "Бой", (170, 615), 30)

                if event.pos[0] in range(300, 500) and event.pos[1] in range(600, 650):
                    pygame.draw.rect(screen, (100, 50, 0), (300, 600, 200, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
                renderText(screen, "Хил", (370, 615), 30)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(100, 300) and event.pos[1] in range(600, 650):
                    if fight:
                        fight = False
                        damage = 1
                        hp_monstor -= damage + bonus_power + bonus_dam
                        bonus_dam = 0
                        if hp_monstor <= 0:
                            close = False
                        else:
                            if attack_power * 0.5 < bonus_def:
                                damageNow = attack_power - int(attack_power * 0.5)
                                bonus_def -= int(attack_power * 0.5)
                                ld = attack_power - damageNow
                                hp -= damageNow
                            else:
                                damageNow = attack_power - bonus_def
                                bonus_def = 0
                                hp -= damageNow
                        if hp <= 0:
                            close = False
                        col = 10
                    else:
                        v = True
                        fight = True
                if event.pos[0] in range(300, 500) and event.pos[1] in range(600, 650):
                    if hill >= 1:
                        hill -= 1
                        hp += 3
                if pobag:
                    if event.pos[0] in range(500, 700) and event.pos[1] in range(600, 650):
                        if pobag:
                            close = False
                            pobeg = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if fight:
                        fight = False
                        damage = 1
                        lb = damage + bonus_power + bonus_dam  # урон от еффекта
                        ld = 0  # защита от щита
                        print(damage + bonus_power + bonus_dam)
                        hp_monstor -= damage + bonus_power + bonus_dam
                        bonus_dam = 0
                        if hp_monstor <= 0:
                            close = False
                        else:
                            if attack_power * 0.5 < bonus_def:
                                damageNow = attack_power - int(attack_power * 0.5)
                                bonus_def -= int(attack_power * 0.5)
                                ld = attack_power - damageNow
                                hp -= damageNow
                            else:
                                damageNow = attack_power - bonus_def
                                ld = attack_power - damageNow
                                bonus_def = 0
                                hp -= damageNow
                        v = False
                        if hp <= 0:
                            close = False
                        col = 10
                        screen.fill((0, 0, 0))

                if event.key == pygame.K_a:
                    if pobag:
                        close = False
                        pobeg = False
                        lvl -= 10
                        hp -= 2
                if event.key == pygame.K_s:
                    if hill >= 1:
                        hill -= 1
                        hp += 3
            if pobag:
                pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
                renderText(screen, "Побег", (570, 615), 30)
            pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
            renderText(screen, "Бой", (170, 615), 30)
            pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
            renderText(screen, "Хил", (370, 615), 30)
        if v:
            screen.fill((0, 0, 0))
        if flag_1:
            font = pygame.font.Font(None, 50)
            if not ld:
                text = font.render(
                    'Вы нанесли ' + str(damage * 2 + bonus_power + lb) + ' урона. Вам нанесли ' + str(attack_power),
                    True,
                    (255, 0, 0))
                place = text.get_rect(center=(400, 400))
                screen.blit(text, place)
            else:
                text = font.render(
                    'Вы нанесли ' + str(damage * 2 + bonus_power + lb) + ' урона.', True,
                    (255, 0, 0))
                place = text.get_rect(center=(400, 400))
                screen.blit(text, place)
                text = font.render('Вам нанесли ' + str(attack_power) + ", но " + str(ld)
                                   + " сдержал щит", True, (255, 0, 0))
                place = text.get_rect(center=(400, 450))
                screen.blit(text, place)
        dog_rect1 = dog_surf1.get_rect(bottomright=(240, 180))
        dog_rect = dog_surf.get_rect(bottomright=(770, 170))
        screen1.blit(dog_surf1, dog_rect1)
        screen1.blit(load_image("hero.png", -1), dog_rect)
        if fight:
            if col >= 770:
                flag = True
            if col <= 10:
                flag = False
            flag_1 = True
            col = board.render_fight_1(screen, x, y, col, maxhp_monstor * 2, hp_monstor * 2, flag)
        else:
            board.render_fight(screen, x, y, maxhp_monstor * 2, hp_monstor * 2, pobag)
        pygame.display.flip()

        '''
        pygame.draw.rect(screen, (150, 50, 0), (100, 600, 200, 50), 1)
        renderText(screen, "Бой", (570, 615), 30)

        pygame.draw.rect(screen, (150, 50, 0), (300, 600, 200, 50), 1)
        renderText(screen, "Хил", (370, 615), 30)

        if pobag:
            pygame.draw.rect(screen, (150, 50, 0), (500, 600, 200, 50), 1)
            renderText(screen, "Побег", (170, 615), 30)
        '''

    screen.fill((0, 0, 0))
    map[t][t1][0] = 12
    board.render(screen, x, y)

    if pobeg:
        drop = random.randint(0, 5)
        drop += 5
        if drop < 4:
            renderText(screen, "Вы пoбедили! и присвоили золотую монету")
            money += 1
        elif 4 < drop < 7:
            renderText(screen, "В сокровищах вы нашли зелье!")
            hill += 1
        else:
            if len(stuff) <= lvl // 10 + 1:
                drop2 = random.choice(weapons)
                renderText(screen, str("Отличный " + drop2[0] + " теперь твой!"))
                stuff.append(drop2)
            else:
                renderText(screen, "В сокровищах вы нашли зелье!")
                hill += 1
        lvl += 7
    battleTheme.stop()
    mainTheme.play()


def ask_room3(screen, coords, atribut):
    global money, x, y, hill
    # Продаём оружее
    atribut = map[atribut[0]][atribut[1]][1]
    if atribut == -1:
        pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
        pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
        pygame.draw.rect(screen, (150, 50, 255), (500, 400, 250, 50), 1)
        if len(stuff) >= 1:
            renderText(screen, "продать" + stuff[-1][0] + " за 5 монет", (500, 320), 30)
        else:
            renderText(screen, "-------------", (500, 320), 30)
        renderText(screen, "купить зелье - 2 монеты", (500, 370), 30)
        renderText(screen, "До свидания", (500, 420), 30)
        runRoom = True
        while runRoom:

            pygame.display.flip()
            for uy in pygame.event.get():
                if uy.type == pygame.QUIT:
                    exit()
                if uy.type == pygame.MOUSEMOTION:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):

                        if len(stuff) >= 1:
                            renderText(screen, "продать" + stuff[-1][0] + " за 5 монет", (500, 320), 30)
                            pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
                        else:
                            renderText(screen, "-------------", (500, 320), 30)
                            pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
                    else:
                        if len(stuff) >= 1:
                            renderText(screen, "продать" + stuff[-1][0] + " за 5 монет", (500, 320), 30)
                        else:
                            renderText(screen, "-------------", (500, 320), 30)
                        pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
                    renderText(screen, "купить зелье - 2 монеты", (500, 370), 30)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                        pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)
                    else:
                        pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                        pygame.draw.rect(screen, (150, 50, 0), (500, 400, 250, 50), 1)
                        renderText(screen, "Досвидания", (500, 420), 30)
                    else:
                        pygame.draw.rect(screen, (150, 50, 255), (500, 400, 250, 50), 1)
                        renderText(screen, "Досвидания", (500, 420), 30)

                if uy.type == pygame.MOUSEBUTTONDOWN:
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                        if len(stuff) >= 1:
                            renderText(screen, "Вы продали: " + stuff[-1][0] + " за 5 монет")
                            stuff.pop(-1)
                            money += 5
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                        if money >= 2:
                            money -= 2
                            hill += 1
                            renderText(screen, "У нас лучшие зелья!")
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                        screen.fill((0, 0, 0))
                        board.render(screen, x, y)
                        runRoom = False
                if uy.type == pygame.KEYDOWN:
                    if uy.key == pygame.K_ESCAPE:
                        screen.fill((0, 0, 0))
                        board.render(screen, x, y)
                        runRoom = False

    else:
        pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
        pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
        pygame.draw.rect(screen, (150, 50, 255), (500, 400, 250, 50), 1)
        if money >= 8:
            renderText(screen, "купить" + random.choice(weapons)[0] + " за 8 монет", (500, 320), 30)
        else:
            renderText(screen, "-------------", (500, 320), 30)
        renderText(screen, "купить зелье - 2 монеты", (500, 370), 30)
        renderText(screen, "Досвидания", (500, 420), 30)
        runRoom = True
        while runRoom:

            pygame.display.flip()
            for uy in pygame.event.get():
                if uy.type == pygame.QUIT:
                    exit()
                if uy.type == pygame.MOUSEMOTION:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):

                        if money >= 8:
                            renderText(screen, "купить пушку за 8 монет", (500, 320), 30)
                            pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
                        else:
                            renderText(screen, "-------------", (500, 320), 30)
                            pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
                    else:
                        if money >= 8:
                            renderText(screen, "купить" + random.choice(weapons)[0] + " за 8 монет", (500, 320), 30)
                        else:
                            renderText(screen, "-------------", (500, 320), 30)
                        pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
                    renderText(screen, "купить зелье - 2 монеты", (500, 370), 30)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                        pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)
                    else:
                        pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                        pygame.draw.rect(screen, (150, 50, 0), (500, 400, 250, 50), 1)
                        renderText(screen, "Досвидания", (500, 420), 30)
                    else:
                        pygame.draw.rect(screen, (150, 50, 255), (500, 400, 250, 50), 1)
                        renderText(screen, "Досвидания", (500, 420), 30)

                if uy.type == pygame.MOUSEBUTTONDOWN:
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                        if money >= 5:
                            stuff.append(random.choice(weapons))
                            renderText(screen, "Вы купили: " + stuff[-1][0] + " за 5 монет")
                            money -= 5
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                        if money >= 2:
                            money -= 2
                            hill += 1
                            renderText(screen, "У нас лучшие зелья!")
                    if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                        screen.fill((0, 0, 0))
                        board.render(screen, x, y)
                        runRoom = False
                if uy.type == pygame.KEYDOWN:
                    if uy.key == pygame.K_ESCAPE:
                        screen.fill((0, 0, 0))
                        board.render(screen, x, y)
                        runRoom = False


def ask_room4(screen, coords):
    global hp, maxhp
    rand = random.randint(0, 3)
    if rand == 0:
        renderText(screen, "Ты истинное порождение тьмы! я помогу тебе")
        maxhp += 2
    else:
        renderText(screen, "Вас пронзила тысяча теневых клинков")
        hp -= 4


def ask_room5(screen, coords, id):
    global hp, ticket, lvl, hill
    # подозрительный

    global money, x, y, hill
    pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
    pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)
    renderText(screen, "перевези меня на лодке - 1м", (500, 320), 30)
    renderText(screen, "... бывай", (500, 370), 30)
    runRoom = True
    while runRoom:
        pygame.display.flip()
        for uy in pygame.event.get():
            if uy.type == pygame.QUIT:
                exit()
            if uy.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                board.render(screen, x, y)

                renderText(screen, "перевези меня на лодке - 1м", (500, 320), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)

                renderText(screen, "... бывай", (500, 370), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)

            if uy.type == pygame.MOUSEBUTTONDOWN:
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    if money >= 1:
                        renderText(screen, str("Спасибо! куда плывём?"))
                        money -= 1
                        ticket += 1
                        lvl += 5
                    else:
                        renderText(screen, str("Прочь мошенник! вернись с деньгами"))
                        hill = 0

                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False
                    return
                # if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                #    screen.fill((0, 0, 0))
                #   board.render(screen, x, y)
                #   runRoom = False
            if uy.type == pygame.KEYDOWN:
                if uy.key == pygame.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False


def ask_room6(screen, coords, id):
    global hp
    # подозрительный
    global money, x, y, hill
    pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
    pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
    if map[id[0]][id[1]][1] == -1:
        renderText(screen, "что ты прячешь?", (500, 320), 30)
    elif map[id[0]][id[1]][1] == -2:
        renderText(screen, "это аптечка?", (500, 320), 30)
    renderText(screen, "... бывай", (500, 370), 30)
    runRoom = True
    while runRoom:
        pygame.display.flip()
        for uy in pygame.event.get():
            if uy.type == pygame.QUIT:
                exit()
            if uy.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                board.render(screen, x, y)

                if map[id[0]][id[1]][1] == -1:
                    renderText(screen, "что ты прячешь?", (500, 320), 30)
                elif map[id[0]][id[1]][1] == -2:
                    renderText(screen, "это аптечка?", (500, 320), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)

                renderText(screen, "... бывай", (500, 370), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)

            if uy.type == pygame.MOUSEBUTTONDOWN:
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    if map[id[0]][id[1]][1] == -2:
                        if len(stuff) >= 1:
                            renderText(screen, str("Ваш " + stuff[-1][0] + " был украден!"))
                            stuff.pop(-1)
                            hp = maxhp
                            map[id[0]][id[1]][1] = 0
                    if map[id[0]][id[1]][1] == -1:
                        hp -= 4
                        stuff.append(random.choice(weapons))
                        renderText(screen, str(stuff[-1][0] + " Впился вам в бок забрав 4 хп,"))
                        renderText(screen, "но силуэт исчез, и похоже, теперь оружее ваше", (40, 300))
                        map[id[0]][id[1]][1] = 0
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False
                    return
                # if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                #    screen.fill((0, 0, 0))
                #   board.render(screen, x, y)
                #   runRoom = False
            if uy.type == pygame.KEYDOWN:
                if uy.key == pygame.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False


def renderText(screen, text, coords=False, size1=False, color=(230, 220, 82)):
    if size1:
        font = pygame.font.Font(None, int(size1))
    else:
        font = pygame.font.Font(None, 50)
    line = font.render(text, True, color)
    line_rect = line.get_rect()
    line_rect.top = size[1] / 2 - 100
    line_rect.left = size[0] / 2 - line_rect.width / 2
    if coords:
        line_rect.top = coords[1]
        line_rect.left = coords[0]
        if not size1:
            pygame.draw.rect(screen, (255, 0, 0), (*coords, line_rect.width + 20, line_rect.height + 10))
    else:
        fonText = pygame.transform.scale(load_image("TextFon.png", -1), (line_rect.width + 300, 100))
        screen.blit(fonText, (line_rect.x - 150, line_rect.y - 30))
        # pygame.draw.rect(screen, (255, 0, 0), (line_rect.x - 10, line_rect.y, line_rect.width + 20, line_rect.height + 10))
    screen.blit(line, line_rect)


def ask_room7(screen, coords, id):
    global maxhp, lvl
    wait()
    rand = random.randint(0, 5)
    map[id[0]][id[1]][1] += 1
    if rand == 0:
        renderText(screen, str("Вы потянули лодыжку -1 ур "))
        lvl -= 1
    else:
        maxhp += 1
        renderText(screen, str("Ваш максимальный хп теперь " + str(maxhp)))


def ask_room8(screen, coords, id):
    global coordinat
    global x
    global y
    global t
    global t1
    global c1
    global x1
    global y1
    c1 = True
    c = random.choice(list(coordinat.keys()))
    print(coordinat)
    x = coordinat[c][1]
    y = coordinat[c][0]
    t = coordinat[c][3]
    t1 = coordinat[c][2]
    x1 = coordinat[c][3]
    y1 = coordinat[c][2]

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


def ask_room10(screen, coords, id):
    global hp, bonus_def, bonus_dam
    renderText(screen, "Вы возносите свои молитвы")
    wait()
    a = random.randint(0, 2)
    if a == 0:
        renderText(screen, "Ты чувствуешь как раны начинают затягиваться")
        hp += 5
    elif a == 1:
        renderText(screen, "невидимый щит защищает тебя")
        bonus_def = 5
    elif a == 2:
        renderText(screen, "Ты чувствуешь невероятную силу")
        bonus_dam = 5
    map[id[0]][id[1]][1] = 0


def ask_room11(screen, id):
    if map[id[0]][id[1]][1] == -1:
        renderText(screen, "Получено семечно солнечника")
        seeds["солнечник"] += 1
    elif map[id[0]][id[1]][1] == -2:
        renderText(screen, "Получено семечно ведьминого стебля")
        seeds["ведьмин стебель"] += 1
    elif map[id[0]][id[1]][1] == -3:
        renderText(screen, "Получено семечно хрустальника")
        seeds["хрустальник"] += 1
    map[id[0]][id[1]][1] = 0


def ask_room13(screen):
    global hp, lvl
    hp -= 1
    lvl += 3
    renderText(screen, "В тебя попал дротик")


def ask_room14(screen):
    global hp, ticket, lvl, hill
    # подозрительный

    global money, x, y, hill
    pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)
    pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)
    renderText(screen, "Cварить", (500, 320), 30)
    renderText(screen, "Выйти", (500, 370), 30)
    runRoom = True
    while runRoom:
        pygame.draw.rect(screen, (150, 50, 0), (200, 550, 150, 150), 1)
        pygame.draw.rect(screen, (150, 50, 0), (400, 550, 150, 150), 1)
        pygame.draw.rect(screen, (150, 50, 0), (600, 550, 150, 150), 1)
        if seeds["солнечник"] >= 1:
            screen.blit(pygame.transform.scale(load_image("s1.png", -1), (100, 100)), (220, 550))
        if seeds["ведьмин стебель"] >= 1:
            screen.blit(pygame.transform.scale(load_image("s2.png", -1), (100, 100)), (420, 550))
        if seeds["хрустальник"] >= 1:
            screen.blit(pygame.transform.scale(load_image("s3.png", -1), (100, 100)), (620, 550))
        pygame.display.flip()
        for uy in pygame.event.get():
            if uy.type == pygame.QUIT:
                exit()
            if uy.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                board.render(screen, x, y)

                renderText(screen, "Сварить", (500, 320), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 300, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 300, 250, 50), 1)

                renderText(screen, "Выйти", (500, 370), 30)
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    pygame.draw.rect(screen, (150, 50, 255), (500, 350, 250, 50), 1)
                else:
                    pygame.draw.rect(screen, (150, 50, 0), (500, 350, 250, 50), 1)

            if uy.type == pygame.MOUSEBUTTONDOWN:
                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(300, 350):
                    if seeds["солнечник"] >= 1 and seeds["ведьмин стебель"] >= 1 and seeds["хрустальник"] >= 1:
                        seeds["солнечник"] -= 1
                        seeds["ведьмин стебель"] -= 1
                        seeds["хрустальник"] -= 1
                        renderText(screen, str("Ммм выглядит... особенно.."))
                        lvl += 5
                    else:
                        renderText(screen, str("Не хватает семян!"))

                if uy.pos[0] in range(500, 750) and uy.pos[1] in range(350, 400):
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False
                    return
                # if uy.pos[0] in range(500, 750) and uy.pos[1] in range(400, 450):
                #    screen.fill((0, 0, 0))
                #   board.render(screen, x, y)
                #   runRoom = False
            if uy.type == pygame.KEYDOWN:
                if uy.key == pygame.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    board.render(screen, x, y)
                    runRoom = False


def start(screen, size, position=False):
    global focus
    startImage = pygame.transform.scale(load_image("ss.gif"), (800, 700))
    screen.blit(startImage, (0, 0))
    startImage = pygame.transform.scale(load_image("logo.png", -1), (400, 300))
    w = startImage.get_width()
    h = startImage.get_height()
    screen.blit(startImage, (size[0] / 2 - w / 2, size[0] / 2 - h / 2))
    if position:
        if position[0] in range(300, 500) and \
                position[1] in range(470, 600):
            startImage = pygame.transform.scale(load_image("btnStart2.png", -1), (220, 180))
            if not focus:
                click.play()
                focus = True
        else:
            startImage = pygame.transform.scale(load_image("btnStart.png", -1), (200, 160))
            focus = False
    else:
        startImage = pygame.transform.scale(load_image("btnStart.png", -1), (200, 160))
        focus = False
    w = startImage.get_width()
    h = startImage.get_height()
    screen.blit(startImage, (size[0] / 2 - w / 2, size[0] / 2 - h / 2 + 150))


focus = False


def wait():
    timer = pygame.time.Clock()
    for _ in range(13):
        pygame.draw.circle(screen, (255, 255, 255), (100 + 50 * _, 400), 25)
        pygame.display.flip()
        timer.tick(4)
    screen.fill((0, 0, 0))
    board.render(screen, x, y)


def dethscreen(screen, size, position=False):
    global focus
    startImage = pygame.transform.scale(load_image("bones.png", -1), (400, 300))
    w = startImage.get_width()
    h = startImage.get_height()
    screen.blit(startImage, (size[0] / 2 - w / 2 - 200, size[0] / 2 - h / 2))
    startImage = pygame.transform.scale(load_image("bones.png", -1), (400, 300))
    w = startImage.get_width()
    h = startImage.get_height()
    screen.blit(startImage, (size[0] / 2 - w / 2 + 200, size[0] / 2 - h / 2))
    if position:
        if position[0] in range(300, 500) and \
                position[1] in range(470, 600):
            startImage = pygame.transform.scale(load_image("btnReStart2.png", -1), (220, 180))
            if not focus:
                click.play()
                focus = True
        else:
            startImage = pygame.transform.scale(load_image("btnReStart.png", -1), (200, 160))
            focus = False
    else:
        startImage = pygame.transform.scale(load_image("btnReStart.png", -1), (200, 160))
        focus = False
    w = startImage.get_width()
    h = startImage.get_height()
    screen.blit(startImage, (size[0] / 2 - w / 2, size[0] / 2 - h / 2 + 150))


# sd
def deth():
    global maxhp, hp, ex, lvl, hill, ticket, stuff, money
    ex = False
    while True:
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                dethscreen(screen, size)
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEMOTION:
                dethscreen(screen, size, i.pos)
            elif i.type == pygame.MOUSEBUTTONDOWN:
                position = i.pos
                if position[0] in range(300, 500) and \
                        position[1] in range(470, 600):
                    ex = True

        if ex:
            break
    maxhp = 10
    hp = maxhp
    stuff = []
    money = 0
    lvl = 10
    hill = 0
    ticket = 0


def ask_room12(screen):
    timer = pygame.time.Clock
    global transition
    transition = True


class Dungeon:
    def __init__(self, width, height):
        global map
        self.width = width
        self.height = height
        self.map = [
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
             [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]
        map = self.map
        self.cor = [9, 10]
        self.colekt_room = {}

    def render(self, screen, x1, y1, booss=False):
        global hp, lvl, hill, maxhp, lvl_hp
        global t
        global t1
        global money
        global n
        global hp_boos
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

        image = pygame.transform.scale(load_image("door.png", -1), (100, 100))
        if booss:
            screen.blit(image, [self.colekt_room[self.id_exit][0] - x1 - 200, self.colekt_room[self.id_exit][1] - y1])
        else:
            screen.blit(image, [self.colekt_room[self.id_exit][0] - x1, self.colekt_room[self.id_exit][1] - y1])
        self.map[self.colekt_room[self.id_exit][-1][0]][self.colekt_room[self.id_exit][-1][1]] = [32, 1]
        if self.id_exit == 50 and n:
            image = pygame.transform.scale(load_image("Boss.png", -1), (150 * 3, 150 * 3))
            screen.blit(image,
                        [self.colekt_room[self.id_exit][0] - x1 - 1650, self.colekt_room[self.id_exit][1] - y1 - 150])
        y22 = 60
        if invent:
            screen.blit(pygame.transform.scale(load_image("inventory.png", -1), (200, 300)), (0, 0))
            for i in stuff:
                renderText(screen, i[0], (30, y22), 50, (0, 0, 0))
                y22 += 30
        else:
            screen.blit(pygame.transform.scale(load_image("inventory.png", -1), (200, 300)), (0, -250))
        screen.blit(pygame.transform.scale(load_image("money.png", -1), (120, 100)), (200, 0))
        renderText(screen, str(money), (250, 40), 40)
        screen.blit(pygame.transform.scale(load_image("hill.png", -1), (100, 100)), (300, 0))
        renderText(screen, str(hill), (340, 40), 40)
        if t == 10 and t1 == 10 and n:
            n = False
            ask_room2(screen, (t, t1), hp_boos, 1, False)
        maxhp = maxhp - lvl_hp
        lvl_hp = lvl // 10
        maxhp += lvl_hp
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, int(size[0] / 10 * (lvl % 10)), 3))
        renderText(screen, str(lvl // 10), (size[0] - 70, 0), 40)
        if hp > maxhp:
            hp = maxhp
        if lvl < 0:
            lvl = 0
        damage = 0
        for i in stuff:
            damage += i[1]
        screen.blit(pygame.transform.scale(load_image("def.png", -1), (50, 70)), (size[0] - 50, size[1] - 100))
        renderText(screen, str(bonus_def), (size[0] - 70, size[1] - 100), 50)
        screen.blit(pygame.transform.scale(load_image("sword.png", -1), (50, 70)), (size[0] - 50, size[1] - 200))
        renderText(screen, str(bonus_dam + damage), (size[0] - 70, size[1] - 200), 50)

    def render_fight(self, screen, x1, y1, maxhp_monstor, hp_monstor, pobag):
        pygame.draw.rect(screen, (255, 255, 255),
                         (770, maxhp1, 15, maxhp * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (770, hp1, 15, hp * 10))
        pygame.draw.rect(screen, (255, 255, 255),
                         (10, 10, 15, maxhp_monstor * 10))
        pygame.draw.rect(screen, (255, 0, 0),
                         (10, 10, 15, hp_monstor * 10))
        font = pygame.font.Font(None, 50)

    def render_fight_1(self, screen, x1, y1, col, maxhp_monstor, hp_monstor, flag):
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
        if flag:
            col -= 2
        else:
            col += 2
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
                self.cor1[0] = 2
            if self.cor1[1] > 20:
                self.cor1[1] = 18
            # for ig in map:
            #    for ad in ig:
            #        print("*" if ad[0] else ".", end="")
            #    print()

            if len(self.map[self.cor1[0] + 1][self.cor1[1]]) == 2:
                if self.map[self.cor1[0] + 1][self.cor1[1]][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0] - 1][self.cor1[1]]) == 2:
                if self.map[self.cor1[0] - 1][self.cor1[1]][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0]][self.cor1[1] + 1]) == 2:
                if self.map[self.cor1[0]][self.cor1[1] + 1][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0]][self.cor1[1] - 1]) == 2:
                if self.map[self.cor1[0]][self.cor1[1] - 1][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0] + 1][self.cor1[1] - 1]) == 2:
                if self.map[self.cor1[0] + 1][self.cor1[1] - 1][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0] - 1][self.cor1[1] + 1]) == 2:
                if self.map[self.cor1[0] - 1][self.cor1[1] + 1][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0] + 1][self.cor1[1] + 1]) == 2:
                if self.map[self.cor1[0] + 1][self.cor1[1] + 1][0]:
                    col_sos += 1
            if len(self.map[self.cor1[0] - 1][self.cor1[1] - 1]) == 2:
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

    def boos(self):
        global map
        map = map_boos
        self.map = map_boos


pygame.init()
bonus_power = 0
lvl_hp = 0
size = 800, 700
n = False
screen = pygame.display.set_mode((size))
floor = 1
invent = False  # открыт или закрыт инвентарь
start(screen, size)
ex = False
click = pygame.mixer.Sound("data/click.mp3")
tap = pygame.mixer.Sound("data/tap.mp3")
mainTheme = pygame.mixer.Sound("data/enchantment.ogg")
battleTheme = pygame.mixer.Sound("data\RudeBuster.mp3")
hallo = pygame.mixer.Sound("data\hallo.mp3")
hallo.play(loops=600)
hp_boos = 0
bonus_def = 0
bonus_dam = 0
c1 = False
map_boos = [
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
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1, 6], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]
while True:
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEMOTION:
            start(screen, size, i.pos)
        elif i.type == pygame.MOUSEBUTTONDOWN:
            position = i.pos
            if position[0] in range(300, 500) and \
                    position[1] in range(470, 600):
                ex = True

    if ex:
        break
mainTheme.play(loops=600)
im = pygame.transform.scale(load_image('heroImage.png', -1), (250, 100))
heroImage = []
floorImage = []
for i in range(4):
    rect = pygame.Rect(0, 0, im.get_width() // 4, im.get_height())
    frame_location = (rect.w * i, 0)
    heroImage.append(im.subsurface(pygame.Rect(frame_location, rect.size)))
pers = 1
if pers == 1:
    dog_surf = heroImage[0]
else:
    dog_surf = pygame.transform.scale(load_image('Седнев.jpg', -1), (100, 100))
im = pygame.transform.scale(load_image('flor.png', -1), (800, 800))
for i in range(4):
    for j in range(4):
        rect = pygame.Rect(0, 0, im.get_width() // 4,
                           im.get_height() // 4)
        frame_location = (rect.w * j, rect.h * i)
        floorImage.append(im.subsurface(pygame.Rect(frame_location, rect.size)))
hallo.stop()
monsters = []
mNames = ["m0.png", "m1.png", "m2.png", "m3.png", "m4.png", "m5.png", 'Boss.png']
for i in mNames:
    monsters.append(pygame.transform.scale(load_image(i, -1), (100, 100)))
while floor != 60:
    board = Dungeon(20, 20)
    karta = pygame.display.set_mode((size))
    x = 1475
    y = 1675
    hp_boos += 2
    if floor % 6 == 0:
        board.generation()
        board.boos()
        board.id_exit = 50
        board.colekt_room[50] = [19 * 200 + 25, 10 * 200 + 25, [18, 10]]
        n = True
    else:
        board.generation()
    coordinat = {}
    y_1 = 0
    h = 0
    for i in map:
        x_1 = 0
        for j in i:
            if len(map[y_1][x_1]) == 2:
                h += 1
                coordinat[h] = [200 * x_1 + 75 - 400, 200 * y_1 + 75 - 400, x_1, y_1]
            x_1 += 1
        y_1 += 1
    t = 9
    t1 = 10
    z = 500
    transition = False
    x1, y1 = 9, 10
    if floor % 6 == 0:
        board.render(screen, x, y, True)
    else:
        board.render(screen, x, y)
    while True:
        if c1:
            screen.fill((0, 0, 0))
            board.render(screen, x, y)
            c1 = False
        for event in pygame.event.get():
            water = False
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if map[x1][y1][0] == 5:
                        water = True
                    if pers:
                        dog_surf = heroImage[3]
                    t1 -= 1
                    tap.play()
                    if board.map[t][t1][0]:
                        y -= 200
                        y1 -= 1
                    else:
                        t1 += 1
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
                    if map[x1][y1][0] == 5:
                        renderText(screen, "Потоп! надо спасаться!")
                    if water:
                        if ticket >= 1:
                            ticket -= 1
                        else:
                            if hill >= 1:
                                hill -= 1
                                renderText(screen, "Уплывая вы обронили зелье!")
                            else:
                                renderText(screen, "вы без проблем уплыли")
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if map[x1][y1][0] == 5:
                        water = True
                    if pers:
                        dog_surf = heroImage[1]
                    tap.play()
                    t1 += 1
                    if board.map[t][t1][0]:
                        y += 200
                        y1 += 1
                    else:
                        t1 -= 1
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
                    if map[x1][y1][0] == 5:
                        renderText(screen, "Потоп! надо спасаться!")
                    if water:
                        if ticket >= 1:
                            ticket -= 1
                        else:
                            if hill >= 1:
                                hill -= 1
                                renderText(screen, "Уплывая вы обронили зелье!")
                            else:
                                renderText(screen, "вы без проблем уплыли")
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if map[x1][y1][0] == 5:
                        water = True
                    if pers:
                        dog_surf = heroImage[2]
                    tap.play()
                    t -= 1
                    if board.map[t][t1][0]:
                        x -= 200
                        x1 -= 1
                    else:
                        t += 1
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
                    if map[x1][y1][0] == 5:
                        renderText(screen, "Потоп! надо спасаться!")
                    if water:
                        if ticket >= 1:
                            ticket -= 1
                        else:
                            if hill >= 1:
                                hill -= 1
                                renderText(screen, "Уплывая вы обронили зелье!")
                            else:
                                renderText(screen, "вы без проблем уплыли")
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if map[x1][y1][0] == 5:
                        water = True
                    if pers:
                        dog_surf = heroImage[0]
                    tap.play()
                    t += 1
                    if board.map[t][t1][0]:
                        x += 200
                        x1 += 1
                    else:
                        t -= 1
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
                    if map[x1][y1][0] == 5:
                        renderText(screen, "Потоп! надо спасаться!")
                    if water:
                        if ticket >= 1:
                            ticket -= 1
                        else:
                            if hill >= 1:
                                hill -= 1
                                renderText(screen, "Уплывая вы обронили зелье!")
                            else:
                                renderText(screen, "вы без проблем уплыли")
                if event.key == pygame.K_z:
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
                    ask_room(screen, (600, 600), (x1, y1))
                elif map[x1][y1][0] == 2 or map[x1][y1][0] == 13:
                    ask_room(screen, (600, 600), (x1, y1))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    exit()
                if event.key == pygame.K_q:
                    if hill >= 1:
                        hill -= 1
                        hp += 3
                if event.key == pygame.K_c:
                    if pers:
                        pers = 0
                        dog_surf = pygame.transform.scale(load_image('Седнев.jpg', -1), (100, 100))
                    else:
                        pers = 1
                if event.key == pygame.K_k:
                    bonus_def = 5
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(0, 200) and event.pos[1] in range(0, 50):
                    if invent:
                        invent = False
                    else:
                        invent = True
                    screen.fill((0, 0, 0))
                    if floor % 6 == 0:
                        board.render(screen, x, y, True)
                    else:
                        board.render(screen, x, y)
        bonus_power = sum([i[1] for i in stuff])
        if hp <= 0:
            deth()
            floor = 0
            board = Dungeon(20, 20)
            karta = pygame.display.set_mode((size))
            x = 1475
            y = 1675
            board.generation()
            t = 9
            t1 = 10
            z = 500
            transition = False
            x1, y1 = 9, 10
            if floor % 6 == 0:
                board.render(screen, x, y, True)
            else:
                board.render(screen, x, y)
        if transition:
            floor += 1
            transition = False
            break
        dog_rect = dog_surf.get_rect(bottomright=(z, z))
        screen.blit(dog_surf, dog_rect)
        pygame.display.flip()
