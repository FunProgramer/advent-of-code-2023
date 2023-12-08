# Not working
from enum import Enum


class HandTypes(Enum):
    FIVE_KIND = 6
    FOUR_KIND = 5
    FULL_HOUSE = 4
    THREE_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


labels = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Hand:
    def __init__(self, cards_str, bid_amount):
        self.cards_str: str = cards_str
        self.bid_amount: int = bid_amount
        self.rank: int or None = None

        # Determine hand type
        count_of_first_label = self.cards_str.count(self.cards_str[0])

        if count_of_first_label == 5:
            self.type = HandTypes.FIVE_KIND
        elif count_of_first_label == 4:
            self.type = HandTypes.FOUR_KIND
        else:
            self.type = determine_hands_type(cards_str, count_of_first_label)
        print(self.type)

    # To be honest, this method is not really necessary
    def __eq__(self, other):
        if self.type == other.type and self.cards_str == other.cards_str:
            return True

    def __lt__(self, other):
        if self.type.value < other.type.value:
            return True

        if self.type == other.type:
            for i in range(0, 5):
                self_label_value = labels.index(self.cards_str[i])
                other_label_value = labels.index(other.cards_str[i])

                if self_label_value < other_label_value:
                    return True

        return False

    # To be honest, this method is also not really necessary
    def __gt__(self, other):
        if self.type.value > other.type.value:
            return True

        if self.type == other.type:
            for i in range(0, 5):
                self_label_value = labels.index(self.cards_str[i])
                other_label_value = labels.index(other.cards_str[i])

                if self_label_value > other_label_value:
                    return True

        return False


def determine_hands_type(cards_str: str, last_found_count: int, pair_found: bool = False):
    label = cards_str[0]
    label_count = cards_str.count(label)
    if last_found_count == 3:
        if label_count == 2:
            return HandTypes.FULL_HOUSE
        else:
            return HandTypes.THREE_KIND
    if last_found_count == 2:
        if label_count == 2:
            return HandTypes.TWO_PAIR
        else:
            determine_hands_type(cards_str.replace(label, ""), label_count, True)
    if last_found_count == 1:
        if pair_found and label_count == 2:
            return HandTypes.TWO_PAIR
        if label_count == 2:
            if len(cards_str) > 3:
                return determine_hands_type(cards_str.replace(label, ""), label_count, True)
            else:
                return HandTypes.ONE_PAIR
        if label_count == 1:
            if len(cards_str) > 3:
                return determine_hands_type(cards_str.replace(label, ""), label_count, pair_found)
            else:
                return HandTypes.HIGH_CARD


def main():
    hands = []
    total_winning = 0
    with open("day7_input.txt", "r") as input_file:
        hand_strs = input_file.readlines()

    for hand_idx, hand_str in enumerate(hand_strs):
        [cards_str, bid_amount] = hand_str.split(" ")
        hands.append(Hand(cards_str, int(bid_amount)))

    hands.sort()

    for rank, hand in enumerate(hands):
        total_winning += rank * hand.bid_amount

    print("Total Winning:", total_winning)


if __name__ == '__main__':
    main()
