def part_one() -> int:
    with open("day_one", "r") as file:
        numbers = []
        for line in file:
            first_digit = None
            last_digit = None
            for char in line.strip():
                if char.isdigit():
                    if not first_digit:
                        first_digit = char
                    last_digit = char
            numbers.append(int(f"{first_digit}{last_digit}"))
    return sum(numbers)


def part_two() -> int:
    res = 0
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("day_one", "r") as file:
        for line in file:
            first_digit, last_digit = -1, -1
            line = line.strip()
            for i in range(len(line)):
                if line[i].isdigit():
                    if first_digit == -1:
                        first_digit = int(line[i])
                    last_digit = int(line[i])
                else:
                    for w in range(len(words)):
                        word_length = len(words[w]) - 1
                        if i - word_length >= 0 and line[i - word_length:i + 1] == words[w]:
                            if first_digit == -1:
                                first_digit = w + 1
                            last_digit = w + 1
            res += (first_digit * 10) + last_digit
    return res


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
