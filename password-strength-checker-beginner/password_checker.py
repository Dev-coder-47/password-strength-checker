# Password Strength Checker
# Beginner Python Project

print("===================================")
print("     PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

score = 0
suggestions = []

# Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Password should have at least 8 characters.")

# Variables for checking different character types
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

special_characters = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|"

# Check every character in the password
for character in password:
    if character.isupper():
        has_uppercase = True
    elif character.islower():
        has_lowercase = True
    elif character.isdigit():
        has_number = True
    elif character in special_characters:
        has_special = True

# Give score and suggestions
if has_uppercase:
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

if has_lowercase:
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

if has_number:
    score += 1
else:
    suggestions.append("Add at least one number.")

if has_special:
    score += 1
else:
    suggestions.append("Add at least one special character.")

# Decide password strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")

# Show suggestions
if len(suggestions) > 0:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nGood password! It meets all the basic requirements.")
