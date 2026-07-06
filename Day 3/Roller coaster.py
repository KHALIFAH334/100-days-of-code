print('Welcome to the roller coaster!')
height = int(input('What is your height in cm? '))
age = int(input('Enter your age: '))
if height > 119:
    print('You can ride the roller coaster!') 
    bill = 0
    if age >= 45 and age <= 55:
        print('Everything is going to be ok. Have a free ride on us!')
    elif age >= 18:
        bill += 12
        print ('Adult ticket costs $12')   
    elif age <= 12:
        bill += 5
        print ('Kids ticket costs $5')
    elif age > 12 and age < 18:
        bill += 7
        print ('Youth  ticket costs $7')
    photo = input('Do you want a photo taken? True/False:')
    if photo == 'True':
        bill += 3
        print(f'Your final bill is ${bill}')
        
else:
    print('Sorry, you have to grow taller before you can ride.')