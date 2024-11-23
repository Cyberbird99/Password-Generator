# Password-Generator
The repository is a bunch of codes to generate a new password with a specific length of string.
password_generator_simple contains only random and string libraries.
There's a function which generates a random password of a specified length.
Inside the function is a chracter_pool which combines letters, digits and some specific puctuation characters.

password_gnerator_complex.py is much improved with these key features:
instead of random library, secrets library is used which is more secure than using random.choice() for generating passwords, as secrets is specifically designed for cryptographic security.

Password Strength Check: The password generator ensures that at least one character from each category (uppercase, lowercase, digit, punctuation) is included. This increases password strength.

Length Check: The code warns if the user selects a password length shorter than 12 characters, which is typically recommended for strong passwords.

Loop Until Criteria Met: The loop ensures that the password meets the strength requirements before being returned.
