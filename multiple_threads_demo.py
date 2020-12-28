import threading
# importing threading module for accessing the data store using multiple threads  
import library as x
# importing CRD main file as a library

#we can use multiple threads like
t1=threading.Thread(target=(x.Create or x.Read or x.Delete),args=("aditya",50,3600))
t1.start()
t2=threading.Thread(target=(x.Create or x.Read or x.Delete),args=("surana",25,10))
t2.start()
t1.join()
t2.join()

print(x.Read("aditya"))
print(x.Read("surana"))
