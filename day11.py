def main():
    with open("day11_input.txt", "r") as input_file:
        space_image = input_file.readlines()

    # Specifies if the current block (row or column) was expanded
    expanded = False
    for y, line in enumerate(space_image):
        if expanded:
            expanded = False
            continue
        if '#' not in line:
            space_image.insert(y, line)
            expanded = True

    for x in range(len(space_image[0])):
        is_empty = True
        if expanded:
            expanded = False
            continue
        for y, line in enumerate(space_image):
            if line[x] == '#':
                is_empty = False
                break
        if is_empty:
            for y, line in enumerate(space_image):
                space_image[y] = line[:x] + '.' + line[x:]
                expanded = True

    galaxies = []
    for y, line in enumerate(space_image):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append({"x": x, "y": y})

    for row in space_image:
        print(row, end='')

    print("")
    print("Galaxies:")
    number_of_pairs = 0
    sum_of_paths_lengths = 0
    for idx, my_galaxy in enumerate(galaxies):
        print(idx, my_galaxy)
        for another_galaxy in galaxies[idx + 1:]:
            number_of_pairs += 1
            sum_of_paths_lengths += compute_length_of_shortest_path_between(my_galaxy, another_galaxy)
            print(f'shortest path between galaxy {my_galaxy} and {another_galaxy}',
                  compute_length_of_shortest_path_between(my_galaxy, another_galaxy))
            print("galaxy:", my_galaxy)
            print("Another Galaxy:", another_galaxy)
    print("number of pairs:", number_of_pairs)
    print("sums of paths lengths:", sum_of_paths_lengths)


def compute_length_of_shortest_path_between(galaxy_a, galaxy_b):
    steps = 0
    current_pos = galaxy_a.copy()
    while current_pos != galaxy_b:
        x_difference = galaxy_b["x"] - current_pos["x"]
        x_difference_negative = x_difference < 0
        y_difference = galaxy_b["y"] - current_pos["y"]
        y_difference_negative = y_difference < 0

        if x_difference_negative:
            x_difference *= -1
        if y_difference_negative:
            y_difference *= -1

        if y_difference > x_difference:
            if y_difference_negative:
                current_pos["y"] -= 1
            else:
                current_pos["y"] += 1
        else:  # If y_difference == x_difference it doesn't matter in which direction we move
            if x_difference_negative:
                current_pos["x"] -= 1
            else:
                current_pos["x"] += 1
        steps += 1
    return steps


if __name__ == "__main__":
    main()
