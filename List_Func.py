numbers = [10, 20, 30, 40, 50]

numbers.append(60)
print("append():", numbers)  # Output: [10, 20, 30, 40, 50, 60]

numbers.insert(2, 25)
print("insert():", numbers)  # Output: [10, 20, 25, 30, 40, 50, 60]


numbers.remove(30)
print("remove():", numbers)  # Output: [10, 20, 25, 40, 50, 60]


popped_element = numbers.pop()
print("pop():", popped_element)  # Output: 60
print("List after pop:", numbers)  # Output: [10, 20, 25, 40, 50]

index = numbers.index(40)
print("index(40):", index)  # Output: 3


numbers.reverse()
print("reverse():", numbers)  # Output: [50, 40, 25, 20, 10]


numbers.sort()
print("sort():", numbers)  # Output: [10, 20, 25, 40, 50]
