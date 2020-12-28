import library as x
#importing CRD main file as a library

x.Create("Aditya",95)
#Creating a key with key name,value given without Time-To-Live property.

x.Create("Hired",50,5000) 
#Creating a key with key name,value and Time-To-Live property value also given.

print(x.Read("Aditya"))
#This will return the value of the given key in json object format -> 'key name:value' if Time-To-live property is not expired, otherwise it will return Error

print(x.Read("Hired"))
#This will return the value of the given key in json object format -> 'key name:value' if Time-To-live property is not expired, otherwise it will return Error

x.Create("Freshworks",5000)
#This will return an ERROR as the key name already exists in the database or say data store.

x.Create("NotHired",0)
print(x.Read("NotHired"))
x.Delete("NotHired")
#This will delete the given key from the database or say data store.

#Code can also produce other errors:-
#If key length is greater than 32 chars. - "Error: Key Length should be less than 32 characters."
#If file size > than 1GB and json object value is also more than 16KB. - "Error: Memory Limit Exceeded!! "
#If entered key contain character other than alphabets. - "Error: Invalid key name, key name must contain only alphabetic charaters!!"
#If there is no key in the data store, key name was wrongly spelt or deleted earlier. - Error: Given Key Does Not Exist In Database. Please Enter Key That Exist.""

