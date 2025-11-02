import os

# Generate a secure random salt
salt = os.urandom(32).hex()
