input_file = 'input.txt'
# input_file = 'test.txt'

report = []
with open(input_file) as f:
    for line in f:
        report.append([int(s) for s in line.strip().split()])

full_report = []
for history in report:
    tmp = []
    row = history
    tmp.append(row)
    while (sum(row) != 0):
        tmp2 = []
        for i in range(len(row) - 1):
            tmp2.append(row[i+1]-row[i])
        tmp.insert(0, tmp2)
        row = tmp2
    full_report.append(tmp)

sum = 0
for part in full_report:
    next = 0
    for i in range(len(part)-1):
        next = next+part[i+1][-1]
    sum += next

print("Part 1:", sum)

sum = 0
for part in full_report:
    next = 0
    for i in range(len(part)-1):
        next = part[i+1][0]-next
    sum += next

print("Part 2:", sum)
