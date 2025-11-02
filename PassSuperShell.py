import hashlib
import secrets

# Generate a 32-character password
password = secrets.token_urlsafe(32)

# Calculate the MD5 sum of the password
md5_sum = hashlib.md5(password.encode()).hexdigest()

print("Password:", password)
print("MD5 Sum:", md5_sum)
