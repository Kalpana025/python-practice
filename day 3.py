#Define a `Car` class with attributes `brand`, `model`, and `year`. Create an object of the class and print its attributes.
 class Car:
     def __init__ (self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def kal(self):
        print(f"brand:{self.brand},model:{self.model},year:{self.year}")
kalp = Car("goooo","MA34","2014")
 kalp.kal()


 #Create a `Rectangle` class with attributes `length` and `width`. Write methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self,length,width):
         self.length = length
         self.width = width
    def cal(self):
         print("to calculate area rectangle:",(self.length)*(self.width))
         print("to calculate perimeter rectangle:",2*(self.length+self.width))
kal=Rectangle(12,3)
kal.cal()


#Define a `Student` class with attributes `name`, `roll_number`, and `grade`. Create an object and print its attributes.

class Student:
    def __init__(self,name,roll_number,grade):
         self.name = name
         self.roll_number = roll_number
         self.grade = grade
    def kal(self):
         print(f"name of:{self.name}, roll number:{self.roll_number}, grade:{self.grade}")
soo=Student("giri",21,'oc')
soo.kal()


#Create a `Book` class with attributes `title`, `author`, and `price`. Write a method to display the book's details.

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def kal(self):
        print(f"title: {self.title} \n author: {self.author} \n price: {self.price}")
soo = Book("python","giri",1200)
soo.kal()


#Define a `Person` class with a constructor that takes `name` and `age` as arguments. Create an object and print its attributes.
         

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def kal(self):
        print(f"name:{self.name}\n age:{self.age}")
so= Person("kalpana",22)
so.kal()


#Inheritance 
#Create a `Vehicle` class with attributes `brand` and `model`. Create a `Car` class that inherits from `Vehicle` and adds an attribute `num_doors`.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
class Car(Vehicle):
        def __init__(self,brand, model,num_doors):
                super().__init__(brand,model)
                self.num_door = num_doors
        def kal(self):
               print(f"brand{self.brand}, model:{self.model},\ndoor:{self.num_door}")
so =Car("BMW","MK4",4)
so.kal()

#Define an `Animal` class with a method `sound()`. Create a `Dog` class that inherits from `Animal` and overrides the `sound()` method.

class Animal:
    def sound(self):
        print("kakakaka")
class dog:
    def sound(self):
        print("oooooo")
soo=Animal()
soo.sound()
    


# Create a `Shape` class with a method `area()`. Create a `Circle` class that inherits from `Shape` and implements the `area()` method.
class Shape:
    def area(self):
        print("lalala")
class Circle(Shape):
    def area(self):
         super().area()
         
         print("Calculating area of circle")
        
soo = Circle()
soo.area()

# Define a `Person` class with attributes `name` and `age`. Create an `Employee` class that inherits from `Person` and adds an attribute in `department`.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age,departmen):
        super().__init__(name, age)
        self.departmen = departmen
    def kal(self):
         print(f"name:{self.name}\nage{self.age}\ndepartment:{self.departmen}")
soo=Employee("akl",12,"cse")
soo.kal()
              
#14. Create a `Vehicle` class with attributes `brand` and `model`. Create a `Truck` class that inherits from `Vehicle` and adds an attribute `capacity`.
 
class Vehicle:
    def __init__(self,brand,model):
         self.brand = brand
         self.model = model
class Truck(Vehicle):
     def __init__(self,brand,model,capacity):
        super().__init__(brand,model)
        self.capacity = capacity
     def kal(self):
      print(f"{self.brand}\n{self.model}\n{self.capacity}")
soo=Truck("kkm","119","123t")
soo.kal()


#15. Define a `Person` class with a destructor that prints a message when an object is destroyed
 
class person:
    def __init__(self,name):
        self.name = name
        print(f"constructor {self.name}")
    def __del__(self):
       print((self.name),"destructor")
so=person("kal")
del.so
        
    
# Create a `Book` class with a destructor that prints a message when an object is destroyed.
class Book:
    def __init__(self,name):
        self.name = name
        print((self.name))
    def __del__(self):
        print((self.name))
so=Book("lala")
del so
        

#Create a `BankAccount` class with private attributes `balance` and `account_number`. Write methods to deposit and withdraw money

class BankAccount:
    def __init__(self,account_num,balance=0):  
        self.__balance = balance      #private
        self.__account_num = account_num  #private
    def deposit(self,amount):
        self.__amount = amount
        if (self.__amount>0):
            self.__balance+=amount
            print(self.__balance)
    def withdraw(self,amount):
        self.__amount=amount
        if(self.__amount>0<self.__balance):
            self.__balance-=amount
            print("withdraw:",(self.__balance))
soo=BankAccount(1234455,100)
soo.deposit(30)
soo.withdraw(10)

       
# Define a `Person` class with private attributes `name` and `age`. Write methods to get and set these attributes


class person:
      def __init__(self,name,age):
            self.name = name
            self.age = age
      def get_name(self):
            return self.name
      def get_age(self):
            return self.age
      def set_name(self,new_name):
            self.nama = new_name
      def set_age(self,new_age):
            self.age = new_age
soo= person("lalala",12)
print("Name:", soo.get_name())
print("Age:", soo.get_age())

soo.set_name("giri")
soo.set_age(22)
print("upd",soo.get_name())
print("upag",soo.get_age())


#Create a `Student` class with private attributes `name`, `roll_number`, and `grade`. Write methods to get and set these attributes.

class student:
    def __init__(self,name,roll,grade):
        self.name=name
        self.roll=roll
        self.grade=grade
    def get_name(self):
        return self.name
    def get_roll(self):
        return self.name 
    def get_grade(self):
        return self.grade
    def set_name(self,new_name):
        self.name= new_name
    def set_roll(self,new_roll):
        self.roll = new_roll
    def set_grade(self,new_grade):
        self.grade= new_grade
soo=student("kal",12,"c")
print("Name:", soo.get_name())
print("Roll:", soo.get_roll())
print("grade:",soo.get_grade())
 
soo.set_name("kal")
soo.set_roll(11)
soo.set_grade('a')
print("upn ",soo.get_name())
print("upr: ",soo.get_roll())
print("upg: ",soo.get_grade())



#Define a `Car` class with private attributes `brand`, `model`, and `year`. Write methods to get and set these attributes.
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model 
    def get_year(self):
        return self.year
    def set_brand(self,new_brand):
        self.brand= new_brand
    def set_model(self,new_model):
        self.model = new_model
    def set_year(self,new_year):
        self.year= new_year
soo=Car("kal",12,2000)
print("Name:", soo.get_brand())
print("Roll:", soo.get_model())
print("grade:",soo.get_year())
 
soo.set_brand("kal")
soo.set_model(11)
soo.set_year(2000)
print("upn ",soo.get_brand())
print("upr: ",soo.get_model())
print("upg: ",soo.get_year())
