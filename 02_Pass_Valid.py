password = input("Enter your password: ")
if len(password) < 8:
    print("Invalid Password")
else:
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")
