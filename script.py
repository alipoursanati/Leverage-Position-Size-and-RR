#By: Ali Rajabpour-Sanati
# ali.poursanati@gmail.com

def calculate_position():
    # Take input from user
    entry = float(input("Enter entry price: "))
    stop_loss = float(input("Enter stop loss price: "))
    targets = list(map(float, input("Enter targets, separated by commas: ").split(",")))
    wallet_size = float(input("Enter wallet size: "))
    risk_percent = int(input("Enter risk percentage(in integer): "))
    # Calculate risk per trade
    risk = (entry - stop_loss) * (risk_percent/100)
    # Check if risk/reward ratio is less than 1.5
    reward = targets[0] - entry
    if reward/risk < 1.5:
        return "Error: Risk/reward ratio is less than 1.5"
    else:
        # Calculate position size
        position_size = (wallet_size * (risk_percent/100)) / risk
        # Calculate leverage
        leverage = int(position_size / wallet_size * 100)
        # Print results
        print("Position size: ", position_size)
        print("Leverage: ", leverage)

result = calculate_position()
if result:
    print(result)
