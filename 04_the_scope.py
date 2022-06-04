# global scope
NAME = "Robert"
AGE = 100
ADDRESS = "Budapest"


def say_hello1():
    # local scope (say_hello1)
    name = "Kriszta"
    print(name)
    print(NAME)


def say_hello2():
    # local scope (say_hello2)
    name = "Tamás"
    print(name)


def say_hello3():
    # local scope (say_hello3)
    name = "Csilla"
    address = "Budapest"
    print(name)


say_hello1()
say_hello2()
say_hello3()