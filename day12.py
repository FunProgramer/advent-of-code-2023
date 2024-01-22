from itertools import groupby


def main():
    row_str = "???.### 1,1,3"
    [row, broken_groups_str] = row_str.split(" ")
    broken_groups_lengths = list(int(length) for length in broken_groups_str.split(","))

    spring_groups = []
    for key, group in groupby(row):
        spring_groups.append((key, len(list(group))))


if __name__ == "__main__":
    main()
