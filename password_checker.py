import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!, @, #, etc.).")

    # Strength evaluation
    if strength == 5:
        result = "Strong Password ✅"
    elif strength >= 3:
        result = "Moderate Password ⚠️"
    else:
        result = "Weak Password ❌"

    return result, feedback


# Main Program
print("🔐 Password Complexity Checker 🔍")
user_password = input("Enter your password: ")
strength_result, suggestions = check_password_strength(user_password)

print("\nResult:", strength_result)
if suggestions:
    print("\nSuggestions to improve your password:")
    for suggestion in suggestions:
        print("- " + suggestion)
