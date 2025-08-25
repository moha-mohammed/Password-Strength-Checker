
---

## 🐍 `checker.py`
```python
import re
from colorama import Fore, Style

# List of very common weak passwords (you can expand this)
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "111111", "123123"]

def check_password_strength(password: str) -> str:
    if password in COMMON_PASSWORDS:
        return "Very Weak ❌ (common password)"

    score = 0

    # Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Upper & lower
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    # Final rating
    if score <= 2:
        return "Weak ❌"
    elif score == 3:
        return "Medium ⚠️"
    elif score >= 4:
        return "Strong ✅"

if __name__ == "__main__":
    pwd = input("Enter a password: ")
    strength = check_password_strength(pwd)
    print(Fore.CYAN + f"Strength: {strength}" + Style.RESET_ALL)
