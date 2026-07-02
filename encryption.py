"""
=========================================================
ENCRYPTION MODULE
Personal Cybersecurity Toolkit
=========================================================
"""

import base64


# ==========================================
# BASE64 ENCRYPTION
# ==========================================

def encrypt_text(text):

    text_bytes = text.encode("utf-8")

    encrypted = base64.b64encode(text_bytes)

    return encrypted.decode("utf-8")


# ==========================================
# BASE64 DECRYPTION
# ==========================================

def decrypt_text(text):

    encrypted_bytes = text.encode("utf-8")

    decrypted = base64.b64decode(encrypted_bytes)

    return decrypted.decode("utf-8")


# ==========================================
# CAESAR CIPHER ENCRYPTION
# ==========================================

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        if char.isupper():

            result += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():

            result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:

            result += char

    return result


# ==========================================
# CAESAR CIPHER DECRYPTION
# ==========================================

def caesar_decrypt(text, shift):

    return caesar_encrypt(text, -shift)


# ==========================================
# XOR ENCRYPTION
# ==========================================

def xor_encrypt(text, key):

    encrypted = ""

    for i in range(len(text)):

        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return base64.b64encode(encrypted.encode()).decode()


# ==========================================
# XOR DECRYPTION
# ==========================================

def xor_decrypt(cipher, key):

    cipher = base64.b64decode(cipher).decode()

    decrypted = ""

    for i in range(len(cipher)):

        decrypted += chr(ord(cipher[i]) ^ ord(key[i % len(key)]))

    return decrypted


# ==========================================
# SAVE ENCRYPTED FILE
# ==========================================

def save_encrypted(filename, encrypted_text):

    with open(filename, "w", encoding="utf-8") as file:

        file.write(encrypted_text)

    print("Encrypted data saved successfully.")


# ==========================================
# LOAD ENCRYPTED FILE
# ==========================================

def load_encrypted(filename):

    with open(filename, "r", encoding="utf-8") as file:

        return file.read()


# ==========================================
# TEXT STATISTICS
# ==========================================

def text_statistics(text):

    letters = 0
    digits = 0
    spaces = 0
    symbols = 0

    for ch in text:

        if ch.isalpha():

            letters += 1

        elif ch.isdigit():

            digits += 1

        elif ch.isspace():

            spaces += 1

        else:

            symbols += 1

    print("\nTEXT STATISTICS")
    print("-" * 35)

    print("Letters :", letters)
    print("Digits  :", digits)
    print("Spaces  :", spaces)
    print("Symbols :", symbols)
  # ==========================================
# ENCRYPTION REPORT
# ==========================================

def encryption_report(original, encrypted):

    print("\n" + "=" * 50)
    print("ENCRYPTION REPORT")
    print("=" * 50)

    print("\nOriginal Text")
    print(original)

    print("\nEncrypted Text")
    print(encrypted)

    print("\nOriginal Length :", len(original))
    print("Encrypted Length :", len(encrypted))


# ==========================================
# FILE ENCRYPTION (BASE64)
# ==========================================

def encrypt_file(input_file, output_file):

    try:

        with open(input_file, "r", encoding="utf-8") as file:

            data = file.read()

        encrypted = encrypt_text(data)

        with open(output_file, "w", encoding="utf-8") as file:

            file.write(encrypted)

        print("File encrypted successfully.")

    except Exception as e:

        print("Error :", e)


# ==========================================
# FILE DECRYPTION (BASE64)
# ==========================================

def decrypt_file(input_file, output_file):

    try:

        with open(input_file, "r", encoding="utf-8") as file:

            data = file.read()

        decrypted = decrypt_text(data)

        with open(output_file, "w", encoding="utf-8") as file:

            file.write(decrypted)

        print("File decrypted successfully.")

    except Exception as e:

        print("Error :", e)


# ==========================================
# DEMO MENU
# ==========================================

def demo():

    while True:

        print("\n" + "=" * 50)
        print("ENCRYPTION MODULE")
        print("=" * 50)

        print("1. Base64 Encrypt")
        print("2. Base64 Decrypt")
        print("3. Caesar Encrypt")
        print("4. Caesar Decrypt")
        print("5. XOR Encrypt")
        print("6. XOR Decrypt")
        print("7. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            text = input("Enter Text : ")

            encrypted = encrypt_text(text)

            encryption_report(text, encrypted)

        elif choice == "2":

            text = input("Enter Encrypted Text : ")

            try:

                print("\nDecrypted Text")
                print(decrypt_text(text))

            except:

                print("Invalid encrypted text.")

        elif choice == "3":

            text = input("Enter Text : ")
            shift = int(input("Shift : "))

            print("\nEncrypted Text")
            print(caesar_encrypt(text, shift))

        elif choice == "4":

            text = input("Enter Encrypted Text : ")
            shift = int(input("Shift : "))

            print("\nDecrypted Text")
            print(caesar_decrypt(text, shift))

        elif choice == "5":

            text = input("Enter Text : ")
            key = input("Enter Secret Key : ")

            print("\nEncrypted Text")
            print(xor_encrypt(text, key))

        elif choice == "6":

            text = input("Enter Encrypted Text : ")
            key = input("Enter Secret Key : ")

            try:

                print("\nDecrypted Text")
                print(xor_decrypt(text, key))

            except:

                print("Wrong key or invalid text.")

        elif choice == "7":

            print("\nReturning...")
            break

        else:

            print("Invalid Choice")


# ==========================================
# MODULE TEST
# ==========================================

if __name__ == "__main__":

    demo()
