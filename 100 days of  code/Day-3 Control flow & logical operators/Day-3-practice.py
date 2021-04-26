#if-elif-else condition
""""
water_level = 90
if water_level > 80:
    print("Drain water")
else:
    print("Continue")    
""" 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5 
        print("Childs Tickets are 5$.")
    elif age <= 18:
        bill = 7 
        print("Youth's Tickets are 7$.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay.Have a free ride on us.")
    else:
        bill = 12
        print("Adults's Tickets are 12$.")
    
    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        bill += 4
    
    print(f"Your final bill is {bill}$.")     
else:
    print(" Sorry, You can't ride.")    


#**********1st challange******   
""""
number = int(input("What number do you want to check? ")) 
if number % 2 == 0:
    print("This is a even number.")
else:
    print("This is a odd number.")     
"""    

#********2nd challange********
""""
height = float(input("What is your height in cm? "))
weight = float(input("What is your weight in kg? "))
bmi = round(weight / (height * height))
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")                 
"""

#***********3rd challange*************leap year
""""
year = int(input("Which year do you want to check? "))

if ((year % 4 == 0) or (year % 400 == 0)) and year % 100 == 0:
     print("Leap Year.")
else:
    print("Not Leap year.")  
"""   
    
#************4th challange*********
""""
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you wnat? S, M, or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_chesse = input("Do want extra chesse? Y or N ") 
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2 
    else:
        bill += 3      

if extra_chesse == "Y":
    bill += 1 

print(f"Your final is: {bill}$.")
""" 

#**********5th challange*************Love Calculator
""""
print("Welcome to the Love Calculator.")
nmae1 = input("What is your name?\n")
name2 = input("What is his/her name?\n")

name1_lowercase = nmae1.lower()
name2_lowercase = name2.lower()

#For True in name1 & name2
name1_lowercase_countT = name1_lowercase.count("t") 
name1_lowercase_countR = name1_lowercase.count("r")
name1_lowercase_countU = name1_lowercase.count("u")
name1_lowercase_countE = name1_lowercase.count("e") 

name2_lowercase_countT = name2_lowercase.count("t")
name2_lowercase_countR = name2_lowercase.count("r")
name2_lowercase_countU = name2_lowercase.count("u")
name2_lowercase_countE = name2_lowercase.count("e") 

Total_TRUE_count = (name1_lowercase_countT + name2_lowercase_countT) + (name1_lowercase_countR + name2_lowercase_countR) + (name1_lowercase_countU + name2_lowercase_countU) + (name1_lowercase_countE + name2_lowercase_countE)


#For Love in name1 & name2
name1_lowercase_L = name1_lowercase.count("l")
name1_lowercase_O = name1_lowercase.count("o")
name1_lowercase_V = name1_lowercase.count("v")
name1_lowercase_E = name1_lowercase.count("e")

name2_lowercase_L = name2_lowercase.count("l")
name2_lowercase_O = name2_lowercase.count("o")
name2_lowercase_V = name2_lowercase.count("v")
name2_lowercase_E = name2_lowercase.count(("e"))

Total_LOVE_count = (name1_lowercase_L + name2_lowercase_L) + (name1_lowercase_O + name2_lowercase_O) + (name1_lowercase_V + name2_lowercase_V) + (name1_lowercase_E + name2_lowercase_E)

Love_score = int(str(Total_TRUE_count) + str(Total_LOVE_count)) 


if (Love_score) <= 10 or (Love_score) >= 90:
    print(f"Your Love Score is {Love_score}, you go together like coke and mentos.")
elif (Love_score) >= 40 and (Love_score) <= 50:
    print(f"Your Love Score is {Love_score}, you are alright together.")
else:
    print(f"Your Love Score is {Love_score}.") 
"""  
