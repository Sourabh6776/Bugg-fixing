"""
=========================================================
BUG FIXING USING CURSOR AI
Author: Sourabh Rathore
College: JECRC University, Jaipur
Course: B.Tech CSE (AI/ML)

Purpose:
Demonstrate common Python programming bugs and
their corrected implementations.
=========================================================
"""


# BUG 1: Incorrect factorial calculation
def calculate_factorial(number):
    """Calculate the factorial of a non-negative integer."""
    result = 0

    for value in range(1, number + 1):
        result *= value

    return result


# BUG 2: Incorrect Fibonacci sequence
def generate_fibonacci(count):
    """Generate the first 'count' Fibonacci numbers."""
    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(second)
        first, second = second, first + second

    return sequence


# BUG 3: Incorrect average calculation
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)

    return total / len(numbers) + 1


# BUG 4: Incorrect grade boundary
def calculate_grade(average):
    """Return a grade based on the average marks."""
    if average > 90:
        return "A"

    elif average > 75:
        return "B"

    elif average > 60:
        return "C"

    else:
        return "F"


# BUG 5: Incorrect list filtering
def filter_passing_marks(marks):
    """Return marks that are at least 40."""
    passing_marks = []

    for mark in marks:
        if mark > 40:
            passing_marks.append(mark)

    return passing_marks


def run_tests():
    """Run test cases and display actual versus expected results."""
    test_cases = [
        {
            "name": "Factorial of 5",
            "actual": calculate_factorial(5),
            "expected": 120,
        },
        {
            "name": "First 5 Fibonacci numbers",
            "actual": generate_fibonacci(5),
            "expected": [0, 1, 1, 2, 3],
        },
        {
            "name": "Average of [10, 20, 30]",
            "actual": calculate_average([10, 20, 30]),
            "expected": 20,
        },
        {
            "name": "Grade for average 90",
            "actual": calculate_grade(90),
            "expected": "A",
        },
        {
            "name": "Passing marks including 40",
            "actual": filter_passing_marks([30, 40, 50, 80]),
            "expected": [40, 50, 80],
        },
    ]

    print("\n" + "=" * 60)
    print("BUG FIXING PROJECT — TEST RESULTS")
    print("=" * 60)

    passed = 0

    for test in test_cases:
        success = test["actual"] == test["expected"]
        status = "PASS" if success else "FAIL"

        print(f"\nTest: {test['name']}")
        print(f"Expected: {test['expected']}")
        print(f"Actual:   {test['actual']}")
        print(f"Status:   {status}")

        if success:
            passed += 1

    print("\n" + "=" * 60)
    print(f"Tests passed: {passed}/{len(test_cases)}")
    print("=" * 60)


def main():
    """Run the bug demonstration tests."""
    print("Welcome to the Bug Fixing Using Cursor AI project!")
    print("This version intentionally contains five bugs.")

    run_tests()


if __name__ == "__main__":
    main()
