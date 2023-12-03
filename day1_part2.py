# This draft is not the solution (it does not work)
with open("day1_input.txt", "r") as input_file:
    input_string = input_file.read()

input_lines = input_string.splitlines()

number_words_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

calibration_values_sum = 0

for line_idx, line in enumerate(input_lines):
    first_idx = None
    first_digit = None
    last_idx = None
    last_digit = None
    for number_word in number_words_dict.keys():
        number_word_idx = line.find(number_word)
        if number_word_idx != -1:
            if first_idx is None:
                first_idx = number_word_idx
                first_digit = number_words_dict[number_word]
            elif number_word_idx < first_idx:
                if last_idx is None:
                    last_idx = first_idx
                    last_digit = first_digit
                first_idx = number_word_idx
                first_digit = number_words_dict[number_word]
            elif last_idx is None:
                last_idx = number_word_idx
                last_digit = number_words_dict[number_word]
            elif number_word_idx > last_idx:
                last_idx = number_word_idx
                last_digit = number_words_dict[number_word]
    for char_idx, char in enumerate(line):
        if char.isdigit():
            if first_idx is None:
                first_idx = char_idx
                first_digit = char
            elif char_idx < first_idx:
                first_idx = char_idx
                first_digit = char
            elif last_idx is None:
                last_idx = char_idx
                last_digit = char
            elif char_idx > last_idx:
                last_idx = char_idx
                last_digit = char

    if last_digit is None:
        last_digit = first_digit
    calibration_value = int(first_digit + last_digit)
    calibration_values_sum += calibration_value

    if line_idx == 20:
        print("line " + str(line_idx + 1) + ": " + line)
        print("first_digit:", first_digit, "idx:", first_idx)
        print("last_digit:", last_digit, "idx:", last_idx)
        print("resulting calibration value:", calibration_value)
        print()


print("Sum of calibration values:", calibration_values_sum)
