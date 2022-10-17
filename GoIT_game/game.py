from random import randint, choice

SIZE_X = randint(7, 15)
SIZE_Y = randint(7, 15)


def check_state(objects_def):
    for obj in objects_def:
        if obj['type'] == 'char':
            char = obj
        elif obj['type'] == 'portal':
            portal = obj
        elif obj['type'] == 'enemy':
            loss_condition = char['x'] == obj['x'] and char['y'] == obj['y']
            if loss_condition:
                char['sing'] = '#'
                print(f'You LOST in {turns} turns!')
                break

    win_condition = char['x'] == portal['x'] and char['y'] == portal['y']

    if win_condition:
        char['sing'] = 'W'
        print(f'You WIN in {turns} turns!')

    return win_condition or loss_condition


def generate_enemies(count):
    enemies = []
    for _ in range(count):
        enemy = {'x': randint(0, SIZE_X - 1),
                 'y': randint(0, SIZE_Y - 1),
                 'sing': '@',
                 'type': 'enemy'}
        enemies.append(enemy)
    return enemies


def generate_map(objects, size_x=SIZE_X, size_y=SIZE_Y):
    world_map = []

    for y in range(size_y):
        row = []

        for x in range(size_x):
            row.append(' ')

        world_map.append(row)

    for obj in objects:
        world_map[obj['y']][obj['x']] = obj['sing']

    return world_map


def move(direction, obj, size_x=SIZE_X, size_y=SIZE_Y):
    if direction == 'w' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 's' and obj['y'] < size_y - 1:
        obj['y'] += 1
    elif direction == 'a' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 'd' and obj['x'] < size_x - 1:
        obj['x'] += 1


def print_map(world_map_def):
    for row in world_map_def:
        print(f'|{"|".join(row)}|')


char = {'x': randint(0, SIZE_X - 1),
        'y': randint(0, SIZE_Y - 1),
        'sing': 'X',
        'type': 'char'}

portal = {'x': randint(0, SIZE_X - 1),
          'y': randint(0, SIZE_Y - 1),
          'sing': 'O',
          'type': 'portal'}

enemies = generate_enemies(5)

objects = [char, portal] + enemies

turns = 0

while True:

    end_flag = check_state(objects)
    world_map = generate_map(objects)
    print_map(world_map)

    if end_flag:
        break

    for obj in objects:
        direction = ''
        if obj['type'] == 'char':
            direction = input('Enter direction (w / s / a / d): ')

        elif obj['type'] == 'enemy':
            direction = choice('wsad')

        move(direction, obj)

    turns += 1
