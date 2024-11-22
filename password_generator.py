import random
import string


def generate_random_string(length: int=15):
    # Define the character pool (letters, digits, and punctuation)
    character_pool = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the character pool
    generated_password = "".join(random.choice(character_pool) for i in range(length))
    return generated_password

# Generate a random password
new_password = generate_random_string()

# Print the generated password
print(f"Generated password: {new_password}")