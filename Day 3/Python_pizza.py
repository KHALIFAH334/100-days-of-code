print("Thank you for choosing python pizza delivery! ")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_extra_cheese = input("Do you want extra cheese? Y or N ")   
bill = 0
if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20
    if add_pepperoni == "Y":
        bill += 5
    if add_extra_cheese == "Y":
        bill += 3
print(f"Your final bill is ${bill}")