import random
import string
import time

print("=" * 40)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 40)

time.sleep(1)

length = int(input("Enter Password Length: "))

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(all_chars) for i in range(length))

print("\nGenerating Password...")
time.sleep(1)

print("\nYour Secure Password Is:")
print(password)

print("\nThank You!")