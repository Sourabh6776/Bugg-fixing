# Bug Fixing Using Cursor AI

**Author:** Sourabh Rathore  
**College:** JECRC University, Jaipur  
**Course:** B.Tech CSE (AI/ML)  
**Semester:** III

## About the Project

This project demonstrates how common Python programming errors can be identified, corrected, and verified using automated tests.

The project contains an intentionally buggy Python program and a corrected implementation.

## Project Files

- `buggy_program.py` — Contains five intentionally introduced bugs.
- `fixed_program.py` — Contains the corrected implementations and automated tests.
- `README.md` — Project documentation.

## Bugs Identified and Fixed

### 1. Factorial Calculation
**Problem:** The result was initialized to zero, so multiplication always produced zero.

**Solution:** Initialize the result to `1`.

### 2. Fibonacci Series
**Problem:** The sequence started with the wrong value.

**Solution:** Append the first Fibonacci value before updating the sequence.

### 3. Average Calculation
**Problem:** An extra `1` was added to the calculated average.

**Solution:** Divide the sum of the numbers by the number of elements.

### 4. Grade Calculation
**Problem:** Incorrect comparison operators caused boundary values to receive the wrong grade.

**Solution:** Use appropriate inclusive comparison operators.

### 5. Passing Marks
**Problem:** A score of exactly `40` was excluded from the passing list.

**Solution:** Use a greater-than-or-equal-to comparison.

## Technologies Used

- Python 3
- Cursor IDE
- PowerShell Terminal
- Automated testing with Python functions

## How to Run the Buggy Version

From the main project directory, execute:

```powershell
python .\bug-fixing-project\buggy_program.py
```

This program intentionally contains errors. Some tests are expected to fail.

## How to Run the Corrected Version

Execute:

```powershell
python .\bug-fixing-project\fixed_program.py
```

The corrected program runs eight automated test cases.

Expected summary:

```text
Total tests: 8
Passed:      8
Failed:      0
SUCCESS: All tests passed!
```

## Learning Outcomes

This project demonstrates:

- Identifying logical programming errors
- Debugging Python functions
- Correcting calculation errors
- Handling boundary conditions
- Writing automated test cases
- Verifying expected and actual outputs
- Improving program reliability

## Conclusion

The project demonstrates how systematic debugging and automated testing help improve the correctness and reliability of Python programs.

## Author

**Sourabh Rathore**  
B.Tech CSE (AI/ML), Semester III  
JECRC University, Jaipur