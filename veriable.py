_cars = 23
cars = 24
CARS = 25

number_of_cars = 23
kind_of_cars = "Ferrari"
print(cars)
print(_cars)
print(CARS)
print(number_of_cars)
print(kind_of_cars)

"""
this is multi-line comment
"""

name="Suchi tripathi"
type_of_car="Rolls Royce"
school="Foundation Elementary School"
print(name+type_of_car+school)
print(type_of_car+ " " +school)
print("{} works at {}.".format(name,school))

#function in python
def addition():
    a=45
    b=10
    print(a+b)
addition()

def addition2():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a+b)
addition2()

#Argument in python
def user_info(name,age,city):
    '''This function print name age and city
    from an argument to the function'''
    print("{} is {} years old, from {}".format(name,age,city))

user_info("Suchi", 25, "Prayagraj")
#user_info("Suchi", "Lucknow12")

#Conditionals in python
lug_weight=int(input("Enter luggage weight:"))
if lug_weight < 20:
    print("No Fee")
elif lug_weight >= 20:
    print("Please Pay Fee")

name=input("Enter your name:")
if name == "Suchi":
    print("Hello, nice to see you {}".format(name))
elif name == "Suchita":
    print("Hi, Suchita")
else:
    print("hi,hi, hi")
print("Thanks for entering your name" +name)