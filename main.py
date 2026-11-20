import random
import string

x = string.ascii_letters + string.digits + string.punctuation

password = ""
try:
    length = int(input("Enter password length from 4 to 32 chars: "))
except ValueError:
    print("You can enter only the number!")
else:
    if length > 32 or length < 4:
        print("Length should be from 4 to 32")
    else:
        for i in range(length):
            password += random.choice(x)
        print(password)
