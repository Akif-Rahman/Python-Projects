#Tip Calculator
print("Welcome to the tip calculator.") 

bill = input("What was the total bill? $")
tip = input("How much tip would ypu like to give? 10, 12, 20? ")
total_people = input("How many people to split the bill? ")

final_bill = float(bill) + float(bill) * (int(tip) / 100)
per_person_bill = round(final_bill / int(total_people), 2)
per_person_bill = "{:.2f}".format(final_bill / int(total_people))
print(f"Each person should pay: ${per_person_bill}")

