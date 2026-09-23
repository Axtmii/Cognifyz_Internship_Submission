def is_valid_email(email):
    if "@" not in email:
        return False

    username, domain = email.split("@", 1)

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True


email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")