#lIST IS A COLLECTION WHICH IS ORDERED AND CHANGABLE
#ALLOWS DUPLICATE MEMBERS
my_list=["Soap","Oil","Maggie","Tea",345,"biscuits","rice"]
print(my_list)
for i in my_list:
    print(i)
my_list.append("Dalia")
print(my_list)
#LIST ELEMENT IS RECOGGNIZED BY IT'S INDEX VALUE
print(my_list[0])
print(my_list[-1])

#slicing
print(my_list[1:4])
print(my_list[:])
print(my_list[2:])
print(my_list[:5])
print(my_list[::-1])
