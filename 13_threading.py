import random, time, threading


def worker1(name):
    print(f"Worker1 started {name}")
    time.sleep(random.randint(3, 20))
    print("Worker1 finished")


def worker2(age):
    print(f"Worker2 started {age}")
    time.sleep(random.randint(3, 20))
    print("Worker2 finished")


def worker3(address):
    print(f"Worker3 started {address}")
    time.sleep(random.randint(3, 20))
    print("Worker3 finished")


t1 = threading.Thread(target=worker1, args=["Robert"])
t2 = threading.Thread(target=worker2, args=[42])
t3 = threading.Thread(target=worker3, args=["Budapest"])

t1.start()
t2.start()
t3.start()

print("Main thread finished")