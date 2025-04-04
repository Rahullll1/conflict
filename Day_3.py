#List
# s = ("rahul",21,7.54,True)
# print(type(s))
# print(s[0])
# print(s[1])
# print((s[2]))

#Tuple
# s = ["rahul",21,7.54,True]
# print(type(s))
# print(s[0])
# print(s[1])
# print((s[2]))

#Boolean
# s = True
# print(type(s))
# print(s)
#print(type(False))

#set
# s = {1,2,3,4,5,2}
# print(type(s))
# s = {"HelloRahoolHelloOOL"}
# print(s)
# s1 = {"HII","Rahul","Hello","Rahool"}
# print(s1)
# s2 = set("Rahoolchandra")
# print(s2)

# s = "Rahool"
# print(s[::-1])

#Range
# s = range(1,20,3)
# print(type(s))
# print(list(s))

# f = frozenset{1,2,3,4}
# f.add{5}

#dictionary
# s = {1:"Rahool","jiju":"Chandra",3:"Hello"}
# print(type(s))
# print(s[1])
# print(s["jiju"])

# #Binary Data Type
# s = bytes([65,66,67,68])
# print(type(s))
# print(s)

# s = None
# print(type(s))

# y
# print((y))

#If else
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# if a > b: 
#     print("a is greater than b")
# elif a < b:
#     print("b is greater than a")
# else:
#     print("a is equal to b")

#example2
# i = 0
# if i!=0:
#     print("The number is not zero")
# if i>0:
#     print("The number is positive")
# if i<0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# n =5
# while n> 0:
#     n -= 1
    
#     if n==2:
#         break
#     print(n) 
    
# print("Loop ended") 



#For Loop

# t = ("Rahool",21,7.54,True)
# for i in t:
#     print(i)

# x =[1,2]
# y = [3,5]

# for i in x:
#     for j in y:
#         print(i,j)
    
    
# def greet(name="Rahool"):
#     print("Hello",name)
    
# # greet()
# greet("Chandra")


# def details():
#     name = "rahool"
#     age = 21
#     return name,age

# n,a = details()
# print("Name:",n,"Age:",a)


# dict = {"name":"Rahool","age":21,"height":7.54}

# for i in dict.keys():
#     print(dict[i])
    
    
    
# def arg(*num):
#     return sum(num)

# print(arg(1,2,3,4,5))
    


# def kwrd(**det):
#     for key,value in det.items():
#         print(f"{key}:{value}")
        
# kwrd(name = "Rahool", age=21, Height=7.54, weight=70)

import array
# r = array.array('u',"Rahool")
# print(r)  

# f = array.array("u","Rahool")
# for f in f:
#     print(f,end = ",")

f = array.array("i",[1,2,3,4])

print(sorted(f))