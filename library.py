import threading
import time

dict={} #'dict' to store data in dictionary format

#Create operation 
#timeout is optional, we can continue by passing two arguments without timeout.
def Create(key,value,timeout=0):
    if key in dict:
        print("Error: This Key Already Exists") #Error Message - if key is already present.
    else:
    	# Checking if the entered key contains only alphabetic charactered. 
        if(key.isalpha()):
        	#file size should be less than 1GB and Jason Object value should be less than 16KB 
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                #Input key length should be less than 32chars
                if len(key)<=32: 
                    dict[key]=l
                else:
                	print("Error: Key Length should be less than 32 characters") #Error Message - if key length is greater than 32 chars.
            else:
                print("Error: Memory Limit Exceeded!! ") #Error Message - If file size > than 1GB and json object value is also more than 16KB
        else:
            print("Error: Invalid key name, key name must contain only alphabetic charaters!!") #Error Message - if entered key contain character other than alphabets.

#Read operation  
def Read(key):
    if key not in dict:
        print("Error: Given Key Does Not Exist In Database. Please Enter Key That Exist.") #Error Message - if there is no given key in the data store.
    else:
        flag=dict[key]
        # flag[0] represents key's value
        # flag[1] represents timeout value
        if flag[1]!=0:
        	#Comparing the present time with expiry time
            if time.time() < flag[1]:
            	#Returning the string in the format of json object-> "key name:value"
                string=str(key)+":"+str(flag[0]) 
                return string
            else:
                print("Error: Time-To-Live Of",key,"Has Expired") #Error Message - if the time limit exceeded
        else:
            string=str(key)+":"+str(flag[0])
            return string

#Delete operation
def Delete(key):
    if key not in dict:
        print("Error: Given Key Does Not Exist In Database. Please Enter Key That Exist.") #Error Message - if there is no given key in the data store.
    else:
        flag=dict[key]
        # flag[0] represents key's value
        # flag[1] represents timeout value
        if flag[1]!=0:
        	#Comparing the current time with expiry time
            if time.time()<flag[1]:
                del dict[key]
                print("Key Is Successfully Deleted")
            else:
                print("Error: Time-To-Live Of",key,"Has Expired") #Error Message - if the time limit exceeded
        else:
            del dict[key]
            print("Key Is Successfully Deleted")
