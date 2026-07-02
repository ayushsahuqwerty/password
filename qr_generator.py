"""
=========================================================
QR CODE GENERATOR
Personal Cybersecurity Toolkit
=========================================================
"""

import os
import qrcode
from datetime import datetime


# ------------------------------------------
# Create QR Code
# ------------------------------------------

def create_qr(data):

    if data.strip() == "":
        raise ValueError("Input cannot be empty.")

    folder = "generated_qr"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    filepath = os.path.join(folder, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black",
                          back_color="white")

    image.save(filepath)

    return filepath


# ------------------------------------------
# QR Information
# ------------------------------------------

def qr_information():

    print("=" * 45)
    print("QR CODE INFORMATION")
    print("=" * 45)

    print("• Supports text")
    print("• Supports URLs")
    print("• Supports phone numbers")
    print("• Supports email addresses")
    print("• Saves PNG images")


# ------------------------------------------
# Demo Program
# ------------------------------------------

def demo():

    while True:

        print("\n" + "=" * 45)
        print("QR CODE GENERATOR")
        print("=" * 45)

        print("1. Generate QR")
        print("2. Information")
        print("3. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            text = input("\nEnter Text or URL : ")

            try:

                path = create_qr(text)

                print("\nQR Generated Successfully!")

                print("Saved At :")
                print(path)

            except Exception as e:

                print("Error :", e)

        elif choice == "2":

            qr_information()

        elif choice == "3":

            print("Goodbye.")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":

    demo()
