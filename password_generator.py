import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

if length < 6:
    print("Password should be at least 6 characters for safety!")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    print(f"\nGenerated Password: {password}")
    print("Keep it safe! Don't share with anyone.")
