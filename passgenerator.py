import string,random
print("pass generator".center(156,"-"))
chars = string.ascii_letters + string.digits + "!@#$%^&()-_=+/."
while True:
    try:
        length = int(input("Enter your password perferred length: " ))
    except ValueError:
        continue
    password = []
    for i in range(length):
        password.append(random.choice(chars))
    "".join(password)
    print("Your password: {}".format("".join(password)))
    while True:
         answer = input("Do you want another password?(Y/N): ").lower()
         if answer == "y" or answer == "n":
            break
    if answer == "n":
        break
