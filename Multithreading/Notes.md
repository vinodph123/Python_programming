	- In python multithreading can be done by using package "Threading"
	- Threading package provides us all sort of methods for multithreading


To create thread using threading package in python :

Ex : a = threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

	- Group Is reserved for future
	- Target is thread handler function where thread function definition
	- Name is the name can be given to the threads while creating
	- Args are the input touples passed as arguments to the thread function
	- Kwargs also passed as input the to the thread function
	- Daemon is nothing but similar to join()
	- Daemon threads are nothing but threads are running in background and processing the required for non-daemon thread(Main thread) but daemon threads will terminate before non-daemon thread terminates when daemon flag set as True 
	- Native_id() -> this will give the thread id of the thread 
	- By default all threads are non-daemon means if main thread terminates and still process is going on in child threads then child threads will continue to execute and terminates once done
	- If daemon is set then daemon threads will terminate if non-daemon thread terminates(Main thread) So it is similar to join()
	- The below example output when daemon is set to the child threads without join() to the main thread 

Main thread = 7540, Thread a = 11840, Thread b = 6192

Refer fig 1 in attached files

	- Below example is for when child threads are not set as daemon the child threads will complete their task completely even though main threads ends 

Main thread = 9980, Thread a = 6336, Thread b = 12120

Refer fig 2 in attached files

	- Ex : below when both child threads are joined to main thread but here main thread can complete its task however can close only once child threads completes their task 

Main thread = 11184, Thread a = 10840, Thread b = 3976

Refer fig 3 in attached files





