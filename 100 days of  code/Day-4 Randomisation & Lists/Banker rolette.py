import random
name_string = input("Give me erverybody's name\n")

name = name_string.split(",")
 
person_who_will_pay = random.choice(name) 
print(f"{person_who_will_pay} is going to buy the mill today!")
