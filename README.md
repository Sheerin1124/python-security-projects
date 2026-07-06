# Password Strength Checker

A Python-based tool built during my Cybersecurity internship at **DecodeLabs**, evaluating password strength through string handling and conditional logic — no hashing or ML involved, just pure security fundamentals.

## What it does

Takes a password as input and classifies it as **Weak**, **Medium**, or **Strong** based on:

- **Length** — must be at least 8 characters
- **Digits** — contains at least one number
- **Uppercase letters** — contains at least one capital letter
- **Lowercase letters** — contains at least one lowercase letter
- **Symbols** — contains at least one non-alphanumeric character
- **Common password check** — flags passwords found in known leaked-password lists (e.g. `password123`, `qwerty123`)

It also gives feedback on exactly what's missing, so a user knows how to improve a weak password.

## How to run

```bash
py password-strength-checker.py
