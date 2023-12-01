input_file = 'input.txt'
# input_file = 'test.txt'

sum = 0

with open(input_file) as f:
    for line in f:
        line = line.strip()
        first_digit = ""
        last_digit = ""
        last_digit_index = 0
        for i, c in enumerate(line):
            if c.isdigit():
                if first_digit == "":
                    first_digit = c
                    last_digit = c
                
                if last_digit_index < i:
                    last_digit = c
        print(first_digit+last_digit)
        sum += int(first_digit+last_digit)
        print(sum)
