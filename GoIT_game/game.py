from random import randint

SIZE_X = randint(5, 10)
SIZE_Y = randint(5, 10)

char_x = randint(0, SIZE_X - 1)
char_y = randint(0, SIZE_Y - 1)
char_sing = 'X'

portal_x = randint(0, SIZE_X - 1)
portal_y = randint(0, SIZE_Y - 1)
portal_sing = 'O'

turns = 0

while True:
    world_map = ''

    win_condition = char_x == portal_x and char_y == portal_y

    if win_condition:
        char_sing = 'W'

    for y in range(SIZE_Y):
        row = '|'
        for x in range(SIZE_X):

            if char_x == x and char_y == y:
                row += f'{char_sing}|'
            elif portal_x == x and portal_y == y:
                row += f'{portal_sing}|'
            else:
                row += ' |'
        world_map += f'{row}\n'

    print(world_map)

    if win_condition:
        print(f'You WIN in {turns} turns!')
        break

    direction = input('Enter direction (w / s / a / d): ')

    if direction == 'w' and char_y > 0:
        char_y -= 1
    elif direction == 's' and char_y < SIZE_Y - 1:
        char_y += 1
    elif direction == 'a' and char_x > 0:
        char_x -= 1
    elif direction == 'd' and char_x < SIZE_X - 1:
        char_x += 1

    turns +=1