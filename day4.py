import re


def main():
    with open("day4_input.txt", "r") as input_file:
        cards = input_file.readlines()

    points_sum = 0
    for card in cards:
        [winning_numbers_str, my_numbers_str] = re.sub("Card +\\d+: ", "", card).split("|")

        winning_numbers_str = winning_numbers_str.strip()
        my_numbers_str = my_numbers_str.strip()

        winning_numbers = []
        for winning_number in winning_numbers_str.split(" "):
            winning_number = winning_number.strip()
            if winning_number != "":
                winning_numbers.append(winning_number)

        my_numbers = []
        for my_number in my_numbers_str.split(" "):
            my_number = my_number.strip()
            if my_number != "":
                my_numbers.append(my_number)

        points = 0
        for idx, my_number in enumerate(my_numbers):
            if my_number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        points_sum += points

    print("Sum of points:", points_sum)


if __name__ == "__main__":
    main()