"""
Caesar & Vigenere Cipher Tool
DecodeLabs Internship - Project 2
Cyber Security Track (Defensive Logic)

Features:
1. Caesar Cipher - encrypt/decrypt using a single shift value
2. Vigenere Cipher - encrypt/decrypt using a keyword
3. Handles uppercase, lowercase, and leaves non-letters unchanged
"""


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # keep spaces, numbers, symbols unchanged
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text, keyword):
    result = ""
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1  # only advance key on actual letters
        else:
            result += char

    return result


def vigenere_decrypt(text, keyword):
    result = ""
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char

    return result


def main():
    print("=== Caesar & Vigenere Cipher Tool ===")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    choice = input("Choose cipher (1 or 2): ").strip()

    mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    text = input("Enter your text: ")

    if choice == "1":
        shift = int(input("Enter shift value (e.g. 3): "))
        if mode == "e":
            output = caesar_encrypt(text, shift)
        else:
            output = caesar_decrypt(text, shift)

    elif choice == "2":
        keyword = input("Enter keyword: ").strip()
        if not keyword.isalpha():
            print("Keyword must contain only letters.")
            return
        if mode == "e":
            output = vigenere_encrypt(text, keyword)
        else:
            output = vigenere_decrypt(text, keyword)

    else:
        print("Invalid choice.")
        return

    print(f"\nResult: {output}")


if __name__ == "__main__":
    main()