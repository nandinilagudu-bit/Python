# Functions and loops practice
# Run with: python functions_loops_practice.py

def sum_to_n():
    """Return the sum of integers from 1 to n."""
    n = int(input("Enter a positive integer: "))
    total = 0
    for value in range(1, n + 1):
        total += value
    print("Sum:", total)


def multiplication_table():
    """Print the first ten multiples of a number."""
    number = int(input("Enter a number: "))
    for value in range(1, 11):
        print(number, "x", value, "=", number * value)


def main():
    while True:
        print("\n1. Sum from 1 to N")
        print("2. Multiplication table")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            sum_to_n()
        elif choice == "2":
            multiplication_table()
        elif choice == "0":
            break
        else:
            print("Please choose 1, 2, or 0.")


if __name__ == "__main__":
    main()
