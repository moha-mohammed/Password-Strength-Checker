import re
from colorama import Fore, Style

# Load common passwords from file (if exists)
try:
    with open("common_passwords.txt", "r", encoding="utf-8", errors="ignore") as f:
        COMMON_PASSWORDS = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    COMMON_PASSWORDS = []


def check_strength(password: str) -> str:
    """
    Check the strength of a given password and return a rating.
    """

    if password in COMMON_PASSWORDS:
        return "Very Weak ❌ (common password)"

    score = 0

    # Length checks
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase + lowercase letters
