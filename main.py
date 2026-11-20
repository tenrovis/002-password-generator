import secrets
import string

x = string.ascii_letters + string.digits + string.punctuation

password = list(secrets.choice(string.ascii_uppercase)+secrets.choice(string.ascii_lowercase)+secrets.choice(string.digits)+secrets.choice(string.punctuation)) 

try:
    length = int(input("Enter password length from 4 to 32 chars: "))
except ValueError:
    print("You can enter only the number!")
else:
    if length > 32 or length < 4:
        print("Length should be from 4 to 32")
    else:
        for i in range(length-4):
            password.append(secrets.choice(x))
        secrets.SystemRandom().shuffle(password)
        print("".join(password))
