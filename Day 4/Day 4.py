def parse_line(line):
    """Parse a line from the input file into two lists of integers."""
    _, numbers_string = line.split(':', 1)
    left, right = numbers_string.strip().split('|')
    return [list(map(int, left.split())), list(map(int, right.split()))]


def calculate_result(numbers):
    """Calculate the result based on the provided number pairs."""
    return sum(2 ** (sum(num in left for num in right) - 1) for left, right in numbers
               if any(num in left for num in right))


# Function to count matches
def count_matches(card, winning_numbers):
    return sum(num in winning_numbers for num in card)


def count_scratchcards(cards):
    """
    Count the total number of scratchcards including original and copies won.
    """
    # Initialize a dictionary to store the count of each card
    card_counts = {i: 1 for i in range(len(cards))}  # Initially, 1 of each card

    # Iterate through each card
    for i, (card, winning_numbers) in enumerate(cards):
        # Count matches for this card
        matches = count_matches(card, winning_numbers)

        # For each match, add a copy of the next cards
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_counts[j] += card_counts[i]

    return sum(card_counts.values())


def main():
    """Main function to process the puzzle input and print the result."""
    with open('puzzle_input_day_4') as file:
        numbers = [parse_line(line) for line in file]

    result_part_1 = calculate_result(numbers)
    result_part_2 = count_scratchcards(numbers)

    print(result_part_1)
    print(result_part_2)


if __name__ == '__main__':
    main()
