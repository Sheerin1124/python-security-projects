# Caesar & Vigenere Cipher Tool

A Python-based encryption tool built during my Cybersecurity internship at **DecodeLabs**, implementing two classic substitution ciphers.

## What it does

Encrypts or decrypts text using either:

- **Caesar Cipher** — shifts each letter by a fixed number of positions
- **Vigenere Cipher** — shifts each letter using a repeating keyword, making the encryption much stronger than Caesar alone

Non-letter characters (spaces, numbers, symbols) are left unchanged, and both uppercase and lowercase letters are handled correctly.

## How to run

py ceaser_vigenere_cipher.py

You'll be asked to choose a cipher, encrypt or decrypt mode, and enter your text (plus a shift number or keyword depending on the cipher).

## Example

Choose cipher (1 or 2): 2
Encrypt or Decrypt? (e/d): e
Enter your text: HELLO
Enter keyword: KEY

Result: RIJVS

## Concepts applied

- **Modular arithmetic** — using `% 26` to wrap letters around the alphabet instead of going out of bounds
- **Polyalphabetic substitution** — Vigenere uses a different shift per letter (based on the keyword), unlike Caesar's single fixed shift, making frequency analysis attacks much harder
- **Input validation** — keyword is checked to ensure it contains only letters before encryption begins

## Part of

DecodeLabs Cybersecurity Internship — Industrial Training Kit, Project 2 (Defensive Logic track).