import re

input_file = 'input.txt'
# input_file = 'test.txt'

ans = 0
numbers = []
winning_numbers = []
cards = []
with open(input_file) as f:
    for line in f:
        tmp = line.strip().split(':')
        all_numbers = tmp[1].split('|')
        winning_numbers.append([int(s) for s in all_numbers[0].split()])
        numbers.append([int(s) for s in all_numbers[1].split()])
        cards.append(1)

for i in range(len(numbers)):
    winnings = 0
    copies = cards[i]
    for num in numbers[i]:
        if (winning_numbers[i].count(num) > 0):
            winnings += 1
            cards[i+winnings] += (1 * copies)
    if winnings > 1:
        ans += 2 ** (winnings - 1)
    else:
        ans += winnings

print("Part 1:", ans)
print("Part 2:",sum(cards))
