days = input("Enter the number of days: ")
hours = int(days) * 24
print(f"{days} days is equal to {hours} hours.")

def study_hours_report(weekly_hours):
    total_hours = sum(weekly_hours)
    return f"I spent a total of {total_hours} hours studying this week."
day = input("Enter a day of the week: ")
listday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
listhours_spent = ["8 hours", "8 hours", "8 hours", "5 hours", "4 hours", "5 hours", "4 hours"]
study_hours = zip(listday, listhours_spent)
daily_study_hours = [f"On {day}, I spent {hours} studying." for day, hours in study_hours]
sum_hours_weekly = sum(int(hours.split()[0]) for hours in listhours_spent)
weekly_study_hours = [study_hours_report([sum_hours_weekly])]
new_list = [f"On {day}, I spent {hours} studying." for day, hours in study_hours]
print(new_list)
print(daily_study_hours)
print(weekly_study_hours)