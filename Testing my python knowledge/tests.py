
def gather_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    return {'name': name, 'age': age, 'email': email}

data = {}
def display_success_message(name, age, email):
    print("\nThank you for providing your information!")
    print("Your information has been saved successfully.")

def store_data(name, age, email):
    #This function creates database file and stores it
    with open ('db.txt', 'a') as f:
        position = f.tell()
        f.write(f'''{"Name; " + name}:{"Age; " + age}:{"Email; " + email}\n''') 
        print(f"Data for {name} stored successfully")
        data[name] = position
    
def get_data(name):
    position = data.get(name)
    if position is None:
        return None
    with open('db.txt', 'r') as f:
        f.seek(position)
        line = f.readline()
        name, age, email = line.strip().split(':')
        return name, age, email
    
def delete_data(name):
    position = data.get(name)
    if position is None:
        return False  
    with open('db.txt', 'a') as f:
        position = f.tell()
        f.write(f'{name}:TOMBSTONE\n')
        data[name] = position
    return True

def user_action():
    print('What will you like to do today?')
    action = input('Store_data, Get_data or Delete_data ')
    action = action.lower()
    if action == "store_data":
        # Catch the user input data using the gather_user_info function
        user_data = gather_user_info()
        # Pass that caught data directly into the store_data function
        store_data(user_data['name'], user_data['age'], user_data['email'])
    elif action == "get_data":
        target_name = input("Enter the name of the person the data belongs to:")
        get_data(target_name)
    elif action == "delete_data":
        target_name = input("Enter the name of the person whose data you want to delete:")
        delete_data(target_name)
    else:
        print('Invalid action. Please choose Store_data, Get_data or Delete_data.')


user_action()