input_file = 'input.txt'
# input_file = 'test.txt'

def count_equal_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    equal_characters = {char: count for char, count in char_count.items() if count > 1}
    
    return equal_characters

sum = 0
cards = []
with open(input_file) as f:
    for lines in f:
        cards.append(lines.strip().replace('A','Z').replace('K','Y').replace('T','E').split())

i = 0
for hand in cards:
    value = count_equal_characters(hand[0])

    rank = 1
    if len(value) == 1:
        score = list(value.values())[0]
        if score == 5:
            rank = 7
        elif score == 4:
            rank = 6
        elif score == 3:
            rank = 4
        elif score == 2:
            rank = 2
    elif len(value) == 2:
        pair1 = list(value.values())[0]
        pair2 = list(value.values())[1]
        if pair1 == pair2:
            rank = 3
        else:
            rank = 5

    cards[i].append(rank)
    i += 1

sorted_cards = sorted(cards, key=lambda x: (x[2], x[0]))

for i in range(len(sorted_cards)):
    sum += int(sorted_cards[i][1]) * (i + 1)

print("Part 1:", sum)
#################################################################

i = 0
for hand in cards:
    value = count_equal_characters(hand[0])

    jokers = hand[0].count('J')
    if jokers > 1:
        del value['J']

    rank = 1
    num_of_pairs = len(value)
    if num_of_pairs == 0:
        score = 1 + jokers
        if score >= 5:
            rank = 7
        elif score == 4:
            rank = 6
        elif score == 3:
            rank = 4
        elif score == 2:
            rank = 2
    else:
        if jokers > 1:
            num_of_pairs = 1

        if num_of_pairs == 1:
            score = list(value.values())[0] + jokers
            if score == 5:
                rank = 7
            elif score == 4:
                rank = 6
            elif score == 3:
                rank = 4
            elif score == 2:
                rank = 2
            elif score == 1:
                rank = 2
            else:
                rank = 7
        elif num_of_pairs == 2:
            pair1 = list(value.values())[0] + jokers
            pair2 = list(value.values())[1]
            if pair1 == pair2:
                rank = 3
            else:
                rank = 5
    
    cards[i].append(rank)
    i += 1

for i in range(len(cards)):
    cards[i][0] = cards[i][0].replace('J','1')

sorted_cards = sorted(cards, key=lambda x: (x[3], x[0]))

sum = 0
for i in range(len(sorted_cards)):
    sum += int(sorted_cards[i][1]) * (i + 1)

print("Part 2:",sum)