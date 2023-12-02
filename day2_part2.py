class Game:

    def __init__(self, game_notation: str):
        [title, description] = game_notation.split(":")
        self.id = int(title.strip("Game "))
        self.sets: [{"red": int, "green": int, "blue": int}] = []
        self.is_possible = True
        set_descriptions = description.split(";")
        for set_description in set_descriptions:
            red = 0
            green = 0
            blue = 0
            color_entries = set_description.split(",")
            for color_entry in color_entries:
                if "red" in color_entry:
                    red = int(color_entry.strip(" red"))
                elif "green" in color_entry:
                    green = int(color_entry.strip(" green"))
                elif "blue" in color_entry:
                    blue = int(color_entry.strip(" blue"))
            self.sets.append({"red": red, "green": green, "blue": blue})

    def get_power(self):
        min_red = 0
        min_green = 0
        min_blue = 0

        for cube_set in self.sets:
            if cube_set["red"] > min_red:
                min_red = cube_set["red"]

            if cube_set["green"] > min_green:
                min_green = cube_set["green"]

            if cube_set["blue"] > min_blue:
                min_blue = cube_set["blue"]

        return min_red * min_green * min_blue


def main():
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    with open("day2_input.txt", "r") as input_file:
        input_string = input_file.read()

    input_lines = input_string.splitlines()
    game_powers_sum = 0

    for idx, input_line in enumerate(input_lines):
        game_powers_sum += Game(input_line).get_power()

    print("Sum of game powers:", game_powers_sum)


if __name__ == "__main__":
    main()
