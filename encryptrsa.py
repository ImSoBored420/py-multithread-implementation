import os
import threading
import time

def deleteUIelements():
    print("y")
    #path1 = "C:\Windows\SystemResources\imageres.dll.mun"
    #os.remove(path1)
    
# Define a function for the thread to execute
def print_numbers(start_event, done_event):
    start_event.wait()
    time.sleep(1)
    for i in range(5):
        os.system("start https://google.com")
    done_event.set()
def francefreestyle(start_event, done_event):
    start_event.wait()
    time.sleep(1)
    for i in range(5):
        os.system("start https://newgrounds.com")
    done_event.set()


# Create Event objects to synchronize the start and completion of threads
start_event = threading.Event()
done_event1 = threading.Event()
done_event2 = threading.Event()
# Create Thread objects targeting the functions
thread1 = threading.Thread(target=print_numbers, args=(start_event, done_event1))
thread2 = threading.Thread(target=francefreestyle, args=(start_event, done_event2))
# Start the threads
thread1.start()
thread2.start()
# Signal the threads to start
start_event.set()
# Wait for both threads to complete
done_event1.wait()
done_event2.wait()

if thread1 or thread2:
    print("yo we did it")
if not thread1 or thread2:
    print("yo we fucked up")
else:
    print("yo we fucked up so much, it's not even thread 1 or 2's fault")