def create_alphabet_file(lines):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars_per_line = 3  # Specify the number of letters per line

    with open('alphabet.txt', 'w') as file:
        for i in range(0, len(alphabet), chars_per_line):
            line = alphabet[i:i + chars_per_line]
            file.write(line + '\n')

    print(f'File "alphabet.txt" created with {lines} lines and {chars_per_line} letters per line.')


# Example usage
create_alphabet_file(9)  # Generate alphabet.txt with 9 lines
