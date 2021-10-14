#############################################################################
# Program : Multithreading demonstration using threading package from python
# Author : Vinod H
# Date : 10/11/2021
# Details :
# Thread can be created using 
# threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# target -> thread_handler_function
# name -> name can be given to the thread
# args and kwargs -> input arguments can be passed to thread functions
# daemon -> to set the child threads as daemon -> For more details please check Notes.md file
#############################################################################


import threading
import time

g = 0 # Common shared buffer section shared to all threads
key = threading.Lock() # Mutex lock created to achieve synchronisation


def fun():
    global g
    key.acquire(blocking=True) #Acquiring the lock to the critical section
    for i in range(100000000):
        g = g + 1
    key.release() #Releasing the lock for critical section 


def fun1():
    global g
    key.acquire(blocking=True)
    for i in range(100000000):
        g = g + 1
    key.release()


if __name__ == '__main__':
    print(f'Main thread id = {threading.current_thread()}') # This will provide main/current thread id details
    print(f'Main thread id = {threading.main_thread()}') # This will provide main/current thread id details
    a = threading.Thread(target=fun, name='vinod') # Named Thread_1 as vinod
    b = threading.Thread(target=fun1)
    print(a.isDaemon()) # Returns True if thread is daemon
    print(b.isDaemon())
    #a.setDaemon(daemonic=True) # This is used to set the thread as daemon
    #b.setDaemon(daemonic=True)
    a.start() #To start the thread created
    b.start()
    print(f'Main thread = {threading.main_thread().native_id}, Thread a = {a.native_id}, Thread b = {b.native_id}')
    print(f'{threading.main_thread().native_id,a.native_id,b.native_id}')
    print(f'I am thread a = {a}')
    print(f'I am thread b = {b}')
    print('Before the join ', a.is_alive()) # This method is used to verify whether the thread is alive or not
    print('Before the join ', b.is_alive())
    a.join() # Join() is used to block the main thread from terminating untill child threads terminates
    b.join()
    #print('After the join ', a.is_alive())
    #print('After the join ', b.is_alive())
    for i in range(10):
        print(i)
    print('Main thread ends its programming execution')
    print(a.is_alive())
    print(b.is_alive())
    print('Thread a is daemon ? = ', a.isDaemon())
    print('Thread b is daemon ? = ', a.isDaemon())
    print(g)
    print(a.is_alive())
    print(b.is_alive())
    #time.sleep(10)

