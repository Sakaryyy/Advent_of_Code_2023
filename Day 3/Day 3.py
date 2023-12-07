import re


def find_pattern_indices(pattern, text):
    return [(match.start(), match.end()) for match in re.finditer(pattern, text)]


def process_puzzle_input(puzzle_input):
    pattern_symbols = r'[^0-9a-zA-Z\.\s]'  # Pattern for symbols
    pattern_numbers = r'\d+'  # Pattern for numbers

    symbol_indices = []
    number_indices = []

    for line in puzzle_input:
        symbol_indices.append(find_pattern_indices(pattern_symbols, line))
        number_indices.append(find_pattern_indices(pattern_numbers, line))

    return symbol_indices, number_indices


def is_neighbour(symbol_range, number_range):
    expanded_number_range = range(number_range[0] - 1, number_range[1] + 1)
    return any(i in expanded_number_range for i in range(symbol_range[0], symbol_range[1]))


def extract_number(puzzle_line, number_range):
    return int(''.join(puzzle_line[i] for i in range(number_range[0], number_range[1])))


def process_neighbouring_numbers(puzzle_input, symbol_index_list, number_index_list):
    neighbouring_numbers = []
    for n, (symbol_line, number_line) in enumerate(zip(symbol_index_list, number_index_list)):
        for symbol in symbol_line:
            for item in check(n, number_index_list, number_line, puzzle_input, symbol):
                neighbouring_numbers.append(item)
    return neighbouring_numbers


def multiply_adjacent_numbers(puzzle_input, symbol_index_list, number_index_list):
    multiplication_results = []

    for n, (symbol_line, number_line) in enumerate(zip(symbol_index_list, number_index_list)):
        for symbol_index in symbol_line:
            # Check if the symbol is "*"
            if puzzle_input[n][symbol_index[0]:symbol_index[1]] == "*":

                # Check for adjacent numbers in the same line
                adjacent_numbers = check(n, number_index_list, number_line, puzzle_input, symbol_index)

                # Multiply if exactly two numbers are adjacent
                if len(adjacent_numbers) == 2:
                    multiplication_results.append(adjacent_numbers[0] * adjacent_numbers[1])

    return multiplication_results


def check(n, number_index_list, number_line, puzzle_input, symbol_index):
    adjacent_numbers = []
    for number in number_line:
        if is_neighbour(symbol_index, number):
            adjacent_numbers.append(extract_number(puzzle_input[n], number))
    # Check for adjacent numbers in the upper line
    if n + 1 < len(number_index_list):
        for upper_number_line in number_index_list[n + 1]:
            if is_neighbour(symbol_index, upper_number_line):
                adjacent_numbers.append(extract_number(puzzle_input[n + 1], upper_number_line))
    # Check for adjacent numbers in the lower line
    if n - 1 >= 0:
        for lower_number_line in number_index_list[n - 1]:
            if is_neighbour(symbol_index, lower_number_line):
                adjacent_numbers.append(extract_number(puzzle_input[n - 1], lower_number_line))
    return adjacent_numbers


def main():
    with open('puzzle_input') as file:
        puzzle_input = file.readlines()

    symbol_index_list, number_index_list = process_puzzle_input(puzzle_input)
    result = process_neighbouring_numbers(puzzle_input, symbol_index_list, number_index_list)
    print(sum(result))
    multiplication_result = multiply_adjacent_numbers(puzzle_input, symbol_index_list, number_index_list)
    print(sum(multiplication_result))


if __name__ == '__main__':
    main()
