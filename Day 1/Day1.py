def main():
    with open('Puzzle_Input_Day_1') as file:
        puzzle_input = file.readlines()

    word_to_digit = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x',
                     'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    def digits(line):
        digit = [integer for integer in line if integer.isdigit()]
        if digit:
            return int(digit[0]+digit[-1])
        return 0

    def convert_to_digit(input_text):
        for word, digit in word_to_digit.items():
            input_text = input_text.replace(word, digit)
        return input_text

    value = sum(digits(line) for line in puzzle_input)
    print(value)
    converted_text = [convert_to_digit(line) for line in puzzle_input]
    value_2 = sum(digits(line) for line in converted_text)
    print(value_2)


if __name__ == '__main__':
    main()
