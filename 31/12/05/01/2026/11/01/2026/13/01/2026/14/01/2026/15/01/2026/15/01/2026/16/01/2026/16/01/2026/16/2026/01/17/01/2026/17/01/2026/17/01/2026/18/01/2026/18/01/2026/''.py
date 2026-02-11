def password_data():
    password = input("Please input your password: ")
    return password

password = password_data()

def check_password(password):
    if len(password) >= 8:
        return password
    else:
        return False

check_password(password)
print(check_password(password))