import random
import string


# --------------------------------------------
# PASSWORD STRENGTH CHECKER
# --------------------------------------------

def password_strength_checker():

    password = input("Enter Password : ")

    score = 0

    upper = False
    lower = False
    digit = False
    symbol = False

    symbols = "!@#$%^&*()_-+=<>?/{}[]"

    for ch in password:

        if ch.isupper():
            upper = True

        elif ch.islower():
            lower = True

        elif ch.isdigit():
            digit = True

        elif ch in symbols:
            symbol = True

    length = len(password)

    if length >= 8:
        score += 20

    if length >= 12:
        score += 20

    if upper:
        score += 15

    if lower:
        score += 15

    if digit:
        score += 15

    if symbol:
        score += 15

    if length >= 16:
        score += 10

    print("\n" + "=" * 50)
    print("PASSWORD REPORT")
    print("=" * 50)

    print("Length :", length)

    print("Uppercase :", "Yes" if upper else "No")
    print("Lowercase :", "Yes" if lower else "No")
    print("Numbers :", "Yes" if digit else "No")
    print("Symbols :", "Yes" if symbol else "No")

    print("\nScore :", score, "/100")

    if score >= 90:
        level = "Excellent"

    elif score >= 75:
        level = "Strong"

    elif score >= 55:
        level = "Medium"

    elif score >= 35:
        level = "Weak"

    else:
        level = "Very Weak"

    print("Strength :", level)

    print("\nEstimated Crack Time")
    print(crack_time(score))

    print("\nSuggestions")

    suggestions(password, upper, lower, digit, symbol)


# --------------------------------------------
# ESTIMATED CRACK TIME
# --------------------------------------------

def crack_time(score):

    if score >= 90:
        return "Millions of Years"

    elif score >= 75:
        return "Thousands of Years"

    elif score >= 55:
        return "Several Months"

    elif score >= 35:
        return "Several Days"

    else:
        return "Few Seconds"


# --------------------------------------------
# PASSWORD SUGGESTIONS
# --------------------------------------------

def suggestions(password, upper, lower, digit, symbol):

    if len(password) < 12:
        print("- Increase password length.")

    if not upper:
        print("- Add uppercase letters.")

    if not lower:
        print("- Add lowercase letters.")

    if not digit:
        print("- Add numbers.")

    if not symbol:
        print("- Add special symbols.")

    if (len(password) >= 12
            and upper
            and lower
            and digit
            and symbol):

        print("Excellent Password.")


# --------------------------------------------
# PASSWORD GENERATOR
# --------------------------------------------

def password_generator():

    print()

    try:

        length = int(input("Enter Password Length : "))

    except:

        print("Invalid Input")
        return

    if length < 8:

        print("Minimum length is 8.")
        return

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    all_characters = (
        uppercase
        + lowercase
        + digits
        + symbols
    )

    password = []

    password.append(random.choice(uppercase))
    password.append(random.choice(lowercase))
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    while len(password) < length:

        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    print("\nGenerated Password\n")
    print(final_password)

    save = input("\nSave Password? (y/n) : ")

    if save.lower() == "y":

        save_password(final_password)

        print("Saved Successfully.")


# --------------------------------------------
# SAVE PASSWORD
# --------------------------------------------

def save_password(password):

    file = open("saved_passwords.txt", "a")

    file.write(password + "\n")

    file.close()


# --------------------------------------------
# PASSWORD STATISTICS
# --------------------------------------------

def password_statistics(password):

    letters = 0
    digits = 0
    symbols = 0

    for ch in password:

        if ch.isalpha():

            letters += 1

        elif ch.isdigit():

            digits += 1

        else:

            symbols += 1

    print("\nStatistics")

    print("Letters :", letters)
    print("Digits :", digits)
    print("Symbols :", symbols)


# --------------------------------------------
# CHECK COMMON PASSWORD
# --------------------------------------------

def common_password(password):

    common = [

        "password",
        "123456",
        "qwerty",
        "admin",
        "india123",
        "letmein",
        "welcome",
        "password123"

    ]

    if password.lower() in common:

        print("Warning : Common Password")

    else:

        print("Password is not common.")


# --------------------------------------------
# TEST
# --------------------------------------------

if __name__ == "__main__":

    while True:

        print("\n1 Strength Checker")
        print("2 Password Generator")
        print("3 Exit")

        choice = input("Choice : ")

        if choice == "1":

            password_strength_checker()

        elif choice == "2":

            password_generator()

        elif choice == "3":

            break

        else:

            print("Invalid Choice")
