input_file = 'input.txt'
# input_file = 'test.txt'
# input_file = 'test2.txt'

tiles = []
with open(input_file) as f:
    for line in f:
        tiles.append(list(line.strip()))

def find_start(lst):
    for y, row in enumerate(lst):
        for x, value in enumerate(row):
            if value == 'S':
                return x, y

x, y = find_start(tiles)
prev_x = x
prev_y = y
y = y + 1
steps = 0
while True:
    steps += 1
    pipe = tiles[y][x]
    if pipe == 'S':
        break
    elif pipe == '|':
        if prev_y < y:
            prev_x = x
            prev_y = y
            y += 1
        else:
            prev_x = x
            prev_y = y
            y -= 1
    elif pipe == '-':
        if prev_x < x:
            prev_x = x
            prev_y = y
            x += 1
        else:
            prev_x = x
            prev_y = y
            x -= 1
    elif pipe == 'L':
        if prev_y < y:
            prev_x = x
            prev_y = y
            x += 1
        else:
            prev_x = x
            prev_y = y
            y -= 1
    elif pipe == 'J':
        if prev_y < y:
            prev_x = x
            prev_y = y
            x -= 1
        else:
            prev_x = x
            prev_y = y
            y -= 1
    elif pipe == '7':
        if prev_x < x:
            prev_x = x
            prev_y = y
            y += 1
        else:
            prev_x = x
            prev_y = y
            x -= 1
    elif pipe == 'F':
        if prev_x > x:
            prev_x = x
            prev_y = y
            y += 1
        else:
            prev_x = x
            prev_y = y
            x += 1
    else:
        print("FEEEEL")
        break

print("Part 1:", steps/2)
