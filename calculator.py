"""
A simple command line calculator that performs addition and subtraction
"""


def get_numbers():
    # get number from user input
    numbers = []
    print("enter numbers (type 'done' when finished): ")
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input please enter a number")
    return numbers


def add_numbers(numbers):
    '''
    Add all numbers in the list
    Args:
        numbers (list): List of numbers to add
    Returns:
        float: Sum of all numbers
    '''
    return sum(numbers)


def multiply_numbers(numbers):
    '''
    Multiply all numbers in the list
    Args:
        numbers (list): List of numbers to multiply
    Returns:
        float: Product of all numbers
    '''
    result = 1
    for number in numbers:
        result *= number

    return result


def main():
    # function to  run the calculator
    print("=" * 50)
    print("Welcome to the collaborative Calculator!")
    print("=" * 50)
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered exiting")
        return
    print(f"\n You entered: {numbers}")
    print("\n What operation would You like to perform?")
    print("1. Add")
    print("2. Multiply")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == '1':
        result = add_numbers(numbers)
        print(f"\n Result: {' + '.join(map(str, numbers))} = {result}")
    elif choice == '2':
        result = multiply_numbers(numbers)
        print(f"\n Result: {' x '.join(map(str, numbers))} = {result}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
