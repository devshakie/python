
import re

# Define the mapping of numbers to words
number_words = {
    '0': 'noti',
    '1': 'Imwe',
    '2': 'Igiri',
    '3': 'Ithatu',
    '4': 'Inya',
    '5': 'Ithano',
    '6': 'Ithathatu',
    '7': 'Mugwanja',
    '8': 'Inyanya',
    '9': 'Kenda'
}

# Define the mapping of words to numbers
word_numbers = {v: k for k, v in number_words.items()}

# Regular expressions for matching numbers and words
number_regex = r'^\d+$'
word_regex = r'^[A-Za-z\s]+$'
def convert_number_to_words(number):
    # Check if the input is a number
    if not re.match(number_regex, number):
        return "Invalid input. Please enter a valid number."

    # Convert the number to words
    if len(number) == 1:
        # Single-digit number
        words = number_words[number]
    elif len(number) == 2:
        # Two-digit number
        if number == '10':
            words = "Ikumi"
        elif number[0] == '1':
            words = "Ikumi na " + number_words[number[1]]
        elif number[1] == '0':
            words = "Mirogo " + number_words[number[0]]
        else:
            words = "Mirogo " + number_words[number[0]] + " na " + number_words[number[1]]
    elif len(number) == 3:
        # Three-digit number
        if number == '100':
            words = "Yirana Imwe"
        elif number[1] == '0' and number[2] == '0':
            words = "Marana " + number_words[number[0]]
        else:
            words = "Marana " + number_words[number[0]] + " " + convert_number_to_words(number[1:])
    elif len(number) <= 4:
         if number == '1000':
            words = "Ngiri Imwe"
         elif number[1] == '0' and number[2] == '0' and number[3] == '0':
            words = "Ngiri " + number_words[number[0]]
         else:
        # Four-digit number or five-digit number
            thousands = "Ngiri " + number_words[number[0]] + " " + convert_number_to_words(number[1:])
            words = thousands + " "
    elif number == '10000':
        words = "Ngiri ikumi"
        return words
    else:
        return "Invalid input. Please enter a valid number.(1 - 10000)"

    return words



def convert_words_to_number(words):
    # Check if the input is a word
    if not re.match(word_regex, words):
        return "Invalid input. Please enter a valid word."

    # Convert each word to its corresponding digit
    digits = [word_numbers[word.capitalize()] for word in words.split()]

    # Join the digits and return the result
    return ''.join(digits)

# Test the conversion functions
while True:
    user_input = input("Enter a number or a word (q to quit): ")


    if user_input.lower() == 'q':
        break

    if re.match(number_regex, user_input):
        result = convert_number_to_words(user_input)
    elif re.match(word_regex, user_input):
        result = convert_words_to_number(user_input)
    else:
        result = "Invalid input. Please enter a valid number or word."

    print(result)