import time, random


# func = function
def my_timer(func):

    # get all params...
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # provide all params to function
        # catch return
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start_time}")

        # return function result
        return result

    return wrapper


def do_nothing(func):
    def wrapper(*args, **kwargs):
        print("Hello! I Do nothing here...")
        result = func(*args, **kwargs)
        print("Did nothing :))")
        return result

    return wrapper


@my_timer
@do_nothing
def worker1(name):
    print("Worker 1 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 1 finished")

    return 42


@my_timer
def worker2():
    print("Worker 2 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 2 finished")


@my_timer
@do_nothing
def worker3(address):
    print("Worker 3 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 3 finished")


result = worker1("Robert")
print(result)