print("welcome to the tip calculator")
input_bill = float(input("What was the total bill? $"))
Total_tip = float(input("What percentage Tip will you like to give? 10%, 15%, or 25%"))
Total_people = int(input("How many people to split the bill? "))
Per_person = (input_bill + (input_bill * Total_tip / 100)) / Total_people
print(f"Each person should pay: ${Per_person:.2f}") 