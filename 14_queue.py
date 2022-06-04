import time, random, threading, queue
from utilities.file_utils import get_all_files

# get a classic file list
root_folder = r"C:\Work\_PythonSuli\pycore-220521\photos"
file_list = []
get_all_files(root_folder, file_list)

# create a job queue
job_queue = queue.Queue()
for f in file_list:
    job_queue.put(f)

# create a file worker
def worker():
    while not job_queue.empty():
        my_job = job_queue.get()
        print(f"Working on: {my_job}")
        time.sleep(random.randint(3, 10))
        job_queue.task_done()


for _ in range(6):
    t = threading.Thread(target=worker)
    t.start()