import copy
import functools


def count_cards(line: str):
    cards, _ = line.split()
    counts = {}
    for card in cards:
        count = counts.get(card, 0)
        counts[card] = count + 1
    return counts


def is_of_kind(counts:dict, number):
    counts = copy.deepcopy(counts)
    number_of_j = counts.pop("J",0)

    if number_of_j == number:
        return True

    for count in counts.values():
        if (count + number_of_j) == number:
            return True

    return False


def is_five_of_kind(counts):
    return is_of_kind(counts, 5)


def is_four_of_kind(counts):
    return is_of_kind(counts, 4)


def is_three_of_kind(counts):
    return is_of_kind(counts, 3)


def is_two_of_kind(counts):
    return is_of_kind(counts, 2)


def is_one_pair(counts):
    return is_two_of_kind(counts)


def is_full_house(counts):
    number_of_j = counts.pop("J",0)
    number_of_pairs = sum([1 for value in counts.values() if value == 2])
    number_of_three_of_kind = sum([1 for value in counts.values() if value == 3])
    if number_of_j == 3 and number_of_pairs >= 1:
        return True
    if (number_of_pairs >= 1 and number_of_j >= 2):
        return True
    if (number_of_three_of_kind >= 1 and number_of_j >= 1):
        return True
    if number_of_pairs >= 2 and number_of_j >= 1:
        return True
    if number_of_pairs>=1 and number_of_three_of_kind>=1:
        return True
    return False


def is_two_pair(counts):
    pairs = 0
    number_of_j = counts.get("J",0)
    for number in counts.values():
        if number == 2:
            pairs += 1
    if pairs >= 2: return True
    if pairs == 1 and number_of_j >=1: return True
    if pairs == 0 and number_of_j >=2: return True
    return pairs == 2


def order(line_a, line_b):
    a = line_a.split()[0]
    b = line_b.split()[0]
    for index in range(len(a)):
        if a[index] == b[index]:
            continue
        return -1 if suit_order.index(a[index]) <= suit_order.index(b[index]) else 1
    return 0


card_types = {
    "5": [],
    "4": [],
    "FH": [],
    "3": [],
    "2": [],
    "1": [],
    "HC": [],
}

suit_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

card_order = [
    ("5", is_five_of_kind),
    ("4", is_four_of_kind),
    ("FH", is_full_house),
    ("3", is_three_of_kind),
    ("2", is_two_pair),
    ("1", is_one_pair),
    ("HC", lambda x: True),
]

with open("input.txt") as handle:
    lines = handle.readlines()
    current_rank = len(lines)
    total = 0
    for line in lines:
        counts = count_cards(line)
        if line.split()[0].strip() == "1224455J":
            print("1224455J")
        for key, func in card_order:
            if func(counts):
                card_types[key].append(line)
                break

    for x in sorted(card_types.get("4"), key=functools.cmp_to_key(order)):
        print("".join(sorted(x.split()[0].strip())))

    for key, _ in card_order:
        lines = sorted(card_types.get(key), key=functools.cmp_to_key(order))
        for line in lines:
            total += int(line.split()[1].strip()) * current_rank
            current_rank -= 1

print(total)
