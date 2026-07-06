"""
Password Strength Checker
DecodeLabs Internship - Project 1
Cyber Security Track (Defensive Logic)

Checks:
1. Minimum length (8 characters)
2. Presence of digits
3. Presence of uppercase letters
4. Presence of symbols
5. Common/leaked password check (bonus, from PDF conclusion)
"""

# A tiny sample of very common leaked passwords (real-world checkers use huge lists)
COMMON_PASSWORDS = {
    "password", "password123", "12345678", "qwerty123",
    "letmein", "admin123", "welcome1", "iloveyou"
}


def check_password_strength(password):
    # Step 1: Common/leaked password check (checked first - no point scoring a known-bad password)
    if password.lower() in COMMON_PASSWORDS:
        return "Weak", "This password appears in common leaked password lists"

    # Step 2: Length check (gatekeeper - immediate fail if too short)
    if len(password) < 8:
        return "Weak", "Password must be at least 8 characters"

    # Step 3: Character variety checks
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Step 4: Score the password
    score = sum([has_digit, has_upper, has_lower, has_symbol])

    # Step 5: Classify based on score
    if score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # Build feedback on what's missing
    missing = []
    if not has_digit:
        missing.append("a number")
    if not has_upper:
        missing.append("an uppercase letter")
    if not has_lower:
        missing.append("a lowercase letter")
    if not has_symbol:
        missing.append("a symbol")

    if missing:
        feedback = "Missing: " + ", ".join(missing)
    else:
        feedback = "All checks passed"

    return strength, feedback


def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"\nStrength: {strength}")
    print(f"Feedback: {feedback}")


if __name__ == "__main__":
    main()