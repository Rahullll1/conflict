class encapsulation:
    a=10
    def __init__(self):
        self._salary=50000
        self.__pf=25000
    def salary(self):
        print(self.__pf)
        return self._salary
obj=encapsulation()
print(obj.a)
print(obj.salary())
print(obj._salary)