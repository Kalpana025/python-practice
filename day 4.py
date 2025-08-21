# encapsulation:
# example A:
# what’s being encapsulated: the account’s internal balance and the rules for changing it.
#  What’s hidden: direct access to the raw balance; no one can set it arbitrarily from outside.
#  What’s exposed: a few safe actions like “deposit,” “withdraw,” and “show balance.”
#  How it works conceptually: all reads and writes to the balance must pass through these actions, which enforce business rules (e.g., no negative deposits, no overdrafts beyond limits).
#  Why it matters: protects data integrity, prevents accidental or malicious tampering, and centralizes validation logic in one place.
#  One-liner for interview: “Encapsulation makes the balance untouchable directly; the only way in or out is through controlled operations that enforce rules.”
# program:

class BankAccount:
    def __init__(self,account\_num,balance=0): 

        self.__balance = balance      #private**

        self.__account_num = account_num  #private**

    def deposit(self,amount):

        self.__amount = amount

        if (self.__amount>0):

          self.__balance+=amount

            print (f"in your account ##{self.__account_num}## the amount was depositedyour currenmt balance {self.__balance}")

    def withdraw(self,amount):

        self.__amount=amount

        if(self.__amount>0<self.__balance):

            self.__balance-=amount

            print(f"in your account ##{self.__account_num}## the amount was withdrawed and your current balance was {self.__balance}")

soo=BankAccount(1234455,100)
soo.deposit(30)
soo.withdraw(10)

# example B:

# Encapsulated: Usernames & passwords storage + rules for checking.

# Hidden: Raw passwords (outsiders can’t see or change them)

# Exposed: Encapsulated: Usernames & passwords storage + rules for checking.

# Hidden: Raw passwords (outsiders can’t see or change them).

# Exposed: Only signup() and login() methods.

# Concept: Store and check credentials internally, never directly outside**.**

# One-liner: “Encapsulation hides passwords and only allows login/signup through safe

# 2) Abstraction

# Example A: Payment Gateway

# Core idea: give a simple “pay” experience while hiding the messy details.
# What’s hidden: card network hops, fraud checks, 3-D Secure flows, retries, webhooks, and settlement.
# What’s exposed: a unified way to request a payment (e.g., “process payment for ₹1000”).
# How it feels to a developer: you don’t need to know if it’s credit card, UPI, or wallet under the hood; you just ask to pay.
# Why it matters: reduces cognitive load, accelerates development, and allows changing providers without affecting the rest of the system.
# One-liner: “Abstraction lets me say ‘take the money’ without caring how the rails work.”

# PROGRAM:

class __Payment:
    def __init__(self,payment_method=["__card","__UPI","__Wallet"]):
        self.payment_method = payment_method
        self.__card = "__card"
        self.__UPI = "__UPI"
        self.__Wallet = "__Wallet"
    def __process_payment (self, amount):
        self.amount = amount
        if amount > 0:
            print(f"Processing payment of ${amount} ")
    def __card(self, amount):
        print(f"using card to payment process ${amount}")
    def __UPI(self, amount):
        print(f"using UPI to payment process ${amount}")
    def __Wallet(self, amount):
        print(f"using Wallet to payment process ${amount}")
        self.__process_payment(amount)
    if __process_payment == "card":
        self.__card(amount)
    elif __process_payment == "UPI":
        self.__UPI(amount)
    elif __process_payment== "Wallet":
        self.__Wallet(amount)
    else:
        print("Invalid payment method")
so=__Payment()
so.__process_payment(1000)
print("Payment processed successfully")

# Example B:
# Core idea: simple way to manage money while hiding database and validation details.

# What’s hidden: SQL queries, connection handling, fraud checks, negative balance rules.

# What’s exposed: clean methods like connect(), get_balance(), set_balance().

# How it feels: you just ask “what’s the balance?” or “update balance” without caring about backend.

# Why it matters: reduces errors, makes code cleaner, and allows backend changes easily.

# One-liner: “Abstraction lets me say ‘set balance to ₹2000’ without caring how the bank or DB works.”

# 3) Inheritance

# Example A: Vehicle System (Vehicle → Car/Truck/Motorcycle)

# Relationship: “is-a.” A car is a vehicle; a truck is a vehicle.
# What’s shared: common capabilities such as starting, stopping, basic identification.
# What’s customized: each subtype adds or overrides behavior (a truck can carry cargo; a motorcycle balances differently).
# Key property: anywhere the system expects a “vehicle,” you should be able to plug in a car, truck, or motorcycle and it still works logically.
# Why it matters: reuse shared logic, minimize duplication, and create a clean hierarchy of capabilities.
# One-liner: “Inheritance factors common vehicle behavior up, and each subtype only adds what’s unique.”

# Eample B:
   
#    PROGRAM;
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}"

emp1 = Developer("Alice", 60000, "Python")
print(emp1.get_details())

# Example B:

# Core idea: simple way to manage different employee roles (Manager, Developer, Tester) while hiding role-specific details.

# What’s hidden: how each role stores extra data like programming language or testing tool.

# What’s exposed: a clean method get_details() that works for any employee type.

# How it feels: you just create a Developer or Tester and ask for details, no need to worry about inheritance or attributes.

# Why it matters: reduces duplicate code, makes adding new roles easier, keeps structure clear.

# One-liner: “Abstraction lets me say ‘give me employee details’ without caring whether it’s a Manager, Developer, or Tester.”

# 4) Polymorphism
# Example A: 
# Shape Calculator (Circle/Rectangle/Triangle → “area”)
# Core idea: same request, different correct answers depending on the actual shape.
# What happens: you call “calculate area,” and the right formula runs for the actual shape at runtime.
# Why it matters: callers don’t need a big “if/else” for every shape type; the objects know how to do their own job.
# Result: extensibility—adding a new shape doesn’t change the code that uses “area”; you just teach the new shape how to compute itself.
# One-liner: “Polymorphism lets ‘area’ pick the right math for the actual shape.

# program:
class Payment:
    def pay(self, amount):
        return f"Processing ₹{amount}"

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

class PayPal(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using PayPal"

class BankTransfer(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Bank Transfer"

p1 = CreditCard()
p2 = PayPal()
p3 = BankTransfer()

print(p1.pay(1000))
print(p2.pay(500))
print(p3.pay(2000))

# Example B:

# Core idea: give a simple “pay” experience while hiding bank transfer steps.

# What’s hidden: account verification, IFSC checks, settlement, transfer confirmation.

# What’s exposed: one method pay(amount) that directly works.

# How it feels: you just say pay(2000) and it’s done, no need to know about banking systems.

# Why it matters: keeps code short, safe, and flexible for any payment type.

# One-liner: “Abstraction lets me say ‘send ₹2000’ without caring how the bank processes it.”



