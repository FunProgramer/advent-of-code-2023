# wrong answer, but seems to work as expected up to line 3 (line_idx=2) number: 667 (number_idx: 57)
# every line in the "engine schematic" (-> the puzzle input) has 141 characters
LINE_LENGTH = 141
# the "engine schematic" has 140 lines
NUMBER_OF_LINES = 140

input_lines = []


def is_part_number(line_idx: int, number_idx: int, number_length: int):
    if number_idx != 0:
        if is_part_marker(input_lines[line_idx][number_idx - 1]):
            return True
        if line_idx != 0:
            if is_part_marker(input_lines[line_idx - 1][number_idx - 1]):
                return True
        if line_idx != NUMBER_OF_LINES - 1:
            if is_part_marker(input_lines[line_idx + 1][number_idx - 1]):
                return True
    if number_idx + number_length != LINE_LENGTH - 1:
        if is_part_marker(input_lines[line_idx][number_idx + number_length]):
            return True
        if line_idx != 0:
            if is_part_marker(input_lines[line_idx - 1][number_idx + number_length]):
                return True
        if line_idx != NUMBER_OF_LINES - 1:
            if is_part_marker(input_lines[line_idx + 1][number_idx + number_length]):
                return True
    if line_idx != 0:
        for idx in range(number_idx, number_idx + number_length):
            if is_part_marker(input_lines[line_idx - 1][idx]):
                return True
    if line_idx != NUMBER_OF_LINES - 1:
        for idx in range(number_idx, number_idx + number_length):
            if is_part_marker(input_lines[line_idx + 1][idx]):
                return True

    return False


# Part Marker refers all symbols except the '.'.
# As stated in the puzzle any number that is in any way adjacent to one of these symbols is a part number.
def is_part_marker(adjacent_char: str):
    return not adjacent_char.isdigit() and adjacent_char != "."


def main():
    with open("day3_input.txt", "r") as input_file:
        input_string = input_file.read()

    global input_lines
    input_lines = input_string.splitlines()
    part_numbers_sum: int = 0

    for line_idx, line in enumerate(input_lines):
        number: str = ""
        number_idx: int | None = None
        for char_idx, char in enumerate(line):
            if char.isdigit():
                number += char
                if not number_idx:
                    number_idx = char_idx
            elif number_idx:
                if is_part_number(line_idx, number_idx, len(number)):
                    part_numbers_sum += int(number)
                number = ""
                number_idx = None

    print("Sum of part numbers:", part_numbers_sum)


if __name__ == '__main__':
    main()
