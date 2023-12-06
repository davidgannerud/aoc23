input_file = 'input.txt'
# input_file = 'test.txt'

sum = 1

with open(input_file) as f:
    race_times = [int(s) for s in f.readline().strip()[10:].split()]
    records = [int(s) for s in f.readline().strip()[10:].split()]

    for i in range(len(race_times)):
        race_sum = 0
        for time in range(race_times[i]):
            race_time = time * (race_times[i] - time)
            if race_time > records[i]:
                race_sum +=1
        if race_sum > 0:
            sum *= race_sum

print("Part 1:", sum)

sum = 0
with open(input_file) as f:
    race_times = int(f.readline().strip()[10:].replace(" ", ""))
    records = int(f.readline().strip()[10:].replace(" ", ""))

    for time in range(race_times):
        race_sum = 0
        race_time = time * (race_times - time)
        if race_time > records:
            race_sum +=1
        if race_sum > 0:
            sum += 1

print("Part 2:",sum)
