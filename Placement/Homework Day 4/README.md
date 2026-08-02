# Homework — Day 4 (Conditionals)

This folder contains homework exercises assigned during Day 4 of the placement training. The exercises focus on conditional statements and comparison logic in Python.

How to run

- Use Python 3.x.
- From the repository root, run a script with:

  ```bash
  python3 "Placement/Homework Day 4/<script_name>.py"
  ```

Files and purpose

- `biggest_of_two.py`
  - Purpose: Prompts for two integers and prints which one is bigger.
  - Behavior: Reads two integers from stdin (`input()`), compares them, and prints either "First number is biggest" or "Second number is biggest".
  - Note: The current implementation does not explicitly handle the case where the numbers are equal — it will report "Second number is biggest" when `a` is not greater than `b`. Consider adding an equality check if you want a different message for equal values.
  - Example usage:
    ```bash
    python3 "Placement/Homework Day 4/biggest_of_two.py"
    # Input (interactive):
    # Enter first number: 5
    # Enter second number: 3
    # Output:
    # First number is biggest
    ```

- `divisible_by_5_and_11.py`
  - Purpose: Check whether a given number is divisible by 5, by 11, by both, or by neither, and print the appropriate message.
  - Example usage:
    ```bash
    python3 "Placement/Homework Day 4/divisible_by_5_and_11.py"
    # The script may prompt for an integer input
    ```

- `homework.py`
  - Purpose: Small practice script that determines whether a number is even or odd.
  - Behavior: Reads an integer from stdin and prints `Even` if it is divisible by 2, otherwise prints `Odd`.
  - Example usage:
    ```bash
    python3 "Placement/Homework Day 4/homework.py"
    # Input (interactive):
    # Enter a number: 4
    # Output:
    # Even
    ```

- `largest_of_three_num.py`
  - Purpose: Determine and print the largest of three numbers using conditional logic.
  - Example usage:
    ```bash
    python3 "Placement/Homework Day 4/largest_of_three_num.py"
    ```

- `placement_eligiblity.py`
  - Purpose: Example script that evaluates placement eligibility based on criteria such as marks, attendance, or other thresholds.
  - Note: Filename contains a typo (`placement_eligiblity.py`). There is also a correctly spelled `placement_eligibility.py` in `Placement/Day 4/`. Consider consolidating and keeping the correctly spelled filename.

Notes and suggestions

- The files `biggest_of_two.py` and `homework.py` are implemented; I updated this README to reflect their actual behavior and included interactive examples.
- Suggested improvements:
  - Add an equality case to `biggest_of_two.py` to explicitly print when the numbers are equal.
  - Consider renaming paths/files to avoid spaces (e.g., `Homework Day 4` -> `homework_day_04`) to make scripting and CI simpler.
  - If you want, I can implement the equality check and add a small test runner (or a `--example` flag) to each script so they can be run non-interactively for demonstrations.
