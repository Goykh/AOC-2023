# Too lazy to properly work in part two, hence returning tuples...

COLOR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

POWER_COUNT = 0


def _compare_colour_counts(set_count: dict) -> bool:
    for key in COLOR_LIMITS:
        if key in set_count:
            if COLOR_LIMITS.get(key) < set_count.get(key):
                return False
    return True


def is_possible_game(game_sets: str) -> tuple[bool, int]:
    sets = game_sets.split(';')
    min_game_count = {"red": 0, "green": 0, "blue": 0}
    is_possible = True
    for set in sets:
        set_count = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        subsets = set.split(",")
        for subset in subsets:
            amount, colour = subset.split()
            set_count[colour] += int(amount)
            min_game_count[colour] = max(min_game_count.get(colour), int(amount))
        if not _compare_colour_counts(set_count):
            is_possible = False
    min_count = min_game_count.get("red") * min_game_count.get("green") * min_game_count.get("blue")
    return is_possible, min_count


def get_sum_of_game_ids(games: list[str]) -> tuple[int, int]:
    count = 0
    possible_games = []
    for game_id, game_set in games:
        is_possible, game_count = is_possible_game(game_set)
        if is_possible:
            possible_games.append(game_id)
        count += game_count
    return sum(int(game_id.split()[1]) for game_id in possible_games), count


def get_records_from_file() -> list:
    games = []
    with open("day_two", "r") as file:
        for line in file:
            game_id, game_sets = line.strip().split(": ")
            games.append((game_id, game_sets))
    return games


if __name__ == "__main__":
    sum_of_game_ids = get_sum_of_game_ids(get_records_from_file())
    print(f"Sum of IDs of possible games: {sum_of_game_ids[0]}")
    print(f"Power sum or whatever of all cubes: {sum_of_game_ids[1]}")
