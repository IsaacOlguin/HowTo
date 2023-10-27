import _thread
import time

print("Begining")

def thread_task(threadName, delay):
    for count in range(1,6):
        time.sleep(delay)
        print("Thread name: {} Count: {}".format(threadName, count))

if __name__ == "__main__":
    print("Main")
    try:
        _thread.start_new_thread( thread_task, ("Thread-1", 2, ))
        _thread.start_new_thread( thread_task, ("Thread-2", 4, ))
    except Exception as error:
        print("Error: unable to start thread", error)

# This while-loop is required to actually how threads are created
while True:
   pass

# Interrupt the operation otherwise it will live forever

print("End")