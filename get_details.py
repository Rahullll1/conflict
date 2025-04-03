
def get(name,age,height, weight):
    print("Hello",name, "You are ",age,"years old","Your height is",height,"and your weight is",weight)
    return name,age,height,weight

name = input("Enter your name:")
age = int(input("Enter your age:"))
height = int(input("Enter your height:"))
weight = int(input("Enter your weight:"))
get(name,age,height,weight)