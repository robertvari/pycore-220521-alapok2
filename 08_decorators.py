import time, random


def worker1():
    print("Worker 1 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 1 finished")


def worker2():
    print("Worker 2 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 2 finished")


def worker3():
    print("Worker 3 started...")
    time.sleep(random.uniform(3.0, 10.0))
    print("Worker 3 finished")


start_time = time.time()
worker1()
print(f"Process time: {time.time() - start_time}")

start_time = time.time()
worker2()
print(f"Process time: {time.time() - start_time}")

start_time = time.time()
worker3()
print(f"Process time: {time.time() - start_time}")