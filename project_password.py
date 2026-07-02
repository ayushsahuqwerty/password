"""
=========================================================
        PERSONAL CYBERSECURITY TOOLKIT
        Python Challenge Project
=========================================================
Author : Your Name
Language : Python 3
=========================================================
"""

import os
from password import password_strength_checker
from password import password_generator

from hashing import file_hash
from hashing import verify_hash

from encryption import encrypt_text
from encryption import decrypt_text

from qr_generator import create_qr


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def banner():

    print("=" * 60)
    print("        PERSONAL CYBERSECURITY TOOLKIT")
    print("=" * 60)
    print("Password Security")
    print("Encryption")
    print("File Hashing")
    print("QR Code Generator")
    print("=" * 60)


def menu():

    while True:

        clear()
        banner()

        print("\nMAIN MENU\n")

        print("1. Password Strength Checker")
        print("2. Secure Password Generator")
        print("3. Generate SHA256 File Hash")
        print("4. Verify File Hash")
        print("5. Encrypt Text")
        print("6. Decrypt Text")
        print("7. Generate QR Code")
        print("8. About Project")
        print("9. Exit")

        choice = input("\nEnter choice : ")

        if choice == "1":

            clear()
            print("PASSWORD STRENGTH CHECKER\n")
            password_strength_checker()
            pause()

        elif choice == "2":

            clear()
            print("PASSWORD GENERATOR\n")
            password_generator()
            pause()

        elif choice == "3":

            clear()
            print("SHA256 HASH GENERATOR\n")
            path = input("Enter file path : ")

            try:
                result = file_hash(path)
                print("\nSHA256 HASH\n")
                print(result)

            except Exception as e:
                print("\nError :", e)

            pause()

        elif choice == "4":

            clear()
            print("HASH VERIFIER\n")

            path = input("Enter file path : ")
            original = input("Enter original hash : ")

            try:

                verify_hash(path, original)

            except Exception as e:

                print(e)

            pause()

        elif choice == "5":

            clear()
            print("TEXT ENCRYPTION\n")

            text = input("Enter text : ")

            encrypted = encrypt_text(text)

            print("\nEncrypted Text\n")
            print(encrypted)

            pause()

        elif choice == "6":

            clear()
            print("TEXT DECRYPTION\n")

            text = input("Enter encrypted text : ")

            try:

                decrypted = decrypt_text(text)

                print("\nDecrypted Text\n")
                print(decrypted)

            except Exception:

                print("Invalid encrypted text.")

            pause()

        elif choice == "7":

            clear()

            print("QR CODE GENERATOR\n")

            data = input("Enter text or URL : ")

            try:

                filename = create_qr(data)

                print("\nQR Code Saved Successfully!")
                print("Filename :", filename)

            except Exception as e:

                print(e)

            pause()

        elif choice == "8":

            clear()

            print("=" * 60)
            print("ABOUT PROJECT")
            print("=" * 60)

            print("""
Personal Cybersecurity Toolkit

This project demonstrates
-------------------------------------
* Password Strength Checking
* Password Generation
* SHA256 File Hashing
* Hash Verification
* Base64 Encryption
* Base64 Decryption
* QR Code Generation

Python Concepts Used
-------------------------------------
Functions
Loops
Modules
Exception Handling
File Handling
Random Module
Hashlib Module
Base64 Module
OS Module

Developed for Python Challenge.
""")

            pause()

        elif choice == "9":

            print("\nThank You for using Cybersecurity Toolkit.")
            break

        else:

            print("\nInvalid Choice.")
            pause()


if __name__ == "__main__":

    menu()
