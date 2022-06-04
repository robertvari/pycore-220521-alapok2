#                 positional required        default param
def register_user(name, password, email=None, age=None, address=None):
    print(f"Name: {name}")
    print(f"Password: {password}")

    if email:
        print(f"Email: {email}")

    if age:
        print(f"Age: {age}")

    if address:
        print(f"Address: {address}")


register_user(
    "Robert",
    "testpas123",
    "robert@gmail.com"
)