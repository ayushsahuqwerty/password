"""
====================================================
HASHING MODULE
Personal Cybersecurity Toolkit
====================================================
"""

import hashlib
import os


# ----------------------------------------
# Calculate SHA-256 Hash
# ----------------------------------------

def file_hash(path):

    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")

    sha256 = hashlib.sha256()

    with open(path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# ----------------------------------------
# Calculate MD5 Hash
# ----------------------------------------

def md5_hash(path):

    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")

    md5 = hashlib.md5()

    with open(path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            md5.update(data)

    return md5.hexdigest()


# ----------------------------------------
# Calculate SHA1 Hash
# ----------------------------------------

def sha1_hash(path):

    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")

    sha1 = hashlib.sha1()

    with open(path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha1.update(data)

    return sha1.hexdigest()


# ----------------------------------------
# Calculate SHA512 Hash
# ----------------------------------------

def sha512_hash(path):

    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")

    sha512 = hashlib.sha512()

    with open(path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha512.update(data)

    return sha512.hexdigest()


# ----------------------------------------
# Verify SHA-256 Hash
# ----------------------------------------

def verify_hash(path, original_hash):

    current_hash = file_hash(path)

    print("\nCurrent Hash\n")
    print(current_hash)

    print("\nOriginal Hash\n")
    print(original_hash)

    if current_hash.lower() == original_hash.lower():

        print("\nFile Integrity Verified")
        print("The file has NOT been modified.")

    else:

        print("\nWARNING!")
        print("The file has been modified.")


# ----------------------------------------
# Display All Hashes
# ----------------------------------------

def all_hashes(path):

    print("=" * 60)
    print("FILE HASH REPORT")
    print("=" * 60)

    print("\nMD5")
    print(md5_hash(path))

    print("\nSHA1")
    print(sha1_hash(path))

    print("\nSHA256")
    print(file_hash(path))

    print("\nSHA512")
    print(sha512_hash(path))


# ----------------------------------------
# Save Report
# ----------------------------------------

def save_report(path):

    report = open("hash_report.txt", "w")

    report.write("FILE HASH REPORT\n")
    report.write("=" * 40)
    report.write("\n\n")

    report.write("File : " + path + "\n\n")

    report.write("MD5\n")
    report.write(md5_hash(path))
    report.write("\n\n")

    report.write("SHA1\n")
    report.write(sha1_hash(path))
    report.write("\n\n")

    report.write("SHA256\n")
    report.write(file_hash(path))
    report.write("\n\n")

    report.write("SHA512\n")
    report.write(sha512_hash(path))
    report.write("\n")

    report.close()

    print("\nReport saved as hash_report.txt")


# ----------------------------------------
# Compare Two Files
# ----------------------------------------

def compare_files(file1, file2):

    hash1 = file_hash(file1)
    hash2 = file_hash(file2)

    print("\nComparing Files...\n")

    if hash1 == hash2:

        print("Both files are IDENTICAL.")

    else:

        print("Files are DIFFERENT.")


# ----------------------------------------
# File Information
# ----------------------------------------

def file_information(path):

    if not os.path.exists(path):

        print("File not found.")
        return

    print("\nFILE INFORMATION")
    print("-" * 40)

    print("File Name :", os.path.basename(path))
    print("Location  :", os.path.abspath(path))
    print("Size      :", os.path.getsize(path), "Bytes")


# ----------------------------------------
# Demo
# ----------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("HASHING MODULE TEST")
    print("=" * 50)

    path = input("Enter File Path : ")

    try:

        file_information(path)

        print()

        all_hashes(path)

        save = input("\nSave Report? (y/n): ")

        if save.lower() == "y":

            save_report(path)

    except Exception as e:

        print("\nError :", e)
