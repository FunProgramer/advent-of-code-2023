def main():
    with open("day5_input.txt", "r") as input_file:
        input_lines = input_file.readlines()

    current_element = None
    seeds = []
    seed_to_soil = {}
    for input_line in input_lines:
        if input_line == "\n":
            current_element = None
            continue
        if input_line.startswith("seeds"):
            seeds = input_line.split(":")[1].strip().split(" ")
            continue
        [name, the_rest] = input_line.split(":")
        if current_element is not None:

            match current_element:
                case "seed-to-soil map":
                    pass
        else:
            current_element = name

    print(seeds)


if __name__ == "__main__":
    main()
