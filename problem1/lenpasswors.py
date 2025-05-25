import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Medium ⚠️"
    elif score == 2:
        strength = "Weak ❗"
    else:
        strength = "Very Weak ❌"

    print("Password Strength:", strength)

# User input
user_password = input("Enter your password: ")
check_password_strength(user_password)