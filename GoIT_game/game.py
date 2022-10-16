from random import randint, choice

SIZE_X = randint(5, 10)
SIZE_Y = randint(5, 10)


def check_state(char_x, char_y, char_sing_def,
                enemy_x, enemy_y,
                portal_x, portal_y):

    win_condition = char_x == portal_x and char_y == portal_y
    loss_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sing_def = 'W'
        print(f'You WIN in {turns} turns!')
    elif loss_condition:
        char_sing_def = '#'
        print(f'You LOST in {turns} turns!')

    return char_sing_def, win_condition or loss_condition


def generate_map(char_x, char_y, char_sing,
                 enemy_x, enemy_y, enemy_sing,
                 portal_x, portal_y, portal_sing,
                 size_x=SIZE_X, size_y=SIZE_Y):
    world_map_def = ''
    for y in range(size_y):
        row = '|'
        for x in range(size_x):

            if char_x == x and char_y == y:
                row += f'{char_sing}|'
            elif enemy_x == x and enemy_y == y:
                row += f'{enemy_sing}|'
            elif portal_x == x and portal_y == y:
                row += f'{portal_sing}|'
            else:
                row += ' |'
        world_map_def += f'{row}\n'
    return world_map_def


def move(direction, x, y, size_x=SIZE_X, size_y=SIZE_Y):
    if direction == 'w' and y > 0:
        y -= 1
    elif direction == 's' and y < size_y - 1:
        y += 1
    elif direction == 'a' and x > 0:
        x -= 1
    elif direction == 'd' and x < size_x - 1:
        x += 1
    return x, y


char_x = randint(0, SIZE_X - 1)
char_y = randint(0, SIZE_Y - 1)
char_sing = 'X'

enemy_x = randint(0, SIZE_X - 1)
enemy_y = randint(0, SIZE_Y - 1)
enemy_sing = '@'

portal_x = randint(0, SIZE_X - 1)
portal_y = randint(0, SIZE_Y - 1)
portal_sing = 'O'

turns = 0

while True:
    char_sing, end_flag = check_state(char_x, char_y, char_sing,
                            enemy_x, enemy_y,
                            portal_x, portal_y)

    world_map = generate_map(char_x, char_y, char_sing,
                             enemy_x, enemy_y, enemy_sing,
                             portal_x, portal_y, portal_sing)

    print(world_map)

    if end_flag:
        break

    direction = input('Enter direction (w / s / a / d): ')
    char_x, char_y = move(direction, char_x, char_y)
    direction_enemy = choice('wsad')
    enemy_x, enemy_y = move(direction_enemy, enemy_x, enemy_y)

    turns += 1
