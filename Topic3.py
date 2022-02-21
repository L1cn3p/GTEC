# 1) Vehicle class
class Vehicle():
    def __init__(self, eating_capacity, fuel, wheels):
        self.eating_capacity = eating_capacity
        self.fuel = fuel
        self.wheels = wheels
    def dict(self):
        return vars(self)

car= Vehicle(100, 200, 21)
print(car.dict())

# 2) abstract class
from abc import ABC, abstractmethod

class Object3D(ABC):
    
    @abstractmethod
    def volume(self):
        print("Override this")
        pass

    @abstractmethod
    def tsa(self):
        print("Override this")
        pass

class Box(Object3D):

    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.vol = self.volume()
        self.sur_area = self.tsa()

    def __add__(self, other):
        l = self.length + other.length
        w = self.width + other.width
        h = self.height + other.height
        return Box(l=l,w=w,h=h)

    def __mul__(self, other):
        l = self.length * other.length
        w = self.width * other.width
        h = self.height * other.height
        return Box(l=l,w=w,h=h)

    def __eq__(self, other):
        return vars(self) == vars(other)

    def volume(self): 
        return (self.length*self.width*self.height)

    def tsa(self):
        return 2*(self.length*self.width + self.width*self.height + self.length*self.height)

my_box = Box(2,3,4)
print(vars(my_box))

from math import pi, sqrt
class Cylinder(Object3D):

    def __init__(self, r, h):
        self.radius = r
        self.height = h
        self.vol = self.volume()
        self.sur_area = self.tsa()
        
    def volume(self): 
        return (pi*self.radius**2*self.height)

    def tsa(self): 
        return (2*pi*self.radius*(self.radius+self.height))

my_cylinder = Cylinder(2,3)
print(vars(my_cylinder))

my_box_2 = Box(2,3,4)

# 3) overloading operators
my_box_3 = my_box + my_box_2
print(vars(my_box_3))
my_box_4 = my_box * my_box_2
print(vars(my_box_4))
print((my_box == my_box_2))
print((my_box == my_box_3))
string = ''
for k,v in vars(my_box_4).items():
    item = (' {0} : {1} |'.format(k,v))
    string+=item
print(string)

# 4) Number class
class Number():
    @staticmethod
    def prime_list(M,N):
        prime_nums = []
        i = M
        while i < N:
            if not Number.is_prime(i):
                i+=1
                continue
            prime_nums.append(i)
            i+=1
        return prime_nums
    @staticmethod
    def fibonacci(N):
        fib_nums = []
        n1, n2 = 0, 1
        count = 0
        if N <= 0:
            return fib_nums
        if N == 1:
            fib_nums.append(n1)
            return fib_nums
        while len(fib_nums) < N:
            fib_nums.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
        return fib_nums
    @staticmethod
    def odd_nums(N):
        odd_list = []
        i = 0
        while len(odd_list) < N:
            if i % 2 == 0:
                i+=1
                continue
            odd_list.append(i)
            i+=1
        return odd_list
    @staticmethod
    def even_nums(N):
        even_list = []
        i = 0
        while len(even_list) < N:
            if i % 2 != 0:
                i+=1
                continue
            even_list.append(i)
            i+=1
        return even_list
    @staticmethod
    def is_palindrome(N):
        return str(N) == str(N)[::-1]
    @staticmethod
    def is_prime(n):
        status = True
        if n < 2:
            status = False
        else:
            for i in range(2,n):
                if n % i == 0:
                    status = False
        return status

print(Number.prime_list(2,20))
print(Number.fibonacci(9))
print(Number.odd_nums(20))
print(Number.even_nums(20))
print(Number.is_palindrome(808))
print(Number.is_prime(7))

# 6) 6. student class

class Student():
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.evaluate()

    def evaluate(self):
        self.total = self.mark1+self.mark2+self.mark3
        if self.total >= 120 and all(i >= 35 for i in [self.mark1,self.mark2,self.mark3]):
            if self.total >= 240:
                self.grade = "Outstanding"
                return
            elif self.total >= 180:
                self.grade = "Excellent"
                return 
            elif self.total >= 150:
                self.grade = "Good"
                return 
            else:
                self.grade = "Average"
                return 
        else:
            self.grade = None
            return
my_student = Student('Fahad',100,90,50)
print(vars(my_student))
my_student.mark1 = 35
my_student.evaluate()
print(vars(my_student))

import pickle

with open("student.dat", "wb") as f:
    pickle.dump(my_student, f)

with open("student.dat", "rb") as f:
    data = pickle.load(f)
    print(vars(data))

data.mark1 = 100
data.evaluate()
print(vars(data))
with open("student.dat", "wb") as f:
    pickle.dump(data, f)