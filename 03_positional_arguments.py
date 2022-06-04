def report_user(email, name, age, address):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Address: {address}")


# report_user("Robert", "robert@gmail.com", 42, "Budapest")
# report_user("Csaba", "csaba@gmail.com", 30, "Pécs")

# this is bad practice :((
# report_user(25, "Kriszta", "kriszta@gmail.com", "Kecskemét")

report_user(
    address="Kecskemét",
    age=25,
    name="Kriszta",
    email="kriszta@gmail.com"
)