def say_hello(name):
    print(f"Hello {name}")

    def nested_function():
        print(f"Hello {name}, I'm a nested function :)")

    nested_function()


say_hello("Csaba")