#import random
#import my_module

#random_integer = random.randint(1, 100)
#print(random_integer)

#random_float = random.random() * 5
#print(random_float)  

#love_score = random.randint(1, 100)
#print(f"Your love score is {love_score}")   

#***********1st challange*****Heads or Tails
""""
random_side = random.randint(0, 1) 

if random_side == 1:
    print("Heads.")
else:
    print("Tails.")    
"""
""""
states_of_america = ["Delware", "Pensylvania", "New Jersey", "Georgia", 
"Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
"Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
"Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa",
"Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
"Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
"Alaska", "Hawaii"] 
"""

#print(states_of_america[50])
  
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
