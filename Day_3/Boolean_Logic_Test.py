#This piece of code is to test my understanding of boolean logic in python. I will be using the logical operators and, or, not to test my understanding of boolean logic.
#The test is to build a boolean logic that will determine if a trade should be made based on the following conditions:
#1. The trend is aligned with the trade direction.
is_trend_aligned = input('Is the trend aligned? (True/False): ')
#2. The risk/reward ratio is at least 2.5.
risk_reward = float(input('What is the risk/reward ratio? (Enter a number): '))
#3. It is not a news day.
is_news_day = input('Is it a news day? (True/False): ')
#To convert the raw input string into a boolean operator
Trend = (is_trend_aligned.lower() == 'true')
News = (is_news_day.lower() == 'true')

# Write your if/else logic below this line
if ((Trend and risk_reward >=2.5) or (not Trend and risk_reward >=4.0)) and not News:
    print('Trade Approved')
else:
    print('Trade Denied')