"""
Python Lists and Strings Practice
---------------------------------
A second beginner-friendly practice file focused on lists and strings.

How to run:
1. Download this file as python_list_string_practice.py
2. Open a terminal in the same folder.
3. Run: python python_list_string_practice.py

Choose an exercise from the menu. Read the comments to understand each step.
"""


def remove_duplicates():
    """Remove repeated values while keeping their original order."""
    numbers = input("Enter numbers separated by spaces: ").split()
    unique_numbers = []

    for number in numbers:
        # Add a value only the first time we see it.
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("List without duplicates:", unique_numbers)


def second_largest():
    """Find the second-largest distinct number in a list."""
    numbers = [int(value) for value in input(
        "Enter integers separated by spaces: "
    ).split()]

    # set() removes repeated numbers; sorted() arranges them from low to high.
    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        print("Please enter at least two different numbers.")
    else:
        print("Second-largest number:", unique_numbers[-2])


def count_words():
    """Count how many words are in a sentence."""
    sentence = input("Enter a sentence: ")

    # split() separates the sentence at spaces and ignores extra spaces.
    words = sentence.split()
    print("Number of words:", len(words))


def character_frequency():
    """Count how often each character appears in text."""
    text = input("Enter text: ").lower()
    frequency = {}

    for character in text:
        if character == " ":
            continue  # Ignore spaces in this example.

        # get(character, 0) gives 0 if this character is new.
        frequency[character] = frequency.get(character, 0) + 1

    print("Character frequencies:")
    for character, count in sorted(frequency.items()):
        print(f"{character}: {count}")


def check_anagram():
    """Check whether two words contain the same letters."""
    first = input("Enter the first word or phrase: ").lower()
    second = input("Enter the second word or phrase: ").lower()

    # Ignore spaces so phrases can be compared too.
    first_letters = sorted(first.replace(" ", ""))
    second_letters = sorted(second.replace(" ", ""))

    if first_letters == second_letters:
        print("These are anagrams.")
    else:
        print("These are not anagrams.")


def find_common_elements():
    """Find values that appear in both lists."""
    first = input("Enter the first list of values: ").split()
    second = input("Enter the second list of values: ").split()

    common = []

    for value in first:
        # Check membership in the second list and avoid repeated results.
        if value in second and value not in common:
            common.append(value)

    print("Common values:", common)


def count_vowels_and_consonants():
    """Count English vowels and consonants in a line of text."""
    text = input("Enter a sentence: ").lower()
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for character in text:
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)


def sort_numbers():
    """Sort a list of integers from smallest to largest."""
    numbers = [int(value) for value in input(
        "Enter integers separated by spaces: "
    ).split()]

    # sorted() creates a new sorted list and leaves the original unchanged.
    print("Sorted numbers:", sorted(numbers))


def main():
    """Show the menu and run the selected exercise."""
    exercises = {
        "1": ("Remove duplicates from a list", remove_duplicates),
        "2": ("Find the second-largest number", second_largest),
        "3": ("Count words in a sentence", count_words),
        "4": ("Count character frequency", character_frequency),
        "5": ("Check whether two phrases are anagrams", check_anagram),
        "6": ("Find common elements in two lists", find_common_elements),
        "7": ("Count vowels and consonants", count_vowels_and_consonants),
        "8": ("Sort a list of numbers", sort_numbers),
    }

    while True:
        print("\n=== LISTS AND STRINGS PRACTICE ===")
        for choice, (description, _) in exercises.items():
            print(f"{choice}. {description}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Practice complete. Keep learning one step at a time!")
            break

        if choice not in exercises:
            print("Invalid choice. Please choose a number from the menu.")
            continue

        try:
            exercises[choice][1]()
        except ValueError:
            print("Invalid number entered. Please try again with valid input.")


if __name__ == "__main__":
    main()
