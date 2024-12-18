#A dictionary is built-in data structure in python that allows you to store a collection of key-value pairs . dictionary is mutable and it is unordered
my_dict={
    "std_id":123,
    "std_name":"Shaktiya",
    "course":"BscIT"
    }
print(my_dict)

x=my_dict["course"]
print("The course selected is ",x)

x=my_dict.get("std_id")
#find all the key present in the dictionary

y=my_dict.keys()
print("The keys present are: ",y)


my_dict.update({"std_name":"Shaktiya Nadar"})
print(my_dict)

my_dict["fees"]=76000
print(my_dict)

my_dict["std_addrs"]="Navi Mumbai"
print(my_dict)

#To remove certain element from the dictionary(removes from last)
my_dict.popitem()
print(my_dict)

#looping over dictionary
for i in my_dict:
    print(i)

#to get the keys from the dictionary
for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

for x,y in my_dict.items():
    print(x,y)

#traversing dictionary
for x,y in my_dict.items():
   print(x,y)

my_dict.pop("std_name")
print(my_dict)
                
