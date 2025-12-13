"""
A simple command-line calculator that performs addition and multiplication.
"""

from typing import List


def get_numbers() -> List[float]:
    """
    Prompt the user to enter numbers until 'done' is typed.

    Returns:
        List[float]: List of numbers entered by the user.
    """
    numbers: List[float] = []
    print("Enter numbers (type 'done' when finished):")

    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a number.")

    return numbers


def add_numbers(numbers: List[float]) -> float:
    """
    Add all numbers in the list.

    Args:
        numbers (List[float]): List of numbers to add.

    Returns:
        float: Sum of all numbers.
    """
    return sum(numbers)


def multiply_numbers(numbers: List[float]) -> float:
    """
    Multiply all numbers in the list.

    Args:
        numbers (List[float]): List of numbers to multiply.

    Returns:
        float: Product of all numbers.
    """
    result = 1
    for number in numbers:
        result *= number
    return result


def main() -> None:
    """
    Run the interactive calculator that allows addition or multiplication.
    """
    print("=" * 50)
    print("Welcome to the collaborative Calculator!")
    print("=" * 50)

    numbers = get_numbers()
    if not numbers:
        print("No numbers entered, exiting.")
        return

    print(f"\nYou entered: {numbers}")
    print("\nWhat operation would you like to perform?")
    print("1. Add")
    print("2. Multiply")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        result = add_numbers(numbers)
        expression = " + ".join(map(str, numbers))
        print(f"\nResult: {expression} = {result}")

    elif choice == "2":
        result = multiply_numbers(numbers)
        expression = " x ".join(map(str, numbers))
        print(f"\nResult: {expression} = {result}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
