# Valid Credentials
valid_username = "user"
valid_password = "password123"

# Number of Attempts
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")

    if username == valid_username and password == valid_password:
        print("Login successful")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"failed to login, {remaining} attempts left")
        if attempts == max_attempts:
            print("account locked")
