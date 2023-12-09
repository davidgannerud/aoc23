import re

input_file = 'input.txt'
# input_file = 'test2.txt'

def create_dict(input_string):
    match = re.match(r'(\w+)\s*=\s*\(([\w, ]+)\)', input_string)

    key = match.group(1)
    values = [value.strip() for value in match.group(2).split(',')]
    
    return {key: values}

map = {}
instructions = ''
with open(input_file) as f:
    instructions = f.readline().strip()
    dummy = f.readline().strip()
    for lines in f:
        map.update(create_dict(lines.strip()))

steps = 0
position = 'AAA'
searching = True
while searching:
    for c in instructions:
        index = 0
        if (c == 'R'):
            index = 1
        
        if position == 'ZZZ':
            searching = False
            break

        position = map.get(position)[index]
        steps += 1

print("Part 1:", steps)
