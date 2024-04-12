import sys

def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        input_number = input("Enter a non-negative integer: ")
        input_number = int(input_number)
        result = factorial(input_number)
        print(f"Factorial of {input_number} is {result}")
        return 0
    except ValueError:
        print("Error: Please enter a valid non-negative integer.")
        return 1



if __name__ == "__main__":
    sys.exit(main())
