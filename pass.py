import random
import string

def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Test the password generator
password_length = 10
password = generate_password(password_length)
print(f"Generated Password: {password}")
