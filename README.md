# Bowling Game Testing Project

## Overview
This project is part of the IT7627 Software Testing and Maintenance assessment. It involves testing, debugging, and refactoring a faulty bowling game scoring system provided by the lecturer.

The goal was to identify defects in the original implementation, fix them, and verify correctness using automated unit testing.

---

## Features Tested
- Roll recording
- Score calculation
- Strike and spare handling
- Consecutive strikes
- Tenth frame bonus logic
- Full game scenarios
- Input validation

---

## Testing Approach
The system was tested as a complete functional unit using automated unit tests (Pytest).

Steps followed:
1. Execute tests on original lecturer code
2. Identify failing test cases
3. Debug and fix defects
4. Re-run tests to verify fixes
5. Refactor code for readability and maintainability

---

## Results
| Stage | Passed | Failed |
|------|------|------|
| Original Code | 2 | 14 |
| Fixed Code | 16 | 0 |

Final result: **100% pass rate**

---

## Technologies Used
- Python 3.12
- Pytest
- Git (version control)

---

## How to Run Tests

Install pytest if not already installed:

```bash
pip install pytest