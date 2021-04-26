import random
name_string = input("Give me erverybody's name\n")

name = name_string.split(",")
 
random_nmae = random.randint(0, 2)
person_who_will_pay = name[random_nmae] 
print(f"{person_who_will_pay} is going to buy the mill today!")
