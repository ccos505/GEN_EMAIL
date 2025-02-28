# Deterministic Credentials Generator

This Python script generates deterministic credentials including **Thai names, email, password, and date of birth**. The email and password change **monthly**, while the name and date of birth remain **static** for each username.

## Features

✅ Generates **Thai first name and surname** (transliterated into English).  
✅ Creates a **deterministic email** that updates **every month**.  
✅ Generates a **secure deterministic password** that updates **every month**.  
✅ Ensures a **static date of birth** (age around 20-40 years).  
✅ Uses **SHA-256 hashing** to ensure consistency across runs.

## Installation

This script runs with Python 3. No external dependencies are required.

## Usage

```python
# Import and initialize the generator
from credentials_generator import DeterministicCredentialsGenerator

generator = DeterministicCredentialsGenerator("gmail.com", 12)
credentials = generator.generate_credentials()

print(f"First Name: {credentials['first_name']}")
print(f"Surname: {credentials['surname']}")
print(f"Email: {credentials['email']}")
print(f"Password: {credentials['password']}")
print(f"Date of Birth: {credentials['date_of_birth']}")
```

## Example Output

```
First Name: Mana
Surname: Rungreung
Email: mana.rungreung5f3b8a21@gmail.com
Password: @dGhpc2lzYXNhZmU=
Date of Birth: 2003-07-15
```

## How It Works

1. **First name and surname** are generated based on the username and remain static.
2. **Email and password** are generated based on the **current month**, so they update automatically.
3. **Date of birth** remains static but ensures an age range of **20-40 years**.
4. **SHA-256 hashing** is used to maintain idempotency (same input → same output).

## License

This project is open-source. Feel free to modify and use it!

---

Made with ❤️ for deterministic and secure identity generation! 🚀
