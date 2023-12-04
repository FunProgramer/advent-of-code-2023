input_lines = []


def main():
    with open("day3_input.txt", "r") as input_file:
        input_string = input_file.read()

    global input_lines
    input_lines = input_string.splitlines()
    gears = {}

    for line_idx, line in enumerate(input_lines):
        number: str = ""
        number_idx: int | None = None
        for char_idx, char in enumerate(line):
            if char.isdigit():
                number += char
                if number_idx is None:
                    number_idx = char_idx
            elif number_idx is not None:
                for x in range(line_idx - 1, line_idx + 2):
                    for y in range(number_idx - 1, number_idx + len(number) + 1):
                        try:
                            if input_lines[x][y] == "*":
                                key = "{}-{}".format(x, y)
                                if key in gears.keys():
                                    gears[key].append(number)
                                else:
                                    gears[key] = [number]
                        except IndexError:
                            pass
                number = ""
                number_idx = None
        if number_idx is not None:
            for x in range(line_idx - 1, line_idx + 2):
                for y in range(number_idx - 1, number_idx + len(number) + 1):
                    try:
                        if input_lines[x][y] == "*":
                            key = "{}-{}".format(x, y)
                            if key in gears.keys():
                                gears[key].append(number)
                            else:
                                gears[key] = [number]
                    except IndexError:
                        pass

    gear_ratios_sum = 0
    for gear in gears.values():
        gear_ratio = 1
        if len(gear) < 2:  # The thing that is currently represented by 'gear' is not a real gear
            continue
        for number in gear:
            gear_ratio *= int(number)
        gear_ratios_sum += gear_ratio

    print("Sum of gear ratios:", gear_ratios_sum)


if __name__ == '__main__':
    main()
