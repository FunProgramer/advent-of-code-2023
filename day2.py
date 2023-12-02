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


def main():
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    with open("day2_input.txt", "r") as input_file:
        input_string = input_file.read()

    input_lines = input_string.splitlines()
    game_ids_sum = 0

    for idx, input_line in enumerate(input_lines):
        game = Game(input_line)
        for cube_set in game.sets:
            if cube_set["red"] > red_cubes or cube_set["green"] > green_cubes or cube_set["blue"] > blue_cubes:
                game.is_possible = False
                break
        if game.is_possible:
            game_ids_sum += game.id

    print("Sum of possible game IDs:", game_ids_sum)


if __name__ == "__main__":
    main()
