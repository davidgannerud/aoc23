import re

input_file = 'input.txt'
# input_file = 'test.txt'

hash_steps = []
with open(input_file) as f:
    for line in f:
        hash_steps = line.strip().split(',')

hashes = []
for hash in hash_steps:
    part_sum = 0
    for c in hash:
        part_sum += ord(c)
        part_sum *= 17
        part_sum %= 256
    hashes.append(part_sum)

print("Part 1:", sum(hashes))
