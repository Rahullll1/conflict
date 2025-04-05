#Lambda Function
# k = lambda x: x**2
# print(k(5)) 

# l = lambda func:func.upper()
# print(l("hello world"))

# n = lambda x : "even" if x%2 == 0 else "odd"
# print(n(3))
# print(n(4))

# t = lambda x : x**2
# print(t(5))

# l = [lambda arg = x : arg * 10 for x in range(1,10)]
# for i in l:
#     print(i(),end = " ")
    
    
# n = lambda x,y:(x+y,x-y,x*y,x/y)
# print(n(10,5))

# n = [1,3,6,2,8,9]
# l = filter(lambda x: x%2 == 0, n)
# print(list(l))

# a =[1,5,3,6]
# k = map(lambda x: x* 2,a)
# print(list(k))


# from functools import reduce
# n = [1,2,3,4,5]
# n = reduce(lambda x,y : x *y,n)
# print(n)

# a = "rahool"
# b = 22

# print("I am {} and my age is {}".format(a,b))
# print(f"I am {a} and my age is {b}") 
# print("I am {} and my age is {}".format("Chand",21))

# def fun1(m):
#     def fun2():
#         print(m)
#     fun2()
# fun1("hello world")


# def decorator(func):
#     def wrapper():
#         print("This is a decorator function")
#         func()
#     return wrapper

# @decorator

# def greet(name = "rahul"):
#     print("Hello, World!")
    
# greet()


# import inspect

# print(inspect.signature(greet))
# print(inspect.signature(decorator))

# class car:
#     color = "red"
#     model = "suv"
    
# car1 = car()
# print(car1.color)
# car2 = car()
# print(f"this car is {car1.color} in color, and model is {car2.model}")


# class solution:
#     def __init__(self, name):

# class solution:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def isage(self):
#         if self.age >= 18:
#             return True
#         else:
#             return False
        
# s1 = solution("Rahool",21)
# print(s1.isage())


# class solution:
#     def __init__(self,name,age):
        
#         self.name = name
#         self.age = age

        
# s1 = solution("Rahool",21)
# s2 = solution("chandra",22)
# print(s1.name)
# print(s2.age)

# s1.name = "vignesh"


# class car:
#     def __init__(self,name):
#         self.name = name
        
#     def color(self):
#         raise NotImplementedError("Subclasses must implement this method")
    
# class bmw(car):
#     def color(self):
#         return "red"
    
# n = car("Benz")

# k = bmw("BMW")
# print(k.color())
# print(k.name)
# print(k.color())
        


# class solution:
#     def __init__(self):
#         self.ig = self.instagram()
        
#     def show(self):
#         print("name", self.name)
        
#     class media:
#         def __init__(self):
#             self.name = "Instagram"
#             self.code = "IG"
            
#         def display(self):
#             print("name", self.name)
#             print("code", self.code)
            
# outer = solution()
# outer.show()
# g = outer.ig
# g.display()

        
        
# class parent():
#     def show(self):
#         print("this is parent class")
        
# class child(parent):
#     def show(self):
#         super().show()
#         print("this is child class")
        
# o = child()
# o.show()



# class solution:
#     def __init__(self):
#         self._age = 21
        
#     def age(self):
#         return self._age
    
    
# o = solution()
# print(o.age())

#Iterators

# n = [1,2,3,4,5]
# i = iter(n)
# print(next(i)) 
# print(next(i))

# def imp():#Local Scope
#     x = 30
#     print(x)
# imp()

# def imp1():#Enclosing Scope
#     x = 20
#     def temp():
#         print(x)
#     temp()
    
# imp1()

# x = 100
# def imp2():#Global Scope
#     print(x)    
    
    
# imp2()

# import sample

# print(sample.addition())

# from sample import addition
# print(addition(2,1))

# import math

# c = math.ceil(2.4)
# print(c)
# print(math.floor(2.4))
# print(math.pi)
# print(math.pow(2,3))
# print(math.sqrt(4))

import numpy as np

# a = np.array([1,2,3])
# print(a)


# print(np.zeros((2,3)))
# print(np.ones((3,3)))
# print(np.array([[1,2,3],[4,5,6]]))
# print(np.arange(1,10,2))
# print(np.linspace(1,10,5))


# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a+b)
# print(np.sqrt(a))

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[7,8,9],[10,11,12]])
# # print(np.dot(a,b))
# print(np.transpose(a))
# print(np.linalg.inv(a))


# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)
# print(arr.max())

import pandas as pd

# s = pd.Series([1,2,3,4.54],index =['a','b','c','d'])
# print(s)

data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}


df = pd.DataFrame(data)
# print(df)

# print(df.info())
# print(df.columns)
df["Age"] += 1

k=df['Name'] = 'Johnnny'

df.rename(columns = {'Name':'First Name'})
print(df)
