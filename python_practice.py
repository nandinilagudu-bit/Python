"""
Python Problem-Solving Practice
-------------------------------
Beginner-friendly exercises with comments.

How to run:
1. Save this file as python_practice.py
2. Open a terminal in the folder containing this file.
3. Run: python python_practice.py

Choose an exercise from the menu and follow the instructions.
"""


def even_or_odd():
    """Check whether an integer is even or odd."""
    number = int(input("Enter an integer: "))

    # A number is even when the remainder after division by 2 is zero.
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


def factorial():
    """Calculate the factorial of a non-negative integer."""
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Factorial is not defined for negative integers.")
        return

    result = 1

    # Multiply result by every integer from 1 up to number.
    for value in range(1, number + 1):
        result *= value

    # The factorial of 0 is 1, so result also works when number is 0.
    print(f"{number}! = {result}")


def check_prime():
    """Determine whether an integer is prime."""
    number = int(input("Enter an integer: "))

    # Prime numbers are greater than 1 and have exactly two positive factors.
    if number < 2:
        print(number, "is not a prime number.")
        return

    # It is enough to test possible factors up to the square root of number.
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            print(number, "is not a prime number.")
            return

    print(number, "is a prime number.")


def check_palindrome():
    """Check whether text reads the same forwards and backwards."""
    text = input("Enter a word or phrase: ")

    # Ignore spaces and letter case to make the check more flexible.
    cleaned = "".join(text.lower().split())

    if cleaned == cleaned[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def fibonacci_sequence():
    """Print the first n numbers in the Fibonacci sequence."""
    count = int(input("How many Fibonacci numbers should be printed? "))

    if count <= 0:
        print("Please enter a positive number.")
        return

    first, second = 0, 1
    sequence = []

    for _ in range(count):
        sequence.append(first)
        # Move forward: the next number is the sum of the previous two.
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)


def largest_of_three():
    """Find the largest of three numbers without using max()."""
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))

    largest = first

    if second > largest:
        largest = second

    if third > largest:
        largest = third

    print("The largest number is:", largest)


def sum_of_digits():
    """Calculate the sum of the digits of an integer."""
    number = abs(int(input("Enter an integer: ")))
    total = 0

    # The modulo operator gets the last digit; // removes that digit.
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    print("Sum of digits:", total)


def count_vowels():
    """Count vowels in a line of text."""
    text = input("Enter some text: ")
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    print("Number of vowels:", count)


def reverse_text():
    """Display a string in reverse order."""
    text = input("Enter text to reverse: ")
    print("Reversed text:", text[::-1])


def main():
    """Display the menu and run the selected exercise."""
    exercises = {
        "1": ("Even or odd", even_or_odd),
        "2": ("Factorial", factorial),
        "3": ("Prime number", check_prime),
        "4": ("Palindrome", check_palindrome),
        "5": ("Fibonacci sequence", fibonacci_sequence),
        "6": ("Largest of three numbers", largest_of_three),
        "7": ("Sum of digits", sum_of_digits),
        "8": ("Count vowels", count_vowels),
        "9": ("Reverse text", reverse_text),
    }

    while True:
        print("\n=== PYTHON PROBLEM-SOLVING PRACTICE ===")
        for choice, (label, _) in exercises.items():
            print(f"{choice}. {label}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Great work! Keep practising Python.")
            break

        if choice in exercises:
            print()
            try:
                exercises[choice][1]()
            except ValueError:
                print("Invalid input. Please enter the requested number or text.")
        else:
            print("Invalid choice. Please select an option from the menu.")


# This starts the menu only when the file is run directly.
if __name__ == "__main__":
    main()
