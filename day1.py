with open("day1_input.txt", "r") as input_file:
    input_string = input_file.read()

input_lines = input_string.splitlines()

digit_lines = []
for line_i in range(len(input_lines)):
    digit_lines.append([])
    for char in input_lines[line_i]:
        if char.isdigit():
            digit_lines[line_i].append(char)

calibration_values_sum = 0

for line in digit_lines:
    if len(line) < 1:
        print(line)
    first_digit = line[0]
    last_digit = line[len(line) - 1]
    number = int(first_digit + last_digit)
    calibration_values_sum += number

print("Sum of calibration values: ", calibration_values_sum)
