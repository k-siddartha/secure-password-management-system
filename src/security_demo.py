#!/usr/bin/env python3
"""
Secure Password Management Demo
Author: k-siddartha
Purpose: Demonstrate core security concepts for portfolio
"""

import bcrypt
import pyotp
from cryptography.fernet import Fernet

# ========== 1. PASSWORD HASHING (bcrypt) ==========
print("=" * 50)
print("1. PASSWORD HASHING DEMO")
print("=" * 50)

password = "MySuperSecretPassword123"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print(f"Original password: {password}")
print(f"Bcrypt hash: {hashed.decode()}")

# Verify
is_correct = bcrypt.checkpw(password.encode(), hashed)
print(f"Verification successful? {is_correct}")
print()

# ========== 2. AES-256 ENCRYPTION (Fernet) ==========
print("=" * 50)
print("2. AES-256 ENCRYPTION DEMO")
print("=" * 50)

# Generate a key (this is AES-256 under the hood)
key = Fernet.generate_key()
cipher = Fernet(key)

secret_message = "My master password is: Hunter2"
encrypted = cipher.encrypt(secret_message.encode())
decrypted = cipher.decrypt(encrypted).decode()

print(f"Original message: {secret_message}")
print(f"Encrypted (AES-256): {encrypted.decode()}")
print(f"Decrypted: {decrypted}")
print()

# ========== 3. MFA SIMULATION (TOTP) ==========
print("=" * 50)
print("3. MULTI-FACTOR AUTH (TOTP) DEMO")
print("=" * 50)

# Generate a shared secret (this would be given to user)
shared_secret = pyotp.random_base32()
totp = pyotp.TOTP(shared_secret)

print(f"Shared secret (store securely): {shared_secret}")
print(f"Current TOTP code: {totp.now()}")
print(f"QR code URI (for Google Authenticator): {totp.provisioning_uri('siddartha@example.com')}")

# Verify a code (simulate user input)
user_code = input("\nEnter the TOTP code shown above to verify: ")
is_valid = totp.verify(user_code)
print(f"Code valid? {is_valid}")
