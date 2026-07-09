pnl_records = [150, -50, 200, -75, -50, 300]
profit = 0
loss = 0

for item in pnl_records:
    if item > 0:
        profit += item
    elif item < 0:
        loss += item 

net_profit = profit + loss
print(net_profit)