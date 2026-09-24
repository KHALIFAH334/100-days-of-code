#THis is a python script that simply creates a text file and stores the exact time the system was called into the system. 
from datetime import datetime
def create_db():
    current_time = datetime.now()
    with open ('time.txt' , 'a') as f:
        f.write(f'The time and date of your log is {current_time}\n')
create_db()
