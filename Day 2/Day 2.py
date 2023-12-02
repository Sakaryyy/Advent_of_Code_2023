def parse_game_data(game_data):
    """
    Parse game data to get the required number of cubes for each color.
    """
    return {color.split(' ')[1].strip('\n'): int(color.split(' ')[0]) for color in game_data.split(', ')}


def is_game_possible(game_data, max_cubes):
    """
    Check if a game configuration is possible given the maximum number of cubes available.
    """
    required_cubes = parse_game_data(game_data)
    return all(required_cubes.get(color, 0) <= max_cubes[color] for color in max_cubes)


def are_all_rounds_possible(game_rounds, max_cubes):
    """
    Check if all rounds in a game are possible.
    """
    return all(is_game_possible(game_data, max_cubes) for game_data in game_rounds.split('; '))


def calculate_power_of_minimum_set(game_rounds):
    """
    Calculate the power of the minimum set of cubes required for a game.
    """
    max_cubes_required = calculate_max_cubes_required_per_round(game_rounds)
    return max_cubes_required['red'] * max_cubes_required['green'] * max_cubes_required['blue']


def calculate_max_cubes_required_per_round(game_rounds):
    """
    Calculate the maximum cubes required for each color across all rounds.
    """
    max_cubes_required = {'red': 0, 'green': 0, 'blue': 0}
    for round_data in game_rounds.split('; '):
        round_cubes = parse_game_data(round_data)
        for color, count in round_cubes.items():
            max_cubes_required[color] = max(max_cubes_required[color], count)
    return max_cubes_required


def calculate_games(file_path, max_cubes):
    """
    Calculate the sum of IDs of all games that are possible and the sum of the powers of the minimum sets.
    """
    with open(file_path) as file:
        puzzle_input = file.readlines()

    game_ids = [int(line.split(':')[0].split(' ')[-1]) for line in puzzle_input]
    games = [line.split(': ')[1] for line in puzzle_input]

    # Part I
    possible_game_ids = [game_id for game_id, game in zip(game_ids, games) if are_all_rounds_possible(game, max_cubes)]
    # Part II
    sum_of_powers_of_set = sum(calculate_power_of_minimum_set(game) for game in games)

    return possible_game_ids, sum(possible_game_ids), sum_of_powers_of_set


def main():
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_game_ids, sum_of_possible_game_ids, sum_of_powers_of_set = calculate_games('Puzzle_Input_Day_2', max_cubes)

    print("Possible Game IDs:", possible_game_ids)
    print("Sum of Possible Game IDs:", sum_of_possible_game_ids)
    print("The Sum of the powers of the miminium required cubes in each game:", sum_of_powers_of_set)


if __name__ == '__main__':
    main()
