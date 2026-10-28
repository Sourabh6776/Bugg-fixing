"""
=========================================================
BUG FIXING USING CURSOR AI
Author: Sourabh Rathore
College: JECRC University, Jaipur
Course: B.Tech CSE (AI/ML)

Purpose:
Demonstrate corrected Python functions and verify
their results using automated test cases.
=========================================================
"""


def calculate_factorial(number):
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Number cannot be negative.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


def generate_fibonacci(count):
    """Generate the first 'count' Fibonacci numbers."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def calculate_average(numbers):
    """Calculate the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")

    return sum(numbers) / len(numbers)


def calculate_grade(average):
    """Return a grade based on the average marks."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


def filter_passing_marks(marks):
    """Return all marks greater than or equal to 40."""
    return [mark for mark in marks if mark >= 40]


def run_tests():
    """Run automated tests and display their results."""
    test_cases = [
        {
            "name": "Factorial of 5",
            "function": lambda: calculate_factorial(5),
            "expected": 120,
        },
        {
            "name": "Factorial of 0",
            "function": lambda: calculate_factorial(0),
            "expected": 1,
        },
        {
            "name": "First 5 Fibonacci numbers",
            "function": lambda: generate_fibonacci(5),
            "expected": [0, 1, 1, 2, 3],
        },
        {
            "name": "Fibonacci with count 0",
            "function": lambda: generate_fibonacci(0),
            "expected": [],
        },
        {
            "name": "Average of [10, 20, 30]",
            "function": lambda: calculate_average([10, 20, 30]),
            "expected": 20,
        },
        {
            "name": "Grade for average 90",
            "function": lambda: calculate_grade(90),
            "expected": "A",
        },
        {
            "name": "Grade for average 75",
            "function": lambda: calculate_grade(75),
            "expected": "B",
        },
        {
            "name": "Passing marks including 40",
            "function": lambda: filter_passing_marks([30, 40, 50, 80]),
            "expected": [40, 50, 80],
        },
    ]

    passed = 0
    failed = 0

    print("\n" + "=" * 65)
    print("BUG FIXING PROJECT — AUTOMATED TEST RESULTS")
    print("=" * 65)

    for test in test_cases:
        try:
            actual = test["function"]()
            success = actual == test["expected"]

            if success:
                passed += 1
                status = "PASS"
            else:
                failed += 1
                status = "FAIL"

            print(f"\nTest:     {test['name']}")
            print(f"Expected: {test['expected']}")
            print(f"Actual:   {actual}")
            print(f"Status:   {status}")

        except (ValueError, TypeError, ZeroDivisionError) as error:
            failed += 1
            print(f"\nTest:   {test['name']}")
            print(f"Status: FAIL — {error}")

    print("\n" + "=" * 65)
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")
    print("=" * 65)

    if failed == 0:
        print("SUCCESS: All tests passed!")
    else:
        print("Some tests failed. Review the function implementations.")


def main():
    """Run the corrected program's automated tests."""
    print("Welcome to the Corrected Bug Fixing Project!")
    print("Author: Sourabh Rathore")

    run_tests()


if __name__ == "__main__":
    main()
