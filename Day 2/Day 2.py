def is_game_possible(game_data, max_cubes):
    """
    Check if a game configuration is possible given the maximum number of cubes available.
    """
    required_cubes = {color.split(' ')[1].strip('\n'): int(color.split(' ')[0]) for color in game_data.split(', ')}
    return all(required_cubes.get(color, 0) <= max_cubes[color] for color in max_cubes)


def are_all_rounds_possible(game_rounds, max_cubes):
    """
    Check if all rounds in a game are possible.
    """
    return all(is_game_possible(round_data, max_cubes) for round_data in game_rounds.split('; '))


def calculate_possible_games(file_path, max_cubes):
    """
    Calculate the sum of IDs of all games that are possible.
    """
    with open(file_path) as file:
        puzzle_input = file.readlines()

    game_ids = [int(line.split(':')[0].split(' ')[-1]) for line in puzzle_input]
    games = [line.split(': ')[1] for line in puzzle_input]

    possible_game_ids = [game_id for game_id, game in zip(game_ids, games) if are_all_rounds_possible(game, max_cubes)]
    return possible_game_ids, sum(possible_game_ids)


def main():
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_game_ids, sum_of_feasible_game_ids = calculate_possible_games('Puzzle_Input_Day_2', max_cubes)

    print("Feasible Game IDs:", possible_game_ids)
    print("Sum of Feasible Game IDs:", sum_of_feasible_game_ids)


if __name__ == '__main__':
    main()
