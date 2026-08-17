# Password Strength Checker

This is a simple Python project that checks the strength of a password.

## What it checks

The program checks whether the password contains:

- At least 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

After checking these conditions, it classifies the password as:

- Weak
- Medium
- Strong

It also gives suggestions if the password can be improved.

## How to run

Make sure Python is installed.

Open the project folder in terminal and run:

```bash
python password_checker.py
```

Then enter a password when the program asks for it.

## Example

```text
Enter your password: hello123

Password Strength: Medium
Score: 3 / 5

Suggestions:
- Add at least one uppercase letter.
- Add at least one special character.
```

## Concepts used

This project uses basic Python concepts such as:

- Variables
- `if` / `elif` / `else`
- `for` loop
- Lists
- Strings
- Built-in string functions
