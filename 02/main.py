import re

input_file = 'input.txt'
# input_file = 'test.txt'

sum = 0
sum2 = 0
index = 0
with open(input_file) as f:
    for line in f:
        index += 1
        line = line.strip()
        red = 0
        green = 0
        blue = 0
        
        game = re.split(': |; |, ', line)
        for color in game:
            if color.find("red") > 0:
                tmp = int(re.findall(r'\d+', color)[0])
                if tmp > red:
                    red = tmp

            if color.find("green") > 0:
                tmp = int(re.findall(r'\d+', color)[0])
                if tmp > green:
                    green = tmp

            if color.find("blue") > 0:
                tmp = int(re.findall(r'\d+', color)[0])
                if tmp > blue:
                    blue = tmp

        if red <= 12 and green <= 13 and blue <= 14:
            sum += index
        sum2 += red * green * blue 

print(sum)
print(sum2)
