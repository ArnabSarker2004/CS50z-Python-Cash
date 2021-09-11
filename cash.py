from cs50 import get_float

while True:
    change = get_float("Change owed: ") #Asks user for change at prompt
    if change > 0: #Break loop if the change at prompt meets requirements
        break

cents = round(change * 100) #Rounds deue to possibility of floating point error
CoinCounter = 0 #Initalize counter for the number of coins needed

while cents >= 25: #Finds the number of quarters needed
    cents -= 25
    CoinCounter += 1

while cents >= 10: #Finds the number of dimes needed
    cents -= 10
    CoinCounter += 1

while cents >= 5: #Finds the number of nickels needed
    cents -= 5
    CoinCounter += 1

while cents >= 1: #Finds the number of pennies needed
    cents -= 1
    CoinCounter += 1



print(f"{CoinCounter}") #Prints the number of coins needed


