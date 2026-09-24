while True:
    account_balance = float(input("What is the account equity? "))
    if account_balance == 0:
        print("Shutting down risk engine")
        break
    risk_percentage = float(input("What is the risk on the account in percent? "))
    entry_price = float(input("What is the entry price? "))
    stop_loss = float(input("What is the SL price? "))

    Risk = account_balance * (risk_percentage / 100)
    price_distance = entry_price - stop_loss

    if price_distance == 0:
        print("Error")
    else:
        position_size = Risk/price_distance
        lot_size = position_size / 100000
        lot_size = round(lot_size, 2)
        lot = (abs(lot_size))
        print(f"You should use {lot} lots for your trade")