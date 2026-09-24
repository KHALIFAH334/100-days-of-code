#This is another boolean logic test to ensure that i have completely understood boolean logic in python. I will be using the logical operators and, or, not to test my understanding of boolean logic.
#This script  needs to determine whether to auto scale the system based on current traffic and system health.

cpu_load = float(input('Enter the current CPU load percentage: '))
memory_usage = float(input('Enter the current memory usage percentage: '))
maintenance_mode = input('Is the system in maintenance mode? (True/False): ')

maintenance = (maintenance_mode.lower() == 'true')

if ((cpu_load >= 95) or (cpu_load >= 80.0 and memory_usage >= 70.0)) and not maintenance:
    print('initialize New Server.')
else:
    print('No need to scale the system at this time.')