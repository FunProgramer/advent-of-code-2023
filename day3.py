input_lines = []


def is_part_number(line_idx: int, number_idx: int, number_length: int):
    for x in range(line_idx - 1, line_idx + 2):
        for y in range(number_idx - 1, number_idx + number_length + 1):
            try:
                if not input_lines[x][y].isdigit() and input_lines[x][y] != ".":
                    return True
            except IndexError:
                pass

    # if number_idx != 0:
    #     if is_part_marker(input_lines[line_idx][number_idx - 1]):
    #         return True
    #     if line_idx != 0:
    #         if is_part_marker(input_lines[line_idx - 1][number_idx - 1]):
    #             return True
    #     if line_idx != NUMBER_OF_LINES - 1:
    #         if is_part_marker(input_lines[line_idx + 1][number_idx - 1]):
    #             return True
    # if number_idx + number_length != LINE_LENGTH - 1:
    #     if is_part_marker(input_lines[line_idx][number_idx + number_length]):
    #         return True
    #     if line_idx != 0:
    #         if is_part_marker(input_lines[line_idx - 1][number_idx + number_length]):
    #             return True
    #     if line_idx != NUMBER_OF_LINES - 1:
    #         if is_part_marker(input_lines[line_idx + 1][number_idx + number_length]):
    #             return True
    # if line_idx != 0:
    #     for idx in range(number_idx, number_idx + number_length):
    #         if is_part_marker(input_lines[line_idx - 1][idx]):
    #             return True
    # if line_idx != NUMBER_OF_LINES - 1:
    #     for idx in range(number_idx, number_idx + number_length):
    #         if is_part_marker(input_lines[line_idx + 1][idx]):
    #             return True

    return False


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
                if number_idx is None:
                    number_idx = char_idx
            elif number_idx is not None:
                if is_part_number(line_idx, number_idx, len(number)):
                    part_numbers_sum += int(number)
                number = ""
                number_idx = None
        if number_idx is not None:
            if is_part_number(line_idx, number_idx, len(number)):
                part_numbers_sum += int(number)

    print("Sum of part numbers:", part_numbers_sum)


if __name__ == '__main__':
    main()
