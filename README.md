# Password Strength Checker

A simple Python project that checks the strength of a password based on basic security rules.

I built this project to understand how password security works and to practice basic Python concepts such as conditions, loops, strings, and lists.

## Features

The program checks whether a password contains:

* At least 8 characters
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Based on these checks, the password is classified as:

* **Weak**
* **Medium**
* **Strong**

The program also gives suggestions to improve the password if some requirements are missing.

## How It Works

Each password gets a score based on the following conditions:

| Requirement                | Score |
| -------------------------- | ----: |
| At least 8 characters      |    +1 |
| Contains uppercase letter  |    +1 |
| Contains lowercase letter  |    +1 |
| Contains number            |    +1 |
| Contains special character |    +1 |

The final strength is decided using the total score:

* **0–2 points:** Weak
* **3–4 points:** Medium
* **5 points:** Strong

## Project Structure

```text
password-strength-checker/
│
├── password_checker.py
├── README.md
└── .gitignore
```

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/Dev-coder-47/password-strength-checker.git
```

Move into the project folder:

```bash
cd password-strength-checker
```

Run the program:

```bash
python password_checker.py
```

## Example

```text
===================================
     PASSWORD STRENGTH CHECKER
===================================

Enter your password: hello123

Password Strength: Medium
Score: 3 / 5

Suggestions:
- Add at least one uppercase letter.
- Add at least one special character.
```

Another example:

```text
Enter your password: Hello@123

Password Strength: Strong
Score: 5 / 5

Good password! It meets all the basic requirements.
```

## Python Concepts Used

While building this project, I practiced:

* Variables
* `if`, `elif`, and `else`
* `for` loops
* Lists
* Strings
* `len()`
* `.isupper()`
* `.islower()`
* `.isdigit()`

## What I Learned

This project helped me understand how simple password-strength checking can be implemented using Python.

I also learned that passwords can be evaluated using different factors such as length and character variety, and that users can be given suggestions to improve weak passwords.

## Limitations

This project uses basic password-strength rules for learning purposes.

A real-world password security system may also check:

* Common or leaked passwords
* Repeated patterns
* Dictionary words
* Password entropy
* Previously compromised passwords

So a password marked as **Strong** by this program only means that it passes the basic checks implemented in this project.

## Future Improvements

Some improvements I may add in the future:

* Common password detection
* Password generator
* Better password scoring
* Graphical user interface
* Password entropy calculation

## Author

**Dev Saini**

GitHub: [Dev-coder-47](https://github.com/Dev-coder-47)
