# Password Strength Checker

A Python-based tool built during my Cybersecurity internship at **DecodeLabs**, evaluating password strength through string handling and conditional logic — no hashing or ML involved, just pure security fundamentals.

## What it does

Takes a password as input and classifies it as **Weak**, **Medium**, or **Strong** based on:

- **Length** — must be at least 8 characters
- **Digits** — contains at least one number
- **Uppercase letters** — contains at least one capital letter
- **Lowercase letters** — contains at least one lowercase letter
- **Symbols** — contains at least one non-alphanumeric character
- **Common password check** — flags passwords found in known leaked-password lists (e.g. password123, qwerty123)

It also gives feedback on exactly what's missing, so a user knows how to improve a weak password.

## How to run

py password-strength-checker.py

You'll be prompted to enter a password, then the tool prints its strength and feedback.

## Example

Enter your password: Hello@123

Strength: Strong
Feedback: All checks passed

## Concepts applied

- **Linear-time validation (O(n))** — the checker scans the password once per condition rather than repeatedly, keeping validation fast regardless of password length.
- **Entropy awareness** — character variety (digits, symbols, case) expands the possible search space an attacker would need to brute-force, which is why each check contributes to the strength score.
- **Defense-in-depth** — checking against known leaked passwords catches weak choices that technically meet length/complexity rules but are still unsafe.

## Part of

DecodeLabs Cybersecurity Internship — Industrial Training Kit, Project 1 (Defensive Logic track).